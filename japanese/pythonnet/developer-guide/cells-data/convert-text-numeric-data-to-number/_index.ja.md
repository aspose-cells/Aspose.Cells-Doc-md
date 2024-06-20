---
title: テキスト数値データを数値に変換する
type: docs
weight: 900
url: /ja/python-net/convert-text-numeric-data-to-number/
description: Aspose.Cells for Python via .NET APIを使用して、Excelでテキストとして保存された数字を数値に変換する方法を学びます。
keywords: python excel テキストを数値に変換, python excel テキストを数値に変換, python excel テキスト数値データを数値に変換, python excel テキスト数値データを数値に変換, python excel 数値テキストを数値に変換, python excel 数値テキストを数値に変換, excel 数値テキストをpythonで数値に変換, pythonでexcelの数値テキストを数値に変換, pythonでexcelの数値テキストを数値に変換, python excelライブラリを使用してexcelの数値テキストを数値に変換, python excel テキスト数値データを数値に変換, python excel 数値文字列を数値に変換
---

## **可能な使用シナリオ**
時々、テキストとして入力された数値データを数値に変換したい場合があります。例えば**'12345**のように、Microsoft Excelで数値をテキストとして入力することができます。その場合、Excelはその数値を文字列として扱います。Aspose.Cells for Python via .NETでは、文字列を数値に変換することができます。


## **Excelでテキストとして保存された数値を数値に変換する方法**
いくつかの簡単な手順に従うことで、テキストとして保存された数値を数値に変換できます。
1. 左上隅にエラーインジケータが付いた単一のセルまたはセル範囲を選択します。
1. 選択したセルまたはセル範囲の隣に表示されるエラーボタンをクリックします。メニューで、**数値に変換**をクリックします。 
<br>
<img src="4.png" width=70% />
1. アラートボタンが利用できない場合は、この問題がある列を選択します。全列を変換したくない場合は、代わりに1つ以上のセルを選択できます。ただし、選択したセルが同じ列にあることを確認してください。そうでないと、このプロセスは機能しません。テキストを列分割ボタンは通常、列を分割するために使用されますが、単一のテキスト列を数値に変換するためにも使用できます。データタブで、テキストを列分割をクリックしてください。
<br>
<img src="1.png" width=70% />
1. ポップアップボックスの「完了」ボタンをクリックします。
<br>
<img src="2.png" width=70% />
1. テキストとして保存されている数値が数値に変換されます。
<br>
<img src="3.png" width=70% />

## **Aspose.Cells for Python Excelライブラリを使用して、テキストとして保存された数値を数値に変換する方法**
Aspose.Cells for Python via .NETは、すべての文字列やテキスト数値データを数値に変換するために使用できる[**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/)メソッドを提供しています。

次のスクリーンショットは、セル **A1:A17** に文字列の数値を示しています。文字列の数値は左寄せされています。
<br>
<img src="5.png" width=70% />

次のスクリーンショットでは、[**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) を使用して文字列の数値を数値に変換しました。これらは今、右寄せになっています。
<br>
<img src="6.png" width=70% />

## **文字列の数値データを実際の数値に変換するPythonコード**

以下のサンプルコードは、すべてのワークシートの文字列数値データを実際の数値に変換する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.py" >}}
