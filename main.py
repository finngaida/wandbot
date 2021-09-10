import time

import telegram_send
import wandb


def process_running(run):
    # check some stats or so via run.scan_history
    pass

def process_freshly_failed(run):
    telegram_send.send(messages=[f"Run {run} just failed!"])

def process_finished(run):
    telegram_send.send(messages=[f"Run {run} just finished!"])

def loop(api, currently_active_runs):
    # TODO: move to args and add filter
    runs = api.runs("fga/endovis")
    now_running = [run for run in runs if run.state == "running"]
    failed = [run for run in runs if run.state == "failed" or run.state == "crashed"]
    finished = [run for run in runs if run.state == "finished"]

    for run in now_running:
        process_running(run)

    for run in currently_active_runs:
        # TODO: are runs really hashable or do I need to check their IDs?
        if run not in now_running:
            if run in failed:
                process_freshly_failed(run)
            elif run in finished:
                process_finished(run)
            else:
                print(f"Run {run} has unhandled state {run.state}")
                continue

    return now_running

def main():
    api = wandb.Api()
    currently_active_runs = []

    while True:
        currently_active_runs = loop(api, currently_active_runs)
        time.sleep(10)

if __name__ == '__main__':

    # TODO: add readme about how to run (esp. to run with WANDB_API_KEY=xxx)
    # TODO: argparser
    main()