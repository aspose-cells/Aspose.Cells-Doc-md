---
title: أشكال في الرسوم البيانية باستخدام C++
linktitle: الأشكال في الرسوم البيانية
description: تعلم كيفية استخدام Aspose.Cells for C++ لإضافة عناصر تحكم وتخصيص الرسوم البيانية في مايكرسوفت إكسل. سيُظهر دليلنا كيفية التلاعب بعناصر الرسم البياني، وتعديل التنسيق، وتحسين المظهر العام وسهولة استخدام الرسوم البيانية.
keywords: Aspose.Cells for C++، عناصر تحكم الرسوم البيانية، تخصيص الرسم البياني، مايكرسوفت إكسل، عناصر الرسم البياني، التنسيق.
type: docs
weight: 70
url: /ar/cpp/controls-in-charts/
---

{{% alert color="primary" %}}

أحيانًا تحتاج إلى إدراج كائنات الرسم مثل التسميات وصناديق النص والصور وما إلى ذلك في رسم بياني. يمكن لـ Aspose.Cells إضافة عناصر التحكم إلى رسم بياني في وقت التشغيل.

{{% /alert %}}

## **إضافة عنصر تحكم التسمية إلى الرسم البياني.**

توفر التسميات وسيلة لإعطاء معلومات للمستخدمين حول محتوى جدول البيانات.
تتيح لك Aspose.Cells إضافة التسميات والتلاعب بها حتى في الرسوم البيانية.

يقدم فصل [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) طريقة باسم [**AddLabelInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabelinchart/)، تُستخدم لإضافة عنصر تسمية إلى الرسم البياني. إليك قائمة بالمعلمات المستخدمة لهذا الأسلوب:

- الأعلى - الإزاحة الرأسية للتسمية عن الزاوية اليسرى العلوية بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- اليسار - الإزاحة الرأسية للتسمية عن الزاوية اليسرى العلوية بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- الارتفاع - ارتفاع التسمية، بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- العرض - عرض التسمية، بوحدات تمثل 1/4000 من منطقة الرسم البياني.

يرجع الأسلوب كائن [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/). يمثل فصل [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) تسمية في الرسم البياني وله بعض الأعضاء المهمة:

- [**Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) (خاصية) – يحدد نص عنوان التسمية.
- [**Fill**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getfill/) (خاصية) - تحدد سمات لون التعبئة.

