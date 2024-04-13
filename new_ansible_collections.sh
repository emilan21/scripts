#!/bin/bash

collection_name=$1

ansible-galaxy collection init --init-path ../ansible_collections em.$collection_name
