---
title: ExcelをHTMLに変換する際にDataBar、ColorScale、IconSetの条件付き書式をエクスポート
linktitle: 条件付き書式をHTMLにエクスポート
type: docs
weight: 30
url: /ja/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
description: Aspose.Cells for C++を使用して、Excelファイルの変換中にDataBar、ColorScale、IconSetの条件付き書式をエクスポートする方法を学びます。
---

{{% alert color="primary" %}} 

ExcelファイルをHTMLに変換する際にDataBar、ColorScale、IconSetの条件付き書式をエクスポートできます。この機能はMicrosoft Excelでも部分的にサポートされていますが、Aspose.Cells for C++は完全に対応しています。

{{% /alert %}} 

## **ExcelをHTMLに変換する際にDataBar、ColorScale、IconSetの条件付き書式をエクスポート**
次のスクリーンショットは、DataBar、ColorScale、IconSetの条件付き書式が設定された [サンプルExcelファイル](5115558.xlsx) を示しています。リンクからサンプルExcelファイルもダウンロード可能です。

![todo:image_alt_text](conversion_1.png)

このスクリーンショットは、DataBar、ColorScale、IconSetの条件付き書式を持つAspose.Cellsの出力HTMLファイルを示しています。見た目は [サンプルExcelファイル](5115558.xlsx) と完全に一致します。

![todo:image_alt_text](conversion_2.png)

### **サンプルコード**
以下のサンプルコードは、サンプルExcelファイルをHTMLに変換する例です。これは通常の [ExcelからHTMLへの変換](/cells/ja/cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml) です。

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
    U16String filePath = srcDir + u"sample.xlsx";

    // Load your sample excel file in a workbook object
    Workbook wb(filePath);

    // Save it in HTML format
    wb.Save(outDir + u"ConvertingToHTMLFiles_out.html", SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
