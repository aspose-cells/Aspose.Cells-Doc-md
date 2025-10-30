---
title: Golang を使った C++ によるポイントを合計に設定する方法
linktitle: 合計としてポイントを設定する方法
description: 例えば、ウォーターフォールチャートなどの一部の Excel チャートでは、ポイントを合計として設定する必要があります。この記事では、 Golang と C++ を使った Aspose.Cells の使用方法について説明します。
keywords: ウォーターフォールチャート、ポイント、合計として設定。
type: docs
weight: 72
url: /ja/go-cpp/how-to-set-point-as-total/
---

## Excelチャートの「ポイントを合計に設定」とは

例えばウォーターフォールチャートのように、いくつかのポイントデータは前のポイントの合計になっています。このポイントを「合計に設定」する必要があります。サンプルコードと図解を以下に示します。

## ウォーターフォールチャートは「ポイントを合計に設定」する必要があります 

![todo:image_alt_text](set-as-total1.png)

この画像はExcelのウォーターフォールチャートです。 "Total"から始まる4つのデータポイントがあり、これらは前のデータポイントの合計を示しています。
この図では設定が正確ではありません。 "Total 2024"ポイントを選択すると、Excel内の"設定を合計にする"オプションがチェックされていないことが確認できます。
以下に修正が必要な[サンプルExcelファイル](SampleSheet.xlsx)を添付します。これをAspose.Cellsを使って正しく設定します。

## Aspose.Cellsを使用して「ポイントを合計に設定」 

正しい設定を行うためのコードは以下の通りです：

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetPointAsTotal.go" >}}
次の正しい[出力ファイル](output.xlsx)を取得できます。

図のように、4つの"合計"データポイントが正しく設定されているのが確認でき、前のチャートとの違いもわかります。

![todo:image_alt_text](set-as-total2.png)
