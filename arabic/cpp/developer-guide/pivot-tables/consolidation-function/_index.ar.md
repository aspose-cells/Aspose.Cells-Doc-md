---
title: وظيفة التوحيد مع C++
linktitle: وظيفة التوحيد
type: docs
weight: 20
url: /ar/cpp/consolidation-function/
description: تعلم كيفية تطبيق وظيفة التوحيد على حقول البيانات في جدول محوري باستخدام Aspose.Cells مع C++.
---

## **وظيفة التوحيد**

يمكن استخدام Aspose.Cells لتطبيق وظيفة التوحيد على حقول البيانات (أو حقول القيم) لجدول Pivot. في Microsoft Excel، يمكنك نقر بزر الماوس الأيمن على حقل القيم ومن ثم تحديد اختيار **إعدادات حقل القيم...** ثم تحديد علامة **تلخيص القيم بواسطة**. من هناك، يمكنك تحديد أي وظيفة توحيد تفضل مثل Sum، Count، Average، Max، Min، Product، Distinct Count، إلخ.

يوفر Aspose.Cells تعدادًا [**ConsolidationFunction**](https://reference.aspose.com/cells/cpp/aspose.cells/consolidationfunction/) لدعم وظائف التوحيد التالية.

- وظيفة التوحيد::متوسط
- وظيفة التوحيد::عدد
- وظيفة التوحيد::عدد الأرقام
- وظيفة التوحيد::العدد المميز
- وظيفة التوحيد::الحد الأقصى
- وظيفة التوحيد::الحد الأدنى
- وظيفة التوحيد::المنتج
- وظيفة التوحيد::الانحراف المعياري
- وظيفة التوحيد::الانحراف المعياري المبلغ
- وظيفة التوحيد::المجموع
- وظيفة التوحيد::التغير
- وظيفة التوحيد::التغير المبلغ

### **تطبيق وظيفة التوحيد على حقول البيانات لجدول الإحصائيات**

يطبق الكود التالي وظيفة تجميع **المتوسط** على الحقل الأول من البيانات (أو حقل القيمة) ووظيفة تجميع **عدد فريد** على الحقل الثاني من البيانات (أو حقل القيمة).

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
    U16String inputFilePath = srcDir + u"Book.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table of the worksheet
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Apply Average consolidation function to first data field
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Average);

    // Apply DistinctCount consolidation function to second data field
    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::DistinctCount);

    // Calculate the data to make changes affect
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

دعم وظيفة تجميع العدد المميز من قبل Microsoft Excel 2013 فقط.

{{% /alert %}}
