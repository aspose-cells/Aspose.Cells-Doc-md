---
title: Satır ve Sütunların Başlangıcını Kırparak CSV Formatına Dışa Aktarma sırasında C++ ile
linktitle: Başlangıçta Boş Satır ve Sütunları Kırparak
type: docs
weight: 100
url: /tr/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Aspose.Cells for C++ kullanarak spreadsheet leri CSV formatına dışa aktarırken başlangıçta boş satırları ve sütunları nasıl kırpacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

Bazen, Excel veya CSV dosyanızda başlangıçta boş sütunlar veya satırlar bulunur. Örneğin, bu satırı düşünün:

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Burada ilk üç hücre veya sütun boştur. Bu tür bir CSV dosyasını Microsoft Excel'de açarsanız, Microsoft Excel bu önde gelen boş satırları ve sütunları atar.

Varsayılan olarak, Aspose.Cells, kaydederken önde gelen boş sütunları ve satırları atmaz, ancak Microsoft Excel gibi onları kaldırmak istiyorsanız, Aspose.Cells [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) özelliğini sağlar. Lütfen onu **true** olarak ayarlayın ve tüm önde gelen boş satırlar ve sütunlar kaydederken atılacaktır.

{{% alert color="primary" %}}

Aspose.Cells for C++ 20.4 sürümünden önce, [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) varsayılan değeri **false** idi. 20.4 sürümünden sonra, [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) varsayılan değeri **true**. 

{{% /alert %}}

## **CSV formatına elektronik tabloları dışa aktarırken Öneki Boş Satırları ve Sütunları Kırp**

Aşağıdaki örnek kod, [örnek Excel dosyasını](sampleTrimBlankColumns.xlsx) yükler, iki önde gelen boş sütunu bulunan Excel dosyasını önce herhangi bir değişiklik yapmadan CSV formatında kaydeder ve sonra [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) özelliğini **true** olarak ayarlar ve tekrar kaydeder. Ekran görüntüsü, [örnek Excel dosyası](sampleTrimBlankColumns.xlsx), önde gelen boş sütunları kırpmadan oluşturulan [çıktı CSV dosyası](outputWithoutTrimBlankColumns.csv) ve kırparak oluşturulan [çıktı CSV dosyası](outputTrimBlankColumns.csv)'ı gösterir.

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Örnek Kod**

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleTrimBlankColumns.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Save in csv format without trimming blank columns
    wb.Save(outDir + u"outputWithoutTrimBlankColumns.csv", SaveFormat::Csv);

    // Create TxtSaveOptions and set TrimLeadingBlankRowAndColumn to true
    TxtSaveOptions opts;
    opts.SetTrimLeadingBlankRowAndColumn(true);

    // Save in csv format with trimming blank columns
    wb.Save(outDir + u"outputTrimBlankColumns.csv", opts);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
