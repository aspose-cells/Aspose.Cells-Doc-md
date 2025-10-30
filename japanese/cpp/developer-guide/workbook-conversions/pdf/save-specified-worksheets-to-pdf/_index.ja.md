---  
title: 指定したワークシートをPDFに保存（C++）  
linktitle: 指定されたワークシートをPDFに保存する  
type: docs  
weight: 140  
url: /ja/cpp/save-specified-worksheets-to-pdf/  
description: Aspose.Cellsを使用して、特定のワークシートをPDFにエクスポートします（C++）。  
---  

デフォルトでは、Aspose.Cellsはブック内のすべての**表示されている**ワークシートをPDFファイルに保存します。[**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/)オプションを使用すると、指定したワークシートをPDFファイルに保存できます。例えば、アクティブなワークシートのみをPDFに保存したり、すべてのワークシート（表示および非表示の両方）をPDFに保存したり、カスタムの複数のワークシートをPDFに保存したりすることが可能です。

## **アクティブワークシートをPDFに保存する**

アクティブシートのみをPDFにエクスポートしたい場合は、[**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/)に[**SheetSet.GetActive()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getactive/)を渡すことで実現できます。

シート「Sheet2」は、ソースファイル[sheetset-example.xlsx](sheetset-example.xlsx)のアクティブシートです。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Set active sheet to output
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(SheetSet::GetActive());

    // Save the pdf file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **すべてのワークシートをPDFに保存**

[**SheetSet.GetVisible()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getvisible/)はブック内の表示されているシートを示し、[**SheetSet.GetAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getall/)は表示されているシートと非表示/隠しシートの両方を含むすべてのシートを示します。すべてのシートをPDFにエクスポートしたい場合は、[**SheetSet.GetAll**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getall/)を[**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/)に渡すだけです。

ソースファイル [sheetset-example.xlsx](sheetset-example.xlsx) には、非表示シート `Sheet3` を含むすべての4つのシートが含まれています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
#include "Aspose.Cells/SheetSet.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template Excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Set all sheets to output
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(SheetSet::GetAll());

    // Save the PDF file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **指定されたワークシートをPDFに保存**

複数の目的のシートやカスタムシートをPDFにエクスポートしたい場合は、複数のシートインデックスを[**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/)に渡すことで実現できます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
#include "Aspose.Cells/SheetSet.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template Excel file
    U16String inputFilePath(u"sheetset-example.xlsx");
    Workbook workbook(inputFilePath);

    // Set custom multiple sheets (Sheet1, Sheet3) to output
    Vector<int32_t> sheetIndexes = {0, 2};
    SheetSet sheetSet(sheetIndexes);

    // Initialize PDF save options
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(sheetSet);

    // Save the PDF file with PdfSaveOptions
    U16String outputFilePath(u"output.pdf");
    workbook.Save(outputFilePath, pdfSaveOptions);

    std::cout << "Excel file saved as PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **ワークシートを並べ替えてPDFに変換**

ソースファイルを変更せずに、シートを逆順などに並べ替えてPDFにしたい場合は、並べ替えたシートインデックスを[**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/)に渡すことで実現できます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Reorder sheets (Sheet1, Sheet2, Sheet3, Sheet4) to (Sheet4, Sheet3, Sheet2, Sheet1)
    Vector<int32_t> sheetIndexes = { 3, 2, 1, 0 };
    SheetSet sheetSet(sheetIndexes);

    // Create PdfSaveOptions and assign the sheet set
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(sheetSet);

    // Save the pdf file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
