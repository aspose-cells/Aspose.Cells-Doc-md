---
title: إلغاء حماية ورقة العمل باستخدام C++
linktitle: إلغاء حماية ورقة العمل
type: docs
weight: 20
url: /ar/cpp/unprotect-a-worksheet/
description: تعلم كيفية إلغاء حماية ورقة العمل باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

إذا كان المطور بحاجة إلى إزالة الحماية من ورقة محمية أثناء التشغيل بحيث يمكن إجراء بعض التغييرات على الملف، يمكن فعل ذلك بسهولة باستخدام Aspose.Cells.

{{% /alert %}}

## **إلغاء حماية ورقة العمل**

### **استخدام Microsoft Excel**

لإزالة الحماية من ورقة العمل:

من قائمة **الأدوات**، اختر **الحماية** ثم **إلغاء حماية الورقة**. سيتم إزالة الحماية ما لم تكن ورقة العمل محمية بكلمة مرور. في هذه الحالة، يظهر مربع حوار يطلب كلمة المرور. أدخل كلمة المرور وسيتم إلغاء حماية الورقة.

### **إزالة الحماية من ورقة العمل المحمية بشكل بسيط باستخدام Aspose.Cells**

يمكن إلغاء حماية ورقة العمل عن طريق استدعاء طريقة [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) من فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). ورقة العمل المحمية ببساطة هي تلك التي لا تُحمي بكلمة مرور. يمكن إلغاء حماية مثل هذه الأوراق عن طريق استدعاء الطريقة [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) بدون تمرير معلمة.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create a Workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet without a password
    worksheet.Unprotect();

    // Save the Workbook in Excel97-2003 format
    workbook.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet unprotected and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **إلغاء حماية ورقة العمل المحمية بكلمة المرور باستخدام Aspose.Cells**

ورقة عمل محمية بكلمة مرور هي تلك التي تمت حمايتها بكلمة مرور. يمكن إلغاء حماية مثل هذه الأوراق عن طريق استدعاء نسخة محملة زائدة من طريقة [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) التي تأخذ كلمة المرور كمعامل.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unprotecting the worksheet with a password
    worksheet.Unprotect(u"");

    // Save Workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
