---
title: Excel çalışma kitabını C++ kullanarak Ods, Sxc ve Fods (OpenOffice / LibreOffice hesap tablosu) formatlarına dönüştürme
linktitle: Ods
type: docs
weight: 20
url: /tr/cpp/convert-excel-to-ods/
description: Aspose.Cells kullanarak, Excel’i Ods (OpenOffice / LibreOffice Hesap Tablosu) veya Ods’yi (OpenOffice / LibreOffice Calc) Excel’e dönüştürme nasıl yapılır.
---

## **OpenDocument Hakkında**
[OpenDocument format (ODF)](https://en.wikipedia.org/wiki/OpenDocument), orijinal olarak Sun tarafından Open Office paketi için geliştirilen elektronik ofis belgeleri için ücretsiz ve açık bir dosya formatıdır. OpenDocument Spreadsheet (ODS), Excel belgelerinin dosya biçimidir. OpenDocument şu anda bir OASIS ve ISO standardıdır.

## **Ods (OpenOffice / LibreOffice calc)'i Excel'e dönüştür**
Aspose.Cells, Ods, Sxc ve Fods formatlarını yüklemeyi ve [Ods](book1.ods), [Sxc](book1.sxc) ve [Fods](book1.fods) dosyalarını Excel dosyalarına dönüştürmeyi destekler.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source ods file
    U16String odsFilePath(u"book1.ods");
    std::shared_ptr<Workbook> workbook = std::make_shared<Workbook>(odsFilePath);

    // Save as xlsx file
    U16String xlsxOutputPath(u"ods_out.xlsx");
    workbook->Save(xlsxOutputPath);

    // Load your source sxc file
    U16String sxcFilePath(u"book1.sxc");
    workbook = std::make_shared<Workbook>(sxcFilePath);

    // Save as xls file
    U16String xlsOutputPath(u"sxc_out.xls");
    workbook->Save(xlsOutputPath);

    // Load your source fods file
    U16String fodsFilePath(u"book1.fods");
    workbook = std::make_shared<Workbook>(fodsFilePath);

    // Save as xlsb file
    U16String xlsbOutputPath(u"fods_out.xlsb");
    workbook->Save(xlsbOutputPath);

    std::cout << "Files converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel'i Ods (OpenOffice / LibreOffice Calc)'e dönüştür**
Aspose.Cells, Excel dosyalarını Ods, Sxc ve Fods dosyalarına dönüştürmeyi destekler. Aşağıdaki kod örneği, [şablonu](book1.xlsx) Ods, Sxc ve Fods dosyalarına nasıl dönüştüreceğinizi gösterir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file 
    workbook.Save(u"Out.ods");

    // Save as sxc file 
    workbook.Save(u"Out.sxc");

    // Save as fods file 
    workbook.Save(u"Out.fods");

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [ODS Dosyasını ODF 1.1 ve 1.2 Özelliklerine Kaydetme](/cells/tr/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [ODS Dosyalarında Arkaplanla Çalışma](/cells/tr/cpp/working-with-background-in-ods-files/)
