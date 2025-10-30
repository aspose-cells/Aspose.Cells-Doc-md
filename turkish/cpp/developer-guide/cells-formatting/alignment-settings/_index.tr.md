---
title: C++ ile Hizalama Ayarları
linktitle: Uyum Ayarları
description: Aspose.Cells kütüphanesinde, metnin düzeni ve gösterimi ayarlamak için hücre uygunluk ayarlarını kullanabilirsiniz. Yatay hizalama, dikey hizalama ve metin kaydırma gibi ayarları ayarlayarak, metnin hücrelerde nasıl akacağı konusunda daha fazla kontrol sahibi olursunuz. Bu belge, hücre uygunluk ayarlarını nasıl kullanacağınızı hızlıca öğrenmenize ve örnek kodlarıyla adım adım rehberlik etmesine yardımcı olacaktır.
keywords: Aspose.Cells, hücre uygunluk, yatay hizalama, dikey hizalama, metin kaydırma
type: docs
weight: 20
url: /tr/cpp/cells-alignment-settings/
---

## **Hizalama Ayarlarının Yapılandırılması**

### **Microsoft Excel'deki hizalama ayarları**

Hücreleri biçimlendirmek için Microsoft Excel kullanan herkes, Microsoft Excel'deki hizalama ayarlarına aşinadır.

Yukarıdaki şekilden görebileceğiniz gibi, farklı türde hizalama seçenekleri bulunmaktadır:

- Metin hizalama (yatay ve dikey)
- Girinti
- Yönlendirme
- Metin kontrol
- Metin yönü

Bu tüm hizalama ayarları, Aspose.Cells tarafından tamamen desteklenir ve aşağıda daha detaylı olarak tartışılmaktadır.

