---
title: تحديد حقول الصيغة عند استيراد البيانات إلى ورقة عمل باستخدام C++
linktitle: تحديد حقول الصيغة أثناء استيراد البيانات إلى الورقة العمل
type: docs
weight: 300
url: /ar/cpp/specify-formula-fields-while-importing-data-to-worksheet/
description: تعلم كيفية تحديد حقول الصيغة عند استيراد البيانات إلى ورقة عمل من خلال API Aspose.Cells for C++.
keywords: تحديد حقول الصيغة أثناء استيراد البيانات إلى ورق العمل، ضبط حقول الصيغة عند إضافة البيانات إلى ورق العمل
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تحديد حقول الصيغة عند استيراد البيانات إلى ورق العمل الخاص بك باستخدام [**ImportTableOptions.GetIsFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/importtableoptions/getisformulas/). يأخذ هذا الخاصية مصفوفة بوليانية حيث القيمة الصحيحة تعني أن الحقل هو حقل صيغة. على سبيل المثال، إذا كان الحقل الثالث هو حقل صيغة، فإن القيمة الثالثة في المصفوفة ستكون صحيحة.

## **تحديد حقول الصيغة أثناء استيراد البيانات إلى الورقة العمل**

يرجى رؤية كود العينة التالي الذي يشرح كيفية تحديد حقل الصيغة أثناء استيراد البيانات إلى ورق العمل. يرجى رؤية ملف الإكسل الناتج المولد عن الكود ولقطة الشاشة التي تظهر تأثير الكود على ملف الإكسل الناتج.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **الكود المثالي**

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

static U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

class DataItems {
public:
    int Number1;
    int Number2;
    U16String Formula1;
    U16String Formula2;

    DataItems() : Number1(0), Number2(0) {}
};

void Run() {
    vector<DataItems> dis;

    DataItems di;
    di.Number1 = 2002;
    di.Number2 = 3502;
    di.Formula1 = u"=SUM(A2,B2)";
    di.Formula2 = u"=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")";
    dis.push_back(di);

    di = DataItems();
    di.Number1 = 2003;
    di.Number2 = 3503;
    di.Formula1 = u"=SUM(A3,B3)";
    di.Formula2 = u"=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")";
    dis.push_back(di);

    di = DataItems();
    di.Number1 = 2004;
    di.Number2 = 3504;
    di.Formula1 = u"=SUM(A4,B4)";
    di.Formula2 = u"=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")";
    dis.push_back(di);

    di = DataItems();
    di.Number1 = 2005;
    di.Number2 = 3505;
    di.Formula1 = u"=SUM(A5,B5)";
    di.Formula2 = u"=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")";
    dis.push_back(di);

    Workbook wb;
    Worksheet ws = wb.GetWorksheets().Get(0);

    for (size_t i = 0; i < dis.size(); ++i) {
        const DataItems& item = dis[i];
        int row = static_cast<int>(i);
        ws.GetCells().Get(row, 0).PutValue(item.Number1);
        ws.GetCells().Get(row, 1).PutValue(item.Number2);
        ws.GetCells().Get(row, 2).SetFormula(item.Formula1);
        ws.GetCells().Get(row, 3).SetFormula(item.Formula2);
    }

    wb.CalculateFormula();
    ws.AutoFitColumns();
    wb.Save(outputDir + u"outputSpecifyFormulaFieldsWhileImportingDataToWorksheet.xlsx");

    cout << "SpecifyFormulaFieldsWhileImportingDataToWorksheet executed successfully." << endl;
}

int main() {
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```
