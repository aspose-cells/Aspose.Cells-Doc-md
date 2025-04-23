---
title: C++を使用したAspose.Cellsによる出力PDFでUnicode補助文字をレンダリング
linktitle: Unicode補助文字をレンダリング
type: docs
weight: 350
url: /ja/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Aspose.Cells for C++を使用して、出力PDFにUnicode補助文字をレンダリングする方法を学びます。
---

{{% alert color="primary" %}}

通常のUnicode文字は2バイトであり、Unicode補助文字は4バイトです。Aspose.Cells はこれらの4バイトのUnicode文字のレンダリングをサポートしています。

Unicode文字標準では、補助文字はU+10000からU+10FFFFまでのコードポイントが割り当てられています。つまり、これらはU+FFFFよりも大きいUnicode文字です。

- UTF-8では、これらの文字はそれぞれ4バイトです。
- UTF-16では、これらの文字は2つのサロゲート（16ビットユニット）が必要です。

{{% /alert %}}

##Aspose.Cellsによる出力PDFでUnicode上位文字をレンダリングする

下記のスクリーンショットは、Aspose.Cellsが[ソースExcelファイル](5115563.xlsx)を[出力PDF](5115564.pdf)にレンダリングした様子を示しています。すべての3つのUnicode上位文字は、Microsoft Excelによって行われるのと同じように正確にレンダリングされています。

![todo:image_alt_text](output.png)

## サンプルコード

[ソースExcelファイル](5115563.xlsx)を[出力PDF](5115564.pdf)に変換するためのサンプルコードを使用できます。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"unicode-supplementary-characters.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"RenderUnicodeInOutput_out.pdf";

    // Load the source excel file containing Unicode Supplementary characters
    Workbook wb(inputFilePath);

    // Save the workbook as PDF
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully with Unicode Supplementary characters!" << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```
