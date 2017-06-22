import sqlite3



conn = sqlite3.connect('data.sqlite')

print ('Opened database successfully')

a='Paul'
b='32'
c='california'

str1 = "INSERT INTO data (input1,output1,output2) VALUES ('%s', '%s', '%s' )" %(a,b,c)

#strHello = "the length of (%s) is %d" %('Hello World',len('Hello World'))

d = {'key1' : a, 'key2' : b , 'key3' : c}
#a.append(dict(d))
#print (d)
str_sqlite = "INSERT INTO data (input1,output1,output2) VALUES ('%s', '%s', '%s' )" %(d["key1"],d["key2"],d["key3"])

str_sqlite1 = "INSERT INTO data (input1,output1,output2) VALUES ('https:////downsub.com//index.php?title=The+Real+Story+Behind+Donald+Trump/%27s+Wealth//&url=http/%3A/%2F/%2Fwww.youtube.com/%2Fapi/%2Ftimedtext/%3Fsignature/%3DE99869E7F8E0761CC477B01963C81FE441279B7C.5A3F95C9D2603449EF84D7DC0036D5C330453E97/%26sparams/%3Dasr/_langs/%2Ccaps/%2Cv/%2Cexpire/%26caps/%3Dasr/%26hl/%3Den/_US/%26asr/_langs/%3Des/%2Cru/%2Cde/%2Cko/%2Cit/%2Cpt/%2Cen/%2Cnl/%2Cja/%2Cfr/%26v/%3DEj1hlQgwXcA/%26key/%3Dyttt1/%26expire/%3D1498183703/%26kind/%3Dasr/%26lang/%3Den', 'English /(auto-generated)', '1
00:00:01,340 --> 00:00:03,710
everyone thinks they know Donald Trump

2
00:00:03,710 --> 00:00:06,570
<font color="#E5E5E5">Trump''s<//font><font color="#CCCCCC"> real-estate<//font><font color="#E5E5E5"> mogul Trump the<//font>

3
00:00:06,570 --> 00:00:09,240
reality<font color="#E5E5E5"> TV personality<//font><font color="#CCCCCC"> Trump''s and<//font>

4
00:00:09,240 --> 00:00:11,580
politician<font color="#E5E5E5"> but do you know how it all<//font>

5
00:00:11,580 --> 00:00:15,150
started<font color="#CCCCCC"> now Trump actually became Trump<//font>

6
00:00:15,150 --> 00:00:17,730
here''s the real<font color="#CCCCCC"> story behind<//font><font color="#E5E5E5"> how Donald<//font>

7
00:00:17,730 --> 00:00:20,250
Trump got<font color="#CCCCCC"> his wealth<//font><font color="#E5E5E5"> his successes and<//font>

8
00:00:20,250 --> 00:00:23,160
his failures<font color="#E5E5E5"> the story started well over<//font>

9
00:00:23,160 --> 00:00:25,380
a century<font color="#CCCCCC"> ago with Donald''s grandfather<//font>

10
00:00:25,380 --> 00:00:28,199
<font color="#CCCCCC">Fredrik Trump you see real<//font><font color="#E5E5E5"> estate runs<//font>

11
00:00:28,199 --> 00:00:29,910
deep in the blood<font color="#CCCCCC"> of<//font><font color="#E5E5E5"> the Trump<//font><font color="#CCCCCC"> family<//font>

12
00:00:29,910 --> 00:00:32,219
<font color="#E5E5E5">and Fredrik was actually the first Trump<//font>

13
00:00:32,219 --> 00:00:34,350
to own a hotel<font color="#E5E5E5"> during<//font><font color="#CCCCCC"> the famous<//font>

14
00:00:34,350 --> 00:00:36,870
<font color="#CCCCCC">Klondike Gold Rush<//font><font color="#E5E5E5"> in Canada Fredrik<//font>

15
00:00:36,870 --> 00:00:38,760
owned an inn<font color="#CCCCCC"> and restaurant that served<//font>

16
00:00:38,760 --> 00:00:41,249
gold miners when he passed<font color="#E5E5E5"> away he left<//font>

17
00:00:41,249 --> 00:00:43,350
<font color="#E5E5E5">an estate<//font><font color="#CCCCCC"> worth just<//font><font color="#E5E5E5"> under five hundred<//font>

18
00:00:43,350 --> 00:00:45,859
<font color="#E5E5E5">thousand in today''s dollars<//font><font color="#CCCCCC"> to his heirs<//font>

