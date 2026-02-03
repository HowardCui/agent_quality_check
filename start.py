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
    checker=Agent_quality_check(
        upload_url=config.get("upload_url"),
        workflow_url=config.get("workflow_url"),
        dialog=config.get("dialog"),
        save_file_name=config.get("save_file_name"),
        user=config.get("user"),
        email_info=config.get("email_info"),
        receiver=config.get("receiver"),
        upload_file_type=config.get("upload_file_type"),
        audio_path=config.get('audio_path'),
        dialog_id=config.get('dialog_id'),
        staff_id=config.get('staff_id'),
        authorization=config.get('authorization')
    )
    checker.run()

