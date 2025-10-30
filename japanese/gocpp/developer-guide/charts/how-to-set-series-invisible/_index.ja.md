---
title: Golang を使った C++ によるシリーズの非表示設定方法
linktitle: シリーズを非表示にする方法
description: Excelチャートでシリーズを非表示にする必要がある場合があります。この記事では、Golongan を使用した C++ での Aspose.Cells の使い方について説明します。
keywords: Excelチャート、シリーズ、非表示、IsFiltered。
type: docs
weight: 74
url: /ja/go-cpp/how-to-set-series-invisible/
---

## Excelチャートでシリーズを非表示にする方法

Excelチャートでは、チャートを右クリックして「データの選択」をクリックし、表示・非表示の設定をチェック・解除できます。以下の[サンプルファイル](SeriesFiltered.xlsx)をダウンロードし、図のように操作してこの機能を実現できます。次に、Aspose.Cellsライブラリを使った方法をご説明します。

![todo:image_alt_text](series-invisible.png)

## Aspose.Cellsでシリーズを非表示に設定する方法 

Aspose.Cellsを使ってシリーズを非表示に設定するコードは以下の通りです：

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetSeriesInvisible.go" >}}
以下の[入力ファイル](SeriesFiltered.xlsx)と[出力ファイル](output.xlsx)を取得できます。

図のように、最初に表示されていた2つのシリーズが、出力ファイルで非表示になっています。  
![todo:image_alt_text](output.png)
