---
title: テキストの数値データを数値に変換（C++）
linktitle: テキスト数値データを数値に変換する
type: docs
weight: 900
url: /ja/cpp/convert-text-numeric-data-to-number/
description: Excel内のテキストとして保存された数字をAspose.Cells for C++ APIを使用して数字に変換する方法を学びます。
keywords: excelでテキストを数字に変換、C++でテキストを数字に変換、Excelの数値テキストを数字に変換、C++で数値テキストを数字に変換、数字のテキストを数字に変換、C++で数値のテキストを数字に変換、Excelで数値テキストを数字に変換、Excelで数値の文字列を数字に変換
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

## Aspose.Cells for C++を使用した数値のテキストからの変換方法
Aspose.Cells は、[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/convertstringtonumericvalue/) メソッドを提供し、すべての文字列またはテキスト数字データを数値に変換するのに使用できます。

次のスクリーンショットは、セル **A1:A17** に文字列の数値を示しています。文字列の数値は左寄せされています。
<br>
<img src="5.png" width=70% />

次のスクリーンショットでは、[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/convertstringtonumericvalue/) を使用して文字列の数値を数値に変換しました。これらは今、右寄せになっています。
<br>
<img src="6.png" width=70% />

## 文字列の数値データを実数に変換するC++コード

以下のサンプルコードは、すべてのワークシートの文字列数値データを実際の数値に変換する方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate workbook object with an Excel file
    U16String inputFilePath = srcDir + u"SampleBook.xlsx";
    Workbook workbook(inputFilePath);

    // Iterate through all worksheets and convert string values to numeric
    for (int32_t i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        workbook.GetWorksheets().Get(i).GetCells().ConvertStringToNumericValue();
    }

    // Save the Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
