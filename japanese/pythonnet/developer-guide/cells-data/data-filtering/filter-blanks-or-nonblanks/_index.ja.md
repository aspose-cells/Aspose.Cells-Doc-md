---
title: 空白または非空白をフィルタリングする方法
type: docs
weight: 85
url: /ja/python-net/how-to-filter-blanks-and-non-blanks/
description: Aspose.Cells for Python via .NET APIを使用して空白と非空白をフィルタリングする方法を学びます。
keywords: Python Excelライブラリ、Python空白をフィルタリング、Python非空白をフィルタリング、ワークシートでのPython空白をフィルタリング、エクセルでのPython非空白をフィルタリング、エクセルでのPython空白をフィルタリング、エクセルでのPython非空白をフィルタリング、エクセルでのPython空白および非空白のフィルタリング
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

## **Python Excel ライブラリ Aspose.Cells for Python Excel でのブランクのフィルタリング方法**
テキストが含まれる列で、いくつかのセルが空白であり、空白のセルのみを選択するためにフィルタリングが必要な場合、[AutoFilter.match_blanks(field_index)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/match_blanks/#int) および [AutoFilter.add_filter(field_index, criteria)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/add_filter/#int) 関数を以下で示すように使用できます。 

[サンプルExcelファイル](sample.xlsx)を読み込み、ダミーデータを含むコード例をご覧ください。サンプルコードでは、ブランクをフィルタリングするための3つの方法を使用し、その後ブックを[output Excel file](FilteredBlanks.xlsx)として保存します。 

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filter-blanks.py" >}}

## **Python Excel ライブラリ Aspose.Cells for Python Excel での空白でないセルのフィルタリング方法**

以下のサンプルコードでは、ダミーデータを含む [サンプル Excel ファイル](sample.xlsx) を読み込みます。 ファイルを読み込んだ後、 [AutoFilter.match_non_blanks(field_index)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/match_non_blanks/#int) 関数を呼び出して、空白でないデータをフィルタリングし、最後にブックを [出力 Excel ファイル](FilteredNonBlanks.xlsx) として保存します。 

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filter-non-blanks.py" >}}

{{< app/cells/assistant language="python-net" >}}
