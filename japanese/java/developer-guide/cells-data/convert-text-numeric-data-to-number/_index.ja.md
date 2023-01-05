---
title: テキスト数値データを数値に変換する
type: docs
weight: 150
url: /ja/java/convert-text-numeric-data-to-number/
description: Aspose.Cells for Java API を使用して、テキストとして保存されている数値を数値に変換する方法を学びます。
keywords: excel convert text to number, excel convert text to number java, excel convert text numeric data to number, excel convert text numeric data to number java, excel convert numeric text to number, excel convert numeric text to number java, excel convert numeric text to number with java, convert numeric text to number in excel with java, convert numeric text to number in excel with java, convert numeric string to number in excel with java, excel convert text numeric data to number java, excel convert numeric string to number java
---
{{% alert color="primary" %}}

テキストとして入力された数値データを数値に変換したい場合があります。 Microsoft Excel では、数字の前にアポストロフィを付けることで、数字をテキストとして入力できます。たとえば、**'12345**.その後、Excel はその数値を文字列として扱います。 Aspose.Cells を使用すると、文字列を数値に変換できます。

{{% /alert %}}

Aspose.Cells for Java API は、[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) メソッドを使用して、すべての文字列またはテキストの数値データを数値に変換できます。

次のスクリーンショットは、セル内の文字列番号を示しています**A1:A17**.文字列番号は左揃えです。

**入力ファイル: テキスト文字列として入力された数値** 

![todo:画像_代替_文章](convert-text-numeric-data-to-number_1.png)

これらの文字列番号は、次を使用して数値に変換されています[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()次のスクリーンショットで。ご覧のとおり、右揃えになりました。

**出力ファイル: 文字列は数値に変換されています** 

![todo:画像_代替_文章](convert-text-numeric-data-to-number_2.png)

次のサンプル コードは、すべてのワークシートですべての文字列数値データを実際の数値に変換する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
