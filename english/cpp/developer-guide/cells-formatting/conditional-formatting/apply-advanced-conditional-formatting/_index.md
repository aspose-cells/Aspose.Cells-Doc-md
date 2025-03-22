---
title: Apply Advanced Conditional Formatting with C++
linktitle: Apply Advanced Conditional Formatting
description: How to use the Aspose.Cells library in C++ to apply advanced conditional formatting. By adjusting these criteria, you have more control over how cells look and appear.
keywords: Aspose.Cells, Advanced Conditional Formatting, C++, Conditional, Formatting
type: docs
weight: 70
url: /cpp/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}}

Microsoft Excel 2007 and later versions (2010/2013/2016) provides some advanced features for conditional formatting. For example, it lets you apply cell shading, borders, colored icons, arrows, flags and font formatting, etc. which has become quite sophisticated.

{{% /alert %}}

## **Apply Advanced Conditional Formatting to Microsoft Excel Files**
Conditional formatting can:

- Add shaded data bars to graphically enhance the underlying numbers by embedding a simple bar chart in the cells.
- Automatically shade cells with color scales based on their relation to values in other cells in the range. The default settings shades the lowest value in red moving up to the highest value in green.
- Use icon sets in a similar way to color scales, but rather than shading the cells it adds small icons, such as arrows and traffic lights to the cells.

