---
title: C++ kullanarak Çalışma Kitabını Katı Açık XML Hesap Tablosu Formatında Kaydetme
linktitle: Sıkı Açık XML Elektronik Tablo Biçimine Çalışma Kitabını Kaydet
type: docs
weight: 150
url: /tr/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Aspose.Cells for C++ kullanarak bir çalışma kitabını Katı Açık XML Hesap Tablosu formatında nasıl kaydedeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, çalışma kitabını *Katı Açık XML Hesap Tablosu* formatında kaydetmenize olanak tanır. Bunun için [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/) özelliğini sağlar. Değerini [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/) olarak ayarlarsanız, çıktı Excel dosyası Katı Açık XML Hesap Tablosu formatında kaydedilir.

## **Sıkı Açık XML Elektronik Tablo Biçimine Çalışma Kitabını Kaydet**

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/) özelliğinin değerini [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/) olarak ayarlar ve [çıktı Excel dosyası](67338272.xlsx) olarak kaydeder. Çıktı Excel dosyasını Microsoft Excel'de açıp "Farklı Kaydet..." iletişim kutusunu açarsanız, formatını *Sıkı Open XML Elektronik Tablo* olarak göreceksiniz, bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Specify - Strict Open XML Spreadsheet - Format
    wb.GetSettings().SetCompliance(OoxmlCompliance::Iso29500_2008_Strict);

    // Add message in cell B4 of first worksheet
    Cell b4 = wb.GetWorksheets().Get(0).GetCells().Get(u"B4");
    b4.PutValue(u"This Excel file has Strict Open XML Spreadsheet format.");

    // Save to output Excel file
    wb.Save(u"outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with Strict Open XML Spreadsheet format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
