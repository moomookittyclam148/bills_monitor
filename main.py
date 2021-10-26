import argparse
from bill_monitor import bill_monitor

def main():
    try:
        argparser = argparse.ArgumentParser(description='Monitor my bills and give me alerts and stuff')
        add_argument('-H', '--headless', help='Run the scripts headless in chrome', action='store_true')
        add_argument('-T', '--tmobile', help='Display T-mobile bill information', action='store_true')
        add_argument('-DA', '--displayall', help='Display all bill information', action='store_true')
        add_argument('-A', '--alert', help='Enable Alerting from text and email about bills due soon', action='store_true')
        # bm = bill_monitor()
        # bm.read_json('user_info.json')
        # bm.get_tmobile_bill()
    finally:
        bm.close_driver()

if __name__ == "__main__":
    main()
