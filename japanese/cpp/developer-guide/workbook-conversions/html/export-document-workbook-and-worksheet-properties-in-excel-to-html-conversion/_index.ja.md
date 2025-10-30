---
title: ExcelからHTMLへの変換において、ドキュメント、ワークブック、ワークシートのプロパティをエクスポートまたはエクスポートしない方法
linktitle: ExcelからHTMLへの変換において、ドキュメント、ワークブック、ワークシートのプロパティをエクスポート
type: docs
weight: 50
url: /ja/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Aspose.Cells for C++を使用して、Excelファイルの変換時にドキュメント、ワークブック、ワークシートのプロパティをエクスポートまたは省略する方法を学びます。
---

## **可能な使用シナリオ**

Microsoft ExcelまたはAspose.Cellsを使用してExcelファイルをHTMLにエクスポートする際、さまざまな種類のドキュメント、ワークブック、ワークシートのプロパティもエクスポートされます（以下のスクリーンショット参照）。これらのプロパティのエクスポートを抑制するには、[**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportdocumentproperties/)、[**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/)、[**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) を **false** に設定します。デフォルトは **true** です。以下のスクリーンショットは、エクスポートされたHTML内のこれらのプロパティの見た目を示しています。

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **ExcelからHTMLへの変換でドキュメント、ワークブック、ワークシートのプロパティをエクスポート**

次のサンプルコードは、[サンプルExcelファイル](61767776.xlsx) を読み込み、ドキュメント、ワークブック、ワークシートのプロパティをエクスポートせずにHTMLに変換します（ [出力HTML](61767779.zip) 参照）。

## **サンプルコード**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html";

    // Load the sample Excel file
    Workbook workbook(inputFilePath);

    // Specify Html Save Options
    HtmlSaveOptions options;

    // We do not want to export document, workbook and worksheet properties
    options.SetExportDocumentProperties(false);
    options.SetExportWorkbookProperties(false);
    options.SetExportWorksheetProperties(false);

    // Export the Excel file to Html with Html Save Options
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file exported to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
