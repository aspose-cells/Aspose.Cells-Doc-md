---
title: Pivot Filtre ile C++
linktitle: Pivot Filtreleri
type: docs
weight: 130
url: /tr/cpp/add-or-clear-pivot-filter/
description: Aspose.Cells kullanarak C++ ile pivot tabloda filtre nasıl eklenir öğrenin.
keywords: Ofis 2013, ofis 2016, ofis 2019 ve ofis 365 olmadan pivot tablosuna filtre eklemek.
---

## **Olası Kullanım Senaryoları**
Bilinen verilerle bir pivot tablo oluşturduğunuzda ve bu tabloyu filtrelemek istediğinizde, filtreyi öğrenmeli ve kullanmalısınız. Bu, istediğiniz veriyi etkili bir şekilde filtrelemenize yardımcı olabilir. Aspose.Cells API kullanarak, Pivot Tablolardaki alan değerlerine filtre ekleyebilir ve temizleyebilirsiniz. 

## **Excel'de Pivot Tabloya Filtre Ekle**
Excel'de Pivot Tabloya filtre eklemek için şu adımları izleyin:

1. Temizlemek istediğiniz PivotTablosunu seçin. 
2. Pivot tabloda eklemek istediğiniz filtre için açılır ok tuşuna tıklayın.
3. Açılır menüden "En Üst 10" seçeneğini seçin.
<br>
<img src="3.png" width=80% />
4. Gösterim modunu ve filtre sayısını ayarlayın.
<br>
<img src="4.png" width=80% />

## **Pivot Tabloya Filtre Ekle**
Lütfen aşağıdaki örnek kodu inceleyin. Veriyi ayarlar ve buna dayalı bir PivotTablo oluşturur. Daha sonra pivot tablosunun satır alanına bir filtre ekler. Son olarak, çalışma kitabını [çıktı XLSX](filterout.xlsx) formatında kaydeder. Örnek kodu çalıştırdıktan sonra, bir sayfada top10 filtresi eklenmiş bir pivot tablosu eklenir.

### **Örnek Kod**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Guava");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Carambola");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Banana");
    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(5);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(20);

    // Add a PivotTable to the worksheet
    int32_t i = ws.GetPivotTables().Add(u"=A1:B8", u"D10", u"PivotTable1");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Count");
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    // Add top10 filter
    PivotField filterField = pivotTable.GetRowFields().Get(0);
    filterField.FilterTop10(0, PivotFilterType::Count, false, 5);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the workbook
    workbook.Save(u"filterout.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Excel'de Pivot Tabloda Filtre Temizle**
Excel'de Pivot Tablosundaki filtrelemeyi temizleme adımları şunlardır:

1. Temizlemek istediğiniz PivotTablosunu seçin. 
2. Pivot tablosundaki temizlemek istediğiniz filtre için açılır ok'a tıklayın.
3. Açılır menüden "Filtreyi Temizle" seçeneğini seçin.
<br>
<img src="1.png" width=80% />
4. PivotTablosunda tüm filtreleri temizlemek isterseniz, Excel'in Ribbon'ındaki PivotTable Analyze sekmesindeki "Filtreleri Temizle" düğmesine de tıklayabilirsiniz.
<br>
<img src="2.png" width=80% />

## **Pivot Tabloda Filtre Temizle**
Aspose.Cells'i kullanarak Pivot Tablosundaki filtreleri temizleyin. Lütfen aşağıdaki örnek kodu inceleyin. 
1. Verileri ayarlayın ve bunlara dayalı bir PivotTablo oluşturun. 
2. Pivot tablosunun sıra alanına bir filtre ekleyin. 
3. İşlem örneği kodunu çalıştırdıktan sonra, [çıktı XLSX](out_add.xlsx) biçimindeki bir çalışma kitabına bir pivot tablosu ve üst10 filtresi eklenir. 
4. Belirli bir pivot alanındaki filtreyi temizleyin. Filtreyi temizlemek için kodu çalıştırdıktan sonra, belirli pivot alanındaki filtre temizlenecektir. Lütfen [çıktı XLSX](out_delete.xlsx) dosyasını kontrol edin.

### **Örnek Kod**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Guava");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Carambola");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Banana");
    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(5);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(20);

    // Add a PivotTable to the worksheet
    int i = ws.GetPivotTables().Add(u"=A1:B8", u"D10", u"PivotTable1");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Count");
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    // Add top10 filter
    PivotField filterField = pivotTable.GetRowFields().Get(0);
    filterField.FilterTop10(0, PivotFilterType::Count, false, 5);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out_add.xlsx");

    // Clear PivotFilter from the specific PivotField
    pivotTable.GetPivotFilters().ClearFilter(field.GetBaseIndex());
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out_delete.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
