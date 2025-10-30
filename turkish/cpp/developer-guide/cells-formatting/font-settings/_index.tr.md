---
title: Yazı Tipi Ayarları ile C++
linktitle: Font Ayarları
type: docs
weight: 30
url: /tr/cpp/cells-font-settings/
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışma konusunda C++ için bir kütüphanedir. Hücrelerin yazı tipi ayarlarını destekler, kullanıcıların hücrelerin yazı tipi stilini ve özelliklerini özelleştirmelerine olanak tanır. Bu makale, Aspose.Cells kütüphanesini kullanarak hücre yazı tipi ayarlarını nasıl yapacağınızı tanıtacaktır.
keywords: Aspose.Cells, Hücreler, Font Ayarları, Stilleri, Özellikleri
---

{{% alert color="primary" %}}

Bir metnin görünüm ve hissi, yazı tipi ayarlarını değiştirerek kontrol edilebilir. Yazı tipi ayarları, isim, stil, boyut, renk ve diğer efektleri içerebilir. Microsoft Excel gibi, Aspose.Cells da hücrelerin yazı tipi ayarlarını yapılandırmayı destekler.

{{% /alert %}}

## **Font Ayarlarını Yapılandırma**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, bir Microsoft Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı bir [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonu sağlar. [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının bir nesnesini temsil eder.

Aspose.Cells, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) ve [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) yöntemlerini sağlar; bu yöntemler bir hücrenin biçimlendirme stiline getirilip alınmasında kullanılır. [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) sınıfı, font ayarlarını yapılandırmak için özellikler sağlar.

### **Yazı Tipi Adını Ayarlama**

Geliştiriciler, [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) objesinin [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) özelliğini kullanarak herhangi bir yazı tipini hücre içindeki metne uygulayabilir.

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font name to "Times New Roman"
    style.GetFont().SetName(u"Times New Roman");

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Yazı Tipi Stilini Kalın Yapma**

Geliştiriciler, metni kalın yapmak için [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) nesnesinin [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) özelliğini **true** olarak ayarlayarak yapabilirler.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font weight to bold
    style.GetFont().SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Yazı Tipi Boyutunu Ayarlama**

[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) nesnesinin [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/) özelliği ile yazı tipi boyutunu ayarlayın.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font size to 14
    style.GetFont().SetSize(14);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Yazı Tipi Rengini Ayarlama**

Yazı tipi rengini ayarlamak için [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) objesinin [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) özelliğini kullanın. C++ çerçevesinin bir parçası olan Renk enumerasyonundan herhangi bir renk seçin ve [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) özelliğine atayın.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font color to blue
    style.GetFont().SetColor(Color::Blue());

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```

### **Yazı Tipi Altı Çizgi Türünü Ayarlama**

[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) nesnesinin [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) özelliğini kullanarak metni altı çizili yapın. Aspose.Cells, [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/) numaralandırmasında çeşitli önceden tanımlanmış yazı tipi altı çizgi tipleri sunar.

|**Yazı Tipi Altı Çizgi Tipleri**|**Açıklama**|
| :- | :- |
|Accounting|Tek hesap çizgisi|
|Double|Çift çizgi|
|DoubleAccounting|Çift hesap çizgisi|
|None|Çizgi yok|
|Single|Tek çizgi|

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font to be underlined
    style.GetFont().SetUnderline(FontUnderlineType::Single);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Üstü Çizili Etkiyi Ayarlama**

Üstü çizili uygulamak için [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) nesnesinin [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) özelliğini **true** olarak ayarlayın.

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

    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Hello Aspose!");

    Style style = cell.GetStyle();
    style.GetFont().SetIsStrikeout(true);
    cell.SetStyle(style);

    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Üst Simge Etkisini Ayarlama**

Abone simgesini ayarlayarak [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) nesnesinin [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) özelliğini **true** olarak ayarlayın.

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set subscript effect
    style.GetFont().SetIsSubscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Yazı Tipi Üzerine Üst Simge Efekti Ayarlama**

Geliştiriciler, yazı tipi üzerine üst simge efektini [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) öğesinin [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) özelliğini **true** olarak ayarlayarak uygulayabilirler.

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set superscript effect
    style.GetFont().SetIsSuperscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Yazı Tipi Üzerine Üst Simge ve Abone Etkileri Uygulama](/cells/tr/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Bir Elektronik Tablo veya Çalışma Kitabında Kullanılan Yazı Tiplerinin Listesini Alın](/cells/tr/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
{{< app/cells/assistant language="cpp" >}}
