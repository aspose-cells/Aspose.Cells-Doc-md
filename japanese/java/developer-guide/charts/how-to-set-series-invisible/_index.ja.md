---
title: シリーズを非表示にする方法
description: Excelチャートでは、シリーズを非表示に設定する必要があります。これをAspose.Cellsで行う方法について説明します。 
keywords: Excelチャート、シリーズ、非表示、IsFiltered。
type: docs
weight: 74
url: /ja/java/how-to-set-series-invisible/
---

## Excelチャートでシリーズを非表示にする方法

Excelのチャートでは、グラフを右クリックして「データの選択」をクリックし、ポップアップウィンドウでシリーズの表示/非表示をチェック・アンチェックして設定できます。
以下の[サンプルファイル](SeriesFiltered.xlsx)をダウンロードし、図のように操作してこの機能を実現します。次に、Aspose.Cellsライブラリを使った方法を紹介します。

![todo:image_alt_text](series-invisible.png)

## Aspose.Cellsでシリーズを非表示に設定する方法 

Aspose.Cellsを使ってシリーズを非表示に設定するコードは以下の通りです：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Set-series-invisible.java" >}}

以下の[入力ファイル](SeriesFiltered.xlsx)と[出力ファイル](output.xlsx)を取得できます。

図のように、最初に表示されていた2つのシリーズが、出力ファイルで非表示になっています。
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="java" >}}
