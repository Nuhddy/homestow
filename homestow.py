#! /usr/bin/env python3

import os
import argparse
import yaml
import sys
import socket


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("-c", "--config", nargs=1,
                   default="./config.yaml")
                   #  default="$XDG_CONFIG_HOME/homestow/config.yaml")

    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("-I", "--install", action="store_true")
    g.add_argument("-U", "--uninstall", action="store_true")
    g.add_argument("-R", "--reinstall", action="store_true")

    args = p.parse_args()
    return args


def read_config(file_path):
    try:
        with open(file_path, "r") as file:
            config = yaml.safe_load(file)
        return config
    except:
        print("config file does not exist")
        sys.exit(1)


def stow(action):
    profile = socket.gethostname()
    try:
        src_dir = "-d " + config[profile]["source-dir"]
        tar_dir = "-t " + config[profile]["target-dir"]
        pkgs = " ".join(config[profile]["packages"])
        cmd = " ".join(["stow -nv", src_dir, tar_dir, action, pkgs])
        os.system(cmd)
    except:
        print("profile for current hostname not defined correctly")
        sys.exit(1)


if __name__ == "__main__":
    args = parse_args()
    config = read_config(args.config)

    if args.install:
        stow("-S")
    elif args.uninstall:
        stow("-D")
    elif args.reinstall:
        stow("-R")
