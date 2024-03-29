import argparse
from bill_monitor import bill_monitor
from bill_monitor import Options

def main():
    try:
        argparser = argparse.ArgumentParser(description='Monitor my bills and give me alerts and stuff')
        argparser.add_argument('-H', '--headless', help='Run the scripts headless in chrome', action='store_true')
        argparser.add_argument('-AU', '--authfile', help='Supply user auth file. If none is given default in directory will be used', default='user_info.json')
        argparser.add_argument('-T', '--tmobile', help='Display T-mobile bill information', action='store_true')
        argparser.add_argument('-S', '--spectrum', help='Display Spectrum bill information', action='store_true')
        argparser.add_argument('-DA', '--displayall', help='Display all bill information', action='store_true')
        argparser.add_argument('-p', '--print', help='Display bill info collected', action='store_true')
        argparser.add_argument('-A', '--alert', help='Enable Alerting from text and email about bills due soon', action='store_true')
        args = argparser.parse_args()
        args = vars(args)

        if args['headless']:
            options = Options()
            options.headless = True
            options.add_argument('window-size=1920,1080')
            options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')
        else:
            options = Options()

        bm = bill_monitor(options)

        bm.read_json(args['authfile'])

        if args['tmobile']:
            bm.get_tmobile_bill()
        elif args['spectrum']:
            bm.get_spectrum_bill()
        elif args['displayall']:
            bm.get_all_bill_info()

        if args['print']:
            bm.display_bill_data()

        if args['alert']:
            print('Do alert stuff')
        else:
            print("Don't do alert stuff" )

    finally:
        bm.close_driver()

if __name__ == "__main__":
    main()