19
00:00:45,859 --> 00:00:49,229
<font color="#E5E5E5">his eldest son Fred Trump carried on the<//font>

20
00:00:49,229 --> 00:00:51,239
Trump legacy by going<font color="#E5E5E5"> into business with<//font>

21
00:00:51,239 --> 00:00:51,749
his mother

22
00:00:51,749 --> 00:00:53,809
using his<font color="#CCCCCC"> inheritance for seed money<//font>

23
00:00:53,809 --> 00:00:56,699
<font color="#E5E5E5">Fred became a very successful builder in<//font>

24
00:00:56,699 --> 00:00:59,010
New York City''s outer boroughs he built

25
00:00:59,010 --> 00:01:00,959
single-family houses in<font color="#E5E5E5"> Queens in the<//font>

26
00:01:00,959 --> 00:01:03,899
1920s<font color="#E5E5E5"> he helped pioneer the<//font><font color="#CCCCCC"> super market<//font>

27
00:01:03,899 --> 00:01:05,640
<font color="#E5E5E5">with the Trump market during the Great<//font>

28
00:01:05,640 --> 00:01:08,280
Depression<font color="#CCCCCC"> he even built barracks for<//font>

29
00:01:08,280 --> 00:01:11,579
the<font color="#E5E5E5"> Navy during<//font><font color="#CCCCCC"> World War Two but Fred''s<//font>

30
00:01:11,579 --> 00:01:14,909
real cash cow<font color="#E5E5E5"> came in 1949<//font><font color="#CCCCCC"> when<//font><font color="#E5E5E5"> he got a<//font>

31
00:01:14,909 --> 00:01:16,859
<font color="#E5E5E5">government loan to build Shore Haven<//font>

32
00:01:16,859 --> 00:01:19,140
<font color="#CCCCCC">apartments in Brooklyn the Federal<//font>

33
00:01:19,140 --> 00:01:21,210
Housing Administration paid him<font color="#E5E5E5"> ten<//font>

34
00:01:21,210 --> 00:01:23,789
point<font color="#CCCCCC"> three million dollars but he was<//font>

35
00:01:23,789 --> 00:01:25,289
able<font color="#CCCCCC"> to<//font><font color="#E5E5E5"> build the apartments for<//font>

36
00:01:25,289 --> 00:01:28,140
significantly less<font color="#E5E5E5"> the government kept<//font>

37
00:01:28,140 --> 00:01:30,179
<font color="#E5E5E5">overpaying for houses<//font><font color="#CCCCCC"> in Brooklyn and<//font>

38
00:01:30,179 --> 00:01:33,179
<font color="#CCCCCC">Queens<//font><font color="#E5E5E5"> and Fred kept<//font><font color="#CCCCCC"> building them<//font><font color="#E5E5E5"> Fred<//font>

39
00:01:33,179 --> 00:01:35,909
Trump was allegedly worth between 250

40
00:01:35,909 --> 00:01:38,700
and 300<font color="#CCCCCC"> million dollars by the<//font><font color="#E5E5E5"> time<//font><font color="#CCCCCC"> of<//font>

41
00:01:38,700 --> 00:01:42,030
<font color="#E5E5E5">his death in 1999 according to Donald<//font>

42
00:01:42,030 --> 00:01:43,799
<font color="#E5E5E5">his father was one<//font><font color="#CCCCCC"> of the biggest<//font>

43
00:01:43,799 --> 00:01:46,429
landlords in New York''s<font color="#E5E5E5"> outer boroughs<//font>

44
00:01:46,429 --> 00:01:49,619
<font color="#E5E5E5">born in Queens<//font><font color="#CCCCCC"> Donald Trump<//font><font color="#E5E5E5"> would join<//font>

45
00:01:49,619 --> 00:01:51,390
his father''s company<font color="#CCCCCC"> early on in his<//font>

46
00:01:51,390 --> 00:01:53,999
career<font color="#CCCCCC"> Donald had a different vision<//font><font color="#E5E5E5"> for<//font>

47
00:01:53,999 --> 00:01:56,340
<font color="#E5E5E5">the Trump name he envisioned<//font><font color="#CCCCCC"> the Trump<//font>

48
00:01:56,340 --> 00:01:58,100
brand<font color="#E5E5E5"> as being synonymous with luxury<//font>

49
00:01:58,100 --> 00:02:00,960
worldwide<font color="#E5E5E5"> using his dad''s business<//font>

