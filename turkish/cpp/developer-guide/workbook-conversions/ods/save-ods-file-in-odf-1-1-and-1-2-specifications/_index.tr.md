---
title: C++ ile ODS Dosyasını ODF 1.1, 1.2 ve 1.3 Özellikleriyle Kaydet
linktitle: ODF 1.1, 1.2 ve 1.3 olarak Kaydet
description: Aspose.Cells kullanarak Excel i ODF 1.1, 1.2 ve 1.3 Özellikleriyle Dönüştür.
type: docs
weight: 230
url: /tr/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells, ODS dosyasını (**OpenDocument Elektronik Tablo**) ODF (**OpenDocument Format**) 1.1, 1.2 ve 1.3 spesifikasyonlara kaydetmeyi destekler. Aspose.Cells'in [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells/odssaveoptions/getodfstrictversion/) özelliği, ODS dosyalarını kaydetmek için ODF sürümünü belirler. Bu özellik varsayılan olarak [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/)'dir, bu yüzden bu ayar olmadan kaydedilen ODS dosyası 1.2 spesifikasyonunu kullanır.

{{% /alert %}}

Aşağıdaki örnek kod, bir çalışma kitabı nesnesi oluşturur, ilk sayfadaki A1 hücresine bazı değerler ekler ve ardından ODS dosyasını ODF 1.1, 1.2 ve 1.3 spesifikasyonlarıyla kaydeder. Varsayılan olarak, ODS dosyası ODF 1.2 spesifikasyonu ile kaydedilir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some value in cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Welcome to Aspose!");

    // Save ODS in ODF 1.2 version which is default
    OdsSaveOptions options;
    workbook.Save(outDir + u"ODF1.2_out.ods", options);

    // Save ODS in ODF 1.1 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf11);
    workbook.Save(outDir + u"ODF1.1_out.ods", options);

    // Save ODS in ODF 1.3 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf13);
    workbook.Save(outDir + u"ODF1.3_out.ods", options);

    std::cout << "ODS files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
