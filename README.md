1.程式功能:

此程式以單原子理想氣體為模型，提供使用者快速求得的其熱力學性質。
藉由使用者所提供的狀態和所要求的過程（如等壓、等體積、絕熱......)，而快速計算熱量、做功、內能變化量、焓、熵

2.技術原理：

本程式涵蓋以波以耳定律 (BOYLE'S LAW)、查理定律 (CHARLES'S LAW)、給呂薩克定律 (GAY-LUSSAC'S LAW)，以及亞佛加厥定律 (AVOGADRO'S LAW)所推得的理想氣體，再運用熱力學之理論公式計算。
熱量和做功的計算提供使用者多種熱力學過程（等壓、等體積、絕熱、等溫），分別套用其對公式計算。

A.熱量： 
Constant volume: q=nCvΔT
Constant pressure : q=nCpΔT
isothermal : q=nRln(V2/V1)
adiabatic : q=0


B.做功
Constant volume: w=0
Constant pressure : w=-PextΔV
isothermal : w=nRTln(V2/V1)
adiabatic : w=CvΔT

C.在能量計算中，單原子理想氣體之內能與焓僅與溫度有關，而其熱容（將物體或系統的溫度升高 1 攝氏度（或 1 K）所需吸收的熱量）
R(氣體常數)=8.314
Cv=3/2R
Cp=5/2R

D.藉由熱力學第一定律ΔU=q+w和理想氣體內能變化量公式求得其內能變化量和焓之值
ΔU=nCvΔT
ΔH=nCpΔT

E.熵的計算則依據其為狀態函數之性質，不計算其實際過程路徑，而用其初末狀態分別推得1.系統熵 2.環境熵 3.宇宙熵

(1.)系統熵

Constant volume: s=nCvln(T2/T1)
Constant pressure : s=nCpln(T2/T1)
reversible isothermal :s=nRln(V2/V1)
reversible adiabatic : s=0
free expension (adiabatic irreversible) : nRln(V2/V1)

(2.)環境熵
Constant volume: s=-qsys/T
Constant pressure : s=-qsys/T
reversible isothermal :s=-qsys/T
reversible adiabatic : s=0.0
free expension (adiabatic irreversible) : 0.0

（3.)宇宙熵
Suniv=Ssys+Ssurr


3.程式架構
列出主選單，供使用者選擇欲計算之熱力學性質
依所選性質提供對應之輸入項目
根據使用者所選之熱力學過程，進行條件判斷
套用相應之理論公式計算並輸出結果

4.開發過程
程式開發初期，先理解熱力學公式原理的推導，且熟悉各公式在不同過程下的計算方式與適用條件後，開始設計程式。

首先，講先將可提供使用者的選項分別列出，且提供使用者輸入。先以熱力學性計算模組化（例如：熱量、做功、內能變化、焓變化...）設計其對應計算架構。

第二步，依據過程類型（等溫、等壓、等容、絕熱、自由膨漲）建立對應熱力學公式，確認程式需計算的性質後，詢問使用者欲求得的狀態。

程式執行時，會根據使用者選擇，呼叫相對應公式，最後將其計算結果整理出並輸出給使用者。


5.資料來源
CENGAGE普通化學課本
https://zh.wikipedia.org/zh-tw/%E7%83%AD%E5%8A%9B%E5%AD%A6
https://case.ntu.edu.tw/CASTUDIO/Files/speech/Ref/CS0099S1B02_10.pdf
