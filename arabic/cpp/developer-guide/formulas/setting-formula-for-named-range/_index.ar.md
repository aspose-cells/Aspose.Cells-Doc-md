---
title: إعداد الصيغة لنطاق مسمى باستخدام ++C
linktitle: وضع صيغة لنطاق مسمى
type: docs
weight: 20
url: /ar/cpp/setting-formula-for-named-range/
description: تعلم كيفية تعيين الصيغ للنطاقات المسماة في ملفات Excel باستخدام Aspose.Cells مع C++.
---

## **وضع صيغة لنطاق مسمى**
مثل تطبيق Excel، توفر واجهات برمجة التطبيقات Aspose.Cells القدرة على تحديد صيغة لنطاق مسمى عند استخدام خاصيتها [GetRefersTo()](https://reference.aspose.com/cells/cpp/aspose.cells/range/getrefersto/). قد توجد العديد من سيناريوهات الاستخدام لهذه الميزة، وفيما يلي بعض الأمثلة التفصيلية.

### **وضع صيغة بسيطة لنطاق مسمى**
يمكن أن تكون الصيغة البسيطة إشارة إلى خلية أخرى في نفس جدول العمل (أو جداول عمل مختلفة). ينشئ المثال التالي نطاقًا مسمى في جدول بيانات جديد ويحدد إشارته إلى خلية أخرى.

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

    // Get the WorksheetCollection
    WorksheetCollection worksheets = book.GetWorksheets();

    // Add a new Named Range with name "NewNamedRange"
    int index = worksheets.GetNames().Add(u"NewNamedRange");

    // Access the newly created Named Range
    Name name = worksheets.GetNames().Get(index);

    // Set RefersTo property of the Named Range to a formula. Formula references another cell in the same worksheet
    name.SetRefersTo(u"=Sheet1!$A$3");

    // Set the formula in the cell A1 to the newly created Named Range
    worksheets.Get(0).GetCells().Get(u"A1").SetFormula(u"NewNamedRange");

    // Insert the value in cell A3 which is being referenced in the Named Range
    worksheets.Get(0).GetCells().Get(u"A3").PutValue(u"This is the value of A3");

    // Calculate formulas
    book.CalculateFormula();

    // Save the result in XLSX format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Named range created and formula calculated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **وضع صيغة معقدة لنطاق مسمى**
يمكن أن تكون الصيغة المعقدة أي شيء مثل نطاق ديناميكي أو صيغة تمتد عبر عدة خلايا في جداول عمل مختلفة. ينشئ المثال التالي نطاقًا ديناميكيًا باستخدام وظيفة INDEX للحصول على القيمة من قائمة استنادًا إلى موقعها.

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

    // Get the WorksheetCollection
    WorksheetCollection worksheets = book.GetWorksheets();

    // Add a new Named Range with name "data"
    int index = worksheets.GetNames().Add(u"data");

    // Access the newly created Named Range from the collection
    Name data = worksheets.GetNames().Get(index);

    // Set RefersTo property of the Named Range to a cell range in same worksheet
    data.SetRefersTo(u"=Sheet1!$A$1:$A$10");

    // Add another Named Range with name "range"
    index = worksheets.GetNames().Add(u"range");

    // Access the newly created Named Range from the collection
    Name range = worksheets.GetNames().Get(index);

    // Set RefersTo property to a formula using the Named Range data
    range.SetRefersTo(u"=INDEX(data,Sheet1!$A$1,1):INDEX(data,Sheet1!$A$1,9)");

    // Save the workbook
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Named ranges created and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

هنا مثال آخر يستخدم نطاقًا مسمى لجمع القيم من 2 خليتين في جداول عمل مختلفة.

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

    // Get the WorksheetCollection
    WorksheetCollection worksheets = book.GetWorksheets();

    // Insert some data in cell A1 of Sheet1
    worksheets.Get(u"Sheet1").GetCells().Get(u"A1").PutValue(10);

    // Add a new Worksheet and insert a value to cell A1
    worksheets.Get(worksheets.Add()).GetCells().Get(u"A1").PutValue(10);

    // Add a new Named Range with name "range"
    int index = worksheets.GetNames().Add(u"range");

    // Access the newly created Named Range from the collection
    Name range = worksheets.GetNames().Get(index);

    // Set RefersTo property of the Named Range to a SUM function
    range.SetRefersTo(u"=SUM(Sheet1!$A$1,Sheet2!$A$1)");

    // Insert the Named Range as formula to 3rd worksheet
    worksheets.Get(worksheets.Add()).GetCells().Get(u"A1").SetFormula(u"range");

    // Calculate formulas
    book.CalculateFormula();

    // Save the result in XLSX format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Output file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