50
00:02:00,960 --> 00:02:03,569
<font color="#E5E5E5">connections and<//font><font color="#CCCCCC"> creditworthiness Donald<//font>

51
00:02:03,569 --> 00:02:05,249
went into real estate<font color="#E5E5E5"> in<//font><font color="#CCCCCC"> Manhattan in<//font>

52
00:02:05,249 --> 00:02:09,149
the<font color="#CCCCCC"> mid<//font><font color="#E5E5E5"> 1970s<//font><font color="#CCCCCC"> he<//font><font color="#E5E5E5"> borrowed a small sum<//font><font color="#CCCCCC"> of<//font>

53
00:02:09,149 --> 00:02:12,720
1<font color="#E5E5E5"> million<//font><font color="#CCCCCC"> dollars to get started<//font><font color="#E5E5E5"> one<//font><font color="#CCCCCC"> of<//font>

54
00:02:12,720 --> 00:02:15,120
<font color="#CCCCCC">Trump''s first moves was also one of<//font><font color="#E5E5E5"> his<//font>

55
00:02:15,120 --> 00:02:18,390
biggest wins<font color="#E5E5E5"> in 1976 Donald Trump and<//font>

56
00:02:18,390 --> 00:02:20,459
Hyatt partnered to buy the<font color="#E5E5E5"> rundown<//font>

57
00:02:20,459 --> 00:02:22,830
Commodore<font color="#CCCCCC"> hotel near Grand Central<//font>

58
00:02:22,830 --> 00:02:23,489
Station

59
00:02:23,489 --> 00:02:25,530
at the time the whole neighborhood was

60
00:02:25,530 --> 00:02:27,930
<font color="#CCCCCC">in disarray with<//font><font color="#E5E5E5"> many nearby buildings<//font>

61
00:02:27,930 --> 00:02:30,510
on the verge of foreclosure<font color="#CCCCCC"> Trump<//font>

62
00:02:30,510 --> 00:02:32,730
negotiated contracts with banks<font color="#E5E5E5"> and the<//font>

63
00:02:32,730 --> 00:02:35,040
city<font color="#E5E5E5"> in an effort<//font><font color="#CCCCCC"> to fund the hotel<//font><font color="#E5E5E5"> and<//font>

64
00:02:35,040 --> 00:02:37,739
rejuvenate the area<font color="#CCCCCC"> the end result was<//font>

65
00:02:37,739 --> 00:02:40,680
the<font color="#CCCCCC"> grand hyatt a 25<//font><font color="#E5E5E5"> story hotel which<//font>

66
00:02:40,680 --> 00:02:43,049
<font color="#E5E5E5">Trump sold his share of for a hundred<//font>

67
00:02:43,049 --> 00:02:45,510
<font color="#E5E5E5">and forty two million dollars in 1996<//font>

68
00:02:45,510 --> 00:02:48,900
<font color="#E5E5E5">another big win for Trump was with 40<//font>

69
00:02:48,900 --> 00:02:50,819
Wall Street which<font color="#E5E5E5"> was once the<//font><font color="#CCCCCC"> tallest<//font>

70
00:02:50,819 --> 00:02:53,430
building in<font color="#CCCCCC"> the world<//font><font color="#E5E5E5"> he bought it for 1<//font>

71
00:02:53,430 --> 00:02:55,709
<font color="#E5E5E5">million<//font><font color="#CCCCCC"> dollars after<//font><font color="#E5E5E5"> years of vacancy<//font>

72
00:02:55,709 --> 00:02:58,019
today<font color="#CCCCCC"> its prime real estate in the<//font>

73
00:02:58,019 --> 00:03:00,720
financial district worth more<font color="#E5E5E5"> than<//font><font color="#CCCCCC"> 500<//font>

74
00:03:00,720 --> 00:03:03,750
million<font color="#E5E5E5"> dollars The Apprentice<//font><font color="#CCCCCC"> was<//font><font color="#E5E5E5"> also<//font>

75
00:03:03,750 --> 00:03:06,329
a financial<font color="#CCCCCC"> homerun as the show''s host<//font>

76
00:03:06,329 --> 00:03:09,180
and<font color="#CCCCCC"> executive producer<//font><font color="#E5E5E5"> Trump raked in 1<//font>

77
00:03:09,180 --> 00:03:11,430
million<font color="#E5E5E5"> dollars per show for a whopping<//font>

