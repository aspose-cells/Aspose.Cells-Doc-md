---
title: C++ kullanarak Çalışma Kitabında HTML yüklerken Otomatik Sığdırma Satır ve Sütunlar
linktitle: Çalışma Kitabında HTML yüklenirken Sütunları ve Satırlar Otomatik Uydurma
type: docs
weight: 120
url: /tr/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Aspose.Cells for C++ kullanarak, HTML yükleme sırasında sütun ve satırların otomatik uyumunu nasıl sağlayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

HTML dosyanızı Çalışma Kitabının içine yüklerken sütun ve satırları otomatik olarak uyarlatabilirsiniz. Bu amaçla lütfen [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) özelliğini **true** olarak ayarlayın.

## **HTML yüklenirken Sütunları ve Satırları Otomatik Uydurma**

Aşağıdaki örnek kod, önce örnek HTML'yi herhangi bir yükleme seçeneği olmadan Çalışma Kitabına yükler ve XLSX formatında kaydeder. Daha sonra örnek HTML'yi tekrar Çalışma Kitabına yükler, bu sefer [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) özelliğini **true** olarak ayarladıktan sonra XLSX formatında kaydeder. Lütfen hem otomatik uyarlama sütunları ve satırları olmadan [OtomatikUyarlanmamışSütunveSatırÇıktıExcelDosyası](outputWithout_AutoFitColsAndRows.xlsx) hem de otomatik uyarlama sütunları ve satırları olan [OtomatikUyarlanmışSütunveSatırÇıktıExcelDosyası](outputWith_AutoFitColsAndRows.xlsx) dosyalarını indirin. Aşağıdaki ekran görüntüsü, [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) özelliğinin her iki çıktı Excel dosyasındaki etkisini gösterir.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

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

    // Sample HTML string
    U16String sampleHtml(u"<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>");

    // Convert HTML string to memory stream
    std::string utf8Data = sampleHtml.ToUtf8();
    Vector<uint8_t> ms(utf8Data.size());
    std::memcpy(ms.GetData(), utf8Data.data(), utf8Data.size());

    // Load memory stream into workbook
    Workbook wb(ms);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputWithout_AutoFitColsAndRows.xlsx");

    // Specify the HTMLLoadOptions and set AutoFitColsAndRows = true
    HtmlLoadOptions opts;
    opts.SetAutoFitColsAndRows(true);

    // Load memory stream into workbook with the above HTMLLoadOptions
    Workbook wbWithOptions(ms, opts);

    // Save the workbook in xlsx format
    wbWithOptions.Save(outDir + u"outputWith_AutoFitColsAndRows.xlsx");

    std::cout << "HTML to Excel conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
