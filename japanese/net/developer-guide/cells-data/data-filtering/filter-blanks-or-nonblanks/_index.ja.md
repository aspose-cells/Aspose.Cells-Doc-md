---
title: 空白または非空白をフィルタリングする方法
type: docs
weight: 85
url: /ja/net/how-to-filter-blanks-and-non-blanks/
description: Aspose.Cells for .NET APIを使用して、空白や非空白をフィルタリングする方法について学びます。
keywords: 空白をフィルタリングし、非空白をフィルタリングし、ワークシート内の空白をフィルタリングし、ワークシート内の非空白をフィルタリングし、Excel内の空白をフィルタリングし、Excel内の非空白をフィルタリングし、Excel内の空白および非空白をフィルタリングする
---

## **可能な使用シナリオ**
Excelでのデータのフィルタリングは、ユーザーが基準に基づいて特定のデータサブセットに焦点を当てることを可能にし、全体的なデータの操作および解釈プロセスをより効率的かつ効果的にします。

## **Excelで空白または非空白をフィルタリングする方法**
Excelでは、フィルタリングオプションを使用して簡単に空白または非空白をフィルタリングすることができます。以下にその方法を示します。

### **Excelで空白をフィルタリングする方法**
1. 範囲を選択する: 列ヘッダーの文字をクリックして列全体を選択するか、空白をフィルタリングしたい範囲を選択します。
1. フィルタメニューを開く: リボンの"データ"タブに移動します。
<br>
<image src="1.png" width="70%" />
1. フィルタオプション: "フィルタ"ボタンをクリックします。これにより、選択した範囲にフィルタ矢印が追加されます。
1. 空白をフィルタリング: 空白をフィルタリングしたい列のフィルタ矢印をクリックします。"空白"以外のすべてのオプションを選択解除し、OKをクリックします。これにより、その列の空白のセルのみが表示されます。
<br>
<image src="2.png" width="70%" />
1. 結果は次のとおりです:
<br>
<image src="3.png" width="70%" />

### **Excelで非空白をフィルタリングする方法**
1. 範囲を選択する: 列ヘッダーの文字をクリックして列全体を選択するか、非空白をフィルタリングしたい範囲を選択します。
1. フィルタメニューを開く: リボンの"データ"タブに移動します。
<br>
<image src="1.png" width="70%" />
1. フィルタオプション: "フィルタ"ボタンをクリックします。これにより、選択した範囲にフィルタ矢印が追加されます。
1. ブランク以外をフィルタする: フィルタ矢印をクリックし、非ブランクをフィルタしたい列を選択します。"非ブランク"または"カスタム"以外のすべてのオプションを選択解除または条件を設定し、「OK」をクリックします。これにより、その列のブランクでないセルのみが表示されます。
<br>
<image src="4.png" width="70%" />
1. 結果は次のとおりです:
<br>
<image src="5.png" width="70%" />

## **Aspose.Cellsを使用してブランクをフィルタする方法**
特定の列にブランクが含まれており、フィルタリングが必要である場合は、[AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchblanks/)および[AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/addfilter/)関数を以下に示すように使用できます。 

[サンプルExcelファイル](sample.xlsx)を読み込み、ダミーデータを含むコード例をご覧ください。サンプルコードでは、ブランクをフィルタリングするための3つの方法を使用し、その後ブックを[output Excel file](FilteredBlanks.xlsx)として保存します。 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-blanks.cs" >}}

## **Aspose.Cellsを使用して非ブランクをフィルタする方法**

[サンプルExcelファイル](sample.xlsx)を読み込み、ダミーデータを含むコードの後、[AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchnonblanks/)関数を呼び出して非ブランクデータをフィルタリングし、最終的にブックを[output Excel file](FilteredNonBlanks.xlsx)として保存します。 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-non-blanks.cs" >}}

{{< app/cells/assistant language="csharp" >}}
