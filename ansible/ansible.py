#!/usr/bin/env python

#author--qinshixu
#coding:utf-8

import platform,json
import shlex
import ansible.runner
def ansible_runner():
    runner = ansible.runner.Runner(
    module_name='shell',
    module_args="cat /etc/issue | awk '{print $1}'",
    host_list='aa.py',
    pattern='AA',
    remote_port='22',
    forks=10,
    remote_user='root'
)
    return runner.run()

results=ansible_runner()
for (hostname, result) in results['contacted'].items():
    if not 'failed' in result:
        for line in  result['stdout'].split('\n\nTo\nN.B.\nTo\nN.B.'):
            if line:
                print line[0:6]