### **Aspose.Cells'te hizalama ayarları**

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, bir [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonu sağlar. [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının bir örneğini temsil eder.

Aspose.Cells, [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) ve [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) metodlarını, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfı için bir hücrenin biçimlendirmesini almak ve ayarlamak için kullanır. [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) sınıfı, hizalama ayarlarını yapılandırmak için kullanışlı özellikler sağlar.

[**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) numarasını kullanarak herhangi bir metin hizalama türünü seçin. [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) numarasındaki önceden tanımlanmış metin hizalama türleri:

|**Metin Hizalama Türleri**|**Açıklama**|
| :- | :- |
|Bottom|, alt metin hizalamasını temsil eder
|Center|, merkez metin hizalamasını temsil eder
|CenterAcross|, metin hizalamasını çapraz merkezlemeyi temsil eder
|Distributed|, dağıtılmış metin hizalamasını temsil eder
|Fill|, doldurma metin hizalamasını temsil eder
|General|, genel metin hizalamasını temsil eder
|Justify|, düzgün metin hizalamasını temsil eder
|Left|, sol metin hizalamasını temsil eder
|Right|, sağ metin hizalamasını temsil eder
|Top|, üst metin hizalamasını temsil eder
|JustifiedLow|, Arapça metin için ayarlanmış bir kashida uzunluğuyla metni hizalar.
|ThaiDistributed|, Özellikle Tayland metnini dağıtır, çünkü her karakter bir kelime olarak kabul edilir.

{{% alert color="primary" %}}

Ayrıca [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/cpp/aspose.cells/style/isjustifydistributed/) özelliğini kullanarak düzgün dağıtılmış ayarını uygulayabilirsiniz.

{{% /alert %}}

#### **Yatay Hizalama**

Metni yatay olarak hizalamak için [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesinin [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gethorizontalalignment/) özelliğini kullanın

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

    // Obtain the reference of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Set the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Dikey Hizalama**

Yatay hizalama ile benzer şekilde metni dikey olarak hizalamak için [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesinin [**GetVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getverticalalignment/) özelliğini kullanın.

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

    // Create workbook
    Workbook workbook;

    // Clearing all the worksheets
    workbook.GetWorksheets().Clear();

    // Adding a new worksheet to the Excel object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Setting the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();

    // Setting the vertical alignment of the text in a cell
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Girinti**

Hücredeki metnin girinti seviyesini [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesinin [**GetIndentLevel()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getindentlevel/) özelliği ile ayarlamak mümkündür.

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
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the indentation level
    style.SetIndentLevel(2);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Yönlendirme**

Hücrede metnin yönlendirmesini (döndürme) [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesinin [**GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) özelliği ile ayarlayın.

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
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the rotation angle of the text to 25 degrees
    style.SetRotationAngle(25);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook in Excel 97-2003 format
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Metin Kontrolü**

Aşağıdaki bölüm metin kaydırma, sığdırmayı daraltma ve diğer biçimlendirme seçeneklerini ayarlayarak metni nasıl kontrol edeceğinizi tartışmaktadır.

##### **Metni Kaydırma**

Hücrede metni kaydırmak onu okumayı kolaylaştırır: hücrenin yüksekliği, metni kesmek yerine veya yan hücrelere taşmak yerine tüm metni sığdırmak için ayarlanır. Metin kaydırma özelliğini [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesinin [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) özelliği ile açın veya kapatın.

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

    // Create Workbook Object
    Workbook wb;

    // Open first Worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Cells cell = ws.GetCells();

    // Increase the width of First Column Width
    cell.SetColumnWidth(0, 35);

    // Increase the height of first row
    cell.SetRowHeight(0, 36);

    // Add Text to the First Cell
    cell.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make Cell's Text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    wb.Save(outDir + u"WrappingText_out.xlsx");

    std::cout << "Text wrapping applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Sığdırmayı Daraltma**

Bir alanın metnini kaydırmak için bir seçenek, metni hücre boyutlarına sığdırmak için metin boyutunu küçültmektir. Bu, **true** olarak [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesinin [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) özelliği ile ayarlanır.

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
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set shrink to fit
    style.SetShrinkToFit(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Hücreleri Birleştirme**

Microsoft Excel gibi, Aspose.Cells birkaç hücreyi birleştirme işlemine destek verir. Aspose.Cells bu göreve iki yaklaşım sağlar. Bir yol, [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonunun [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) yöntemini çağırmaktır. [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) yöntemi hücreleri birleştirmek için aşağıdaki parametreleri alır:

- İlk satır: Birleştirmeye başlamak için ilk satır.
- İlk sütun: Birleştirmeye başlamak için ilk sütun.
- Satır sayısı: Birleştirilecek satır sayısı.
- Sütun sayısı: Birleştirilecek sütun sayısı.

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

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Diğer yol, öncelikle [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonunun [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) yöntemini çağırmak ve birleştirilecek hücrelerin aralığını oluşturmaktır. [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) yöntemi yukarıdaki [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) yönteminin aynı parametre setini alır ve bir [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) nesnesi döndürür. [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) nesnesi ayrıca [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) yöntemi sağlar, bu yöntem [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) nesnesinde belirtilen aralığı birleştirir.

##### **Metin Yönü**

Hücrelerdeki metnin okuma sırasını ayarlamak mümkündür. Okuma sırası, karakterlerin, kelimelerin vb. görüntülendiği görsel sıradır. Örneğin, İngilizce soldan sağa bir dil iken Arapça sağdan sola bir dildir.

Okuma sırası, [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesinin [**GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gettextdirection/) özelliği ile ayarlanır. Aspose.Cells, [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/) numaralandırmasında önceden tanımlanmış metin yönü türlerini sağlar.

|**Metin Yönü Türleri**|**Açıklama**|
| :- | :- |
|Context|Girilen ilk karakterin diline uygun okuma sırası|
|LeftToRight|Soldan sağa okuma sırası|
|RightToLeft|Sağdan sola okuma sırası|

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
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"I am using the latest version of Aspose.Cells to test this functionality.");

    // Get the style of cell A1
    Style style = cell.GetStyle();

    // Set text direction to left-to-right
    style.SetTextDirection(TextDirectionType::LeftToRight);

    // Apply the modified style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(u"book1.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Gelişmiş Konular**
- [Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma](/cells/tr/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Satır Sonları ve Metin Kaydırma](/cells/tr/cpp/line-breaks-and-text-wrapping/)
{{< app/cells/assistant language="cpp" >}}
