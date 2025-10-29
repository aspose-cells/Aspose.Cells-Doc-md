---
title: Добавить строку подписи в лист с помощью C++
linktitle: Добавить линию подписи
type: docs
weight: 200
url: /ru/cpp/add-signature-line/
description: Эта статья описывает, как добавить линию подписи в рабочий лист с помощью кода C++ и Aspose.Cells for C++.
keywords: Добавить строку подписи на рабочем листе, Как добавить строку подписи на рабочем листе, Как добавить строку подписи на рабочем листе, Как добавить строку подписи на рабочем листе.
---

## **Введение**

Aspose.Cells предоставляет свойство [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) для добавления строки подписи листа.

## **Как добавить строку подписи на рабочем листе**

Следующий пример кода демонстрирует, как использовать свойство [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) для добавления линии подписи в рабочий лист. Скриншот показывает эффект работы примера кода на тестовом файле Excel после выполнения.

![todo:image_alt_text](add-signature-line.png)

## **Образец кода**

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
