---
title: C++を使って、保存時に特定のUnicode文字だけのフォントを変更する方法
linktitle: Unicode文字のフォントを変更する
type: docs
weight: 260
url: /ja/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Aspose.Cellsを使用して、C++でPDFに保存する際に特定のUnicode文字のフォントを変更する方法を学びます。
---

{{% alert color="primary" %}}

一部のUnicode文字は、ユーザー指定のフォントでは表示されません。そのようなUnicode文字の1つが **Non-breaking Hyphen** (U+2011) で、Unicode番号は8209です。この文字は **Times New Roman** では表示できませんが、**Arial Unicode MS** のような他のフォントでは表示できます。

特定の単語や文章内にこのような文字が出現し、それがTimes New Romanのような特定のフォントである場合、Aspose.Cellsはその文字を表示できるフォント（Arial Unicode MSなど）に変換し、全体の単語や文章のフォントを変更します。

ただし、これは一部のユーザーにとって望ましくない動作であり、特定の文字だけのフォントを変更し、全体のフォントを変更しないようにしたい場合があります。

この問題に対処するために、Aspose.Cellsは`PdfSaveOptions.IsFontSubstitutionCharGranularity`プロパティを提供しており、これを`true`に設定すると、表示できない文字だけのフォントが置き換えられ、残りの部分は元のフォントのまま維持されます。

{{% /alert %}}

## **例**

以下のスクリーンショットは、以下のサンプルコードによって生成された2つの出力 PDF を比較しています。

一つは`PdfSaveOptions.IsFontSubstitutionCharGranularity`を設定しない状態で生成されたもので、もう一つは設定後に`true`にしたもので生成されたものです。

最初のPDFでは、ノンブレッディングハイフンのために全体のフォントがTimes New RomanからArial Unicode MSに変わっていますが、二つ目のPDFでは、ノンブレッディングハイフンだけのフォントが変更されています。

|**最初のPDFファイル**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**二つ目のPDFファイル**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **サンプルコード**

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

    // Create workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style style = cell1.GetStyle();
    style.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(style);
    cell2.SetStyle(style);

    // Put the values inside the cell
    cell1.PutValue(u"Hello without Non-Breaking Hyphen");
    cell2.PutValue(u"Hello\u2011 with Non-Breaking Hyphen");

    // Autofit the columns
    worksheet.AutoFitColumns();

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.pdf");

    // Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
    PdfSaveOptions opts;
    opts.SetIsFontSubstitutionCharGranularity(true);
    workbook.Save(outDir + u"SampleOutput2_out.pdf", opts);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
