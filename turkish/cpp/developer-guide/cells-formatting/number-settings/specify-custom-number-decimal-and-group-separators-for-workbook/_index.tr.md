---
title: Çalışma Kitabı için Özel Sayı Ondalık ve Grubu Ayrıştırıcılarını C++ ile Belirle
linktitle: Özel Sayı Ondalık ve Grubu Ayrıştırıcılarını Belirle
type: docs
weight: 110
url: /tr/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: MS Excel de ve C++ kodu kullanarak Aspose.Cells for C++ API si ile sayıların ondalık ve grup ayırıcılarını değiştirin.
keywords: özel ondalık ayırıcı excel belirle, özel ondalık ayırıcı excel c++ belirle, özel grup ayırıcı excel belirle, özel grup ayırıcı excel c++ belirle, özel ondalık ve grup ayırıcı excel belirle, özel ondalık ve grup ayırıcı excel c++ belirle, ondalık ve grup ayırıcı excel değiştir, ondalık ayırıcı excel değiştir, grup ayırıcı excel değiştir, grup ayırıcı excel c++ değiştir
---

{{% alert color="primary" %}}

Microsoft Excel'de, Ekran Görüntüsünde gösterildiği gibi **Gelişmiş Excel Seçenekleri**'nden Sistem Ayraçlarını kullanmak yerine Özel Ondalık ve Binlerce Ayraçları belirleyebilirsiniz.

Aspose.Cells, biçimlendirme/analiz için özel ayırıcıları belirlemek için [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumberdecimalseparator/) ve [**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) özelliklerini sağlar.

{{% /alert %}}

## **Microsoft Excel Kullanarak Özel Ayraçları Belirtme**

Aşağıdaki ekran görüntüsü, **Gelişmiş Excel Seçenekleri**'ni ve **Özel Ayraçları** belirtmek için bölümü vurgular.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Aspose.Cells Kullanarak Özel Ayraçları Belirtme**

Aşağıdaki örnek kod, Aspose.Cells API'sini kullanarak Belirtilmemiş Ayırıcıları belirtmeyi gösterir. Özel Sayı Ondalık ve Grup Ayırıcılarını nokta ve boşluk olarak belirtir.

### C++ ile özel Sayı Ondalık ve Grup Ayrıştırıcıları belirleme kodu

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

    // Create a new workbook
    Workbook workbook;

    // Specify custom separators
    workbook.GetSettings().SetNumberDecimalSeparator(u'.');
    workbook.GetSettings().SetNumberGroupSeparator(u' ');

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set cell value
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(123456.789);

    // Set custom cell style
    Style style = cell.GetStyle();
    style.SetCustom(u"#,##0.000;[Red]#,##0.000", true);
    cell.SetStyle(style);

    // Auto-fit columns
    worksheet.AutoFitColumns();

    // Save workbook as PDF
    workbook.Save(outDir + u"CustomSeparator_out.pdf");

    std::cout << "Workbook saved successfully with custom separators!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
