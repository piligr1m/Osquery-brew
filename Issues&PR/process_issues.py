#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import datetime
from json_helpers import extract_datetime


ORG = 'owner'
REPO = 'name'
FILENAME_ISSUES = ORG + 'issues.json'
BUG_LABEL = ['bug']
CRITICAL_BUG_LABEL = ['sev1-critical', 'sev2-high']


one_day = datetime.timedelta(days=1)
now = datetime.datetime.now(datetime.timezone.utc)

f = open(FILENAME_ISSUES)
data = json.load(f)
f.close()

if REPO not in data.keys() and len(data[REPO]) == 0:
    raise SystemExit()


for i in data[REPO].keys():
    data[REPO][i]['created_at'] = extract_datetime(data[REPO][i]['created_at'])
    if data[REPO][i]['closed_at'] is not None:
        data[REPO][i]['closed_at'] = extract_datetime(data[REPO][i]['closed_at'])


last_number = min([int(i) for i in data[REPO].keys()])
first_date = extract_datetime(data[REPO][str(last_number)]['created_at'])

day = datetime.datetime(first_date.year, first_date.month, first_date.day, tzinfo=datetime.timezone.utc)
day += one_day

result = {}

f = open('result.tsv', 'w')
f.write('date\tammount_of_closed_issues\tammount_of_closed_prs\t%s\n'%'\t')

while day < now:
    key = day.strftime('%Y-%m-%d')
    print(key)

    open_pr_count = 0
    closed_pr_count = 0
    open_issue_count = 0
    closed_issue_count = 0

    

    for i in data[REPO]:
        element = data[REPO][i]


        is_open = True
        if isinstance(element['closed_at'], datetime.datetime) and element['closed_at']:
            is_open = False
        if element['is_pull_request']:
            if is_open:
                open_pr_count += 1
            else:
                closed_pr_count += 1
        else:
            if is_open:
                open_issue_count += 1
            else:
                closed_issue_count += 1



    output = '%s\t%i\t%i'%(key, closed_issue_count, closed_pr_count)



    

    day += one_day
    
    f.write(output + '\n')

f.close()
