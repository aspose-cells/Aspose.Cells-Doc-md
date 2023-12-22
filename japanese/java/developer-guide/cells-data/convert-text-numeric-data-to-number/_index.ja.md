---
title: テキスト数値データを数値に変換
type: docs
weight: 150
url: /ja/java/convert-text-numeric-data-to-number/
description: Aspose.Cells for Java API を使用して、テキストとして保存された数値を数値に変換する方法を学びます。
keywords: excel convert text to number, excel convert text to number java, excel convert text numeric data to number, excel convert text numeric data to number java, excel convert numeric text to number, excel convert numeric text to number java, excel convert numeric text to number with java, convert numeric text to number in excel with java, convert numeric text to number in excel with java, convert numeric string to number in excel with java, excel convert text numeric data to number java, excel convert numeric string to number java
---
##  **考えられる使用シナリオ**
テキストとして入力された数値データを数値に変換したい場合があります。 Microsoft Excel では、*'12345** のように、数字の前にアポストロフィを置くことで、数字をテキストとして入力できます。 Excel は数値を文字列として扱います。 Aspose.Cells を使用すると、文字列を数値に変換できます。


## テキストとして保存されている数値を Excel の数値に変換します
いくつかの簡単な手順に従って、テキストとして保存された数値を数値に変換できます。
1. 左上隅にエラー インジケーターがある単一のセルまたはセル範囲を選択します。
1. 選択したセルまたはセル範囲の横に表示されるエラー ボタンをクリックします。メニューで、「数値に変換」をクリックします。
<br>
<img src="4.png" width=70% />
1. アラート ボタンが使用できない場合は、この問題のある列を選択してください。列全体を変換したくない場合は、代わりに 1 つ以上のセルを選択できます。選択したセルが同じ列にあることを確認してください。そうでない場合、このプロセスは機能しません。 [テキストを列に変換] ボタンは通常、列を分割するために使用されますが、単一列のテキストを数値に変換するために使用することもできます。 [データ] タブで、[テキストを列に変換] をクリックします。
<br>
<img src="1.png" width=70% />
1. ポップアップボックスの「完了」ボタンをクリックします。
<br>
<img src="2.png" width=70% />
1. テキストとして保存された数値は数値に変換されます。
<br>
<img src="3.png" width=70% />

##  JAVA の Aspose.Cells を使用して、テキストとして保存された数値を数値に変換します
Aspose.Cells for Java API は、[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) すべての文字列またはテキスト数値データを数値に変換するために使用できるメソッド。

次のスクリーンショットは、セル *A1:A17** の文字列番号を示しています。文字列番号は左揃えになります。
<br>
<img src="5.png" width=70% />

これらの文字列数値は、次を使用して数値に変換されています。[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) 次のスクリーンショット。ご覧のとおり、右揃えになりました。
<br>
<img src="6.png" width=70% />

##  Java 文字列数値データを実際の数値に変換するコード
次のサンプル コードは、すべてのワークシート内のすべての文字列数値データを実際の数値に変換する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
