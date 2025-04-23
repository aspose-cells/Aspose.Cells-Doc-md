---
title: Pivot Tablo Biçimlendirme C++ ile
linktitle: Pivot Tablosunu Biçimlendirme
type: docs
weight: 10
url: /tr/cpp/formatting-pivot-table/
description: Pivot tablolarının görünümünü nasıl özelleştireceğinizi Aspose.Cells for C++ ile öğrenin.
---

## **Döndürme Tablosu Görünümü**

Bir Pivot Tablosu Nasıl Oluşturulur, basit bir pivot tablosu nasıl oluşturulurun açıklanmasının yanı sıra bu makale, çeşitli özellikleri ayarlayarak bir pivot tablosunun görünümünü özelleştirmeyi açıklar:

- Pivot tablo format seçenekleri
- Pivot alanları format seçenekleri
- Veri alanı format seçenekleri

### **Döndürme Tablosu Biçim Seçeneklerini Ayarlama**

Toplam Otomatik Biçim Türünü Ayarlama

#### **Microsoft Excel, birkaç farklı önceden ayarlanmış rapor formatı sunar. Aspose.Cells, bu formatlama seçeneklerini de destekler. Bunlara erişmek için:**

Microsoft Excel çeşitli ön ayarlı rapor formatları sunar. Aspose.Cells bu biçimlendirme seçeneklerini de destekler. Onlara erişmek için:

1. [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/isautoformat/) değerini **true** olarak ayarlayın.
1. [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottableautoformattype/) numaralandırmasından bir biçimlendirme seçeneği atayın.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    int pivotindex = 0;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Setting the PivotTable report is automatically formatted
    pivotTable.SetIsAutoFormat(true);

    // Setting the PivotTable autoformat type
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "PivotTable formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Biçim Seçeneklerini Ayarlama**

Aşağıdaki kod örneği, satır ve sütunlar için genel toplamları gösteren ve raporun alan sırasını ayarlayan biçimlendirmeyi gösterir. Ayrıca, boş değerler için özel bir dize ayarlamayı da gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Setting the PivotTable report shows grand totals for rows.
    pivotTable.SetShowRowGrandTotals(true);

    // Setting the PivotTable report shows grand totals for columns.
    pivotTable.SetShowColumnGrandTotals(true);

    // Setting the PivotTable report displays a custom string in cells that contain null values.
    pivotTable.SetDisplayNullString(true);
    pivotTable.SetNullString(u"null");

    // Setting the PivotTable report's layout
    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "PivotTable settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Aşağıdaki kod örneği, pivot tablosunu satır ve sütunlar için toplamları göstermek üzere biçimlendirme ve raporun alan sırasını ayarlamayı gösterir. Ayrıca, null değerler için özel bir dize ayarlamak da gösterilir.**

Pivot tablo raporunun görünümünü manuel olarak biçimlendirmek için, ön ayarlı rapor biçimleri yerine, [**PivotTable.Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) ve [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) yöntemlerini kullanın. İstediğiniz biçimlendirme için bir stil nesnesi oluşturun, örneğin:

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    auto pivot = worksheet.GetPivotTables().Get(0);

    // Set pivot table style
    pivot.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleDark1);

    // Create a new style
    Style style = workbook.CreateStyle();
    style.GetFont().SetName(u"Arial Black");
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);

    // Apply style to pivot table
    pivot.FormatAll(style);

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table style applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Pivot Tablo Raporunun nasıl göründüğü ile ilgili nasıl biçimlendirileceğiniz, önceden ayarlanmış rapor formatlarını değil, {0} ve {1} yöntemlerini kullanarak el ile ayarlamak için kullanılır. İstenen biçimlendirme için bir stil nesnesi oluşturun, örneğin:**

Pivot Alanı Biçim Seçeneklerini Ayarlama

- Satır alanlarına erişim.
- Alt toplamları ayarlama.
- Otomatik sıralamayı ayarlama.
- Otomatik gösterimi ayarlama.

#### **Satır/Sütun/Sayfa Alanları Biçimi Ayarlama**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load a template file
    Workbook workbook(srcDir + u"Book1.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Setting the PivotTable report shows grand totals for rows.
    pivotTable.SetShowRowGrandTotals(true);

    // Accessing the row fields.
    PivotFieldCollection pivotFields = pivotTable.GetRowFields();

    // Accessing the first row field in the row fields.
    PivotField pivotField = pivotFields.Get(0);

    // Setting Subtotals.
    pivotField.SetSubtotals(PivotFieldSubtotalType::Sum, true);
    pivotField.SetSubtotals(PivotFieldSubtotalType::Count, true);

    // Setting autosort options.
    // Setting the field auto sort.
    pivotField.SetIsAutoSort(true);

    // Setting the field auto sort ascend.
    pivotField.SetIsAscendSort(true);

    // Setting the field auto sort using the field itself.
    pivotField.SetAutoSortField(-5);

    // Setting autoShow options.
    // Setting the field auto show.
    pivotField.SetIsAutoShow(true);

    // Setting the field auto show ascend.
    pivotField.SetIsAscendShow(false);

    // Setting the auto show using field(data field).
    pivotField.SetAutoShowField(0);

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "PivotTable settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Veri Alanları Biçimini Ayarlama**

Aşağıdaki kod örneği, veri alanları için görüntü biçimlerini ve sayı biçimini ayarlamayı göstermektedir.

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

    // Load a template file
    U16String inputFilePath = srcDir + u"Book1.xls";
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Accessing the data fields
    PivotFieldCollection pivotFields = pivotTable.GetDataFields();

    // Accessing the first data field in the data fields
    PivotField pivotField = pivotFields.Get(0);

    // Setting data display format
    pivotField.GetShowValuesSetting().SetCalculationType(PivotFieldDataDisplayFormat::PercentageOf);

    // Setting the base field
    pivotField.GetShowValuesSetting().SetBaseFieldIndex(1);

    // Setting the base item
    pivotField.GetShowValuesSetting().SetBaseItemPositionType(PivotItemPositionType::Next);

    // Setting number format
    pivotField.SetNumber(10);

    // Saving the Excel file
    U16String outputFilePath = outDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Pivot Alanlarını Temizleme**

[**PivotFieldCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfieldcollection/), örneğin sayfa, sütun, satır veya veri gibi tüm pivot alanlarını temizlemenize izin veren [**Clear()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfieldcollection/clear/) adında bir yönteme sahiptir. Örneğin, tüm veri alanlarını temizlemek istediğinizde, bunu kullanın.
Aşağıdaki kod örneği, bir veri alanındaki tüm pivot alanlarını temizlemeyi göstermektedir.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the pivot tables in the sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();

    // Get the first PivotTable
    PivotTable pivotTable = pivotTables.Get(0);

    // Clear all the data fields
    pivotTable.GetDataFields().Clear();

    // Add new data field
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Betrag Netto FW");

    // Set the refresh data flag off
    pivotTable.SetRefreshDataFlag(false);

    // Refresh and calculate the pivot table data
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
