---
title: Aggiungi riga di firma al foglio di lavoro con C++
linktitle: Aggiungi riga di firma
type: docs
weight: 200
url: /it/cpp/add-signature-line/
description: Questo articolo descrive come aggiungere una riga di firma al foglio di lavoro utilizzando codici C++ con Aspose.Cells for C++.
keywords: Aggiungere una linea di firma al foglio di lavoro, Come aggiungere una linea di firma al foglio di lavoro, Come aggiungere una linea di firma al foglio di lavoro, Come aggiungere la linea di firma del foglio di lavoro.
---

## **Introduzione**

Aspose.Cells fornisce la proprietà [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) per aggiungere la linea di firma del foglio di lavoro.

## **Come Aggiungere una Linea di Firma al Foglio di Lavoro**

Il seguente esempio di codice dimostra come usare la proprietà [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) per aggiungere la riga di firma del foglio di lavoro. Lo screenshot mostra l'effetto del codice di esempio sul file Excel di esempio dopo l'esecuzione.

![todo:image_alt_text](add-signature-line.png)

## **Codice di Esempio**

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
