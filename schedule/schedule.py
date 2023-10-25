
# time of presentation
invited_t=45
normal_t =20
start_h = 9
start_t = 30
lunchi_t = 90
kyukei_t = 20



d = []


d+=[[" 但木謙一 "," 北海学園大学 "," I "," アルマ望遠鏡による遠方銀河観測 "]]
d+=[[" 喜友名正樹 "," 京都大学 "," N "," cold accretionと輻射フィードバックによる超大質量星形成 "]]
d+=[[" 東翔 "," 甲南大学 "," N "," Amplification and saturation of turbulent magnetic field in collapsing primordial gas clouds "]]
d+=[[" 鈴木悠太 "," 愛媛大学 "," N "," Quasar Environment and Feedback at z~2 Probed with Lyα Emitters and Continuum Selected Galaxies "]]
d+=[[" 佐藤恭輔 "," Hosei univ./NAOJ "," N "," すばる望遠鏡/HSC で探るこぐま座矮小楕円体銀河の形成メカニズム "]]
d+=[["rest"]]
d+=[[" 伊藤 茉那 "," 東北大学 "," N "," z>100の極初期宇宙における初代星の形成 "]]
d+=[[" 大向一行 "," 東北大学 "," I "," 宇宙初期の星形成 "]]
d+=[[" 尾形絵梨花 "," 筑波大学 "," N "," 遠方宇宙における超大質量ブラックホールの起源：浮遊する種ブラックホールの進化 "]]
d+=[[" 矢島秀伸 "," 筑波大学 "," I "," 超遠方銀河の形成過程：最新のシミュレーションと観測のレビュー "]]
d+=[[" 播金優一 "," 東京大学 "," I "," JWSTによる遠方銀河観測（TBD） "]]
d+=[["lunchi"]]
d+=[[" 倉田昂季 "," 甲南大学大学院 "," N "," 恒星風を考慮した星間物質降着による金属汚染により初代星が金属欠乏星になりうるか "]]
d+=[[" 稲吉恒平 "," 北京大学 "," I "," The assembly of first massive black holes and prospects of JWST observations "]]
d+=[[" 登口暁 "," 信州大学 "," N "," これまでの BluDOGs と JWST による high-z BluDOGs 研究 "]]
d+=[[" 中根美七海 "," 東京大学 "," N "," JWSTによる遠方銀河のLyα輝線観測で探る宇宙再電離 "]]
d+=[[" 仲野友将 "," 筑波大学 "," N "," 銀河衝突過程における多重AGN発現機構の解明 "]]
d+=[["next_day"]]
d+=[[" 竹内努 "," 名古屋大学素粒子宇宙物理学専攻 "," N "," High-Dimensional Statistical Analysis of Interstellar and Intergalactic Matter "]]
d+=[[" 山田麟 "," 名古屋大学 "," N "," 低金属量銀河WLMのCI観測: 観測の意義と戦略 "]]
d+=[[" 大森清顕クリストファ "," Nagoya University "," N "," Mergers and AGNs in the HSC-SSP: Do Mergers Trigger AGN Activity? "]]
d+=[[" 津久井崇史 "," Australian National University "," N "," Disk-driven galaxy transformation at z=4: insights from spatially resolved ALMA data "]]
d+=[[" 松木場亮喜 "," 京都大学 "," N "," 低金属量原始惑星系円盤におけるダストリング形成 "]]
d+=[[" 福井康雄 "," Nagoya University "," N "," 低金属量中間速度水素雲(IVC)とその起源 "]]

lists = []
days = ["11月20日(月)", "11月21日(火)", "11月22日(水)"]

iday = 0
lists += ["<span style=\"font-size: 150%; color: black;\">"+days[iday]+"</span><br><br>"]

def get_start_time(time):
  time_h = int((time+start_t) / 60) + start_h
  time_t = time+start_t - 60*(time_h-start_h)
  return str(time_h).zfill(2)+":"+str(time_t).zfill(2)

get_start_time(100)

time = 0
for i in range(len(d)):

  if(d[i][0] == "lunchi"):
    tstr = get_start_time(time)
    lists += [tstr+" 昼食<br>"]
    time += lunchi_t
    continue

  if(d[i][0] == "rest"):
    tstr = get_start_time(time)
    lists += [tstr+" 休憩<br>"]
    time += kyukei_t
    continue

  if(d[i][0] == "next_day"):
    lists += ["\n"]
    iday  += 1
    lists += ["<span style=\"font-size: 150%; color: black;\">"+days[iday]+"</span><br><br>"]
    time = 0
    continue

  
  if(d[i][2].replace(' ', '') == "I"):
    invite = True
  else:
    invite = False

  tstr = get_start_time(time)

  if invite:
    time += invited_t
  else:
    time += normal_t


  if invite:
    lists += [tstr+" I"+ d[i][0].replace(' ', '')+ " (" + d[i][1].replace(' ', '')+") "+  d[i][3] +"<br>"]
  else:
    lists += [tstr+" "+ d[i][0].replace(' ', '')+ " (" + d[i][1].replace(' ', '')+") "+  d[i][3] +"<br>"]

filename = "program.md"
f = open(filename, 'w')
for lis in lists:
    f.write(lis)
    f.write("\n")
f.close()
