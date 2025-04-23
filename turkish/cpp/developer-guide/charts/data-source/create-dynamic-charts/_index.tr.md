---
title: C++ kullanarak Dinamik Grafikler Oluşturma
linktitle: Dinamik Grafikler Oluşturma
description: Aspose.Cells for C++ te dinamik grafikler nasıl oluşturulacağını öğrenin. Kılavuzumuz, ihtiyaçlarınıza göre grafik verisi, serisi ve biçimlendirmeyi dinamik olarak nasıl güncelleyeceğinizi göstererek verilerinizi görsel olarak sunmanıza olanak tanıyacaktır.
keywords: Aspose.Cells for C++, grafik çizimi, dinamik grafikler, veri, seri, biçimlendirme, çalışma sayfaları, güncelleme.
type: docs
weight: 240
url: /tr/cpp/create-dynamic-charts/
---

{{% alert color="primary" %}}

Dinamik (veya etkileşimli) grafikler, veri kapsamını değiştirdiğinizde değişme yeteneğine sahiptir. Diğer bir deyişle, dinamik grafikler, veri kaynağı değiştiğinde otomatik olarak değişiklikleri yansıtabilir. Veri kaynağında değişikliği tetiklemek için, Excel Tablolarının filtreleme seçeneğini veya ComboBox veya Dropdown listesi gibi bir kontrolü kullanabilirsiniz.

Bu makale, yukarıda belirtilen iki yaklaşımı kullanarak dinamik grafikler oluşturmak için Aspose.Cells for C++ API'lerinin kullanımını göstermektedir.

{{% /alert %}}

## **Excel Tablolarını Kullanma**

{{% alert color="primary" %}}

Excel tabloları Aspose.Cells perspektifinde ListObjects olarak adlandırılır, bu yüzden açıklık ve netlik için "Table" yerine "ListObject" terimini kullanacağız. [ListObject Oluşturma](/cells/tr/cpp/create-and-format-table/) ile ilgili detayları lütfen detaylı şekilde okuyunuz ve Aspose.Cells for C++ API'yi kullanınız.

{{% /alert %}}

ListObject, kullanıcı etkileşimi üzerine sıralama ve filtreleme yapmak için yerleşik fonksiyonlar sağlar. Her iki sıralama ve filtreleme seçeneği, [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) başlık satırına otomatik olarak eklenen açılır listeler aracılığıyla sağlanır. Bu özellikler (sıralama ve filtreleme) nedeniyle, [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) dinamik grafik için veri kaynağı olarak mükemmel aday olur çünkü sıralama veya filtreleme değiştiğinde, grafikteki veri gösterimi güncellenecek ve [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/)nin mevcut durumunu yansıtacaktır.

Demoyu basit tutmak amacıyla, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)'ı sıfırdan oluşturacağız ve aşağıda belirtilen adımlarla ilerleyeceğiz.