78
00:03:11,430 --> 00:03:13,230
<font color="#CCCCCC">total<//font><font color="#E5E5E5"> of a<//font><font color="#CCCCCC"> hundred<//font><font color="#E5E5E5"> and<//font><font color="#CCCCCC"> eighty-five<//font>

79
00:03:13,230 --> 00:03:16,019
episodes but like<font color="#E5E5E5"> many businessmen<//font>

80
00:03:16,019 --> 00:03:18,239
<font color="#E5E5E5">Trump''s career also had its share of<//font>

81
00:03:18,239 --> 00:03:21,150
<font color="#CCCCCC">failures Donald''s biggest failure may be<//font>

82
00:03:21,150 --> 00:03:23,549
his ill-fated venture into<font color="#CCCCCC"> casinos in<//font>

83
00:03:23,549 --> 00:03:26,310
Atlantic City<font color="#E5E5E5"> the bleeding started in<//font>

84
00:03:26,310 --> 00:03:28,530
1988 when<font color="#CCCCCC"> he acquired the<//font><font color="#E5E5E5"> Taj Mahal<//font>

85
00:03:28,530 --> 00:03:32,160
<font color="#E5E5E5">casino funded primarily by junk bonds<//font>

86
00:03:32,160 --> 00:03:34,109
the massive casino would<font color="#E5E5E5"> be three<//font>

87
00:03:34,109 --> 00:03:36,359
billion dollars in<font color="#CCCCCC"> debt<//font><font color="#E5E5E5"> within just a<//font>

88
00:03:36,359 --> 00:03:39,959
year<font color="#CCCCCC"> of opening<//font><font color="#E5E5E5"> Trump who racked up<//font><font color="#CCCCCC"> 900<//font>

89
00:03:39,959 --> 00:03:42,120
million<font color="#E5E5E5"> dollars<//font><font color="#CCCCCC"> in personal liabilities<//font>

90
00:03:42,120 --> 00:03:44,849
<font color="#E5E5E5">had the business declare bankruptcy<//font><font color="#CCCCCC"> to<//font>

91
00:03:44,849 --> 00:03:47,129
stay afloat<font color="#E5E5E5"> he ditched many personal<//font>

92
00:03:47,129 --> 00:03:50,609
assets such as his airline<font color="#CCCCCC"> a 282 foot<//font>

93
00:03:50,609 --> 00:03:52,799
mega yacht and half of his stake in<font color="#CCCCCC"> the<//font>

94
00:03:52,799 --> 00:03:55,769
company things were dire and<font color="#E5E5E5"> Trump''s dad<//font>

95
00:03:55,769 --> 00:03:58,019
chipped in with a<font color="#E5E5E5"> 3.5 million dollar<//font>

96
00:03:58,019 --> 00:04:00,870
loan in<font color="#E5E5E5"> the form of casino chips to help<//font>

97
00:04:00,870 --> 00:04:03,269
make a debt payment<font color="#E5E5E5"> Trump''s casino<//font>

98
00:04:03,269 --> 00:04:05,099
<font color="#E5E5E5">Holding Company would enter bankruptcy<//font>

99
00:04:05,099 --> 00:04:08,370
<font color="#E5E5E5">two additional times once in 2004 after<//font>

100
00:04:08,370 --> 00:04:11,400
accruing 1.8 billion in debt and again

101
00:04:11,400 --> 00:04:14,160
in 2009<font color="#E5E5E5"> after missing a bond payment<//font>

102
00:04:14,160 --> 00:04:16,589
during<font color="#E5E5E5"> the financial crisis each time<//font>

103
00:04:16,589 --> 00:04:19,470
<font color="#E5E5E5">Trump stake in the company fell while<//font>

104
00:04:19,470 --> 00:04:21,089
<font color="#E5E5E5">three of trumps four bankruptcies<//font>

105
00:04:21,089 --> 00:04:23,520
involved Atlantic City casinos<font color="#CCCCCC"> he has<//font>

106
00:04:23,520 --> 00:04:25,530
also<font color="#E5E5E5"> struggled in other ventures outside<//font>

107
00:04:25,530 --> 00:04:27,400
<font color="#E5E5E5">of real estate<//font>

108
00:04:27,400 --> 00:04:30,040
<font color="#CCCCCC">barré lines from<//font><font color="#E5E5E5"> vodka<//font><font color="#CCCCCC"> trump<//font><font color="#E5E5E5"> the game<//font>

109
00:04:30,040 --> 00:04:32,650
<font color="#CCCCCC">trump magazine<//font><font color="#E5E5E5"> Trump steaks and Trump<//font>

