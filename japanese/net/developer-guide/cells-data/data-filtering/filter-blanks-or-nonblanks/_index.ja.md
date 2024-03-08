---
title: 空白または空白以外をフィルタリングする方法
type: docs
weight: 85
url: /ja/net/how-to-filter-blanks-and-non-blanks/
description: Aspose.Cells for .NET API を使用して空白と空白以外をフィルタリングする方法を学びます。
keywords: Filter Blanks, Filter Non-Blanks, Filter Blanks in worksheet, Filter Non-Blanks in worksheet, Filter Blanks in excel, Filter Non-Blanks in excel, Filter Blanks and Non-Blanks in excel
---
##  **考えられる使用シナリオ**
Excel でのデータのフィルター処理は、ユーザーが基準に基づいてデータの特定のサブセットに注目できるようにすることで、データの分析、調査、プレゼンテーションを強化し、全体的なデータの操作と解釈のプロセスをより効率的かつ効果的に行うことができる貴重なツールです。

##  **Excel で空白または空白以外をフィルタリングする方法**
Excel では、フィルター オプションを使用して、空白または空白以外を簡単にフィルターできます。その方法は次のとおりです。

###  **Excelで空白をフィルタリングする方法**
1. 範囲を選択する: 列ヘッダーの文字をクリックして列全体を選択するか、空白をフィルターする範囲を選択します。
1. フィルター メニューを開きます。リボンの [データ] タブに移動します。
<br>
<image src="1.png" width="70%" />
1. フィルター オプション: [フィルター] ボタンをクリックします。これにより、選択した範囲にフィルター矢印が追加されます。
1. 空白をフィルタリングする: 空白をフィルタリングする列のフィルタ矢印をクリックします。 「空白」を除くすべてのオプションの選択を解除し、「OK」をクリックします。これにより、その列の空白セルのみが表示されます。
<br>
<image src="2.png" width="70%" />
1. 結果は次のとおりです。
<br>
<image src="3.png" width="70%" />

###  **Excel で空白以外をフィルターする方法**
1. 範囲を選択する: 列ヘッダーの文字をクリックして列全体を選択するか、空白以外をフィルタリングする範囲を選択します。
1. フィルター メニューを開きます。リボンの [データ] タブに移動します。
<br>
<image src="1.png" width="70%" />
1. フィルター オプション: [フィルター] ボタンをクリックします。これにより、選択した範囲にフィルター矢印が追加されます。
1. 空白以外をフィルタリングする: 空白以外をフィルタリングする列のフィルタ矢印をクリックします。 「非空白」または「カスタム」を除くすべてのオプションの選択を解除し、それに応じて条件を設定します。 「OK」をクリックします。これにより、その列の空白でないセルのみが表示されます。
<br>
<image src="4.png" width="70%" />
1. 結果は次のとおりです。
<br>
<image src="5.png" width="70%" />

##  **Aspose.Cells を使用して空白をフィルタリングする方法**
列に空白のセルがほとんどないようなテキストが含まれており、空白のセルが存在する行のみを選択するためにフィルタが必要な場合、[AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchblanks/)そして[AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/addfilter/)以下に示すように関数を使用できます。

をロードする次のサンプルコードを参照してください。[サンプル Excel ファイル](sample.xlsx)いくつかのダミーデータが含まれています。サンプル コードでは、3 つの方法を使用して空白をフィルターします。次に、ワークブックを次のように保存します。[Excelファイルを出力](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-blanks.cs" >}}

##  **Aspose.Cells を使用して空白以外をフィルタリングする方法**

をロードする次のサンプルコードを参照してください。[サンプル Excel ファイル](sample.xlsx)いくつかのダミーデータが含まれています。ファイルをロードした後、[AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchnonblanks/)空白以外のデータをフィルタリングし、最後にワークブックを次の名前で保存する関数[Excelファイルを出力](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-non-blanks.cs" >}}

