---
title: HTML保存時に非表示のワークシート内容をエクスポートしない設定（C++）
linktitle: 非表示のワークシート内容をエクスポートしない
type: docs
weight: 210
url: /ja/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Aspose.Cells for C++を使用して、ExcelワークブックをHTMLに保存するときに非表示のシート内容のエクスポートを防ぐ方法を学びます。
---

{{% alert color="primary" %}}

ExcelワークブックをHTMLに保存できます。ただし、ワークブックに非表示のワークシートが含まれている場合、Aspose.Cellsはデフォルトでは非表示のワークシートのコンテンツをHTML出力（_files）ディレクトリにエクスポートします。この方法で非表示のワークシートのコンテンツをエクスポートすることは適切ではありません。たとえば、非表示のワークシートにHTML出力ディレクトリにエクスポートされてはならない画像が含まれている場合などです。

{{% /alert %}}

Aspose.Cellsはプロパティ[**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexporthiddenworksheet/)を提供します。デフォルトでは、**true**に設定されており、非表示のワークシートがHTMLにエクスポートされます。**false**に設定すると、Aspose.Cellsは非表示のワークシート内容をエクスポートしません。

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
    U16String inputFilePath = srcDir + u"WorkbookWithHiddenContent.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"HtmlWithoutHiddenContent_out.html";

    // Create workbook object
    Workbook workbook(inputFilePath);

    // Create HTML save options
    HtmlSaveOptions options;

    // Do not export hidden worksheet contents
    options.SetExportHiddenWorksheet(false);

    // Save the workbook
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully without hidden content!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
