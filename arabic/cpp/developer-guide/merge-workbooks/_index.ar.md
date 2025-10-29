---
title: دمج عدة دفاتر عمل في دفتر عمل واحد باستخدام C++
linktitle: مدمج السجل
type: docs
weight: 66
url: /ar/cpp/combine-multiple-workbooks-into-a-single-workbook/
description: تعلّم كيفية دمج العديد من دفاتر العمل في دفتر واحد باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى دمج دفاتر عمل تحتوي على محتوى مختلف مثل الصور، المخططات، والبيانات إلى دفتر عمل واحد. يدعم Aspose.Cells هذه الميزة. تظهر هذه المقالة كيفية إنشاء تطبيق وحدة التحكم في Visual Studio ودمج دفاتر العمل ببضع أسطر برمجية بسيطة باستخدام Aspose.Cells.

{{% /alert %}}

## **دمج أسجل العمل مع الصور والرسوم البيانية**

يقوم الكود المثالي بدمج سجلي عمل في سجل عمل واحد باستخدام Aspose.Cells. الكود يحمل سجلي العمل المصدر ويستخدم الطريقة [**Workbook::Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/) لدمجهم ويحفظ سجل العمل الناتج.

### **السجلات المصدر**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **مصنفات الإخراج**

- [combined.xlsx](5473095.xlsx)

### **لقطات الشاشة**

أدناه تظهر لقطات من المصنفات الأصلية والمخرّجة.

{{% alert color="primary" %}}

يمكنك استخدام أي مصنف أصلي. هذه الصور مجرد لأغراض توضيحية.

{{% /alert %}}

**الورقة العمل الأولى لمصنف الرسوم البيانية - مكدسة** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**الورقة العمل الثانية لمصنف الرسوم البيانية - خطية** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**الورقة العمل الأولى لمصنف الصور - صورة** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**كل الورقات الثلاثة في مصنف الدمج - مكدسة، خطية، صورة** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of the first source excel file
    U16String sourceFile1 = srcDir + u"SampleChart.xlsx";

    // Path of the second source excel file
    U16String sourceFile2 = srcDir + u"SampleImage.xlsx";

    // Open the first excel file.
    Workbook sourceBook1(sourceFile1);

    // Open the second excel file.
    Workbook sourceBook2(sourceFile2);

    // Combining the two workbooks
    sourceBook1.Combine(sourceBook2);

    // Define the output file path
    U16String outputFilePath = srcDir + u"Combined.out.xlsx";

    // Save the target book file.
    sourceBook1.Save(outputFilePath);

    std::cout << "Workbooks combined and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [دمج الورقات المتعددة في ورقة عمل واحدة](/cells/ar/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [دمج الملفات](/cells/ar/cpp/merge-files/)
{{< app/cells/assistant language="cpp" >}}
