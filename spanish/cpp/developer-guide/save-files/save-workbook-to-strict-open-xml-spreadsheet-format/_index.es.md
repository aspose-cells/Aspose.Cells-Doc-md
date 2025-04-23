---
title: Guardar libro de trabajo en formato de hoja de cálculo XML abierto estricto con C++
linktitle: Guardar libro de trabajo en formato de hoja de cálculo de Open XML estricto
type: docs
weight: 150
url: /es/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Aprenda cómo guardar un libro de trabajo en formato de hoja de cálculo XML abierto estricto usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Aspose.Cells le permite guardar el libro en formato *Strict Open XML Spreadsheet*. Para ello, proporciona la propiedad [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/). Si configura su valor como [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/), entonces el archivo Excel de salida se guardará en formato *Strict Open XML Spreadsheet*.

## **Guardar libro de trabajo en formato de hoja de cálculo de Open XML estricto**

El siguiente código de ejemplo crea un libro de trabajo y establece el valor de la propiedad [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/) como [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/) y lo guarda como [archivo Excel de salida](67338272.xlsx). Si abres el archivo Excel en Microsoft Excel y abres el cuadro de diálogo Guardar como..., verás su formato como *Strict Open XML Spreadsheet* como se muestra en esta captura de pantalla.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Specify - Strict Open XML Spreadsheet - Format
    wb.GetSettings().SetCompliance(OoxmlCompliance::Iso29500_2008_Strict);

    // Add message in cell B4 of first worksheet
    Cell b4 = wb.GetWorksheets().Get(0).GetCells().Get(u"B4");
    b4.PutValue(u"This Excel file has Strict Open XML Spreadsheet format.");

    // Save to output Excel file
    wb.Save(u"outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with Strict Open XML Spreadsheet format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
