---
title: C++ ile Excel deki Çalışma Sayfalarının Mevcut PrinterSettings lerini Kaldırma
linktitle: Mevcut PrinterSettings leri Kaldırma
type: docs
weight: 60
url: /tr/cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Aspose.Cells kullanarak programlı şekilde Excel dosyası içindeki Çalışma Sayfasındaki mevcut PrinterSettings lerini kaldırmayı öğrenin.
keywords: Çalışma sayfasının yazıcı ayarlarını kaldırın c++, excel çalışma sayfası yazıcı ayarlarını kaldır c++
---

## **Olası Kullanım Senaryoları**
Bazı geliştiriciler, Excel'in kaydedilen XLSX dosyalarında yazıcı ayarlarındaki *.bin* dosyalarını önlemek isteyebilir. Yazıcı ayarları dosyaları, *“[file "root"]\xl\printerSettings”* altında bulunur. Bu belge, Aspose.Cells API'lerini kullanarak mevcut yazıcı ayarlarını nasıl kaldıracağınızı açıklar.

## **Excel dosyasındaki Mevcut Çalışma Sayfası Yazıcı Ayarlarını Kaldırma**
Aspose.Cells, Excel dosyasındaki farklı sayfalarda belirtilen mevcut yazıcı ayarlarını kaldırmanıza izin verir. Aşağıdaki örnek kod, çalışma kitabındaki tüm çalışma sayfaları için mevcut yazıcı ayarlarını kaldırmanın nasıl yapıldığını göstermektedir. Lütfen [örnek Excel dosyasını](45056020.xlsx), [çıktı Excel dosyasını](45056021.xlsx), konsol çıktısını ve referans için ekran görüntüsünü görün.

## **Ekran Görüntüsü**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Örnek Kod**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sampleRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    int sheetCount = wb.GetWorksheets().GetCount();

    for (int i = 0; i < sheetCount; i++)
    {
        Worksheet ws = wb.GetWorksheets().Get(i);
        PageSetup ps = ws.GetPageSetup();

        if (ps.GetPrinterSettings().GetLength() != 0)
        {
            std::cout << "PrinterSettings of this worksheet exist." << std::endl;
            std::cout << "Sheet Name: " << ws.GetName().ToUtf8() << std::endl;
            std::cout << "Paper Size: " << static_cast<int>(ps.GetPaperSize()) << std::endl;

            ps.SetPrinterSettings(Vector<uint8_t>());
            std::cout << "Printer settings of this worksheet are now removed by setting it null." << std::endl;
            std::cout << std::endl;
        }
    }

    wb.Save(outDir + u"outputRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Konsol Çıktısı**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
