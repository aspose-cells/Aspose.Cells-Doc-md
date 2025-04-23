---
title: C++ ile Çalışma Sayfasına İmza Satırı Ekleme
linktitle: İmza Satırı Ekle
type: docs
weight: 200
url: /tr/cpp/add-signature-line/
description: Bu makale, C++ kodlarıyla ve Aspose.Cells for C++ kullanarak çalışma sayfasına imza satırı ekleme yöntemini anlatır.
keywords: Çalışma sayfasına imza çizgisi eklemek, çalışma sayfasına imza çizgisi eklemenin ve çalışma sayfasına imza çizgisi eklemenin nasıl yapılacağını açıklar.
---

## **Giriş**

Aspose.Cells, çalışma sayfasına imza satırı eklemek için [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) özelliğini sağlar.

## **Çalışma Sayfasına İmza Çizgisi Eklemek**

Aşağıdaki örnek kod, [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) özelliğini kullanarak çalışma sayfasının imza satırını nasıl ekleyeceğinizi gösterir. Ekran görüntüsü, kodun çalıştırıldıktan sonra örnek Excel dosyasına etkisini gösterir.

![todo:image_alt_text](add-signature-line.png)

## **Örnek Kod**

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
