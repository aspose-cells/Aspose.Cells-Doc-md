---
title: C++ ile Pivot Tablo ve Pivot Grafikler Oluşturun
linktitle: Özet Tabloları ve Özet Grafikler Oluşturma
type: docs
weight: 20
url: /tr/cpp/create-pivot-tables-and-pivot-charts/
description: Aspose.Cells kullanarak Excel dosyalarında pivot tablolar ve pivot grafikler nasıl oluşturulur öğrenin.
---

{{% alert color="primary" %}}

Bir pivot tablo, kayıtların etkileşimli bir özetidir. Örneğin, bir çalışma sayfasında yüzlerce fatura kaydı olabilir. Bir pivot tablo, faturaları müşteri, ürün veya tarihe göre toplamlandırabilir. Microsoft Excel ile, pivot tablodaki bilgileri yeni bir konuma sürükleyerek hızla yeniden düzenlemek mümkündür.

Bir özet grafik, bir özet tablonun verilerinin etkileşimli grafiksel bir temsilidir. Özet grafikler Excel 2000'de tanıtılmıştır. Özet grafik kullanmak, özet tablonun alt toplamlarını ve toplamlarını otomatik olarak oluşturduğu için verileri anlamak daha da kolaylaştırır.

Aspose.Cells, [pivot tablolar](/cells/tr/cpp/create-pivot-tables-and-pivot-charts/) ve [pivot grafikler](/cells/tr/cpp/create-pivot-tables-and-pivot-charts/) destekler.

{{% /alert %}}

## **Özet Tabloları ve Grafikler Eklemek**

Aspose.Cells, özet tabloları oluşturmak için kullanılan özel bir sınıf kümesi sağlar. Bu sınıflar, PivotTable nesnelerini oluşturmak ve ayarlamak için kullanılır ve temel PivotTable nesnesinin yapı taşları olarak hareket ederler:

- **PivotField**, pivot tablo raporundaki bir alan.
- **PivotFields**, bir pivot tabloda bulunan tüm PivotField nesnelerinin koleksiyonu.
- **PivotTable**, bir çalışma sayfasında bir PivotTable raporu.
- **PivotTables**, çalışma sayfasındaki tüm PivotTable nesnelerinin koleksiyonu.

### **Aspose.Cells'i kullanmaya hazırlık**