1. Boş bir [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) oluşturun.
1. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) içinde ilk [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) in [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) erişimi.
1. Hücrelere bazı veriler ekleyin.
1. Eklenen verilere dayanarak [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) oluşturun.
1. [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) nin veri aralığına göre [**Chart**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/) oluşturun.
1. Sonucu diske kaydedin.

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

    // Create an instance of Workbook
    Workbook book;

    // Access first worksheet from the collection
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Access cells collection of the first worksheet
    Cells cells = sheet.GetCells();

    // Insert data column wise
    cells.Get(u"A1").PutValue(u"Category");
    cells.Get(u"A2").PutValue(u"Fruit");
    cells.Get(u"A3").PutValue(u"Fruit");
    cells.Get(u"A4").PutValue(u"Fruit");
    cells.Get(u"A5").PutValue(u"Fruit");
    cells.Get(u"A6").PutValue(u"Vegetables");
    cells.Get(u"A7").PutValue(u"Vegetables");
    cells.Get(u"A8").PutValue(u"Vegetables");
    cells.Get(u"A9").PutValue(u"Vegetables");
    cells.Get(u"A10").PutValue(u"Beverages");
    cells.Get(u"A11").PutValue(u"Beverages");
    cells.Get(u"A12").PutValue(u"Beverages");

    cells.Get(u"B1").PutValue(u"Food");
    cells.Get(u"B2").PutValue(u"Apple");
    cells.Get(u"B3").PutValue(u"Banana");
    cells.Get(u"B4").PutValue(u"Apricot");
    cells.Get(u"B5").PutValue(u"Grapes");
    cells.Get(u"B6").PutValue(u"Carrot");
    cells.Get(u"B7").PutValue(u"Onion");
    cells.Get(u"B8").PutValue(u"Cabage");
    cells.Get(u"B9").PutValue(u"Potatoe");
    cells.Get(u"B10").PutValue(u"Coke");
    cells.Get(u"B11").PutValue(u"Coladas");
    cells.Get(u"B12").PutValue(u"Fizz");

    cells.Get(u"C1").PutValue(u"Cost");
    cells.Get(u"C2").PutValue(2.2);
    cells.Get(u"C3").PutValue(3.1);
    cells.Get(u"C4").PutValue(4.1);
    cells.Get(u"C5").PutValue(5.1);
    cells.Get(u"C6").PutValue(4.4);
    cells.Get(u"C7").PutValue(5.4);
    cells.Get(u"C8").PutValue(6.5);
    cells.Get(u"C9").PutValue(5.3);
    cells.Get(u"C10").PutValue(3.2);
    cells.Get(u"C11").PutValue(3.6);
    cells.Get(u"C12").PutValue(5.2);

    cells.Get(u"D1").PutValue(u"Profit");
    cells.Get(u"D2").PutValue(0.1);
    cells.Get(u"D3").PutValue(0.4);
    cells.Get(u"D4").PutValue(0.5);
    cells.Get(u"D5").PutValue(0.6);
    cells.Get(u"D6").PutValue(0.7);
    cells.Get(u"D7").PutValue(1.3);
    cells.Get(u"D8").PutValue(0.8);
    cells.Get(u"D9").PutValue(1.3);
    cells.Get(u"D10").PutValue(2.2);
    cells.Get(u"D11").PutValue(2.4);
    cells.Get(u"D12").PutValue(3.3);

    // Create ListObject, Get the List objects collection in the first worksheet
    ListObjectCollection listObjects = sheet.GetListObjects();

    // Add a List based on the data source range with headers on
    int32_t index = listObjects.Add(0, 0, 11, 3, true);

    sheet.AutoFitColumns();

    // Create chart based on ListObject
    index = sheet.GetCharts().Add(ChartType::Column, 21, 1, 35, 18);
    Chart chart = sheet.GetCharts().Get(index);
    chart.SetChartDataRange(u"A1:D12", true);
    chart.GetNSeries().SetCategoryData(u"A2:B12");

    // Save spreadsheet
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Spreadsheet created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Dinamik Formüller Kullanma**

Eğer [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/)’ı dinamik grafik için veri kaynağı olarak kullanmak istemiyorsanız, diğer seçenek Excel fonksiyonlarını (veya formülleri) kullanmak ve veriyi değiştiren bir kontrol (örneğin, ComboBox) oluşturmaktır. Bu senaryoda, seçim yapıldığında VLOOKUP fonksiyonu uygun değerleri getirecek şekilde kullanılır. Seçim değiştirildiğinde, VLOOKUP fonksiyonu hücre değeri yenilenir. Bir hücre aralığı VLOOKUP fonksiyonu kullanıyorsa, tüm aralık kullanıcı etkileşimiyle yenilenebilir ve bu nedenle dinamik grafikte veri kaynağı olarak kullanılabilir.

Demonstrasyonu anlaşılır tutmak için Workbook'ı sıfırdan oluşturacağız ve aşağıda belirtilen adımları adım adım ilerleteceğiz.

