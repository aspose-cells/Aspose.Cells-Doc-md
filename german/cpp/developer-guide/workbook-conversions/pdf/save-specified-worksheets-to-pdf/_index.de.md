---  
title: Bestimmte Arbeitsblätter mit C++ in PDF speichern  
linktitle: Gewählte Arbeitsblätter als PDF speichern  
type: docs  
weight: 140  
url: /de/cpp/save-specified-worksheets-to-pdf/  
description: Spezifische Arbeitsblätter mit Aspose.Cells bei C++ in PDF exportieren.  
---  

Standardmäßig speichert Aspose.Cells alle **sichtbaren** Arbeitsblätter in einer Arbeitsmappe in eine PDF-Datei. Mit [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/)-Option können Sie bestimmte Arbeitsblätter in eine PDF-Datei speichern. z.B., Sie können das aktive Arbeitsblatt in PDF speichern, alle Arbeitsblätter (sichtbare und versteckte) in PDF speichern oder mehrere benutzerdefinierte Arbeitsblätter in PDF umwandeln.

## **Aktives Arbeitsblatt als PDF speichern**

Wenn Sie nur das aktive Blatt in PDF exportieren möchten, können Sie dies erreichen, indem Sie [**SheetSet.GetActive()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getactive/) an die [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/)-Option übergeben.

Das Blatt `Sheet2` ist das aktive Blatt der Quelldatei [sheetset-example.xlsx](sheetset-example.xlsx).

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

## **Alle Arbeitsblätter in PDF speichern**

[**SheetSet.GetVisible()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getvisible/) zeigt sichtbare Arbeitsblätter in einer Arbeitsmappe an, und [**SheetSet.GetAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getall/) umfasst alle Blätter, einschließlich sichtbarer und versteckter/invisibler Blätter. Wenn Sie alle Blätter in PDF exportieren möchten, können Sie einfach [**SheetSet.GetAll**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getall/) an [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/)-Option übergeben.

Die Quelldatei [sheetset-example.xlsx](sheetset-example.xlsx) enthält alle vier Blätter mit dem versteckten Blatt `Blatt3`.

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

## **Bestimmte Arbeitsblätter als PDF speichern**

Wenn Sie gewünschte/benutzerdefinierte mehrere Blätter in PDF exportieren möchten, können Sie dies erreichen, indem Sie mehrere Blattsindizes an [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) übergeben.

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

## **Arbeitsblätter nach PDF neu anordnen**

Wenn Sie Blätter in der Reihenfolge ändern möchten (z.B. in umgekehrter Reihenfolge), um sie in PDF zu speichern, ohne die Quelldatei zu modifizieren, können Sie dies erreichen, indem Sie umgeordnete Blattsindizes an [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) übergeben.

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

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
