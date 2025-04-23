---
title: C++ ile Adlandırılmış Aralıkları Biçimlendirme ve Değiştirme
linktitle: Biçimlendirme ve Adlandırılmış Aralıkları Düzenleme
type: docs
weight: 85
url: /tr/cpp/format-and-modify-named-ranges/
description: Aspose.Cells kullanarak, Excel dosyalarında adlandırılmış aralıkları biçimlendirmeyi, yeniden adlandırmayı, birleştirmeyi ve kaldırmayı öğrenin.
---

## **Aralıkları Biçimlendirme**

### **Bir Adlandırılmış Aralığa Arkaplan Rengi ve Yazı Tipi Ayarlarını Tanımlama**

Biçimlendirme uygulamak için, stil ayarlarını belirtmek için bir [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesi tanımlayın ve ardından bu ayarları [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) nesnesine uygulayın.

Aşağıdaki örnek, bir aralığa katı doldurmalı rengi (gölge rengi) ve yazı tipi ayarlarını nasıl ayarlayacağınızı göstermektedir.

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
    Worksheet WS = workbook.GetWorksheets().Get(0);
    Range range = WS.GetCells().CreateRange(1, 1, 1, 18);

    range.SetName(u"MyRange");

    Style stl = workbook.CreateStyle();

    stl.GetFont().SetName(u"Arial");
    stl.GetFont().SetIsBold(true);
    stl.GetFont().SetColor(Color::Red());
    stl.SetForegroundColor(Color::Yellow());
    stl.SetPattern(BackgroundType::Solid);

    StyleFlag flg;
    flg.SetFont(true);
    flg.SetCellShading(true);

    range.ApplyStyle(stl, flg);

    workbook.Save(outDir + u"rangestyles.out.xls");

    Aspose::Cells::Cleanup();
}
```

### **Bir Adlandırılmış Aralığa Sınırlar Ekleme**

Yalnızca tek bir hücre değil, bir hücre aralığına sınırlar eklemek mümkündür. [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) nesnesi, hücre aralığına sınır eklemek için aşağıdaki parametreleri alabilen bir [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/) yöntemi sağlar.

- Kenar tipi, [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/) numaralandırmasından seçilen kenar tipi.
- Çizgi stili, [**CellBorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellbordertype/) numaralandırmasından seçilen çizgi stili.
- Renk, Renk numaralandırmasından seçilen çizgi rengi.

Aşağıdaki örnek, bir aralığa kenarlık eklemeyi gösterir.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Clears the worksheets
    workbook.GetWorksheets().Clear();

    // Adding a new worksheet to the Workbook object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
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

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Aşağıdaki örnek, aralıktaki her hücreye sınırların nasıl ayarlanacağını gösterir.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Access the cells in the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a range of cells
    Range range = cells.CreateRange(u"A6", u"P216");

    // Create the style adding to the style collection
    Style stl = workbook.CreateStyle();

    // Specify the font settings
    stl.GetFont().SetName(u"Arial");
    stl.GetFont().SetIsBold(true);
    stl.GetFont().SetColor(Color::Blue());

    // Set the borders
    stl.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    stl.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Blue());
    stl.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    stl.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Blue());
    stl.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    stl.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Blue());
    stl.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    stl.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Blue());

    // Create StyleFlag object
    StyleFlag flg;

    // Make the corresponding formatting attributes ON
    flg.SetFont(true);
    flg.SetBorders(true);

    // Apply the style with format settings to the range
    range.ApplyStyle(stl, flg);

    // Save the excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **İsimlendirilmiş Bir Aralığı Yeniden Adlandır**

Aspose.Cells, bir adınızı yeniden adlandırmak için olanak tanır. Adı alabilir ve [**Name.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells/name/gettext/) özniteliğini kullanarak yeniden adlandırabilirsiniz. Aşağıdaki örnek, bir adını yeniden adlandırmanın nasıl yapılacağını gösterir.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"RenamingRange.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the Cells of the sheet
    Cells cells = sheet.GetCells();

    // Get the named range "TestRange"
    Name name = workbook.GetWorksheets().GetNames().Get(u"TestRange");

    // Rename it
    name.SetText(u"NewRange");

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Range renamed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aralıkların Birleşimi**

Aspose.Cells, aralıklar için birliktelik almak amacıyla [**Range.UnionRang**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unionrang/) yöntemini sağlar, bu yöntem bir [*std::vector*](https://en.cppreference.com/w/cpp/container/vector) nesnesi döndürür. Aşağıdaki örnek, aralıklar için birliktelik almayı gösterir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook(srcDir + u"book1.xls");

    Vector<Range> ranges = workbook.GetWorksheets().GetNamedRanges();

    Style style = workbook.CreateStyle();
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);

    StyleFlag flag;
    flag.SetCellShading(true);

    Vector<Range> unionParams{ ranges[1] };
    UnionRange unionResult = ranges[0].UnionRanges(unionParams);
    Vector<Range> al = unionResult.GetRanges();

    for (int i = 0; i < al.GetLength(); i++)
    {
        Range rng = al[i];
        rng.ApplyStyle(style, flag);
    }

    workbook.Save(outDir + u"rngUnion.out.xls");

    std::cout << "Style applied to union ranges successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aralıkların Kesişimi**

Aspose.Cells, iki aralığın kesişimini belirlemek için [**Range.Intersect**](https://reference.aspose.com/cells/cpp/aspose.cells/range/intersect/) yöntemini sağlar. Yöntem bir [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) nesnesi döndürür. Bir aralığın başka bir aralıkla kesişip kesişmediğini kontrol etmek için [**Range.Intersect**](https://reference.aspose.com/cells/cpp/aspose.cells/range/intersect/) yöntemini kullanın, bu yöntem bir Boolean değeri döndürür. Aşağıdaki örnek, aralıkların nasıl kesiştirileceğini gösterir.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"rngIntersection.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the named ranges
    Vector<Range> ranges = workbook.GetWorksheets().GetNamedRanges();

    // Check whether the first range intersects the second range
    bool isIntersect = ranges[0].IsIntersect(ranges[1]);

    // Create a style object
    Style style = workbook.CreateStyle();

    // Set the shading color with solid pattern type
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);

    // Create a styleflag object
    StyleFlag flag;

    // Apply the cell shading
    flag.SetCellShading(true);

    // If first range intersects second range
    if (isIntersect)
    {
        // Create a range by getting the intersection
        Range intersection = ranges[0].Intersect(ranges[1]);

        // Name the range
        intersection.SetName(u"Intersection");

        // Apply the style to the range
        intersection.ApplyStyle(style, flag);
    }

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Range intersection processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **İsimlendirilmiş Aralıklarda Hücreleri Birleştirme**

Aspose.Cells, aralıktaki hücreleri birleştirmek için bir [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) yöntemi sağlar. Aşağıdaki örnek, bir isimlendirilmiş aralıktaki bireysel hücrelerin nasıl birleştirileceğini gösterir.

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

    // Instantiate a new Workbook
    Workbook wb1;

    // Get the first worksheet in the workbook
    Worksheet worksheet1 = wb1.GetWorksheets().Get(0);

    // Create a range
    Range mrange = worksheet1.GetCells().CreateRange(u"A18", u"J18");

    // Name the range
    mrange.SetName(u"Details");

    // Merge the cells of the range
    mrange.Merge();

    // Get the range by name
    Range range1 = wb1.GetWorksheets().GetRangeByName(u"Details");

    // Define a style object
    Style style = wb1.CreateStyle();

    // Set the alignment
    style.SetHorizontalAlignment(TextAlignmentType::Center);

    // Create a StyleFlag object
    StyleFlag flag;
    // Make the relative style attribute ON
    flag.SetHorizontalAlignment(true);

    // Apply the style to the range
    range1.ApplyStyle(style, flag);

    // Input data into range
    range1.Get(0, 0).PutValue(u"Aspose");

    // Save the excel file
    wb1.Save(outDir + u"mergingrange.out.xls");

    std::cout << "Range merged and styled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Adlandırılmış Bir Aralığı Kaldır**

Aspose.Cells, isimlendirdiğiniz aralığın adını silmeniz için [**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/) yöntemini sağlar. Aralığın içeriğini temizlemek için [**Cells.ClearRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/clearrange/) yöntemini kullanın. Aşağıdaki örnek, bir adlandırılmış aralığı nasıl kaldıracağını gösterir.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range of cells
    Range range1 = worksheet.GetCells().CreateRange(u"E12", u"I12");

    // Name the range
    range1.SetName(u"MyRange");

    // Set the outline border to the range
    range1.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Medium, Color::AliceBlue());
    range1.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Medium, Color::Red());
    range1.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Medium, Color::AliceBlue());
    range1.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Medium, Color::Red());

    // Input some data with some formattings into a few cells in the range
    range1.Get(0, 0).PutValue(u"Test");
    range1.Get(0, 4).PutValue(u"123");

    // Create another range of cells
    Range range2 = worksheet.GetCells().CreateRange(u"B3", u"F3");

    // Name the range
    range2.SetName(u"testrange");

    // Copy the first range into second range
    range2.Copy(range1);

    // Remove the previous named range (range1) with its contents
    worksheet.GetCells().ClearRange(11, 4, 11, 8);
    worksheets.GetNames().RemoveAt(0);

    // Save the excel file
    workbook.Save(outDir + u"copyranges.out.xls");

    Aspose::Cells::Cleanup();
}
```
