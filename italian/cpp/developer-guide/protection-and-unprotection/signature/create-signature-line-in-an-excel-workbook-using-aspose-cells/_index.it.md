---
title: Crea una riga di firma in un workbook Excel con C++ usando Aspose.Cells
linktitle: Creare una linea di firma in un Workbook Excel
type: docs
weight: 150
url: /it/cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: Questo articolo descrive come creare una riga di firma in un workbook Excel usando codici C++ con Aspose.Cells for C++.
keywords: Creare una linea di firma in un documento Excel, Come creare una linea di firma in un documento Excel, Come aggiungere una linea di firma, Come aggiungere una linea di firma a un file Excel.
---

## **Introduzione**

Microsoft Excel fornisce la funzionalità di aggiungere **Linea firma** in workbook Excel. È possibile aggiungere una linea di firma facendo clic sulla scheda **Inserisci** e quindi selezionando **Linea firma** dal gruppo **Testo**.

## **Come Creare una Linea di Firma per Excel**

Aspose.Cells fornisce anche questa funzionalità ed ha esposto la proprietà [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) a questo scopo. Questo articolo spiegherà come utilizzare questa proprietà per aggiungere una linea di firma utilizzando Aspose.Cells.

Il seguente codice di esempio aggiunge una linea di firma utilizzando la proprietà [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) e salva il workbook.

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

    // Create workbook object
    Workbook workbook;

    // Create signature line object
    SignatureLine s;
    s.SetSigner(u"John Doe");
    s.SetTitle(u"Development Lead");
    s.SetEmail(u"john.doe@aspose.com");

    // Adds a Signature Line to the worksheet.
    workbook.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, s);

    // Save the workbook
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully with signature line!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
