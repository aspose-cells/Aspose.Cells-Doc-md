---
title: C++ ile Excel Temaları ve Renkleri
linktitle: Excel Temaları ve Renkler
type: docs
weight: 100
url: /tr/cpp/excel-themes-and-colors/
description: Aspose.Cells for C++ API ile Excel Renk Düzeni kullanmak için C++ kodu
keywords: Renk Düzeni Oluştur ve Uygula, C++ ile Programlı Olarak Özel Renk Düzeni Oluşturma, Programlı olarak nasıl özel renk düzeni uygulanır, C++ ile excel de renk düzeni nasıl kullanılır
---

## **Excel'de Tema Uygulama ve Oluşturma**
Belge temaları, Excel belgelerinin renklerini, yazı tiplerini ve grafik biçimlendirme efektlerini kolayca koordine etmenizi ve bunları hızlı bir şekilde güncellemenizi sağlar. 
Temalar, bir çalışma kitabında kullanılan adlandırılmış stiller, grafik efektleri ve diğer nesneler ile birleştirilmiş bir görünüm sunar. Örneğin, Accent1 stili, Ofis ve Apex temalarında farklı görünür. Genellikle, bir belge teması uygular ve ardından istediğiniz şekilde değiştirirsiniz.

### **Excel'de Bir Renk Şeması Nasıl Uygulanır**
1. Excel'i açın ve Excel menü şeridinde "Sayfa Düzeni" sekmesine gidin.
1. "Temalar" bölümündeki "Renkler" düğmesine tıklayın.
<br>
<img src="color.png" width=70% />
1. Gereksinimlerinize uygun bir renk paleti seçin veya canlı bir önizleme görmek için şema üzerinde gezdirin.

### **Excel'de Özel Renk Şeması Nasıl Oluşturulur**
Belgenize taze, benzersiz bir görünüm vermek veya kuruluşunuzun marka standartlarına uygun olmak için kendi renk setinizi oluşturabilirsiniz.

1. Excel'i açın ve Excel menü şeridinde "Sayfa Düzeni" sekmesine gidin.
1. "Temalar" bölümündeki "Renkler" düğmesine tıklayın.
1. "Renkleri Özelleştir..." düğmesine tıklayın.
<br>
<img src="color2.png" width=70% />

1. "Yeni Tema Renkleri Oluştur" iletişim kutusunda, her bir öğe için renk seçmek için yanlarındaki renk açılır listelerine tıklayabilirsiniz. Renkleri paletten seçebilir veya "Daha Fazla Renkler" seçeneğini kullanarak özel renkler tanımlayabilirsiniz.
<br>
<img src="color3.png" width=70% />
1. Tüm istenen renkleri seçtikten sonra, özel renk şemanıza bir ad sağlamak için "Ad" alanına bir ad girin.

1. Özel renk şemanızı kaydetmek için "Kaydet" düğmesine tıklayın. Özel renk şemanız artık gelecekte kullanılmak üzere "Renkler" açılır menüsünde mevcut olacaktır.

## **Aspose.Cells'te Renk Şeması Oluşturma ve Uygulama**
Aspose.Cells, temaları ve renkleri özelleştirmek için özellikler sağlar.

### **Aspose.Cells'te Özel Renk Teması Nasıl Oluşturulur**
Dosyada tema renkleri kullanılıyorsa, her bir hücreyi ayrı ayrı değiştirmemize gerek yok, sadece temadaki renkleri değiştirmemiz yeterlidir.

Aşağıdaki örnek, istediğiniz renklerle özel temaları nasıl uygulayacağınızı gösterir. Microsoft Excel 2007'de manuel olarak oluşturulmuş bir örnek şablon dosyası kullanıyoruz.

