---
title: قراءة ملف CSV مع الترميز المتعدد باستخدام C++
linktitle: قراءة ملف CSV بترميزات متعددة
type: docs
weight: 200
url: /ar/cpp/reading-csv-file-with-multiple-encodings/
description: تعلم كيفية قراءة ملفات CSV ذات الترميزات المتعددة باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، يحتوي ملف CSV الخاص بك على ترميزات متعددة (Unicode، ANSI، UTF8، UTF7، إلخ). تتيح لك Aspose.Cells تحميل مثل هذه الملفات وتحويلها إلى تنسيقات أخرى، على سبيل المثال، PDF أو XLSX.

{{% /alert %}}

توفر Aspose.Cells الخاصية [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/)، والتي تحتاج إلى ضبطها على **true** لتحميل ملف CSV الخاص بك مع ترميزات متعددة بشكل صحيح.

 تظهر الصورة التالية مثالاً على ملف CSV يحتوي على سطرين. السطر الأول بالترميز **ANSI** والسطر الثاني بالترميز **Unicode**.

|**ملف الإدخال**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

 تظهر الصورة التالية ملف XLSX الذي تم تحويله من ملف CSV أعلاه دون ضبط الخاصية [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) على **true**. كما ترى، لم يتم تحويل النص Unicode بشكل صحيح.

|**ملف الإخراج 1: لم يتم اتخاذ إجراءات للتعامل مع الترميز المتعدد**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

تُظهر لقطة الشاشة التالية ملف XLSX الذي تم تحويله من ملف CSV أعلاه بعد تعيين خاصية [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) إلى **صحيح**. كما ترى، النص اليونيكود يُحوّل الآن بشكل صحيح.

|**ملف الإخراج 2: تم تعيين IsMultiEncoded على true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

أدناه الكود النموذجي الذي يحول ملف CSV أعلاه إلى صيغة XLSX بشكل صحيح.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input CSV file
    U16String filePath = srcDir + u"MultiEncoded.csv";

    // Create TxtLoadOptions and set MultiEncoded property to true
    TxtLoadOptions options;
    options.SetIsMultiEncoded(true);

    // Load the CSV file into Workbook with the specified options
    Workbook workbook(filePath, options);

    // Save the workbook in XLSX format
    workbook.Save(filePath + u".out.xlsx", SaveFormat::Xlsx);

    std::cout << "File converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## مقالات ذات صلة

- [فتح ملفات CSV](/cells/ar/cpp/opening-files-with-different-formats/#opening-csv-files)