المثال التالي يوضح كيفية إضافة تسمية إلى الرسم البياني. يستخدم المثال ملف مصمم (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نستخدم هذا الملف لإدراج تسمية في الرسم البياني. وفيما يلي الشفرة الأصلية لإضافة تسمية إلى الرسم البياني. يتم إنشاء الناتج التالي عند تنفيذ الشفرة.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Aspose::Cells::Charts::Chart chart = sheet.GetCharts().Get(0);

    // Add a new label to the chart
    Label label = chart.GetShapes().AddLabelInChart(100, 100, 350, 900);

    // Set the caption of the label
    label.SetText(u"A Label In Chart");

    // Set the Placement Type, the way the Label is attached to the cells
    label.SetPlacement(PlacementType::FreeFloating);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Label added to chart successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إضافة عنصر تحكم مربع نص إلى الرسم البياني**

واحدة من الطرق لتسليط الضوء على معلومات مهمة في تقرير هي استخدام مربع نص. على سبيل المثال، أدخل نصًا لتسليط الضوء على اسم الشركة أو الإشارة إلى المنطقة الجغرافية ذات أعلى مبيعات. يوفر فصل [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) طريقة باسم [**AddTextBoxInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addtextboxinchart/)، تُستخدم لإضافة عنصر مربع النص إلى الرسم البياني. إليك قائمة المعلمات المستخدمة لهذا الأسلوب:

- **top** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **left** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **height** - ارتفاع مربع النص ، بوحدات 1/4000 من منطقة الرسم البياني.
- **width** - عرض مربع النص ، بوحدات 1/4000 من منطقة الرسم البياني.

يرجع الأسلوب كائن [**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/). يمثل فصل [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/) مربع نص في الرسم البياني.

المثال التالي يوضح كيفية إضافة مربع نص إلى رسم بياني. يستخدم المثال الملف المصمم السابق (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نستخدم هذا الملف لإدراج مربع نص في الرسم البياني لعرض عنوان الرسم البياني. يتم إنشاء الشفرة الأصلية لإضافة مربع نص إلى الرسم البياني أدناه.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Aspose::Cells::Charts::Chart chart = sheet.GetCharts().Get(0);

    // Add a new textbox to the chart
    TextBox textbox0 = chart.GetShapes().AddTextBoxInChart(100, 1100, 350, 2550);

    // Fill the text
    textbox0.SetText(u"Sales By Region");

    // Set the font color
    textbox0.GetFont().SetColor(Color::Maroon());

    // Set the font to bold
    textbox0.GetFont().SetIsBold(true);

    // Set the font size
    textbox0.GetFont().SetSize(14);

    // Set font attribute to italic
    textbox0.GetFont().SetIsItalic(true);

    // Get the fill format of the textbox
    FillFormat fillformat = textbox0.GetFill();

    // Get the line format type of the textbox
    LineFormat lineformat = textbox0.GetLine();

    // Set the line weight
    lineformat.SetWeight(2);

    // Set the dash style to solid
    lineformat.SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Textbox added to chart successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إضافة صورة إلى الرسم البياني**

تسمح Aspose.Cells لك بإدراج الصور في الرسم البياني. على سبيل المثال ، أضف صورة لتسليط الضوء على الرسم البياني أو محتوياته بمعنى أكبر ، أو قم بإدراج ملف صورة العلامة التجارية.

يقدم فصل [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) طريقة باسم [**AddPictureInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpictureinchart/)، تُستخدم لإضافة كائن صورة إلى الرسم البياني. إليك قائمة المعلمات المستخدمة لهذا الأسلوب:

- **top** - الإزاحة الرأسية للصورة من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **left** - الإزاحة الرأسية للصورة من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **stream** - كائن تدفق يحتوي على بيانات الصورة.
- **widthScale** - مقياس عرض الصورة ، قيمة نسبية.
- **heightScale** - مقياس ارتفاع الصورة ، قيمة نسبية.

يرجع الأسلوب كائن [**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). يمثل فصل [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) كائن صورة في الرسم البياني.

المثال التالي يوضح كيفية إضافة صورة إلى الرسم البياني. يستخدم المثال الملف التصميمي السابق (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نحن نستخدم هذا الملف لإدراج صورة في الرسم البياني. أدناه هو الكود الأصلي لإضافة صورة إلى الرسم البياني.

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

std::vector<uint8_t> ReadFileData(const U16String& filePath) {
    std::ifstream file(filePath.ToUtf8(), std::ios::binary | std::ios::ate);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector<uint8_t> buffer(size);
    if (!file.read(reinterpret_cast<char*>(buffer.data()), size)) {
        throw std::runtime_error("Error reading file");
    }
    return buffer;
}

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"chart.xls");
    std::vector<uint8_t> imageData = ReadFileData(srcDir + u"logo.jpg");

    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Chart chart = sheet.GetCharts().Get(0);
    Vector<uint8_t> data(imageData.data(), static_cast<int32_t>(imageData.size()));
    Picture pic0 = chart.GetShapes().AddPictureInChart(50, 50, data, 40, 40);
    LineFormat lineFormat = pic0.GetLine();

    lineFormat.SetDashStyle(MsoLineDashStyle::Solid);
    lineFormat.SetWeight(4);

    workbook.Save(outDir + u"chart.out.xls");
    std::cout << "Chart modified successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **إضافة خانة اختيار في الرسم البياني**

تسمح Aspose.Cells بإدراج خانات الاختيار في ورقة الرسم البياني باستخدام تعداد [**MsoDrawingType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msodrawingtype/). يوضح المثال التالي إضافة خانة اختيار إلى ورقة الرسم البياني.

الصورة التالية تظهر ورقة الرسم البياني مع خانة الاختيار في ملف الإخراج.

![todo:image_alt_text](controls-in-charts_1.jpg)

الملف الناتج (101089316.xlsx) الذي تم إنشاؤه بواسطة مقتطف الكود التالي مرفق للرجوع إليه.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a chart sheet to the workbook
    int32_t index = workbook.GetWorksheets().Add(SheetType::Chart);

    // Get the newly added chart sheet
    Worksheet sheet = workbook.GetWorksheets().Get(index);

    // Add a floating chart to the sheet
    sheet.GetCharts().AddFloatingChart(ChartType::Column, 0, 0, 1024, 960);

    // Add data series to the chart
    sheet.GetCharts().Get(0).GetNSeries().Add(U16String(u"{1,2,3}"), false);

    // Add a checkbox to the chart
    sheet.GetCharts().Get(0).GetShapes().AddShapeInChart(MsoDrawingType::CheckBox, PlacementType::Move, 400, 400, 1000, 600);

    // Set text for the checkbox
    sheet.GetCharts().Get(0).GetShapes().Get(0).SetText(U16String(u"CheckBox 1"));

    // Save the workbook
    workbook.Save(outDir + u"InsertCheckboxInChartSheet_out.xlsx");

    std::cout << "Checkbox added to chart sheet successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [إضافة علامة مائية WordArt إلى الرسم البياني](/cells/ar/cpp/add-wordart-watermark-to-chart/)
{{< app/cells/assistant language="cpp" >}}
