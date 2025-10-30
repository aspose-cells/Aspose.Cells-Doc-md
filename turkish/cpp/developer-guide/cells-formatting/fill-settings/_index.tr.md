---
title: Doldurma Ayarları ile C++
linktitle: Doldurma Ayarları
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışma konusunda C++ için bir kütüphanedir. Hücrelerin dolgu ayarlarını ayarlamayı destekler, kullanıcıların hücrelerin arka planını ve stilini özelleştirmelerine olanak tanır. Bu makale, Aspose.Cells kütüphanesini kullanarak hücre doldurma ayarlarını nasıl yapacağınızı tanıtacaktır.
keywords: Aspose.Cells, Hücreler, Doldurma Ayarları, Arka Plan, Stil
type: docs
weight: 50
url: /tr/cpp/cells-fill-settings/
---

## **Renkler ve Arka Plan Desenleri**

Microsoft Excel, hücrelerin ön plan (çerçeve) ve arka plan (doldurma) renklerini ve arka plan desenlerini ayarlayabilir.

Aspose.Cells, bu özellikleri esnek bir şekilde destekler. Bu konuda, Aspose.Cells kullanarak bu özellikleri nasıl kullanacağımızı öğreneceğiz.

### **Renkler ve Arka Plan Desenlerini Ayarlama**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sunar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir koleksiyon içerir. Bir çalışma sayfası [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, bir koleksiyon sağlar. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, bir koleksiyon sağlar. [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının bir nesnesini temsil eder.

[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/), hücre biçimlendirme işlemlerini almak ve ayarlamak için kullanılan [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) ve [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) metodlarına sahiptir. [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) sınıfı, hücrelerin ön plan ve arka plan renklerini ayarlamak için özellikler sağlar. Aspose.Cells, aşağıda verilen önceden tanımlanmış arka plan desenlerini içeren bir [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) numaralı sıralı koleksiyon sağlar.

|**Arka Plan Desenleri**|**Açıklama**|
| :- | :- |
|DiagonalCrosshatch|Çapraz çizgili deseni temsil eder|
|DiagonalStripe|Çapraz şerit deseni temsil eder|
|Gray6|%6,25 gri deseni temsil eder|
|Gray12|%12,5 gri deseni temsil eder|
|Gray25|%25 gri deseni temsil eder|
|Gray50|%50 gri deseni temsil eder|
|Gray75|%75 gri deseni temsil eder|
|HorizontalStripe|Dikey şerit deseni temsil eder|
|None|Arka plan yok|
|ReverseDiagonalStripe|Çapraz ters şerit deseni temsil eder|
|Solid|Düz deseni temsil eder|
|ThickDiagonalCrosshatch|Kalın çapraz çizgili deseni temsil eder|
|ThinDiagonalCrosshatch|İnce çapraz çizgili deseni temsil eder|
|ThinDiagonalStripe|İnce çapraz şerit deseni temsil eder|
|ThinHorizontalCrosshatch|İnce yatay çapraz çizgili deseni temsil eder|
|ThinHorizontalStripe|İnce yatay şerit deseni temsil eder|
|ThinReverseDiagonalStripe|İnce ters çapraz şerit deseni temsil eder|
|ThinVerticalStripe|İnce dikey şerit deseni temsil eder|
|VerticalStripe|Dikey şerit deseni temsil eder|

Aşağıdaki örnekte, A1 hücresinin ön plan rengi ayarlanmış ancak A2, dikey çizgili bir arka plan deseni olan hem ön plan rengi hem de arka plan rengi olarak yapılandırılmıştır.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Define a Style and get the A1 cell style
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    // Setting the foreground color to yellow
    style.SetForegroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A1 cell
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    // Get the A2 cell style
    style = worksheet.GetCells().Get(u"A2").GetStyle();

    // Setting the foreground color to blue
    style.SetForegroundColor(Color::Blue());

    // Setting the background color to yellow
    style.SetBackgroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A2 cell
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Bilinmesi Gerekenler**

