---  
title: تحقق مما إذا كان رمز VBA موقعًا باستخدام C++  
linktitle: التحقق مما إذا كان كود VBA موقع بالتوقيع  
type: docs  
weight: 100  
url: /ar/cpp/check-if-vba-code-is-signed/  
description: تعلم كيفية التحقق مما إذا كان رمز VBA في ملفات Excel موقعًا باستخدام Aspose.Cells و C++.  
---  

{{% alert color="primary" %}}  

يسمح Aspose.Cells للمستخدم بالتحقق مما إذا كان مشروع رمز VBA موقعًا أم لا. يرجى استخدام الخاصية [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/) للتحقق مما إذا كان مشروع رمز VBA موقعًا أم لا.  

{{% /alert %}}  

يوضح الكود التالي كيفية التحقق مما إذا كان رمز VBA موقعًا أم لا باستخدام الخاصية [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/). يمكنك استخدام أي من ملفات إكسل الخاصة بك لاختبار هذا الرمز. للاختبار، يمكنك استخدام [هذا الملف المستخدم في الكود](5115032.xlsm).  

## **تحقق مما إذا كان رمز VBA موقعًا في C++**  

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleVBAProjectSigned.xlsm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Check if the VBA code project is signed
    std::wcout << U"Is VBA Code Project Signed: " << workbook.GetVbaProject().IsSigned() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  

## مخرج الكونسول  

أدناه مخرج الكونسول للكود أعلاه باستخدام [ملف Excel عينة](5115032.xlsm) المقدم من خلال الرابط.  

{{< highlight java >}}  

Is VBA Code Project Signed: True  

{{< /highlight >}}  
{{< app/cells/assistant language="cpp" >}}
