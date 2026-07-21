#!/usr/bin/env python 3.8
# -*- coding: utf-8 -*-
# time: 2025/08/05
# name: Haowen Cui

import json
from agent_quality_check import Agent_quality_check

def load_config(path="config_agent_check.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__=="__main__":
    config=load_config()
    test_sample=load_config("test_sample.json")
    checker=Agent_quality_check(
        upload_url=config.get("upload_url"),
        workflow_url=config.get("workflow_url"),
        dialog=test_sample.get("dialog"),
        save_file_name=test_sample.get("save_file_name"),
        user=test_sample.get("user"),
        email_info=test_sample.get("email_info"),
        receiver=test_sample.get("receiver"),
        upload_file_type=test_sample.get("upload_file_type"),
        audio_path=test_sample.get('audio_path'),
        dialog_id=test_sample.get('dialog_id'),
        staff_id=test_sample.get('staff_id'),
        authorization=config.get('authorization')
    )
    checker.run()

