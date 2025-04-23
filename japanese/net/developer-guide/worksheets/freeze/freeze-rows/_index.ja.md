---
title: Excelワークシートの先頭行を凍結する
linktitle: 行を凍結
type: docs
weight: 190
url: /ja/net/how-to-freeze-rows-of-excel-worksheet
description: この記事では、.NET APIを使用してC#ライブラリをプログラムでExcelワークシートの先頭行を凍結する方法について学びます。
keywords: 上部行を固定、上部行を固定
---

## **紹介**

この記事では、上の行（複数）を固定する方法について学びます。共通の見出しの下に大量のデータがある場合、ワークシートを垂直にスクロールすると見出しが見えなくなることがあります。上の行（複数）を固定しておくと、残りのデータをスクロールしているときでもその固定された部分を見ることができます。

## **Excelで行を凍結する**

**![Excelで行を凍結](Freeze-Rows.png)**


1. 上部行を凍結したい場合は、まず、凍結する行の下にある行を選択します。
2. 表示 > ウィンドウ枠の固定をクリックします。
3. ドロップダウンメニューで「上部行を凍結」をクリックします。
4. 下にスクロールすると、最初の行が常に上部で表示されます。

**![行の凍結](Frozen-Row.png)**

見ての通り、1行目が凍結され、スクロールしても常に最上部に表示されます。

行を凍結すると、行ラベルを追跡することなく大きなデータを表示できます。




## **Aspose.Cells for .Netを使用した行の凍結**
Aspose.Cells for .Netで行（複数可）を凍結するのは簡単です。 
選択した行で行を凍結するには、[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) メソッドを使用してください。
1. ファイルを開くためにワークブックを作成します。または空のファイルを作成します。
2. Worksheet.FreezePanes() メソッドを使用して最初の行を凍結します。
3. ファイルを保存します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

添付の[サンプルソースExcelファイル](../Freeze.xlsx)。
{{< app/cells/assistant language="csharp" >}}
