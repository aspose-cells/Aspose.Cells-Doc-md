---
title: Her Çalışma Sayfasını Farklı PDF Dosyasına Kaydetme  C++ ile
linktitle: Her bir Çalışsayfayı Farklı Bir PDF Dosyasına Kaydet
type: docs
weight: 130
url: /tr/cpp/save-each-worksheet-to-a-different-pdf-file/
description: Her bir çalışma sayfasını ayrı bir PDF dosyasına kaydetmeyi Aspose.Cells for C++ kullanarak nasıl yapacağınızı öğrenin.
---

{{% alert color="primary" %}} 

Aspose.Cells, resimler, grafikler vb. içeren XLS dosyalarını PDF belgelerine dönüştürmeyi destekler. Aspose.Cells for C++, bir elektronik tablonun PDF'ye dönüştürülmesi için bağımsız olarak çalışabilir ve dönüştürme için Aspose.PDF for C++ kullanmanıza gerek yoktur. Dönüştürme, geçici dosyalar oluşturmadan veya kullanmadan tüm sürecin bellek içinde yapılabilmesiyle olasıdır.

{{% /alert %}} 

## **Her Çalışsayarı Farklı Bir PDF Dosyasına Kaydet**
Şablon Excel dosyanızdaki her çalışma sayfasını farklı PDF dosyaları oluşturmak için kaydetmeniz gerekiyorsa, bunu kolayca başarabilirsiniz. Bir seferde bir sheet indeksini [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) seçeneğiyle ayarlayarak PDF'ye dönüştürmeyi deneyebilirsiniz.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Get the Excel file path
    U16String filePath = srcDir + u"input.xlsx";

    // Instantiate a new workbook and open the Excel file from its location
    Workbook workbook(filePath);

    // Get the count of the worksheets in the workbook
    int sheetCount = workbook.GetWorksheets().GetCount();

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Take PDFs of each sheet
    for (int j = 0; j < sheetCount; j++)
    {
        Worksheet ws = workbook.GetWorksheets().Get(j);

        // Set worksheet to output
        SheetSet sheetSet(Vector<int32_t>{ ws.GetIndex() });
        pdfSaveOptions.SetSheetSet(sheetSet);

        // Save the workbook with the current worksheet as PDF
        workbook.Save(srcDir + u"worksheet-" + ws.GetName() + u".out.pdf", pdfSaveOptions);
    }

    std::cout << "PDFs generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

 Eğer çalışma sayfanız formüller içeriyorsa, çalışma sayfasını PDF formatına dönüştürmeden hemen önce [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) çağırmak en iyisidir. Bu, formüle bağlı değerlerin yeniden hesaplanmasını sağlar ve PDF'de doğru değerler gösterilir.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
