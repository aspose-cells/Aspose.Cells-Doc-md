---
title: C++ kullanarak Excel dosyasını PDFA 1a ile uyumlu PDF formatına dönüştürün
linktitle: Excel Dosyasını PDFA 1a Uyumlu PDF Biçimine Dönüştürme
type: docs
weight: 130
url: /tr/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Aspose.Cells ile C++ kullanarak Excel dosyalarını PDF/A 1a uyumlu PDF formatına dönüştürmeyi öğrenin.
---

## **Olası Kullanım Senaryoları**

PDF/A, belgelerin uzun süreli korunması için tasarlanmış benzersiz bir PDF çeşididir. PDF/A, PDF'nin ISO standartlaştırılmış bir versiyonudur ve dokümanlarda kullanılan tüm yazı tiplerini gömülü olarak içeren arşivleme formatıdır. PDF/A, font bağlantısı (font gömme yerine) ve şifreleme gibi özellikleri engeller. Aspose.Cells, Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenize olanak tanır (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab ve PDF/A-3u desteklenir). Bu konu, Excel çalışma kitabını PDF/A uyumlu (PDF/A-1a) PDF dosyasına kaydetme adımlarını anlatır.

## **Excel dosyasını PDF/A-1a uyumlu PDF formatına dönüştürme**

Geliştiriciler, dönüştürme için farklı özellikleri ayarlamak üzere [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) sınıfını kullanabilir. [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) sınıfının farklı özelliklerini ayarlamak, çıktı PDF'sinin yazdırma, font, güvenlik ve sıkıştırma ayarları üzerinde kontrol sağlar. En önemli özellik, Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlayan [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/)'dir.

Aşağıdaki örnek kod, Excel dosyasını PDF/A-1a uyumlu PDF formatına dönüştürmenin nasıl yapıldığını açıklar. Lütfen [çıktı PDF](outputCompliancePdfA1a.pdf) ve referans için ekran görüntüsünü inceleyin.

## **Ekran Görüntüsü**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and add some message inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This PDF format is compatible with PDFA-1a.");

    // Create pdf save options and set its compliance to PDFA-1a
    PdfSaveOptions opts;
    opts.SetCompliance(PdfCompliance::PdfA1a);

    // Save the output pdf
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputCompliancePdfA1a.pdf", opts);

    std::cout << "PDF created successfully with PDFA-1a compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
