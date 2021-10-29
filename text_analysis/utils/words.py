# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/11/26 22:02
# @author   :Mo
# @function :stop_words of dict, from pkuseg
# @url      :https://github.com/lancopku/pkuseg-python


stop_words = {0: "…………………………………………………③", 1: "...................", 2: "......", 3: "关于具体地说", 4: "ＺＸＦＩＴＬ", 5: "）÷（１－",
              6: "－［＊］－", 7: "］∧′＝［", 8: "~~~~", 9: "与此同时", 10: "具体地说", 11: "具体说来", 12: "反过来说", 13: "另一方面", 14: "如上所述",
              15: "尽管如此", 16: "总的来看", 17: "总的来说", 18: "总的说来", 19: "总而言之", 20: "恰恰相反", 21: "换句话说", 22: "由此可见",
              23: "相对而言", 24: "综上所述", 25: "这么点儿", 26: "这就是说", 27: "除此之外", 28: "２．３％", 29: "Ｒ．Ｌ．", 30: "［①①］",
              31: "［①②］", 32: "［①③］", 33: "［①④］", 34: "［①⑤］", 35: "［①⑥］", 36: "［①⑦］", 37: "［①⑧］", 38: "［①⑨］",
              39: "［①Ａ］", 40: "［①Ｂ］", 41: "［①Ｃ］", 42: "［①Ｄ］", 43: "［①Ｅ］", 44: "［①ａ］", 45: "［①ｃ］", 46: "［①ｄ］",
              47: "［①ｅ］", 48: "［①ｆ］", 49: "［①ｇ］", 50: "［①ｈ］", 51: "［①ｉ］", 52: "［①ｏ］", 53: "［②①］", 54: "［②②］",
              55: "［②③］", 56: "［②⑤］", 57: "［②⑥］", 58: "［②⑦］", 59: "［②⑧］", 60: "［②⑩］", 61: "［②Ｂ］", 62: "［②Ｇ］",
              63: "［②ａ］", 64: "［②ｂ］", 65: "［②ｃ］", 66: "［②ｄ］", 67: "［②ｅ］", 68: "［②ｆ］", 69: "［②ｇ］", 70: "［②ｈ］",
              71: "［②ｉ］", 72: "［②ｊ］", 73: "［③①］", 74: "［③⑩］", 75: "［③Ｆ］", 76: "［③ａ］", 77: "［③ｂ］", 78: "［③ｃ］",
              79: "［③ｄ］", 80: "［③ｅ］", 81: "［③ｇ］", 82: "［③ｈ］", 83: "［④ａ］", 84: "［④ｂ］", 85: "［④ｃ］", 86: "［④ｄ］",
              87: "［④ｅ］", 88: "［⑤］］", 89: "［⑤ａ］", 90: "［⑤ｂ］", 91: "［⑤ｄ］", 92: "［⑤ｅ］", 93: "［⑤ｆ］", 94: "...", 95: "://",
              96: "Lex", 97: "exp", 98: "sub", 99: "sup", 100: "×××", 101: "———", 102: "∪φ∈", 103: "》），", 104: "一方面",
              105: "一转眼", 106: "不外乎", 107: "不尽然", 108: "不至于", 109: "与其说", 110: "且不说", 111: "为什么", 112: "乃至于",
              113: "之所以", 114: "于是乎", 115: "什么样", 116: "他们们", 117: "加当期", 118: "中列明", 119: "以至于", 120: "借傥然",
              121: "先不先", 122: "再其次", 123: "再者说", 124: "反过来", 125: "就是了", 126: "就是说", 127: "怎么办", 128: "怎么样",
              129: "换言之", 130: "没奈何", 131: "甚至于", 132: "简言之", 133: "紧接着", 134: "自个儿", 135: "自各儿", 136: "莫不然",
              137: "要不是", 138: "要不然", 139: "这一来", 140: "这么些", 141: "这么样", 142: "这会儿", 143: "那么些", 144: "那么样",
              145: "那会儿", 146: "难道说", 147: "０：２", 148: "１２％", 149: "５：０", 150: "［①］", 151: "［②④", 152: "［②］",
              153: "［③］", 154: "［④］", 155: "［⑤］", 156: "［⑥］", 157: "［⑦］", 158: "［⑧］", 159: "［⑨］", 160: "［⑩］",
              161: "［＊］", 162: "ｎｇ昉", 163: "--", 164: "..", 165: "./", 166: ".一", 167: ".数", 168: ".日", 169: "//",
              170: "::", 171: ">>", 172: "φ．", 173: "——", 174: "’‘", 175: "”，", 176: "……", 177: "′∈", 178: "′｜",
              179: "∈［", 180: "②ｃ", 181: "③］", 182: "──", 183: "〕〔", 184: "一.", 185: "一些", 186: "一何", 187: "一切",
              188: "一则", 189: "一旦", 190: "一来", 191: "一样", 192: "一般", 193: "万一", 194: "上下", 195: "不仅", 196: "不但",
              197: "不光", 198: "不单", 199: "不只", 200: "不如", 201: "不妨", 202: "不尽", 203: "不得", 204: "不怕", 205: "不惟",
              206: "不成", 207: "不拘", 208: "不料", 209: "不是", 210: "不比", 211: "不然", 212: "不特", 213: "不独", 214: "不管",
              215: "不若", 216: "不论", 217: "不过", 218: "不问", 219: "与其", 220: "与否", 221: "且说", 222: "两者", 223: "个别",
              224: "为了", 225: "为何", 226: "为止", 227: "为此", 228: "为着", 229: "乃至", 230: "之一", 231: "之类", 232: "乌乎",
              233: "也好", 234: "也罢", 235: "二来", 236: "于是", 237: "云云", 238: "云尔", 239: "人们", 240: "人家", 241: "什么",
              242: "介于", 243: "仍旧", 244: "从此", 245: "从而", 246: "他人", 247: "他们", 248: "以上", 249: "以为", 250: "以便",
              251: "以免", 252: "以及", 253: "以故", 254: "以期", 255: "以来", 256: "以至", 257: "以致", 258: "任何", 259: "任凭",
              260: "似的", 261: "但凡", 262: "但是", 263: "何以", 264: "何况", 265: "何处", 266: "何时", 267: "余外", 268: "作为",
              269: "你们", 270: "使得", 271: "例如", 272: "依据", 273: "依照", 274: "便于", 275: "俺们", 276: "倘使", 277: "倘或",
              278: "倘然", 279: "倘若", 280: "假使", 281: "假如", 282: "假若", 283: "光是", 284: "全体", 285: "全部", 286: "关于",
              287: "其一", 288: "其中", 289: "其二", 290: "其他", 291: "其余", 292: "其它", 293: "其次", 294: "兼之", 295: "再则",
              296: "再有", 297: "再者", 298: "再说", 299: "况且", 300: "几时", 301: "凡是", 302: "凭借", 303: "出于", 304: "出来",
              305: "分别", 306: "则甚", 307: "别人", 308: "别处", 309: "别是", 310: "别的", 311: "别管", 312: "别说", 313: "前后",
              314: "前此", 315: "前者", 316: "加之", 317: "加以", 318: "即令", 319: "即使", 320: "即便", 321: "即如", 322: "即或",
              323: "即若", 324: "又及", 325: "及其", 326: "及至", 327: "反之", 328: "反而", 329: "受到", 330: "另外", 331: "另悉",
              332: "只当", 333: "只怕", 334: "只是", 335: "只有", 336: "只消", 337: "只要", 338: "只限", 339: "叮咚", 340: "可以",
              341: "可是", 342: "可见", 343: "各个", 344: "各位", 345: "各种", 346: "各自", 347: "同时", 348: "后者", 349: "向使",
              350: "向着", 351: "否则", 352: "吧哒", 353: "呜呼", 354: "呵呵", 355: "呼哧", 356: "咱们", 357: "哈哈", 358: "哎呀",
              359: "哎哟", 360: "哪个", 361: "哪些", 362: "哪儿", 363: "哪天", 364: "哪年", 365: "哪怕", 366: "哪样", 367: "哪边",
              368: "哪里", 369: "哼唷", 370: "唯有", 371: "啪达", 372: "啷当", 373: "喔唷", 374: "嗡嗡", 375: "嘎登", 376: "嘿嘿",
              377: "因为", 378: "因了", 379: "因此", 380: "因着", 381: "因而", 382: "固然", 383: "在下", 384: "在于", 385: "基于",
              386: "处在", 387: "多么", 388: "多少", 389: "大家", 390: "她们", 391: "如上", 392: "如下", 393: "如何", 394: "如其",
              395: "如同", 396: "如是", 397: "如果", 398: "如此", 399: "如若", 400: "始而", 401: "孰料", 402: "孰知", 403: "宁可",
              404: "宁愿", 405: "宁肯", 406: "它们", 407: "对于", 408: "对待", 409: "对方", 410: "对比", 411: "尔后", 412: "尔尔",
              413: "尚且", 414: "就是", 415: "就算", 416: "就要", 417: "尽管", 418: "岂但", 419: "已矣", 420: "巴巴", 421: "并且",
              422: "庶乎", 423: "庶几", 424: "开外", 425: "开始", 426: "归齐", 427: "当地", 428: "当然", 429: "当着", 430: "彼时",
              431: "彼此", 432: "得了", 433: "怎么", 434: "怎奈", 435: "怎样", 436: "总之", 437: "惟其", 438: "慢说", 439: "我们",
              440: "或则", 441: "或是", 442: "或曰", 443: "或者", 444: "截至", 445: "所以", 446: "所在", 447: "所幸", 448: "所有",
              449: "才能", 450: "打从", 451: "抑或", 452: "按照", 453: "据此", 454: "接着", 455: "故此", 456: "故而", 457: "旁人",
              458: "无宁", 459: "无论", 460: "既往", 461: "既是", 462: "既然", 463: "时候", 464: "是以", 465: "是的", 466: "替代",
              467: "有些", 468: "有关", 469: "有及", 470: "有时", 471: "有的", 472: "朝着", 473: "本人", 474: "本地", 475: "本着",
              476: "本身", 477: "来着", 478: "来自", 479: "来说", 480: "极了", 481: "果然", 482: "果真", 483: "某个", 484: "某些",
              485: "某某", 486: "根据", 487: "正值", 488: "正如", 489: "正巧", 490: "正是", 491: "此地", 492: "此处", 493: "此外",
              494: "此时", 495: "此次", 496: "此间", 497: "毋宁", 498: "每当", 499: "比及", 500: "比如", 501: "比方", 502: "沿着",
              503: "漫说", 504: "然则", 505: "然后", 506: "然而", 507: "照着", 508: "犹且", 509: "犹自", 510: "甚且", 511: "甚么",
              512: "甚或", 513: "甚而", 514: "甚至", 515: "用来", 516: "由于", 517: "由是", 518: "由此", 519: "的确", 520: "的话",
              521: "直到", 522: "省得", 523: "眨眼", 524: "着呢", 525: "矣乎", 526: "矣哉", 527: "竟而", 528: "等到", 529: "等等",
              530: "类如", 531: "纵令", 532: "纵使", 533: "纵然", 534: "经过", 535: "结果", 536: "继之", 537: "继后", 538: "继而",
              539: "罢了", 540: "而且", 541: "而况", 542: "而后", 543: "而外", 544: "而已", 545: "而是", 546: "而言", 547: "能否",
              548: "自从", 549: "自后", 550: "自家", 551: "自己", 552: "自打", 553: "自身", 554: "至于", 555: "至今", 556: "至若",
              557: "般的", 558: "若夫", 559: "若是", 560: "若果", 561: "若非", 562: "莫如", 563: "莫若", 564: "虽则", 565: "虽然",
              566: "虽说", 567: "要不", 568: "要么", 569: "要是", 570: "譬喻", 571: "譬如", 572: "许多", 573: "设使", 574: "设或",
              575: "设若", 576: "诚如", 577: "诚然", 578: "说来", 579: "诸位", 580: "诸如", 581: "谁人", 582: "谁料", 583: "谁知",
              584: "贼死", 585: "赖以", 586: "起见", 587: "趁着", 588: "越是", 589: "较之", 590: "还是", 591: "还有", 592: "还要",
              593: "这个", 594: "这么", 595: "这些", 596: "这儿", 597: "这时", 598: "这样", 599: "这次", 600: "这般", 601: "这边",
              602: "这里", 603: "进而", 604: "连同", 605: "逐步", 606: "通过", 607: "遵循", 608: "遵照", 609: "那个", 610: "那么",
              611: "那些", 612: "那儿", 613: "那时", 614: "那样", 615: "那般", 616: "那边", 617: "那里", 618: "鄙人", 619: "鉴于",
              620: "针对", 621: "除了", 622: "除外", 623: "除开", 624: "除非", 625: "随后", 626: "随时", 627: "随着", 628: "非但",
              629: "非徒", 630: "非特", 631: "非独", 632: "顺着", 633: "首先", 634: "）、", 635: "＋ξ", 636: "＋＋", 637: "，也",
              638: "－β", 639: "－－", 640: "１．", 641: "＜±", 642: "＜Δ", 643: "＜λ", 644: "＜φ", 645: "＜＜", 646: "＝″",
              647: "＝☆", 648: "＝（", 649: "＝－", 650: "＝［", 651: "＝｛", 652: "＞λ", 653: "ＬＩ", 654: "［②", 655: "［－",
              656: "［］", 657: "］［", 658: "ａ］", 659: "ｂ］", 660: "ｃ］", 661: "ｅ］", 662: "ｆ］", 663: "｛－", 664: "｝＞",
              665: "～±", 666: "～＋", 667: """, 668: "#", 669: "$", 670: "%", 671: "&", 672: """, 673: "(", 674: ")",
              675: "*", 676: "+", 677: ",", 678: "-", 679: ".", 680: "/", 681: "0", 682: "1", 683: "2", 684: "3",
              685: "4", 686: "5", 687: "6", 688: "7", 689: "8", 690: "9", 691: ":", 692: ";", 693: "<", 694: "=",
              695: ">", 696: "?", 697: "@", 698: "A", 699: "[", 700: "\\", 701: "]", 702: "^", 703: "_", 704: "`",
              705: "|", 706: "}", 707: "~", 708: "·", 709: "×", 710: "Δ", 711: "Ψ", 712: "γ", 713: "μ", 714: "φ",
              715: "В", 716: "—", 717: "‘", 718: "’", 719: "“", 720: "”", 721: "…", 722: "℃", 723: "Ⅲ", 724: "↑",
              725: "→", 726: "≈", 727: "①", 728: "②", 729: "③", 730: "④", 731: "⑤", 732: "⑥", 733: "⑦", 734: "⑧",
              735: "⑨", 736: "⑩", 737: "■", 738: "▲", 739: "、", 740: "。", 741: "〈", 742: "〉", 743: "《", 744: "》",
              745: "」", 746: "『", 747: "』", 748: "【", 749: "】", 750: "〔", 751: "〕", 752: "㈧", 753: "一", 754: "、",
              755: "。", 756: "〈", 757: "〉", 758: "《", 759: "》", 760: "一", 761: "七", 762: "三", 763: "上", 764: "下",
              765: "不", 766: "与", 767: "且", 768: "个", 769: "中", 770: "临", 771: "为", 772: "乃", 773: "么", 774: "之",
              775: "乎", 776: "乘", 777: "九", 778: "也", 779: "了", 780: "二", 781: "于", 782: "五", 783: "些", 784: "亦",
              785: "人", 786: "什", 787: "今", 788: "仍", 789: "从", 790: "他", 791: "以", 792: "们", 793: "任", 794: "会",
              795: "但", 796: "何", 797: "你", 798: "使", 799: "依", 800: "俺", 801: "倘", 802: "借", 803: "做", 804: "像",
              805: "儿", 806: "八", 807: "六", 808: "兮", 809: "共", 810: "其", 811: "内", 812: "再", 813: "冒", 814: "冲",
              815: "几", 816: "凡", 817: "凭", 818: "分", 819: "则", 820: "别", 821: "到", 822: "即", 823: "却", 824: "去",
              825: "又", 826: "及", 827: "另", 828: "只", 829: "叫", 830: "可", 831: "各", 832: "同", 833: "后", 834: "向",
              835: "吓", 836: "吗", 837: "吧", 838: "含", 839: "吱", 840: "呀", 841: "呃", 842: "呕", 843: "呗", 844: "呜",
              845: "呢", 846: "呵", 847: "呸", 848: "咋", 849: "和", 850: "咚", 851: "咦", 852: "咧", 853: "咱", 854: "咳",
              855: "哇", 856: "哈", 857: "哉", 858: "哎", 859: "哗", 860: "哟", 861: "哦", 862: "哩", 863: "哪", 864: "哼",
              865: "唉", 866: "啊", 867: "啐", 868: "啥", 869: "啦", 870: "喂", 871: "喏", 872: "喽", 873: "嗡", 874: "嗬",
              875: "嗯", 876: "嗳", 877: "嘎", 878: "嘘", 879: "嘛", 880: "嘻", 881: "嘿", 882: "四", 883: "因", 884: "在",
              885: "地", 886: "多", 887: "大", 888: "她", 889: "好", 890: "如", 891: "宁", 892: "它", 893: "对", 894: "将",
              895: "小", 896: "尔", 897: "就", 898: "尽", 899: "己", 900: "已", 901: "巴", 902: "年", 903: "并", 904: "归",
              905: "当", 906: "彼", 907: "往", 908: "待", 909: "很", 910: "得", 911: "怎", 912: "您", 913: "我", 914: "或",
              915: "所", 916: "才", 917: "打", 918: "把", 919: "拿", 920: "按", 921: "据", 922: "故", 923: "无", 924: "既",
              925: "日", 926: "时", 927: "是", 928: "更", 929: "曾", 930: "替", 931: "最", 932: "月", 933: "有", 934: "望",
              935: "朝", 936: "本", 937: "来", 938: "某", 939: "欤", 940: "此", 941: "每", 942: "比", 943: "沿", 944: "焉",
              945: "照", 946: "用", 947: "由", 948: "的", 949: "看", 950: "着", 951: "矣", 952: "离", 953: "秒", 954: "第",
              955: "等", 956: "管", 957: "纵", 958: "经", 959: "给", 960: "者", 961: "而", 962: "能", 963: "腾", 964: "自",
              965: "至", 966: "致", 967: "若", 968: "虽", 969: "被", 970: "要", 971: "让", 972: "论", 973: "该", 974: "说",
              975: "请", 976: "诸", 977: "谁", 978: "赶", 979: "起", 980: "趁", 981: "距", 982: "跟", 983: "较", 984: "边",
              985: "过", 986: "还", 987: "这", 988: "连", 989: "那", 990: "都", 991: "阿", 992: "除", 993: "随", 994: "零",
              995: "非", 996: "靠", 997: "顺", 998: "︿", 999: "！", 1000: "＃", 1001: "＄", 1002: "％", 1003: "＆", 1004: "（",
              1005: "）", 1006: "＊", 1007: "＋", 1008: "，", 1009: "０", 1010: "１", 1011: "２", 1012: "３", 1013: "４",
              1014: "５", 1015: "６", 1016: "７", 1017: "８", 1018: "９", 1019: "：", 1020: "；", 1021: "＜", 1022: "＞",
              1023: "？", 1024: "＠", 1025: "［", 1026: "］", 1027: "｛", 1028: "｜", 1029: "｝", 1030: "～", 1031: "￥",
              1032: "︿", 1033: "！", 1034: "＃", 1035: "＄", 1036: "％", 1037: "＆", 1038: "＇", 1039: "（", 1040: "）",
              1041: "＊", 1042: "＋", 1043: "，", 1044: "－", 1045: "．", 1046: "／", 1047: "０", 1048: "１", 1049: "２",
              1050: "３", 1051: "４", 1052: "５", 1053: "６", 1054: "７", 1055: "８", 1056: "９", 1057: "：", 1058: "；",
              1059: "＜", 1060: "＝", 1061: "＞", 1062: "？", 1063: "＠", 1064: "Ａ", 1065: "［", 1066: "］", 1067: "＿",
              1068: "｛", 1069: "｜", 1070: "｝", 1071: "～", 1072: "￥", 1073: "\n", 1074: "", 1075: ",", 1076: " ",
              1077: ";", 1078: "!", 1079: "?", 1080: ". ", 1081: "'", 1082: "\"", 1083: "，"}

