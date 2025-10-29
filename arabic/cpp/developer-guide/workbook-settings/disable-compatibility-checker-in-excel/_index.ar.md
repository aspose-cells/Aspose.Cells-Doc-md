---
title: تعطيل مدقق التوافق في Excel باستخدام C++
linktitle: تعطيل مدقق التوافق
type: docs
weight: 170
url: /ar/cpp/disable-compatibility-checker-in-excel/
description: تظهر هذه المقالة كيفية تعطيل مدقق التوافق من خلال API الخاص بـ Aspose.Cells for C++.
keywords: تعطيل مدقق التوافق في C++، تعطيل مدقق التوافق في Excel باستخدام C++، تعطيل مدقق التوافق في دفتر العمل. 
---

## تعطيل مدقق التوافق في أوراق عمل Excel باستخدام C++

{{% alert color="primary" %}}

يُعلق مُدقق التوافق في Microsoft Excel علامة عند حفظ ملف في تنسيق ملف أقدم قد يتسبب في مشكلات الوظائف أو فقدان الصِدق. مُدقق التوافق هو ميزة في Microsoft Office Excel 2007 و Microsoft Excel 2010.

عند حفظ دفتر عمل في إصدار سابق، Excel 97 من خلال Excel 2003، من Excel 2007 أو Excel 2010، يقوم مُدقق التوافق بفحص الدفتر لمعرفة ما إذا كان يحتوي على ميزات لا تدعمها الإصدار السابق. لمساعدتك في اتخاذ قرارات حول كيفية التعامل مع مشكلات التوافق، يعرض مُدقق التوافق صناديق حوار مع خيارات. يمكن أيضًا استخدامه لإنشاء تقرير عن أي مشكلات في الدفتر، أو تعطيل الميزة.

في بعض الأحيان، قد تحتاج إلى تعطيل مُدقق التوافق لجدول بيانات معين. باستخدام واجهات برمجة التطبيقات لـ Aspose.Cells يمكنك القيام بذلك بشكل برمجي حتى لا يشعر المستخدمون بالإحباط أو الارتباك بظهور صندوق حوار مُدقق التوافق عند إعادة حفظ الملف في Microsoft Excel يدويًا.

{{% /alert %}}

## **كيفية تعطيل مُدقق التوافق باستخدام Microsoft Excel**

- (Excel 2007) على زر الأوفيس، انقر على **إعداد**, ثم **تشغيل مُدقق التوافق**, ثم قم بمسح خيار **التحقق من التوافق عند حفظ هذا الدفتر**.

- (Excel 2010) على علامة التبويب الملف، انقر فوق **معلومات**, ثم **البحث عن مشكلات**, انقر على **التحقق من التوافق**, وبصورة نهائية، قم بمسح خيار **التحقق من التوافق عند حفظ هذا الدفتر**.
كيفية تعطيل مُدقق التوافق باستخدام واجهات برمجة التطبيقات لـ Aspose.Cells

## **قم بتعيين الخاصية {0} إلى **False** لتعطيل مُدقق التوافق في Microsoft Excel.**

قم بتعيين الخاصية [**Workbook.GetCheckCompatibility()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcompatibility/) إلى **False** لتعطيل مُحقق التوافق في Microsoft Excel.

### **أمثلة على الشفرة**

 تظهر الأمثلة التالية كيفيه تعطيل مدقق التوافق باستخدام Aspose.Cells for C++.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open a template file
    U16String templateFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(templateFilePath);

    // Disable the compatibility checker
    workbook.GetSettings().SetCheckCompatibility(false);

    // Path to save the output file
    U16String outputFilePath = srcDir + u"Output_BK_CompCheck.out.xlsx";

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
