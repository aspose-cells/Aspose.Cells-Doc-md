---
title: テキスト数値データを数値に変換する
type: docs
weight: 150
url: /ja/java/convert-text-numeric-data-to-number/
description: Aspose.Cells for Java APIを使用して、テキストとして保存された数値を数値に変換する方法を学びます。
keywords: エクセルのテキストを数値に変換, エクセルのテキストを数値に変換java, エクセルのテキスト数値データを数値に変換, エクセルのテキスト数値データを数値に変換java, エクセルの数値テキストを数値に変換, エクセルの数値テキストを数値に変換java, エクセルの数値テキストをjavaで数値に変換, エクセルの数値テキストをjavaで数値に変換, エクセルの数値文字列をjavaで数値に変換, エクセルのテキスト数値データを数値に変換java, エクセルの数値文字列を数値に変換java
---

## **可能な使用シナリオ**
時々、テキストとして入力された数値データを数値に変換したいと思うことがあります。Microsoft Excelでは、数字の前にアポストロフィを付けることでテキストとして数字を入力できます。たとえば**'12345**とします。そうすることでエクセルはその数字を文字列として扱います。Aspose.Cellsでは、文字列を数値に変換することができます。


## エクセルのテキストとして保存された数値を数値に変換する
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

## Aspose.Cells for JAVAを使用してテキストとして保存されている数値を数値に変換する
Aspose.Cells for Java APIには、すべての文字列またはテキスト数値データを数値に変換するために使用できるメソッド [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue--) が提供されています。

次のスクリーンショットは、セル **A1:A17** に文字列の数値を示しています。文字列の数値は左寄せされています。
<br>
<img src="5.png" width=70% />

次のスクリーンショットでは、[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue--) を使用して文字列の数値を数値に変換しました。これらは今、右寄せになっています。
<br>
<img src="6.png" width=70% />

## Javaコード：文字列として保存されている数値データを実際の数値に変換する
以下のサンプルコードは、すべてのワークシートの文字列数値データを実際の数値に変換する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
