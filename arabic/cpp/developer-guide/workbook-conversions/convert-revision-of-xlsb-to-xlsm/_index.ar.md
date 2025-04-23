---
title: تحويل مراجعة XLSB إلى XLSM باستخدام C++
linktitle: تحويل مراجعة ملف XLSB إلى ملف XLSM
type: docs
weight: 290
url: /ar/cpp/convert-revision-of-xlsb-to-xlsm/
description: تعلم كيفية تحويل مراجعات ملفات XLSB إلى تنسيق XLSM باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}} 

يدعم Aspose.Cells الآن التحويل الكامل لمراجعات ملفات XLSB إلى ملفات XLSM. توجد المراجعات داخل مسار \xl\revisions. يمكنك عرضها بتغيير امتداد ملف XLSB الخاص بك إلى ZIP. يحتوي مسار \xl\revisions على ملفات تنتهي بامتدادات .bin.

عند تحويل ملف XLSB الخاص بك إلى ملف XLSM باستخدام Aspose.Cells، يتم تحويل ملفات .bin بنجاح إلى ملفات .xml كما هو موضح في هذين اللقطتين.

{{% /alert %}} 

يعرض الكود التالي كيفية تحويل ملف XLSB إلى تنسيق XLSM باستخدام Aspose.Cells.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsb";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Save Workbook to XLSM format
    workbook.Save(outDir + u"output_out.xlsm", SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully in XLSM format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
