---
title: حفظ الملف إلى كائن الاستجابة باستخدام C++
linktitle: حفظ الملف في كائن الاستجابة
type: docs
weight: 50
url: /ar/cpp/saving-file-to-response-object/
description: تعلم كيفية حفظ الملفات بشكل ديناميكي وإرسالها مباشرة إلى متصفح العميل باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

تجعل Aspose.Cells من الممكن التلاعب بالملفات. يشرح هذا المقال الطرق المختلفة التي يمكن بواسطتها حفظ الملفات في كائن الاستجابة.

{{% /alert %}}

## **حفظ الملف في كائن الاستجابة**

من الممكن أيضًا إنشاء ملف بشكل ديناميكي وإرساله مباشرة إلى متصفح العميل. من أجل القيام بذلك، استخدم النسخة المطوَّرة خصيصًا للطريقة [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) التي تقبل المعاملات التالية:

- كائن **HttpResponse**.
- اسم الملف.
- [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/)، نوع إعلان المحتوى النوعي لملف الإخراج.
- [**SaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/saveoptions/)، نوع تنسيق الملف.

تحدد تعداد [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/) ما إذا كان الملف المرسل إلى المستعرض يوفر الخيار للفتح بذاته مباشرة في المستعرض أو في تطبيق مرتبط بامتداد .xls/.xlsx أو امتداد آخر.

يحتوي التعداد على أنواع الحفظ المحددة مسبقًا التالية:

|**النوع**|**الوصف**|
| :- | :- |
|المرفقات|يُرسل جدول البيانات إلى المستعرض ويُفتح في تطبيق كمرفق مرتبط بامتداد .xls/.xlsx أو امتدادات أخرى|
|مضمن|يُرسل المستند إلى المتصفح ويعرض خيارًا لحفظ جدول البيانات على القرص أو فتحه داخل المتصفح|

### **ملفات XLS**

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

    // Create a new workbook
    Workbook workbook;

    // Save in Excel2003 XLS format
    U16String outputPath = outDir + u"output.xls";
    XlsSaveOptions saveOptions;
    workbook.Save(outputPath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **ملفات XLSX**

```cpp
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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook;

    // Save in Xlsx format
    OoxmlSaveOptions saveOptions;
    workbook.Save(outputFilePath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **ملفات PDF**

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

    // Path of output PDF file
    U16String outputPdf = outDir + u"output.pdf";

    // Creating a Workbook object
    Workbook workbook;

    // Save in Pdf format
    PdfSaveOptions saveOptions;
    workbook.Save(outputPdf, saveOptions);

    Aspose::Cells::Cleanup();
}
```

### **ملاحظة**

نظرًا لكون الكائن "System.Web.HttpResponse" غير مدرج في .NET5 و .Netstandard
وبالتالي، هذه الوظيفة غير موجودة في إصدار Aspose.Cells .NET5 و .Netstandard. يمكنك الرجوع إلى الكود التالي لحفظ الملف في التدفق، ثم القيام بالعمليات على التدفق.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```