1. Boş bir [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) oluşturun.
1. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) içinde ilk [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) in [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) erişimi.
1. Hücrelere Adlandırılmış Aralık oluşturarak bazı veriler ekleyin. Bu veriler, dinamik grafik için seri olarak hizmet edecektir.
1. Önceki adımda oluşturulan Adlandırılmış Aralık kullanılarak [**ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) oluştur.
1. VLOOKUP işlevine veri kaynağı olacak hücrelere başka veriler ekleyin.
1. Uygun parametrelerle VLOOKUP işlevini bir hücre aralığına ekleyin. Bu aralık, dinamik grafik için kaynak olarak hizmet edecektir.
1. Önceki adımda oluşturulan aralığa göre [**Chart**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/) oluştur.
1. Sonucu diske kaydedin.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range in the second worksheet
    Range range = worksheet.GetCells().CreateRange(u"C21", u"C24");

    // Name the range
    range.SetName(u"MyRange");

    // Fill different cells with data in the range
    range.Get(0, 0).PutValue(u"North");
    range.Get(1, 0).PutValue(u"South");
    range.Get(2, 0).PutValue(u"East");
    range.Get(3, 0).PutValue(u"West");

    // Add a combo box to the worksheet
    ComboBox comboBox = worksheet.GetShapes().AddComboBox(15, 0, 2, 0, 17, 64);
    comboBox.SetInputRange(u"=MyRange");
    comboBox.SetLinkedCell(u"=B16");
    comboBox.SetSelectedIndex(0);

    // Get the cell and set its style
    Cell cell = worksheet.GetCells().Get(u"B16");
    Style style = cell.GetStyle();
    style.GetFont().SetColor(Color::White());
    cell.SetStyle(style);

    // Set formula for cell C16
    worksheet.GetCells().Get(u"C16").SetFormula(u"=INDEX(Sheet1!$C$21:$C$24,$B$16,1)");

    // Put some data for chart source
    // Data Headers
    worksheet.GetCells().Get(u"D15").PutValue(u"Jan");
    worksheet.GetCells().Get(u"D20").PutValue(u"Jan");

    worksheet.GetCells().Get(u"E15").PutValue(u"Feb");
    worksheet.GetCells().Get(u"E20").PutValue(u"Feb");

    worksheet.GetCells().Get(u"F15").PutValue(u"Mar");
    worksheet.GetCells().Get(u"F20").PutValue(u"Mar");

    worksheet.GetCells().Get(u"G15").PutValue(u"Apr");
    worksheet.GetCells().Get(u"G20").PutValue(u"Apr");

    worksheet.GetCells().Get(u"H15").PutValue(u"May");
    worksheet.GetCells().Get(u"H20").PutValue(u"May");

    worksheet.GetCells().Get(u"I15").PutValue(u"Jun");
    worksheet.GetCells().Get(u"I20").PutValue(u"Jun");

    // Data
    worksheet.GetCells().Get(u"D21").PutValue(304);
    worksheet.GetCells().Get(u"D22").PutValue(402);
    worksheet.GetCells().Get(u"D23").PutValue(321);
    worksheet.GetCells().Get(u"D24").PutValue(123);

    worksheet.GetCells().Get(u"E21").PutValue(300);
    worksheet.GetCells().Get(u"E22").PutValue(500);
    worksheet.GetCells().Get(u"E23").PutValue(219);
    worksheet.GetCells().Get(u"E24").PutValue(422);

    worksheet.GetCells().Get(u"F21").PutValue(222);
    worksheet.GetCells().Get(u"F22").PutValue(331);
    worksheet.GetCells().Get(u"F23").PutValue(112);
    worksheet.GetCells().Get(u"F24").PutValue(350);

    worksheet.GetCells().Get(u"G21").PutValue(100);
    worksheet.GetCells().Get(u"G22").PutValue(200);
    worksheet.GetCells().Get(u"G23").PutValue(300);
    worksheet.GetCells().Get(u"G24").PutValue(400);

    worksheet.GetCells().Get(u"H21").PutValue(200);
    worksheet.GetCells().Get(u"H22").PutValue(300);
    worksheet.GetCells().Get(u"H23").PutValue(400);
    worksheet.GetCells().Get(u"H24").PutValue(500);

    worksheet.GetCells().Get(u"I21").PutValue(400);
    worksheet.GetCells().Get(u"I22").PutValue(200);
    worksheet.GetCells().Get(u"I23").PutValue(200);
    worksheet.GetCells().Get(u"I24").PutValue(100);

    // Dynamically load data on selection of Dropdown value
    worksheet.GetCells().Get(u"D16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,2,FALSE),0)");
    worksheet.GetCells().Get(u"E16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,3,FALSE),0)");
    worksheet.GetCells().Get(u"F16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,4,FALSE),0)");
    worksheet.GetCells().Get(u"G16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,5,FALSE),0)");
    worksheet.GetCells().Get(u"H16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,6,FALSE),0)");
    worksheet.GetCells().Get(u"I16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,7,FALSE),0)");

    // Create Chart
    int index = worksheet.GetCharts().Add(ChartType::Column, 0, 3, 12, 9);
    Chart chart = worksheet.GetCharts().Get(index);
    chart.GetNSeries().Add(u"='Sheet1'!$D$16:$I$16", false);
    chart.GetNSeries().Get(0).SetName(u"=C16");
    chart.GetNSeries().SetCategoryData(u"=$D$15:$I$15");

    // Save result on disc
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
