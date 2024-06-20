---
title: Excelワークシートの最初の列を固定する
linktitle: 列を固定する
type: docs
weight: 190
url: /ja/net/how-to-freeze-columns-of-excel-worksheet
description: この記事では、C#ライブラリと.NET APIを使用してExcelワークシートの左側の列をプログラムで固定する方法について学びます。
keywords: 左列を固定し、最初の列を固定する、列をロックする
---

## **紹介**

この記事では、左の列（複数）を固定する方法について学びます。行に大量のデータがある場合、ワークシートを水平にスクロールすると左の列が見えなくなることがあります。最初の列（複数）を固定してロックすると、残りのデータをスクロールしているときでもその固定された部分を見ることができます。


## **Excelでの列の固定**

**![Excelで左列を固定する](freeze-columns.png)**


1. 左の列を固定したい列の下にある列をまず選択します
2. 表示 > ウィンドウ枠の固定をクリックします。
3. ドロップダウンメニューで「最初の列を固定」をクリックします。
4. 下にスクロールしても、最初の列が常に左側に表示されます。

**![固定された列](frozen-columns.png)**

1列が固定されている様子がわかります。横にスクロールしても、1列目は常に表示されます。

フリーズ列を使用すると、最初の列を追跡することなく長いデータを表示できます。




## **Aspose.Cells for .Netを使用した列の凍結**
Aspose.Cells for .Netで最初の列（複数可）を凍結するのは簡単です。 
選択した列で列を凍結するには、[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) メソッドを使用してください。
1. ファイルを開くためにワークブックを作成します。または空のファイルを作成します。
2. Worksheet.FreezePanes() メソッドを使用して最初の列を凍結します。
3. ファイルを保存します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

添付 [サンプルExcelファイル](Freeze.xlsx)。
