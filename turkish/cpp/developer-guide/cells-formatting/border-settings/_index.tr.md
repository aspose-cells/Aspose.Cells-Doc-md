---
title: C++ ile Kenarlık Ayarları
linktitle: Kenar Ayarları
description: Hücrelerin kenar stilini ve rengini ayarlamak için Aspose.Cells kütüphanesini nasıl kullanacağınızı gösterir. Kenarın genişliğini, stilini ve rengini ayarlayarak hücrelerin görünümünü ve görünüşünü kontrol edebilirsiniz.
keywords: Aspose.Cells, Hücre Kenarlık Ayarları, C++, Kenar Genişliği, Kenar Stili, Kenar Rengi
type: docs
weight: 40
url: /tr/cpp/cells-border-settings/
---

## **Hücrelere Kenarlık Eklemek**

Microsoft Excel, hücreleri kenarlıklar ekleyerek biçimlendirmeye izin verir. Kenarlık tipi, eklendiği konuma göre değişir. Örneğin, üst kenarlık, hücrenin üst konumuna eklenmiş bir kenarlıktır. Kullanıcılar ayrıca kenarlıkların çizgi stilini ve rengini değiştirebilir.

Aspose.Cells ile geliştiriciler, sınırlar ekleyebilir ve bunları Microsoft Excel'de olduğu gibi esnek bir şekilde özelleştirebilirler.

### **Hücrelere Kenarlık Eklemek**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her sayfaya erişim sağlayan [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir sayfa, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunu sağlar. [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının bir nesnesini temsil eder.

Aspose.Cells, [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) metodunu [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfında sağlar. [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) yöntemi, hücre biçimlendirme stilini ayarlamak için kullanılır. [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) sınıfı, hücrelere kenarlık eklemek için özellikler sağlar.

#### **Bir Hücreye Sınır Ekleme**

Geliştiriciler, bir hücreye kenarlık eklemek için [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesinin [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/) koleksiyonunu kullanabilir. Kenarlık türü, [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/) koleksiyonuna indeks olarak geçirilir. Tüm kenarlık türleri önceden tanımlanmış [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/) enum'unda yer alır.

**Sınır numaralandırması**

| **Kenar Tipleri** | **Açıklama** |
|------------------|-----------------|
| AltKenarlık     | Alt kenar çizgisi |
| DiagonalAşağı      | Sol üstten sağ alt çapraz çizgi |
| DiagonalYukarı | Sol alttan sağ üst çapraz çizgi |
| SolKenarlık    | Sol kenar çizgisi |
| SağKenarlık   | Sağ kenar çizgisi |
| ÜstKenarlık     | Üst kenar çizgisi |

[**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/) koleksiyonu tüm kenarlıkları depolar. [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/) koleksiyonundaki her kenarlık, [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/) nesnesi tarafından temsil edilir ve bu nesne, sırasıyla [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/) ve [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/) özellikleri ile kenarlığın çizgi rengi ve stilini ayarlamayı sağlar.

Bir kenarlığın çizgi rengini ayarlamak için, Color enum'undan bir renk seçin ve bunu Kenarlık nesnesinin Color özelliğine atayın.

Kenarın çizgi stili, [**CellBorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellbordertype/) enum'undan bir çizgi stili seçilerek ayarlanır.

**HücreSınırTürü numaralandırması**

| **Çizgi Stilleri**       | **Açıklama**               |
|------------------------|-------------------------------|
| DashDot               | İnce kesik çizgi         |
| DashDotDot            | İnce kesik noktali çizgi     |
| Dashed                | Kesik çizgi                  |
| Dotted                | Noktalı çizgi                  |
| Double                | Çift çizgi                  |
| Hair                  | Saç çizgisi                     |
| MediumDashDot         | Orta kalınlıkta kesik çizgi       |
| MediumDashDotDot      | Orta kalınlıkta kesik noktali çizgi   |
| MediumDashed          | Orta kalınlıkta kesik çizgi            |
| None                  | Hiçbir çizgi                      |
| Medium                | Orta kalınlıkta çizgi                  |
| SlantedDashDot        | Eğik orta kalınlıkta kesik çizgi |
| Thick                 | Kalın çizgi                   |
| Thin                  | İnce çizgi                    |

Çizgi stillerinden birini seçin ve ardından onu [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/) nesnesinin [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/) özelliğine atayın.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Visit Aspose!");

    Style style = cell.GetStyle();

    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());

    cell.SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls");
    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Her iki çizgi stili ve rengi aynı anda ayarlamalısınız. İki çapraz kenar çizgisi aynı çizgi stiline ve renge sahip olmalıdır.

{{% /alert %}}

#### **Hücre Aralığına Sınırlar Ekleme**

Sadece bir hücre yerine hücre aralığına da sınırlar eklemek mümkündür. Bunu yapmak için önce, [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) yöntemini çağırarak bir hücre aralığı oluşturun. Aşağıdaki parametreleri alır:

- İlk Sütun, aralığın ilk sütunu.
- İlk Sütun, aralığın ilk sütunu.
- Satır Sayısı, aralıktaki satır sayısı.
- Sütun Sayısı, aralıktaki sütun sayısı.

[**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) yöntemi, belirtilen hücre aralığını içeren bir [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) nesnesi döner. [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) nesnesi, aşağıdaki parametreleri alan bir [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/) yöntemi sağlar ve hücre aralığına sınır ekler:

- **Sınır Türü**, [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/) enumerasyonundan seçilen sınır tipi.
- **Çizgi Stili**, sınır çizgi stili, [**CellBorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellbordertype/) enumerasyonundan seçilir.
- **Renk**, Renk sıralamasından seçilen çizgi rengi.

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

    // Create workbook
    Workbook workbook;

    // Obtain the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello World From Aspose");

    // Creating a range of cells starting from "A1" cell to 3rd column in a row
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 3);

    // Adding a thick top border with blue line
    range.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick bottom border with blue line
    range.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick left border with blue line
    range.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick right border with blue line
    range.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Thick, Color::Blue());

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
