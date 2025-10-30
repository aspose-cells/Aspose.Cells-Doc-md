---
title: 空白または非空白をフィルタリングする方法
type: docs
weight: 85
url: /ja/nodejs-cpp/how-to-filter-blanks-and-non-blanks/
description: Aspose.Cells for Node.js via C++ APIを使用して空白と空白でないセルをフィルタリングする方法について学習します。
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

## **空白セルを【Aspose.Cells for Node.js via C++】でフィルタリングする方法**
列にテキストが含まれ、一部のセルが空白の場合に、その空白セルを含む行だけを選択するには、[**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchBlanks-number-)と[**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#addFilter-number-string-)関数を使用します。 

[サンプルExcelファイル](sample.xlsx)を読み込み、ダミーデータを含むコード例をご覧ください。サンプルコードでは、ブランクをフィルタリングするための3つの方法を使用し、その後ブックを[output Excel file](FilteredBlanks.xlsx)として保存します。 

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FilterBlanks.js" >}}


## **空白セル以外のセルを【Aspose.Cells for Node.js via C++】でフィルタリングする方法**

ダミーデータを含む[サンプルExcelファイル](sample.xlsx)をロードし、非空のデータをフィルタリングして[出力Excelファイル](FilteredNonBlanks.xlsx)として保存するサンプルコードを示します。 

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FilterNonBlanks.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