Aşağıdaki örnek, bir şablon XLSX dosyası yükler, farklı tema renk tipleri için renkleri tanımlar, özel renkleri uygular ve Excel dosyasını kaydeder.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Define Color array (of 12 colors) for Theme
    Vector<Aspose::Cells::Color> carr(12);
    carr[0] = Color::AntiqueWhite(); // Background1
    carr[1] = Color::Brown();       // Text1
    carr[2] = Color::AliceBlue();   // Background2
    carr[3] = Color::Yellow();      // Text2
    carr[4] = Color::YellowGreen(); // Accent1
    carr[5] = Color::Red();         // Accent2
    carr[6] = Color::Pink();        // Accent3
    carr[7] = Color::Purple();      // Accent4
    carr[8] = Color::PaleGreen();   // Accent5
    carr[9] = Color::Orange();      // Accent6
    carr[10] = Color::Green();      // Hyperlink
    carr[11] = Color::Gray();       // Followed Hyperlink

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Instantiate a Workbook and open the template file
    Workbook workbook(inputFilePath);

    // Set the custom theme with specified colors
    workbook.CustomTheme(u"CustomeTheme1", carr);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Save as the excel file
    workbook.Save(outputFilePath);

    std::cout << "Custom theme applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Aspose.Cells'te Tema Renklerinin Uygulanması**

Aşağıdaki örnek, bir hücrenin ön planı ve yazı tipi renklerini (çalışbook'un varsayılan temasına göre) uygular. Ayrıca Excel dosyasını diske kaydeder.

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

    // Get cells collection in the first (default) worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Get the D3 cell
    Cell c = cells.Get(u"D3");

    // Get the style of the cell
    Style s = c.GetStyle();

    // Set foreground color for the cell from the default theme Accent2 color
    s.SetForegroundThemeColor(ThemeColor(ThemeColorType::Accent2, 0.5));

    // Set the pattern type
    s.SetPattern(BackgroundType::Solid);

    // Get the font for the style
    Font f = s.GetFont();

    // Set the theme color
    f.SetThemeColor(ThemeColor(ThemeColorType::Accent4, 0.1));

    // Apply style
    c.SetStyle(s);

    // Put a value
    c.PutValue(u"Testing1");

    // Save the excel file
    workbook.Save(outDir + u"output.out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Aspose.Cells'te Tema Renklerinin Alınması ve Ayarlanması**
 Aşağıda temalı renkleri uygulayan ve ayarlayan birkaç yöntem ve özellik bulunmaktadır.

- [**Style.GetForegroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundthemecolor/): Ön plan rengini ayarlamak için kullanılır.
- [**Style.GetBackgroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundthemecolor/): Arka plan rengini ayarlamak için kullanılır.
- [**Font.GetThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getthemecolor/): Yazı tipi rengini ayarlamak için kullanılır.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getthemecolor/): Bir tema rengini almak için kullanılır.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setthemecolor/): Bir tema rengini ayarlamak için kullanılır.

Aşağıdaki örnek, temalı renkleri almanın ve ayarlamanın nasıl yapılacağını gösterir.

Aşağıdaki örnek, bir şablon XLSX dosyası kullanır, farklı tema renk tipleri için renkleri alır, renkleri değiştirir ve Microsoft Excel dosyasını kaydeder.

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
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Background1 theme color
    Color c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the color
    std::cout << "theme color Background1: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Get the Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the color
    std::cout << "theme color Accent2: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Background1 theme color
    workbook.SetThemeColor(ThemeColorType::Background1, Color::Red());

    // Get the updated Background1 theme color
    c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the updated color for confirmation
    std::cout << "theme color Background1 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Accent2 theme color
    workbook.SetThemeColor(ThemeColorType::Accent2, Color::Blue());

    // Get the updated Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the updated color for confirmation
    std::cout << "theme color Accent2 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Save the updated file
    workbook.Save(outputFilePath);

    std::cout << "Theme colors updated and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Excel Dosyasından Tema Verisi Çıkarın](/cells/tr/cpp/extract-theme-data-from-excel-file/)
