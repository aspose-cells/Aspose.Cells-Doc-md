---
title: Specificare i separatori decimali e di gruppo personalizzati per il workbook con C++
linktitle: Specificare i separatori decimali e di gruppo personalizzati
type: docs
weight: 110
url: /it/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Modificare il separatore decimale e di gruppo in MS Excel e con codice C++ utilizzando l API di Aspose.Cells for C++.
keywords: specificare separatore decimale personalizzato excel, specificare separatore decimale personalizzato C++, specificare separatore di gruppo personalizzato excel, specificare separatore di gruppo personalizzato C++, specificare separatore decimale e di gruppo personalizzato excel, specificare separatore decimale e di gruppo personalizzato C++, cambiare separatore decimale in excel, cambiare separatore di gruppo in excel, cambiare separatore decimale in excel C++, cambiare separatore di gruppo in excel C++
---

{{% alert color="primary" %}}

In Microsoft Excel, è possibile specificare i separatori decimali e migliaia personalizzati invece di utilizzare i separatori di sistema dalle **Opzioni Avanzate di Excel** come mostrato nella schermata sottostante.

Aspose.Cells fornisce le proprietà [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumberdecimalseparator/) e [**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) per impostare i separatori personalizzati per la formattazione/analisi dei numeri.

{{% /alert %}}

## **Specificare i Separatori Personalizzati utilizzando Microsoft Excel**

La seguente schermata mostra le **Opzioni Avanzate di Excel** e evidenzia la sezione per specificare i **Separatori Personalizzati**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Specificare separatori personalizzati utilizzando Aspose.Cells**

Il seguente codice di esempio illustra come specificare i separatori personalizzati utilizzando l'API Aspose.Cells. Specifica i separatori personalizzati per il numero decimale e per il raggruppamento come rispettivamente punto e spazio.

### Codice C++ per specificare separatori decimali e di gruppo personalizzati

```cpp
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

    // Create a new workbook
    Workbook workbook;

    // Specify custom separators
    workbook.GetSettings().SetNumberDecimalSeparator(u'.');
    workbook.GetSettings().SetNumberGroupSeparator(u' ');

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set cell value
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(123456.789);

    // Set custom cell style
    Style style = cell.GetStyle();
    style.SetCustom(u"#,##0.000;[Red]#,##0.000", true);
    cell.SetStyle(style);

    // Auto-fit columns
    worksheet.AutoFitColumns();

    // Save workbook as PDF
    workbook.Save(outDir + u"CustomSeparator_out.pdf");

    std::cout << "Workbook saved successfully with custom separators!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
