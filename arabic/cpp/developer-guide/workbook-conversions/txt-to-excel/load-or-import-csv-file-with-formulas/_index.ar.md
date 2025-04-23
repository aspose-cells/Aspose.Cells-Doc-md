---
title: تحميل أو استيراد ملف CSV مع صيغ باستخدام C++
linktitle: تحميل أو استيراد ملف CSV مع الصيغ
type: docs
weight: 350
url: /ar/cpp/load-or-import-csv-file-with-formulas/
description: تحميل أو استيراد ملف CSV يحتوي على صيغ باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}} 

عادةً ما تحتوي ملفات CSV على بيانات نصية ولا تتضمن صيغ. ومع ذلك، قد تحتوي ملفات CSV على صيغ في بعض الحالات. يجب تحميل مثل هذه الملفات بضبط الخاصية [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/gethasformula/) على **true**. بمجرد ضبط هذه الخاصية على **true**، لن تتعامل Aspose.Cells مع الصيغ كنص بسيط. ستتم معاملتها كصيغ، وسيقوم محرك حساب الصيغ في Aspose.Cells بمعالجتها كالمعتاد.

{{% /alert %}} 

يوضح الكود التالي كيف يمكنك تحميل واستيراد ملف CSV بصيغ. يمكنك استخدام أي ملف CSV. للأغراض التوضيحية، نستخدم ملف CSV بسيط يحتوي على هذه البيانات. كما ترى، فإنه يحتوي على صيغة.

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    //For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    //Create TxtLoadOptions with specified settings
    TxtLoadOptions opts;
    opts.SetSeparator(u','); // Set the separator to a comma
    opts.SetHasFormula(true); // Indicate that the CSV may have formulas

    // Load the CSV file into a Workbook object
    Workbook workbook(srcDir + u"sample.csv", opts);

    // You can also import the CSV file starting from cell D4 (indices 3,3)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().ImportCSV(srcDir + u"sample.csv", opts, 3, 3);

    // Save the workbook in Xlsx format
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "CSV file loaded and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

يتم أولاً تحميل ملف CSV، ثم استيراده مرة أخرى في الخلية D4. وأخيراً، يتم حفظ مصنف العمل بصيغة XLSX. يبدو ملف XLSX الناتج هكذا. كما ترى، الخلية C3 و F4 تحتويان على صيغ ونتيجتهما 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