110
00:04:32,650 --> 00:04:35,710
University were all destined for failure

111
00:04:35,710 --> 00:04:38,380
Trump mortgages was launched in 2006

112
00:04:38,380 --> 00:04:40,570
<font color="#CCCCCC">right<//font><font color="#E5E5E5"> before the real estate crash and<//font>

113
00:04:40,570 --> 00:04:42,220
it also imploded

114
00:04:42,220 --> 00:04:44,710
according to Trump''s campaign<font color="#E5E5E5"> he is<//font>

115
00:04:44,710 --> 00:04:47,550
worth in excess<font color="#E5E5E5"> of ten<//font><font color="#CCCCCC"> billion dollars<//font>

116
00:04:47,550 --> 00:04:49,630
however he has been accused<font color="#CCCCCC"> of<//font>

117
00:04:49,630 --> 00:04:51,509
artificially inflating<font color="#CCCCCC"> his net worth<//font>

118
00:04:51,509 --> 00:04:54,370
<font color="#CCCCCC">Forbes and Bloomberg News<//font><font color="#E5E5E5"> both have<//font>

119
00:04:54,370 --> 00:04:56,259
<font color="#E5E5E5">drastically different estimates of his<//font>

120
00:04:56,259 --> 00:04:58,509
wealth using<font color="#CCCCCC"> the<//font><font color="#E5E5E5"> middle-of-the-road<//font>

121
00:04:58,509 --> 00:05:01,030
figure<font color="#E5E5E5"> from Forbes here is how Trump''s<//font>

122
00:05:01,030 --> 00:05:04,180
wealth breaks down about 7/%<font color="#CCCCCC"> of trumps<//font>

123
00:05:04,180 --> 00:05:06,310
net worth is in cash<font color="#E5E5E5"> in liquid assets<//font>

124
00:05:06,310 --> 00:05:09,669
<font color="#E5E5E5">such as investments<//font><font color="#CCCCCC"> 8 percent is in golf<//font>

125
00:05:09,669 --> 00:05:12,070
courses<font color="#CCCCCC"> and 4 percent is in his toys<//font>

126
00:05:12,070 --> 00:05:14,830
<font color="#E5E5E5">such as his helicopters<//font><font color="#CCCCCC"> penthouses or<//font>

127
00:05:14,830 --> 00:05:18,250
Boeing 757 the majority<font color="#CCCCCC"> however is in<//font>

128
00:05:18,250 --> 00:05:20,110
real estate<font color="#E5E5E5"> with<//font><font color="#CCCCCC"> manhattan properties<//font>

129
00:05:20,110 --> 00:05:22,660
<font color="#CCCCCC">alone making up about<//font><font color="#E5E5E5"> half of his total<//font>

130
00:05:22,660 --> 00:05:25,660
<font color="#CCCCCC">portfolio value<//font><font color="#E5E5E5"> now<//font><font color="#CCCCCC"> that you<//font><font color="#E5E5E5"> know the<//font>

131
00:05:25,660 --> 00:05:27,729
real story<font color="#CCCCCC"> behind Donald Trump''s wealth<//font>

132
00:05:27,729 --> 00:05:30,550
<font color="#E5E5E5">his successes and failures and the help<//font>

133
00:05:30,550 --> 00:05:32,650
he<font color="#E5E5E5"> got along the way it''s time to see<//font>

134
00:05:32,650 --> 00:05:35,380
how he<font color="#CCCCCC"> actually did as an investor go to<//font>

135
00:05:35,380 --> 00:05:37,870
the money project or our<font color="#E5E5E5"> YouTube channel<//font>

136
00:05:37,870 --> 00:05:40,000
to<font color="#E5E5E5"> subscribe and get our<//font><font color="#CCCCCC"> next video<//font>

137
00:05:40,000 --> 00:05:42,039
evaluating Trump''s investment return

138
00:05:42,039 --> 00:05:45,190
over<font color="#E5E5E5"> the years is he a great investor or<//font>

139
00:05:45,190 --> 00:05:47,409
did he just get lucky<font color="#CCCCCC"> find out in our<//font>

140
00:05:47,409 --> 00:00:00,000
<font color="#E5E5E5">next<//font><font color="#CCCCCC"> video<//font>

' )"

print (str_sqlite)

conn.execute(str_sqlite1)

conn.commit()
print ('Records created successfully')
conn.close()
