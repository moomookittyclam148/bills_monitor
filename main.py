from bills_monitor import bill_monitor

def main():
    try:
        bm = bill_monitor()
        bm.get_tmobile_bill()
    finally:
        bm.close_driver()

if __name__ == "__main__":
    main()
