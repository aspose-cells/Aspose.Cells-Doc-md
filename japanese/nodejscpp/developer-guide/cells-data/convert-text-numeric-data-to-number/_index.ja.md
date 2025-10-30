---
title: テキスト数値データを数値に変換する
type: docs
weight: 900
url: /ja/nodejs-cpp/convert-text-numeric-data-to-number/
description: Excelのテキストとして保存された数値をAspose.Cells for Node.js via C++ APIを使用して数値に変換する方法を学びます。
keywords: エクセルのテキストを数字に変換、Node.js用のExcelのテキスト数字データを数値に変換するNode.jsコード、エクセルのテキスト数字データを数値に変換、Node.jsコード、エクセルの数値テキストを数値に変換、Node.jsコード、エクセルの数字文字列を数値に変換、Node.jsコード、Node.jsコードを使用したExcel内の数字テキストを数値に変換
---

## **可能な使用シナリオ**
時には、入力された数値データをテキストから数値に変換したい場合があります。Microsoft Excelでは、先頭にアポストロフィを付けて数字を入力することで、例：**'12345**、数字を文字列として扱います。Aspose.Cells for Node.js via C++を使用して文字列を数値に変換できます。


## Excel でテキストとして保存されている数値を数値に変換する方法
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

## Aspose.Cells for Node.js via C++を使ったテキストとして保存された数字を数値に変換する方法
Aspose.Cells for Node.js via C++は、すべての文字列またはテキスト形式の数値データを数値に変換できる[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#convertStringToNumericValue--)メソッドを提供します。

次のスクリーンショットは、セル **A1:A17** に文字列の数値を示しています。文字列の数値は左寄せされています。
<br>
<img src="5.png" width=70% />

次のスクリーンショットでは、[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#convertStringToNumericValue--) を使用して文字列の数値を数値に変換しました。これらは今、右寄せになっています。
<br>
<img src="6.png" width=70% />

## 文字列の数字データを実際の数値に変換するNode.jsコード

以下のサンプルコードは、すべてのワークシートの文字列数値データを実際の数値に変換する方法を示しています。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-ConvertTextNumericDatatoNumber.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