{{% alert color="primary" %}}

- Bir hücrenin ön plan veya arka plan rengini ayarlamak için, [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesinin [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) veya [**GetBackgroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundcolor/) özelliklerini kullanın. Her iki özellik de, [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesinin [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) özelliği yapılandırılmışsa yalnızca etki eder.
- [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) özelliği hücrenin gölge rengini belirler.
  [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) özelliği, önyüz veya arka plan rengi için kullanılan arka plan deseninin türünü belirtir. Aspose.Cells, bir dizi önceden tanımlanmış arka plan desenlerini içeren [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) adlı bir numaralandırmayı sağlar.
- Eğer [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) numaralandırmasından *BackgroundType.None* değerini seçerseniz, ön plan rengi uygulanmaz.
  Benzer şekilde, *BackgroundType.None* veya *BackgroundType.Solid* değerlerini seçerseniz arka plan rengi uygulanmaz.
- Hücrenin gölgelendirme/dolgu rengini alırken, [**Style.GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) *BackgroundType.None* ise, [**Style.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) *Color.Empty* değerini döndürecektir.

{{% /alert %}}

### **Gradyan Dolgu Efektleri Uygulama**

Hücreye istenilen Gradyan Dolgu Efektlerini uygulamak için, [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesinin [**SetTwoColorGradient**](https://reference.aspose.com/cells/cpp/aspose.cells/style/settwocolorgradient/) metodunu kullanın.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::System;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(2, 1).PutValue(u"test");

    Cell cell = worksheet.GetCells().Get(u"B3");
    Style style = cell.GetStyle();
    style.SetIsGradient(true);
    style.SetTwoColorGradient(
        Color{ 0xFF, 0xFF, 0xFF, 0xFF },
        Color{ 0xFF, 0x4F, 0x81, 0xBD },
        GradientStyleType::Horizontal,
        1
    );

    style.GetFont().SetColor(Color::Red());
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    worksheet.GetCells().SetRowHeightPixel(2, 53);
    worksheet.GetCells().Merge(2, 1, 1, 2);

    workbook.Save(outDir + u"output.xlsx");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Renkler ve Palet**

Bir palet, bir görüntü oluşturmak için kullanılabilen renk sayısıdır. Bir sunumda standart bir palet kullanımı, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyasının bir hücrelere, fontlara, ızgaralara, grafik nesnelerine, doldurmalara ve çizgilere uygulanabilen 56 renklik bir paleti vardır.

Aspose.Cells ile sadece paletin mevcut renklerini değil aynı zamanda özel renkleri de kullanmak mümkündür. Özel bir rengi kullanmadan önce, önce paletine ekleyin.

Bu konu, paletine özel renkler eklemenin nasıl yapıldığını tartışmaktadır.

### **Paletine Özel Renkler Eklemek**

Aspose.Cells, Microsoft Excel'in 56 renkli paletini destekler. Paletine tanımlanmamış özel bir renk kullanmak için, rengi paletine ekleyin.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, paleti değiştirmek için özel bir renk eklemek için aşağıdaki parametreleri alan bir [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/) yöntemi sağlar:

- Özel Renk, paletine eklenecek özel renk.
- İndeks, özel rengin paletindeki rengin yerini belirtir. 0-55 arasında olmalıdır.

Aşağıdaki örnek, (Orkide) özel bir rengi paletine ekleyip bunu bir font üzerine uygulamadan önce paletine ekler.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid color is now in the palette
    std::cout << "Is Orchid in palette after change: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Palet sadece 56 renk tutar. Bir özel rengi paletine eklediğinizde, palet değişir ve önceki rengiyle biçimlendirilen dosyadaki her eleman değişir. Bu nedenle, paleti değiştirirken lütfen çok dikkatli olun. Dahası, bu sadece XLS (Excel 97 - 2003) dosya biçiminde bir kısıtlama olarak mevcuttur, XLSX veya diğer gelişmiş MS Excel (2007/2010 veya 2013) dosya biçimleri için böyle bir kısıtlama yoktur.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
