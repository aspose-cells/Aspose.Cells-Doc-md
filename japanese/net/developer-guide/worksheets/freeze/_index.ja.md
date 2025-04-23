---
title: Excelワークシートのウィンドウ枠の固定
linktitle: ウィンドウ枠の固定
type: docs
weight: 190
url: /ja/net/how-to-freeze-panes-of-excel-worksheet
description: この記事では、C#ライブラリと.NET APIを使用してExcelワークシートのウィンドウ枠をプログラムで固定する方法について学びます。
keywords: ウィンドウ枠の固定、ウィンドウの固定
---

## **紹介**

この記事では、ペインの固定方法を学びます。共通の見出しの下に大量のデータがあるときには、ワークシートをスクロールしても見出しを見ることができません。そして、各レコードには多くのデータが含まれています。ペインを固定すると、スクロールしても凍結された部分を見ることができます。上部行や最初の列のヘッダーを簡単に見ることができます。ペインを固定または解除すると、データ自体は変わらず、表示だけが変わります。

## **Excelで**

**![Excelでのウィンドウ枠の固定](Freeze-panes.png)**


1. ウィンドウ枠を固定し、行と列を固定する場合は、まずセルを選択します（例えばB2など）
2. 表示 > ウィンドウ枠の固定をクリックします。
3. ドロップダウンメニューで、ウィンドウ枠の固定をクリックします。
4. 下にスクロールするか、右にスクロールすると、最初の行と列が固定されます。

**![ウィンドウ枠の凍結](Frozen-Panes.png)**

1行目と列Aが凍結されていることがわかります。2行目は32で、2番目の表示可能な列はDです。 

ウィンドウ枠を固定すると、大きなデータを行または列のラベルを追跡せずに表示できます。




## **.NetのAspose.Cellsでウィンドウ枠を固定する**
Aspose.Cells for .Netでウィンドウ枠を簡単に固定できます。選択したセルでパネを固定するには、[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) メソッドを使用してください。
1. ファイルを開くためにワークブックを作成します。または空のファイルを作成します。
2. Worksheet.FreezePanes()メソッドを使用してウィンドウ枠を固定します。
3. ファイルを保存します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

添付 [サンプルExcelファイル](Freeze.xlsx)。
{{< app/cells/assistant language="csharp" >}}