Aspose.Cells fully supports the conditional formatting provided by Microsoft Excel 2007 and later versions in XLSX format on cells at runtime. This example demonstrates an exercise for advanced conditional formatting types including IconSets, DataBars, Color Scales, TimePeriods, Top/Bottom and other rules with different sets of attributes.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class ConditionalFormatting
{
private:
    Worksheet _sheet;

public:
    static void Run()
    {
        // Source directory path
        U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

        // Output directory path
        U16String outDir(u"..\\Data\\02_OutputDirectory\\");

        ConditionalFormatting obj;
        obj.DoTest(srcDir, outDir);
    }

    void DoTest(const U16String& srcDir, const U16String& outDir)
    {
        // Instantiate a workbook object
        Workbook book;

        // Create a worksheet object and get the first worksheet
        Worksheet sheet1 = book.GetWorksheets().Get(0);

        // Set the first worksheet to _sheet object
        _sheet = sheet1;

        // Call different custom methods
        AddDefaultIconSet();
        AddIconSet2();
        AddIconSet3();
        AddIconSet4();
        AddIconSet5();
        AddIconSet6();
        AddIconSet7();
        AddIconSet8();
        AddIconSet9();
        AddIconSet10();
        AddIconSet11();
        AddIconSet12();
        AddIconSet13();
        AddIconSet14();
        AddIconSet15();
        AddIconSet16();
        AddIconSet17();
        AddIconSet18();
        AddDefaultColorScale();
        Add3ColorScale();
        Add2ColorScale();
        AddAboveAverage();
        AddAboveAverage2();
        AddAboveAverage3();
        AddTop10_1();
        AddTop10_2();
        AddTop10_3();
        AddTop10_4();
        AddDataBar1();
        AddDataBar2();
        AddContainsText();
        AddNotContainsText();
        AddContainsBlank();
        AddNotContainsBlank();
        AddBeginWith();
        AddEndWith();
        AddContainsError();
        AddNotContainsError();
        AddDuplicate();
        AddUnique();
        AddTimePeriod_1();
        AddTimePeriod_2();
        AddTimePeriod_3();
        AddTimePeriod_4();
        AddTimePeriod_5();
        AddTimePeriod_6();
        AddTimePeriod_7();
        AddTimePeriod_8();
        AddTimePeriod_9();
        AddTimePeriod_10();

        // AutoFit M Column in the worksheet
        _sheet.AutoFitColumn(12);

        // Specify the output file path
        U16String outfn = outDir + u"Testoutput.out.xlsx";

        // Save the excel file
        book.Save(outfn, SaveFormat::Xlsx);
    }

private:
    void AddIconSet2()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M1:O2", Color::AliceBlue());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::Arrows3);
        Cell c = _sheet.GetCells().Get(u"M1");
        c.PutValue(u"Arrows3");
    }

    void AddIconSet3()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M3:O4", Color::AntiqueWhite());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::Arrows4);
        Cell c = _sheet.GetCells().Get(u"M3");
        c.PutValue(u"Arrows4");
    }

    void AddIconSet4()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M5:O6", Color::Aqua());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::Arrows5);
        Cell c = _sheet.GetCells().Get(u"M5");
        c.PutValue(u"Arrows5");
    }

    void AddIconSet5()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M7:O8", Color::Aquamarine());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::ArrowsGray3);
        Cell c = _sheet.GetCells().Get(u"M7");
        c.PutValue(u"ArrowsGray3");
    }

    void AddIconSet6()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M9:O10", Color::Azure());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::ArrowsGray4);
        Cell c = _sheet.GetCells().Get(u"M9");
        c.PutValue(u"ArrowsGray4");
    }

    void AddIconSet7()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M11:O12", Color::Beige());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::ArrowsGray5);
        Cell c = _sheet.GetCells().Get(u"M11");
        c.PutValue(u"ArrowsGray5");
    }

    void AddIconSet8()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M13:O14", Color::Bisque());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::Flags3);
        Cell c = _sheet.GetCells().Get(u"M13");
        c.PutValue(u"Flags3");
    }

    void AddIconSet9()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M15:O16", Color::BlanchedAlmond());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::Quarters5);
        Cell c = _sheet.GetCells().Get(u"M15");
        c.PutValue(u"Quarters5");
    }

    void AddIconSet10()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M17:O18", Color::Blue());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::Rating4);
        Cell c = _sheet.GetCells().Get(u"M17");
        c.PutValue(u"Rating4");
    }

    void AddIconSet11()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M19:O20", Color::BlueViolet());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::Rating5);
        Cell c = _sheet.GetCells().Get(u"M19");
        c.PutValue(u"Rating5");
    }

    void AddIconSet12()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M21:O22", Color::Brown());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::RedToBlack4);
        Cell c = _sheet.GetCells().Get(u"M21");
        c.PutValue(u"RedToBlack4");
    }

    void AddIconSet13()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M23:O24", Color::BurlyWood());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::Signs3);
        Cell c = _sheet.GetCells().Get(u"M23");
        c.PutValue(u"Signs3");
    }

    void AddIconSet14()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M25:O26", Color::CadetBlue());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::Symbols3);
        Cell c = _sheet.GetCells().Get(u"M25");
        c.PutValue(u"Symbols3");
    }

    void AddIconSet15()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M27:O28", Color::Chartreuse());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::Symbols32);
        Cell c = _sheet.GetCells().Get(u"M27");
        c.PutValue(u"Symbols32");
    }

    void AddIconSet16()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M29:O30", Color::Chocolate());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::TrafficLights31);
        Cell c = _sheet.GetCells().Get(u"M29");
        c.PutValue(u"TrafficLights31");
    }

    void AddIconSet17()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M31:O32", Color::Coral());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::TrafficLights32);
        Cell c = _sheet.GetCells().Get(u"M31");
        c.PutValue(u"TrafficLights32");
    }

    void AddIconSet18()
    {
        FormatConditionCollection conds = GetFormatCondition(u"M33:O35", Color::CornflowerBlue());
        int32_t idx = conds.AddCondition(FormatConditionType::IconSet);
        FormatCondition cond = conds.Get(idx);
        cond.GetIconSet().SetType(IconSetType::TrafficLights4);
        Cell c = _sheet.GetCells().Get(u"M33");
        c.PutValue(u"TrafficLights4");
    }

    void AddTimePeriod_10()
    {
        FormatConditionCollection conds = GetFormatCondition(u"I19:K20", Color::MediumSeaGreen());
        int32_t idx = conds.AddCondition(FormatConditionType::TimePeriod);
        FormatCondition cond = conds.Get(idx);
        cond.GetStyle().SetBackgroundColor(Color::Pink());
        cond.GetStyle().SetPattern(BackgroundType::Solid);
        cond.SetTimePeriod(TimePeriodType::Yesterday);
        Cell c = _sheet.GetCells().Get(u"I19");
        Style style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);
        c.PutValue(Date(2008, 7, 30));
        c = _sheet.GetCells().Get(u"K20");
        c.PutValue(Date(2008, 8, 3));

        style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);

        c = _sheet.GetCells().Get(u"I20");
        c.PutValue(u"Yesterday");
    }

    void AddTimePeriod_9()
    {
        FormatConditionCollection conds = GetFormatCondition(u"I17:K18", Color::MediumPurple());
        int32_t idx = conds.AddCondition(FormatConditionType::TimePeriod);
        FormatCondition cond = conds.Get(idx);
        cond.GetStyle().SetBackgroundColor(Color::Pink());
        cond.GetStyle().SetPattern(BackgroundType::Solid);
        cond.SetTimePeriod(TimePeriodType::Tomorrow);
        Cell c = _sheet.GetCells().Get(u"I17");
        Style style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);
        c.PutValue(Date(2008, 8, 1));
        c = _sheet.GetCells().Get(u"K18");
        c.PutValue(Date(2008, 8, 3));
        style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);

        c = _sheet.GetCells().Get(u"I18");
        c.PutValue(u"Tomorrow");
    }

    void AddTimePeriod_8()
    {
        FormatConditionCollection conds = GetFormatCondition(u"I15:K16", Color::MediumOrchid());
        int32_t idx = conds.AddCondition(FormatConditionType::TimePeriod);
        FormatCondition cond = conds.Get(idx);
        cond.GetStyle().SetBackgroundColor(Color::Pink());
        cond.GetStyle().SetPattern(BackgroundType::Solid);
        cond.SetTimePeriod(TimePeriodType::ThisWeek);
        Cell c = _sheet.GetCells().Get(u"I15");
        Style style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);
        c.PutValue(Date(2008, 7, 28));
        c = _sheet.GetCells().Get(u"K16");
        c.PutValue(Date(2008, 8, 3));
        style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);

        c = _sheet.GetCells().Get(u"I16");
        c.PutValue(u"ThisWeek");
    }

    void AddTimePeriod_7()
    {
        FormatConditionCollection conds = GetFormatCondition(u"I13:K14", Color::MediumBlue());
        int32_t idx = conds.AddCondition(FormatConditionType::TimePeriod);
        FormatCondition cond = conds.Get(idx);
        cond.GetStyle().SetBackgroundColor(Color::Pink());
        cond.GetStyle().SetPattern(BackgroundType::Solid);
        cond.SetTimePeriod(TimePeriodType::ThisMonth);
        Cell c = _sheet.GetCells().Get(u"I13");
        Style style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);
        c.PutValue(Date(2008, 7, 5));
        c = _sheet.GetCells().Get(u"K14");
        c.PutValue(Date(2008, 5, 30));
        style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);

        c = _sheet.GetCells().Get(u"I14");
        c.PutValue(u"ThisMonth");
    }

    void AddTimePeriod_6()
    {
        FormatConditionCollection conds = GetFormatCondition(u"I11:K12", Color::MediumAquamarine());
        int32_t idx = conds.AddCondition(FormatConditionType::TimePeriod);
        FormatCondition cond = conds.Get(idx);
        cond.GetStyle().SetBackgroundColor(Color::Pink());
        cond.GetStyle().SetPattern(BackgroundType::Solid);
        cond.SetTimePeriod(TimePeriodType::NextWeek);
        Cell c = _sheet.GetCells().Get(u"I11");
        Style style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);
        c.PutValue(Date(2008, 8, 5));
        c = _sheet.GetCells().Get(u"K12");
        c.PutValue(Date(2008, 7, 30));
        style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);

        c = _sheet.GetCells().Get(u"I12");
        c.PutValue(u"NextWeek");
    }

    void AddTimePeriod_5()
    {
        FormatConditionCollection conds = GetFormatCondition(u"I9:K10", Color::Maroon());
        int32_t idx = conds.AddCondition(FormatConditionType::TimePeriod);
        FormatCondition cond = conds.Get(idx);
        cond.GetStyle().SetBackgroundColor(Color::Pink());
        cond.GetStyle().SetPattern(BackgroundType::Solid);
        cond.SetTimePeriod(TimePeriodType::NextMonth);
        Cell c = _sheet.GetCells().Get(u"I9");
        Style style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);
        c.PutValue(Date(2008, 8, 25));
        c = _sheet.GetCells().Get(u"K10");
        c.PutValue(Date(2008, 7, 30));
        style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);
        c = _sheet.GetCells().Get(u"I10");
        c.PutValue(u"NextMonth");
    }

    void AddTimePeriod_4()
    {
        FormatConditionCollection conds = GetFormatCondition(u"I7:K8", Color::Linen());
        int32_t idx = conds.AddCondition(FormatConditionType::TimePeriod);
        FormatCondition cond = conds.Get(idx);
        cond.GetStyle().SetBackgroundColor(Color::Pink());
        cond.GetStyle().SetPattern(BackgroundType::Solid);
        cond.SetTimePeriod(TimePeriodType::LastWeek);
        Cell c = _sheet.GetCells().Get(u"I7");
        Style style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);
        c.PutValue(Date(2008, 7, 25));
        c = _sheet.GetCells().Get(u"K8");
        c.PutValue(Date(2008, 7, 30));
        style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);

        c = _sheet.GetCells().Get(u"I8");
        c.PutValue(u"LastWeek");
    }

    void AddTimePeriod_3()
    {
        FormatConditionCollection conds = GetFormatCondition(u"I5:K6", Color::Linen());
        int32_t idx = conds.AddCondition(FormatConditionType::TimePeriod);
        FormatCondition cond = conds.Get(idx);
        cond.GetStyle().SetBackgroundColor(Color::Pink());
        cond.GetStyle().SetPattern(BackgroundType::Solid);
        cond.SetTimePeriod(TimePeriodType::LastMonth);
        Cell c = _sheet.GetCells().Get(u"I5");
        Style style = c.GetStyle();
        style.SetNumber(30);
        c.SetStyle(style);
        c.PutValue(Date(2008, 6, 26));
        c = _sheet.GetCells().Get(u"K6");
        c.PutValue(Date(2008,

### **Compute the Color Chosen by Microsoft Excel for ColorScale Conditional Formatting**
Aspose.Cells lets you calculate the color selected by Microsoft Excel when ColorScale conditional formatting is used in a template file. See the sample code below to learn how to compute the color selected by Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a workbook object and open the template file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Get the conditional formatting resultant object
    ConditionalFormattingResult cfr1 = a1.GetConditionalFormattingResult();

    // Get the ColorScale resultant color object
    Aspose::Cells::Color c = cfr1.GetColorScaleResult();

    // Read the color
    std::cout << c.GetArgb() << std::endl;
    std::cout << c.ToString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```