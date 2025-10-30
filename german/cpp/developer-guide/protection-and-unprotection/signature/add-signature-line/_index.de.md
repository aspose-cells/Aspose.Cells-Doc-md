---
title: Signaturlinie zum Arbeitsblatt mit C++ hinzufügen
linktitle: Unterschriftenzeile hinzufügen
type: docs
weight: 200
url: /de/cpp/add-signature-line/
description: Dieser Artikel beschreibt, wie man mit C++ Codes eine Unterschriftenzeile in das Arbeitsblatt mit Aspose.Cells for C++ hinzufügt.
keywords: Signaturlinie im Arbeitsblatt hinzufügen, Wie fügt man eine Signaturlinie im Arbeitsblatt hinzu, Wie fügt man eine Signaturlinie zum Arbeitsblatt hinzu, Wie fügt man die Signaturlinie zum Arbeitsblatt hinzu.
---

## **Einführung**

Aspose.Cells stellt die Eigenschaft [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) bereit, um die Signaturlinie des Arbeitsblatts hinzuzufügen.

## **Wie fügt man eine Signaturlinie zum Arbeitsblatt hinzu**

Das folgende Beispiel zeigt, wie man die Eigenschaft [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) nutzt, um die Unterschriftenzeile des Arbeitsblatts hinzuzufügen. Das Screenshot zeigt den Effekt des Beispielcodes auf die Beispieldatei nach der Ausführung.

![todo:image_alt_text](add-signature-line.png)

## **Beispielcode**

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
