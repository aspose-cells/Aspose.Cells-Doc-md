--- 
title: ExcelをHTMLに保存しながらコメントをエクスポート 
linktitle: Excel ファイルを HTML に保存する際にコメントをエクスポート 
type: docs 
weight: 40 
url: /ja/cpp/export-comments-while-saving-excel-file-to/ 
description: Aspose.CellsとC++を使用して、ExcelファイルをHTMLに保存する際にコメントをエクスポートする方法を学びます。 
--- 

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存する際にコメントはエクスポートされませんが、Aspose.Cellsはこの機能を [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/) プロパティで提供しています。これを **true** に設定すると、コメントもHTMLに表示されます。

## **ExcelファイルをHTMLに保存する際にコメントをエクスポート**

以下のサンプルコードは、[**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/) プロパティの使い方を説明しています。スクリーンショットは、設定を **true** にした場合のHTMLへの影響を示しています。参考のために [サンプルExcelファイル](50528260.xlsx) と [生成されたHTML](5052826.txt) をダウンロードしてください。

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleExportCommentsHTML.xlsx";
    Workbook workbook(inputFilePath);

    // Export comments - set IsExportComments property to true
    HtmlSaveOptions opts;
    opts.SetIsExportComments(true);

    // Save the Excel file to HTML
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outputDir + u"outputExportCommentsHTML.html", opts);

    std::cout << "Excel file exported to HTML with comments successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
