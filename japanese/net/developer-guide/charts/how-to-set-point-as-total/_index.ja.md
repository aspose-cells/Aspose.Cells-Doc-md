---
title: 合計としてポイントを設定する方法
description: 一部のExcelチャート、例えばウォーターフォールチャートでは、ポイントを合計として設定する必要があります。この方法について、Aspose.Cellsを使用した手順を説明します。 
keywords: ウォーターフォールチャート、ポイント、合計として設定。
type: docs
weight: 72
url: /ja/net/how-to-set-point-as-total/
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

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Set-point-as-total.cs" >}}

次の正しい[出力ファイル](output.xlsx)を取得できます。

図のように、4つの"合計"データポイントが正しく設定されているのが確認でき、前のチャートとの違いもわかります。

![todo:image_alt_text](set-as-total2.png)
{{< app/cells/assistant language="csharp" >}}
