---
title: تحويل البيانات النصية الرقمية إلى أرقام باستخدام C++
linktitle: تحويل بيانات النص الرقمي إلى رقم
type: docs
weight: 900
url: /ar/cpp/convert-text-numeric-data-to-number/
description: تعلم كيفية تحويل الأرقام المخزنة كنص في Excel إلى أرقام باستخدام واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: تحويل النص إلى عدد في Excel، تحويل النص إلى عدد باستخدام C++، تحويل البيانات النصية الرقمية إلى رقم، تحويل البيانات النصية الرقمية إلى رقم C++، تحويل النص الرقمي إلى رقم، تحويل النص الرقمي إلى رقم باستخدام C++، تحويل النص الرقمي إلى رقم في Excel باستخدام C++، تحويل النص الرقمي إلى رقم في Excel، تحويل السلسلة الرقمية إلى رقم في Excel، تحويل البيانات النصية الرقمية إلى رقم C++، تحويل السلسلة الرقمية إلى رقم C++
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، ترغب في تحويل البيانات الرقمية التي تم إدخالها كنص إلى أرقام. يمكنك إدخال الأرقام كنص في Microsoft Excel عن طريق وضع علامة ترقيمية قبل الرقم، على سبيل المثال **'12345**. بعد ذلك، يعامل Excel الرقم كسلسلة. Aspose.Cells تتيح لك تحويل السلاسل إلى أرقام.

## كيفية تحويل الأرقام المخزنة كنصوص إلى أرقام في Excel
يمكنك تحويل الأرقام المخزنة كنصوص إلى أرقام باتباع خطوات بسيطة قليلة.
1. حدد أي خلية واحدة أو مجموعة من الخلايا التي تحتوي على مؤشر خطأ في الزاوية العلوية اليسرى.
2. بجانب الخلية المحددة أو مجموعة الخلايا، انقر فوق زر الخطأ الذي يظهر. في القائمة، انقر على تحويل إلى رقم. 
<br>
<img src="4.png" width=70% />
3. إذا كان زر التنبيه غير متاح، حدد العمود الذي يوجد به المشكلة. إذا كنت لا ترغب في تحويل العمود كاملاً، يمكنك تحديد خلية واحدة أو أكثر بدلاً من ذلك. فقط تأكد من أن الخلايا التي تحددها في نفس العمود، وإلا فإن هذه العملية لن تعمل. زر النص إلى أعمدة عادة ما يستخدم لتقسيم عمود، ولكن يمكن أيضاً استخدامه لتحويل عمود واحد من النصوص إلى أرقام. في علامة البيانات، انقر فوق النص إلى أعمدة.
<br>
<img src="1.png" width=70% />
4. انقر فوق زر الانتهاء في صندوق البوب ​​آب.
<br>
<img src="2.png" width=70% />
5. يتم تحويل الأرقام المخزنة كنصوص إلى أرقام.
<br>
<img src="3.png" width=70% />

## كيفية تحويل الأرقام المخزنة كنص إلى أرقام باستخدام Aspose.Cells for C++
توفر Aspose.Cells الطريقة [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/convertstringtonumericvalue/) التي يمكن استخدامها لتحويل جميع البيانات الرقمية النصية إلى أرقام.

تظهر اللقطة الشاشية التالية أرقام سلسلة في الخلايا **A1:A17**. تم تحويل أرقام السلسلة إلى أرقام باستخدام {0} في اللقطة الشاشية التالية. كما يمكنك رؤيتها، فهي محاذاة الآن إلى اليمين.
<br>
<img src="5.png" width=70% />

تم تحويل هذه الأرقام النصية إلى أرقام باستخدام [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/convertstringtonumericvalue/) في اللقطة الشاشية التالية. كما يمكنك رؤيتها، فهي الآن محاذاة إلى اليمين.
<br>
<img src="6.png" width=70% />

## رمز C++ لتحويل البيانات النصية الرقمية إلى أرقام فعلية

يوضح الكود العيني التالي كيفية تحويل جميع البيانات الرقمية النصية إلى أرقام فعلية في جميع أوراق العمل.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate workbook object with an Excel file
    U16String inputFilePath = srcDir + u"SampleBook.xlsx";
    Workbook workbook(inputFilePath);

    // Iterate through all worksheets and convert string values to numeric
    for (int32_t i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        workbook.GetWorksheets().Get(i).GetCells().ConvertStringToNumericValue();
    }

    // Save the Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
