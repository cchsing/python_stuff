import re

def main(*args):
    testData = ["F1PRODDB 1521 NULL CIMB+ MYWCBPCDBMAPP03 2022-12-01 10:00:02  0.0000 GOOD 20.9000 GOOD -5.0000 GOOD 20.9000 GOOD 32.0000 GOOD",
                "F1PRODDB 1521 NULL CIMB+ MYWCBPCDBMAPP03 2022-12-01 10:04:52  0.0000 GOOD 20.9000 GOOD -5.0000 GOOD 20.9000 GOOD 30.0000 GOOD",
                "F1PRODDB 1521 NULL CIMB+ MYWCBPCDBMAPP03 2022-12-01 10:10:17  0.0063 GOOD 20.2258 GOOD 0.0063 GOOD 20.9000 GOOD 31.0000 GOOD",
                "F1PRODDB 1521 NULL CIMB+ MYWCBPCDBMAPP03 2022-12-01 10:14:53  0.0000 GOOD 20.9000 GOOD -5.0000 GOOD 20.9000 GOOD 32.0000 GOOD",
                "F1PRODDB 1521 NULL CIMB+ MYWCBPCDBMAPP03 2022-12-01 10:19:39  0.0000 GOOD 20.2667 GOOD -5.0000 GOOD 20.9000 GOOD 33.0000 GOOD",
                "F1PRODDB 1521 NULL CIMB+ MYWCBPCDBMAPP03 2022-12-01 10:24:43  0.0000 GOOD 20.9000 GOOD -5.0000 GOOD 20.9000 GOOD 30.0000 GOOD",
                "F1PRODDB 1521 NULL CIMB+ MYWCBPCDBMAPP03 2022-12-01 10:29:32  0.0000 GOOD 20.5677 GOOD -5.0000 GOOD 20.9000 GOOD 31.0000 GOOD",
                "F1PRODDB 1521 NULL CIMB+ MYWCBPCDBMAPP03 2022-12-01 10:34:34  0.0000 GOOD 20.9000 GOOD -5.0000 GOOD 20.9000 GOOD 30.0000 GOOD",
                "F1PRODDB 1521 NULL CIMB+ MYWCBPCDBMAPP03 2022-12-01 10:39:33  0.0031 GOOD 20.2469 GOOD 0.0031 GOOD 20.9000 GOOD 32.0000 GOOD"]
    testData_0 = testData[0]
    print(testData_0)
    # ^(.+?)\s+(.+?)\s+(.+?)\s+(.+?)\s+(.+?)\s+(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s+(.+?)\s+$
    match1 = re.search(r"^(.+?)\s+(.+?)\s+",testData_0)
    print(match1)
    match2 = re.search(r"^(.+?)\s+(.+?)\s+(.+?)\s+(.+?)\s+(.+?)\s+(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s+(.+)",testData_0)
    print(match2.group(1,2,3,4,5,6,7))
    data_split = match2.group(7).split()
    output = ''
    for i in range(6,len(testData_0),1):
        print(data_split[i-6])
    
        
    # for i in range(0,7,1):
    #     print(i)
    print(output)


if __name__ == "__main__":
    main()