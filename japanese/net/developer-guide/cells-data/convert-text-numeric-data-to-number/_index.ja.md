---
title: テキスト数値データを数値に変換する
type: docs
weight: 900
url: /ja/net/convert-text-numeric-data-to-number/
description: Aspose.Cells for .NET API を使用して、Excel でテキストとして保存されている数字を数値に変換する方法を学びます。
keywords: excel テキストを数値に変換, excel テキストを数値に変換 c#, excel テキスト数値データを数値に変換, excel テキスト数値データを数値に変換 c#, excel 数値テキストを数値に変換, excel 数値テキストを数値に変換 c#, excel 数値テキストを数値に変換 c# で, 数値テキストを Excel で数値に変換する, 数値テキストを Excel で数値に変換する c#, 数値テキストを Excel で数値に変換する c#, 数値を Excel でテキストから数値に変換する, 数値を Excel でテキストから数値に変換する c#, excel テキスト数値データを数値に変換 c#, excel 数値をテキストから数値に変換 c#
---

## **可能な使用シナリオ**
時々、テキストとして入力された数値データを数値に変換したいと思うことがあります。Microsoft Excelでは、数字の前にアポストロフィを付けることでテキストとして数字を入力できます。たとえば**'12345**とします。そうすることでエクセルはその数字を文字列として扱います。Aspose.Cellsでは、文字列を数値に変換することができます。


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

## Aspose.Cells for .NET を使用してテキストとして保存されている数値を数値に変換する方法
Aspose.Cells は、[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue) メソッドを提供し、すべての文字列またはテキスト数字データを数値に変換するのに使用できます。

次のスクリーンショットは、セル **A1:A17** に文字列の数値を示しています。文字列の数値は左寄せされています。
<br>
<img src="5.png" width=70% />

次のスクリーンショットでは、[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue) を使用して文字列の数値を数値に変換しました。これらは今、右寄せになっています。
<br>
<img src="6.png" width=70% />

## テキスト形式の数値データを実際の数値に変換するための C# コード

以下のサンプルコードは、すべてのワークシートの文字列数値データを実際の数値に変換する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
{{< app/cells/assistant language="csharp" >}}
