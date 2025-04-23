---
title: Aspose.Cells kullanarak Metni Sütunlara Çevirme C++ ile
linktitle: Metni Sütunlara Dönüştürme
type: docs
weight: 30
url: /tr/cpp/convert-text-to-columns-using-aspose-cells/
description: Excel dosyalarında metni sütunlara dönüştürmeyi nasıl yapacağınızı öğrenin Aspose.Cells for C++ kullanarak.
---

## **Olası Kullanım Senaryoları**

Metni Sütunlara Çevirebilirsiniz Microsoft Excel kullanarak metni sütunlara çevirebilirsiniz. Bu özellik, *Data* sekmesi altındaki *Data Tools* menüsünden erişilebilir. Bir sütunun içeriğini birden fazla sütuna ayırmak için, verinin Microsoft Excel'in hücre içeriğini birden fazla hücreye ayırdığı belirli bir ayırıcı içermesi gerekmektedir. Aspose.Cells, bu özelliği [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/) metodu aracılığıyla sağlar.

## **Aspose.Cells Kullanarak Metni Sütunlara Dönüştürme**

Aşağıdaki örnek kod, [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/) metodunun kullanımını açıklar. Kod, önce ilk çalışma sayfasının A sütununa bazı isimler ekler. İlk ve soy isimler boşluk karakteriyle ayrılmıştır. Sonra A sütununa [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/) metodunu uygular ve çıktıyı bir Excel dosyası olarak kaydeder. Eğer [dış hat dosyasını](25395213.xlsx) açarsanız, ilk isimlerin A sütununda, soy isimlerin ise B sütununda olduğunu göreceksiniz, bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Örnek Kod**

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add people name in column A. Fast name and Last name are separated by space.
    ws.GetCells().Get(u"A1").PutValue(u"John Teal");
    ws.GetCells().Get(u"A2").PutValue(u"Peter Graham");
    ws.GetCells().Get(u"A3").PutValue(u"Brady Cortez");
    ws.GetCells().Get(u"A4").PutValue(u"Mack Nick");
    ws.GetCells().Get(u"A5").PutValue(u"Hsu Lee");

    // Create text load options with space as separator
    TxtLoadOptions opts;
    opts.SetSeparator(u' ');

    // Split the column A into two columns using TextToColumns() method
    // Now column A will have first name and column B will have second name
    ws.GetCells().TextToColumns(0, 0, 5, opts);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputTextToColumns.xlsx");

    std::cout << "Text to columns conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