1. Aspose.Cells'i indirin ve kurun:
   1. [Aspose.Cells'i İndirin](https://downloads.aspose.com/cells/cpp).
   1. Geliştirme bilgisayarınıza kurun.
      Tüm [Aspose](http://www.aspose.com/) bileşenleri kurulduktan sonra değerlendirme modunda çalışır. Değerlendirme modu zaman limiti olmadan çalışır ve sadece üretilen belgelere filigran ekler. Bileşeni tam kapasiteyle kullanmak için geçerli bir lisansa sahip olmanız gerekir.
1. Bir proje oluşturun:
   1. C++ IDE'nizi başlatın (ör., Visual Studio).
   1. Yeni bir konsol uygulaması oluşturun.
1. Referanslar ekleyin:
   Projenize Aspose.Cells bileşenine referans ekleyin, örneğin, `...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll`.

### **Pivot Tablo Ekleme**

Aspose.Cells kullanarak bir pivot tablosu oluşturmak için:

1. Bir hücreye veri eklemek için `Cell` nesnesinin `PutValue` metodunu kullanın. Ayrıca, zaten veriyle doldurulmuş bir şablon dosyası kullanabilirsiniz. Veriler, pivot tablonun veri kaynağı olarak kullanılacaktır.
1. `PivotTables` koleksiyonunu `Add` yöntemiyle (`Worksheet` nesnesine kapsüllenmiş) kullanarak yeni bir pivot tablo ekleyin.
1. `PivotTables` koleksiyonundan yeni `PivotTable` nesnesine erişin ve onun indeksini kullanın. `PivotTable` nesnesine kapsüllenmiş herhangi bir pivot tablo nesnesini kullanarak tabloyu yönetin.

Kod örnekleri aşağıda verilmiştir.

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

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Name the sheet
    sheet.SetName(u"Data");

    // Get the cells collection
    Cells cells = sheet.GetCells();

    // Set values to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Employee");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Quarter");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Product");
    cell = cells.Get(u"D1");
    cell.PutValue(u"Continent");
    cell = cells.Get(u"E1");
    cell.PutValue(u"Country");
    cell = cells.Get(u"F1");
    cell.PutValue(u"Sale");

    // Fill employee names
    cell = cells.Get(u"A2");
    cell.PutValue(u"David");
    cell = cells.Get(u"A3");
    cell.PutValue(u"David");
    cell = cells.Get(u"A4");
    cell.PutValue(u"David");
    cell = cells.Get(u"A5");
    cell.PutValue(u"David");
    cell = cells.Get(u"A6");
    cell.PutValue(u"James");
    cell = cells.Get(u"A7");
    cell.PutValue(u"James");
    cell = cells.Get(u"A8");
    cell.PutValue(u"James");
    cell = cells.Get(u"A9");
    cell.PutValue(u"James");
    cell = cells.Get(u"A10");
    cell.PutValue(u"James");
    cell = cells.Get(u"A11");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A12");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A13");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A14");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A15");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A16");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A17");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A18");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A19");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A20");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A21");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A22");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A23");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A24");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A25");
    cell.PutValue(u"Jean");
    cell = cells.Get(u"A26");
    cell.PutValue(u"Jean");
    cell = cells.Get(u"A27");
    cell.PutValue(u"Jean");
    cell = cells.Get(u"A28");
    cell.PutValue(u"Ada");
    cell = cells.Get(u"A29");
    cell.PutValue(u"Ada");
    cell = cells.Get(u"A30");
    cell.PutValue(u"Ada");

    // Fill quarters
    cell = cells.Get(u"B2");
    cell.PutValue(1);
    cell = cells.Get(u"B3");
    cell.PutValue(2);
    cell = cells.Get(u"B4");
    cell.PutValue(3);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(1);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(3);
    cell = cells.Get(u"B9");
    cell.PutValue(4);
    cell = cells.Get(u"B10");
    cell.PutValue(4);
    cell = cells.Get(u"B11");
    cell.PutValue(1);
    cell = cells.Get(u"B12");
    cell.PutValue(1);
    cell = cells.Get(u"B13");
    cell.PutValue(2);
    cell = cells.Get(u"B14");
    cell.PutValue(2);
    cell = cells.Get(u"B15");
    cell.PutValue(3);
    cell = cells.Get(u"B16");
    cell.PutValue(4);
    cell = cells.Get(u"B17");
    cell.PutValue(4);
    cell = cells.Get(u"B18");
    cell.PutValue(1);
    cell = cells.Get(u"B19");
    cell.PutValue(1);
    cell = cells.Get(u"B20");
    cell.PutValue(2);
    cell = cells.Get(u"B21");
    cell.PutValue(3);
    cell = cells.Get(u"B22");
    cell.PutValue(3);
    cell = cells.Get(u"B23");
    cell.PutValue(4);
    cell = cells.Get(u"B24");
    cell.PutValue(4);
    cell = cells.Get(u"B25");
    cell.PutValue(1);
    cell = cells.Get(u"B26");
    cell.PutValue(2);
    cell = cells.Get(u"B27");
    cell.PutValue(3);
    cell = cells.Get(u"B28");
    cell.PutValue(1);
    cell = cells.Get(u"B29");
    cell.PutValue(2);
    cell = cells.Get(u"B30");
    cell.PutValue(3);

    // Fill products
    cell = cells.Get(u"C2");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C3");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C4");
    cell.PutValue(u"Chai");
    cell = cells.Get(u"C5");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C6");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C7");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C8");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C9");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C10");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C11");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C12");
    cell.PutValue(u"Chai");
    cell = cells.Get(u"C13");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C14");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C15");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C16");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C17");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C18");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C19");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C20");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C21");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C22");
    cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C23");
    cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C24");
    cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C25");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C26");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C27");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C28");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C29");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C30");
    cell.PutValue(u"Chocolade");

    // Fill continents
    cell = cells.Get(u"D2");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D3");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D4");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D5");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D6");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D7");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D8");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D9");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D10");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D11");
    cell.PutValue(u"America");
    cell = cells.Get(u"D12");
    cell.PutValue(u"America");
    cell = cells.Get(u"D13");
    cell.PutValue(u"America");
    cell = cells.Get(u"D14");
    cell.PutValue(u"America");
    cell = cells.Get(u"D15");
    cell.PutValue(u"America");
    cell = cells.Get(u"D16");
    cell.PutValue(u"America");
    cell = cells.Get(u"D17");
    cell.PutValue(u"America");
    cell = cells.Get(u"D18");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D19");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D20");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D21");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D22");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D23");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D24");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D25");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D26");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D27");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D28");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D29");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D30");
    cell.PutValue(u"Africa");

    // Fill countries
    cell = cells.Get(u"E2");
    cell.PutValue(u"China");
    cell = cells.Get(u"E3");
    cell.PutValue(u"India");
    cell = cells.Get(u"E4");
    cell.PutValue(u"Korea");
    cell = cells.Get(u"E5");
    cell.PutValue(u"India");
    cell = cells.Get(u"E6");
    cell.PutValue(u"France");
    cell = cells.Get(u"E7");
    cell.PutValue(u"France");
    cell = cells.Get(u"E8");
    cell.PutValue(u"Germany");
    cell = cells.Get(u"E9");
    cell.PutValue(u"Italy");
    cell = cells.Get(u"E10");
    cell.PutValue(u"France");
    cell = cells.Get(u"E11");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E12");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E13");
    cell.PutValue(u"Brazil");
    cell = cells.Get(u"E14");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E15");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E16");
    cell.PutValue(u"Canada");
    cell = cells.Get(u"E17");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E18");
    cell.PutValue(u"Italy");
    cell = cells.Get(u"E19");
    cell.PutValue(u"France");
    cell = cells.Get(u"E20");
    cell.PutValue(u"Italy");
    cell = cells.Get(u"E21");
    cell.PutValue(u"New Zealand");
    cell = cells.Get(u"E22");
    cell.PutValue(u"Australia");
    cell = cells.Get(u"E23");
    cell.PutValue(u"Australia");
    cell = cells.Get(u"E24");
    cell.PutValue(u"New Zealand");
    cell = cells.Get(u"E25");
    cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E26");
    cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E27");
    cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E28");
    cell.PutValue(u"Egypt");
    cell = cells.Get(u"E29");
    cell.PutValue(u"Egypt");
    cell = cells.Get(u"E30");
    cell.PutValue(u"Egypt");

    // Fill sales
    cell = cells.Get(u"F2");
    cell.PutValue(2000);
    cell = cells.Get(u"F3");
    cell.PutValue(500);
    cell = cells.Get(u"F4");
    cell.PutValue(1200);
    cell = cells.Get(u"F5");
    cell.PutValue(1500);
    cell = cells.Get(u"F6");
    cell.PutValue(500);
    cell = cells.Get(u"F7");
    cell.PutValue(1500);
    cell = cells.Get(u"F8");
    cell.PutValue(800);
    cell = cells.Get(u"F9");
    cell.PutValue(900);
    cell = cells.Get(u"F10");
    cell.PutValue(500);
    cell = cells.Get(u"F11");
    cell.PutValue(1600);
    cell = cells.Get(u"F12");
    cell.PutValue(600);
    cell = cells.Get(u"F13");
    cell.PutValue(2000);
    cell = cells.Get(u"F14");
    cell.PutValue(500);
    cell = cells.Get(u"F15");
    cell.PutValue(900);
    cell = cells.Get(u"F16");
    cell.PutValue(700);
    cell = cells.Get(u"F17");
    cell.PutValue(1400);
    cell = cells.Get(u"F18");
    cell.PutValue(1350);
    cell = cells.Get(u"F19");
    cell.PutValue(300);
    cell = cells.Get(u"F20");
    cell.PutValue(500);
    cell = cells.Get(u"F21");
    cell.PutValue(1000);
    cell = cells.Get(u"F22");
    cell.PutValue(1500);
    cell = cells.Get(u"F23");
    cell.PutValue(1500);
    cell = cells.Get(u"F24");
    cell.PutValue(1600);
    cell = cells.Get(u"F25");
    cell.PutValue(1000);
    cell = cells.Get(u"F26");
    cell.PutValue(1200);
    cell = cells.Get(u"F27");
    cell.PutValue(1300);
    cell = cells.Get(u"F28");
    cell.PutValue(1500);
    cell = cells.Get(u"F29");
    cell.PutValue(1400);
    cell = cells.Get(u"F30");
    cell.PutValue(1000);

    // Add a new sheet
    Worksheet sheet2 = workbook.GetWorksheets().Get(workbook.GetWorksheets().Add());
    sheet2.SetName(u"PivotTable");

    // Get the pivot tables collection
    PivotTableCollection pivotTables = sheet2.GetPivotTables();

    // Add a pivot table
    int index = pivotTables.Add(u"=Data!A1:F30", u"B3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(index);

    // Show grand totals
    pivotTable.SetShowRowGrandTotals(true);
    pivotTable.SetShowColumnGrandTotals(true);

    // Set auto format
    pivotTable.SetIsAutoFormat(true);
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report6);

    // Add fields to row area
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 1);

    // Add fields to column area
    pivotTable.AddFieldToArea(PivotFieldType::Column, 3);

    // Add fields to data area
    pivotTable.AddFieldToArea(PivotFieldType::Data, 5);

    // Set number format for the first data field
    pivotTable.GetDataFields().Get(0).SetNumberFormat(u"$#,##0.00");

    // Save the workbook
    workbook.Save(outDir + u"pivotTable_test.out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Pivot Grafik Ekleme**

Aspose.Cells kullanarak bir PivotChart oluşturmak için:

1. Bir grafik ekleyin.
1. Grafiğin `PivotSource` özelliğini, mevcut bir pivot tabloya referans olacak şekilde ayarlayın.
1. Diğer özellikleri ayarlayın.

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
    U16String inputFilePath = srcDir + u"pivotTable_test.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"pivotChart_test_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Adding a new sheet
    Worksheet sheet3 = workbook.GetWorksheets().Get(workbook.GetWorksheets().Add(SheetType::Chart));

    // Naming the sheet
    sheet3.SetName(u"PivotChart");

    // Adding a column chart
    int index = sheet3.GetCharts().Add(ChartType::Column, 0, 5, 28, 16);

    // Setting the pivot chart data source
    sheet3.GetCharts().Get(index).SetPivotSource(u"PivotTable!PivotTable1");
    sheet3.GetCharts().Get(index).SetHidePivotFieldButtons(false);

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
