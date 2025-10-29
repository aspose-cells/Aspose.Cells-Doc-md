---
title: Ajouter une ligne de signature à la feuille de calcul avec C++
linktitle: Ajouter une ligne de signature
type: docs
weight: 200
url: /fr/cpp/add-signature-line/
description: Cet article décrit comment ajouter une ligne de signature à la feuille de calcul en utilisant des codes C++ avec Aspose.Cells for C++.
keywords: Ajouter une ligne de signature à la feuille de calcul, comment ajouter une ligne de signature à la feuille de calcul, comment ajouter une ligne de signature à la feuille de calcul, comment ajouter une ligne de signature à la feuille de calcul.
---

## **Introduction**

Aspose.Cells fournit la propriété [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) pour ajouter la ligne de signature de la feuille de calcul.

## **Comment ajouter une ligne de signature à la feuille de calcul**

 Le code d'exemple suivant montre comment utiliser la propriété [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) pour ajouter la ligne de signature de la feuille de calcul. La capture d'écran montre l'effet du code exemple sur le fichier Excel après exécution.

![todo:image_alt_text](add-signature-line.png)

## **Code d'exemple**

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
{{< app/cells/assistant language="cpp" >}}
