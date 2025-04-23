---
title: Agregar línea de firma a la hoja de trabajo con C++
linktitle: Agregar línea de firma
type: docs
weight: 200
url: /es/cpp/add-signature-line/
description: Este artículo describe cómo agregar una línea de firma a la hoja de trabajo usando códigos C++ con Aspose.Cells for C++.
keywords: Agregar una línea de firma a la hoja de cálculo, Cómo agregar una línea de firma a la hoja de cálculo, Cómo agregar una línea de firma a la hoja de cálculo, Cómo agregar la línea de firma de la hoja de cálculo.
---

## **Introducción**

Aspose.Cells proporciona la propiedad [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) para agregar la línea de firma al documento de Excel.

## **Cómo agregar una línea de firma a la hoja de cálculo**

El siguiente código de ejemplo demuestra cómo usar la propiedad [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) para agregar la línea de firma de la hoja de trabajo. La captura de pantalla muestra el efecto del código de ejemplo en el archivo de Excel de ejemplo después de la ejecución.

![todo:image_alt_text](add-signature-line.png)

## **Código de muestra**

```cpp
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook wb;

    SignatureLine signatureLine;
    signatureLine.SetSigner(u"Aspose.Cells");
    signatureLine.SetTitle(u"signed by Aspose.Cells");

    wb.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, signatureLine);

    U16String certificatePath = srcDir + u"rsa2048.pfx";
    U16String password = u"123456";

    std::time_t now = std::time(nullptr);
    struct tm now_tm;
    localtime_s(&now_tm, &now);

    Date currentDate{
        now_tm.tm_year + 1900,
        now_tm.tm_mon + 1,
        now_tm.tm_mday,
        now_tm.tm_hour,
        now_tm.tm_min,
        now_tm.tm_sec,
        0
    };

    DigitalSignature signature(certificatePath, password, u"test Microsoft Office signature line", currentDate);

    DigitalSignatureCollection dsCollection;
    dsCollection.Add(signature);

    wb.SetDigitalSignature(dsCollection);

    U16String outputPath = srcDir + u"signatureLine.xlsx";
    wb.Save(outputPath);

    std::cout << "Workbook with signature line saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
