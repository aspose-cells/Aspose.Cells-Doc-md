---
title: Excel, OpenOffice, Json, Csv ve Html Dosyalarını C++ ile Yükleme ve Yönetme
linktitle: Dosyaları Açma
type: docs
weight: 20
url: /tr/cpp/loading-saving-and-managing/
description: Aspose.Cells for C++ ile, Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, Görüntü, Mht ve XPS dosyalarını oluşturmak, açmak ve yönetmek oldukça basittir.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ ile, örneğin veri almak veya geliştirme sürecini hızlandırmak için tasarımcı şablonu kullanmak gibi, Excel dosyalarını oluşturmak, açmak ve yönetmek oldukça basittir.

{{% /alert %}}

## **Yeni Bir Çalışma Kitabı Oluşturma**
Aşağıdaki örnek sıfırdan yeni bir çalışma kitabı oluşturur.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    try
    {
        // Create a License object
        License license;

        // Set the license of Aspose.Cells to avoid the evaluation limitations
        license.SetLicense(srcDir + u"Aspose.Cells.lic");
    }
    catch (const std::exception& ex)
    {
        std::cerr << ex.what() << std::endl;
    }

    // Instantiate a Workbook object that represents Excel file.
    Workbook wb;

    // When you create a new workbook, a default "Sheet1" is added to the workbook.
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Access the "A1" cell in the sheet.
    Cell cell = sheet.GetCells().Get(u"A1");

    // Input the "Hello World!" text into the "A1" cell
    cell.PutValue(u"Hello World!");

    // Save the Excel file.
    wb.Save(srcDir + u"MyBook_out.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Bir Dosya Açma ve Kaydetme**
Aspose.Cells for C++ ile Excel dosyalarını açmak, kaydetmek ve yönetmek oldukça basittir.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"dest.xlsx";

    // Create a Workbook object and open an Excel file using its file path
    Workbook workbook1(inputFilePath);

    // Adding new sheet
    WorksheetCollection sheets = workbook1.GetWorksheets();
    Worksheet sheet = sheets.Add(u"MySheet");

    // Setting active sheet
    sheets.SetActiveSheetIndex(1);

    // Setting values
    Cells cells = sheet.GetCells();

    // Setting text
    cells.Get(u"A1").PutValue(u"Hello!");

    // Setting number
    cells.Get(u"A2").PutValue(1000);

    // Setting Date Time
    Cell cell = cells.Get(u"A3");
    Date currentDate;
    currentDate.year = 2023; // Replace with actual current year
    currentDate.month = 10;  // Replace with actual current month
    currentDate.day = 5;     // Replace with actual current day
    currentDate.hour = 12;   // Replace with actual current hour
    currentDate.minute = 30; // Replace with actual current minute
    currentDate.second = 0;  // Replace with actual current second
    cell.PutValue(currentDate);

    // Setting style for date
    Style style = cell.GetStyle();
    style.SetNumber(14);
    cell.SetStyle(style);

    // Setting formula
    cells.Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Saving the workbook to disk
    workbook1.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Dosyaları Açmanın Farklı Yolları](/cells/tr/cpp/different-ways-to-open-files/)
- [İş kitabı yüklerken Tanımlanmış İsimleri Filtreleme](/cells/tr/cpp/filter-defined-names-while-loading-workbook/)
- [İş kitabı veya çalışma sayfası yüklerken Nesneleri Filtreleme](/cells/tr/cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Şablon dosyasından iş kitabı yüklerken veri türüne göre filtreleme](/cells/tr/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Excel Dosyasını Yüklerken Uyarılar Alın](/cells/tr/cpp/get-warnings-while-loading-excel-file/)
- [Grafikleri Olmadan Kaynak Excel Dosyasını Yükleme](/cells/tr/cpp/load-source-excel-file-without-charts/)
- [Bir Çalışma Kitabındaki Belirli Çalışma Sayfalarını Yükleme](/cells/tr/cpp/load-specific-worksheets-in-a-workbook/)
- [Belirtilen Yazıcı Kağıt Boyutuyla Çalışma Kitabını Yükle](/cells/tr/cpp/load-workbook-with-specified-printer-paper-size/)
- [Farklı Microsoft Excel Sürümlerini Açma](/cells/tr/cpp/opening-different-microsoft-excel-versions-files/)
- [Farklı Biçimlerde Dosyaları Açma](/cells/tr/cpp/opening-files-with-different-formats/)
- [Büyük Veri Setlerine Sahip Büyük Dosyalarla Çalışırken Bellek Kullanımını Optimize Etme](/cells/tr/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Apple Inc. Tarafından Geliştirilen Sayılar Tablosunu Aspose.Cells Kullanarak Oku](/cells/tr/cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Çok Uzun Süren İşlemler veya Dönüşümler İçin InterruptMonitor Kullanarak Durdur](/cells/tr/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [LightCells API'sını Kullanma](/cells/tr/cpp/using-lightcells-api/)
- [CSV'yi JSON'a dönüştür](/cells/tr/cpp/convert-csv-to-json/)
- [Excel’i JSON’a dönüştürmek](/cells/tr/cpp/convert-excel-to-json/)
- [JSON'ı CSV'ye dönüştür](/cells/tr/cpp/convert-json-to-csv/)
- [JSON’u Excel’e dönüştürmek](/cells/tr/cpp/convert-json-to-excel/)
- [Excel’i Html’e dönüştürmek](/cells/tr/cpp/convert-excel-to-html/)
