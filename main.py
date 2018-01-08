#! /usr/bin/env python
import bt_client
#import google_sheets_client

def main():
    print 'getting ticker'
    print bt_client.get_ticker()
    #google_sheets_client.add_row()


if __name__ == '__main__':
    main()
