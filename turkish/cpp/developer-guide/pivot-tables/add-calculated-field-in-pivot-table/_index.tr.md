---
title: C++ kullanarak Pivot Tabloya hesaplanmış alan ekleme
linktitle: Pivot Tablosunda Hesaplanmış Alan Ekleme
type: docs
weight: 130
url: /tr/cpp/add-calculated-field-in-pivot-table/
description: Aspose.Cells for C++ numaralı ile pivot tabloya hesaplanmış alan nasıl eklenir.
keywords: Pivot tablosuna hesaplanmış bir alan ekleme.
---

## **Olası Kullanım Senaryoları**
Bilgisine sahip olduğunuz verilere dayalı olarak bir pivot tablosu oluşturduğunuzda, içindeki verilerin istediğiniz gibi olmadığını fark edersiniz. İstediğiniz veri, bu orijinal verilerin bir kombinasyonudur. Örneğin, veriden önce verilerin çıkarılması, çarpılması ve bölünmesi gerekebilir. Bu durumda, bir hesaplanmış alan oluşturmanız ve hesaplama için ilgili formülü ayarlamanız gerekir. Daha sonra hesaplanmış alanda bazı istatistikler ve diğer işlemleri gerçekleştirin. 

## **Excel'de Pivot Tablosunda Hesaplanmış Alan Ekleme**
Excel'de bir PivotTable'a hesaplanmış bir alan eklemek için şu adımları izleyin:

1. Bir hesaplanmış alan eklemek istediğiniz PivotTable'ı seçin. 
2. Kuruluş sekmesine gidin ve üzerinde PivotTable Analizi olan sekmeyi seçin.
3. "Alanlar, Öğeler ve Kümeler" üzerine tıklayın ve ardından açılır menüden "Hesaplanmış Alan"ı seçin.
4. "Ad" alanına hesaplanmış alan için bir ad girin.
5. "Formül" alanına, kullanmak istediğiniz PivotTable alan adları ve matematiksel operatörleri kullanarak gerçekleştirmek istediğiniz hesaplama için formülü girin. 
<br>
<img src="1.png" width=80% />
6. Hesaplanmış alan oluşturmak için "tamam"a tıklayın.
7. Yeni hesaplanmış alan, Değerler bölümü altında PivotTable Alan Listesinde görünecektir.
8. Hesaplanmış alanı PivotTable'ın Değerler bölümüne sürükleyerek hesaplanmış değerleri görüntüleyin.
<br>
<img src="2.png" width=80% />

## **C++ kullanarak Pivot Tabloya Hesaplanmış Alan Ekleme**
Aspose.Cells kullanarak Excel dosyasına hesaplanmış alan eklemek. Örnek kodu yürüttükten sonra, hesaplanmış bir alan içeren bir pivot tablo oluşturulur.
1. Orijinal verileri ayarlayın ve bir pivot tablosu oluşturun. 
2. Mevcut PivotField'a göre hesaplanmış alanı oluşturun.
3. Hesaplanmış alanı veri alanına ekleyin. 
4. Son olarak, çalışma kitabını [çıktı XLSX](out.xlsx) formatında kaydeder. 

## **Örnek Kod**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Creating a Workbook object
    Workbook workbook;

    // Obtaining the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the values to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");

    cell = cells.Get("B1");
    cell.PutValue(u"Count");

    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");

    cell = cells.Get("A3");
    cell.PutValue(u"Mango");

    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");

    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);

    cell = cells.Get("B3");
    cell.PutValue(3);

    cell = cells.Get("B4");
    cell.PutValue(6);

    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);

    cell = cells.Get("C3");
    cell.PutValue(20);

    cell = cells.Get("C4");
    cell.PutValue(30);

    cell = cells.Get("C5");
    cell.PutValue(60);

    // Adding a PivotTable to the worksheet
    int32_t i = ws.GetPivotTables().Add(u"=A1:C5", u"D10", u"PivotTable1");

    // Accessing the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    // Adding a calculated field to PivotTable and dragging it to data area
    pivotTable.AddCalculatedField(u"total", u"=Count*Price", true);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
