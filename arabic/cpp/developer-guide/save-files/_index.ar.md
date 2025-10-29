---
title: طرق مختلفة لحفظ الملفات باستخدام C++
linktitle: حفظ الملفات
type: docs
weight: 40
url: /ar/cpp/different-ways-to-save-files/
description: يستطيع Aspose.Cells for C++ حفظ الملفات إلى تنسيقات مختلفة. حفظ الملفات كملف PDF. حفظ الملفات كملف HTML. حفظ الملفات كملف DOCX. حفظ الملفات كملف PPTX. حفظ الملفات كملف JSON. حفظ الملفات كملف MHTML.
keywords: Aspose.Cells حفظ إكسل إلى PDF، HTML، JSON، CSV، TXT، XML، DOCX، PPTX، MHT، MHTML وغيرها باستخدام C++، حفظ أو تحويل دفتر العمل إلى PDF HTML JSON TXT SQL في C++.
---

{{% alert color="primary" %}}

‏تجعل Aspose.Cells من الممكن إنشاء الملفات وحفظها. يشرح هذا المقال الطرق المختلفة التي يمكن بها حفظ الملفات.

{{% /alert %}}

## **طرق مختلفة لحفظ الملفات**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، التي تمثل ملف Microsoft Excel وتوفر الخصائص والطرق الضرورية للعمل مع ملفات Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) طريقة [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) المستخدمة لحفظ ملفات Excel. تحتوي الطريقة [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) على العديد من الأوزان المستخدمة لحفظ الملفات بطرق مختلفة.

يتم تقرير تنسيق الملف الذي يتم حفظ الملف إليه بواسطة تعداد [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/).

|**أنواع تنسيق الملفات**|**الوصف**|
| :- | :- |
|CSV|يمثل ملف CSV|
|Excel97To2003| يمثل ملف Excel 97-2003|
||Xlsx| يمثل ملف Excel 2007 XLSX|
||Xlsm| يمثل ملف Excel 2007 XLSM|
||Xltx| يمثل قالب Excel 2007 XLTX|
||Xltm| يمثل ملف Excel 2007 الممكن للتشغيل الآلي XLTM|
|Xlsb| يمثل ملف XLSB بتنسيق Excel 2007 الثنائي
|SpreadsheetML| يمثل ملف XML لجدول بيانات
|TSV|يمثل ملف قيم مفصولة بعلامة التبويب|
|TabDelimited|يمثل ملف نصي بقيم مفصولة بواسطة علامة التبويب|
|ODS|يمثل ملف ODS|
|Html| يمثل ملف HTML
|MHtml| يمثل ملف MHTML
|Pdf| يمثل ملف PDF
|XPS| يمثل مستند XPS
|TIFF| يمثل ملف TIFF

## **كيفية حفظ الملف بتنسيقات مختلفة**

لحفظ الملفات في موقع تخزين، حدد اسم الملف (مع المسار التخزيني الكامل) وتنسيق الملف المطلوب (من تعداد [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)) عند استدعاء طريقة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) للكائن [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

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
    U16String filePath = srcDir + u"Book1.xls";

    // Load your source workbook
    Workbook workbook(filePath);

    // Save in Excel 97 to 2003 format
    workbook.Save(outDir + u".output.xls");
    // OR
    XlsSaveOptions xlsSaveOptions;
    workbook.Save(outDir + u".output.xls", xlsSaveOptions);

    // Save in Excel2007 xlsx format
    workbook.Save(outDir + u".output.xlsx", SaveFormat::Xlsx);

    // Save in Excel2007 xlsb format
    workbook.Save(outDir + u".output.xlsb", SaveFormat::Xlsb);

    // Save in ODS format
    workbook.Save(outDir + u".output.ods", SaveFormat::Ods);

    // Save in Pdf format
    workbook.Save(outDir + u".output.pdf", SaveFormat::Pdf);

    // Save in Html format
    workbook.Save(outDir + u".output.html", SaveFormat::Html);

    // Save in SpreadsheetML format
    workbook.Save(outDir + u".output.xml", SaveFormat::SpreadsheetML);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **كيفية حفظ الكتاب الدراسي إلى صيغة PDF**
صيغة ملف الـ PDF هي نوع من المستندات التي تم إنشاؤها من قبل Adobe في تسعينيات القرن الماضي. الغرض من هذه الصيغة كان تقديم معيار لتمثيل المستندات والمواد المرجعية الأخرى في صيغة مستقلة من البرامج التطبيقية والأجهزة وكذلك نظام التشغيل. تحتوي صيغة ملف الـ PDF بالكامل على القدرة على استيعاب معلومات مثل النصوص والصور والروابط الفائقة وحقول النماذج ووسائط غنية والتواقيع الرقمية والمرفقات والبيانات الوصفية والميزات الجغرافية والأجسام ثلاثية الأبعاد التي يمكن أن تصبح جزءًا من المستند المصدر

تظهر الأكواد التالية كيفية حفظ الكتاب الدراسي كملف PDF باستخدام Aspose.Cells
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the Workbook object
    Workbook workbook;

    // Set value to Cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"Hello World!");

    // Save the workbook to PDF
    workbook.Save(u"pdf1.pdf");

    // Save as Pdf format compatible with PDFA-1a
    PdfSaveOptions saveOptions;
    saveOptions.SetCompliance(PdfCompliance::PdfA1a);

    workbook.Save(u"pdfa1a.pdf", saveOptions);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **كيفية حفظ الكتاب الدراسي إلى تنسيق نصي أو CSV**

في بعض الأحيان ، تريد تحويل أو حفظ دفتر عمل بعدة ورقات عمل إلى تنسيق نصي. بالنسبة لتنسيقات النص (مثل TXT، TabDelim، CSV، إلخ) ، يحفظ كل من Microsoft Excel وAspose.Cells افتراضيًا محتويات الورقة العمل النشطة فقط.

يوضح مثال الكود التالي كيفية حفظ دفتر عمل بأكمله في تنسيق نصي. يُحمّل دفتر العمل المصدري الذي يمكن أن يكون أي ملف جداول بيانات Microsoft Excel أو OpenOffice (مثل XLS وXLSX وXLSM وXLSB وODS وما إلى ذلك) مع أي عدد من ورقات العمل.

عند تنفيذ الكود ، يتم تحويل بيانات كافة الأوراق في دفتر العمل إلى تنسيق TXT.

يمكنك تعديل المثال نفسه لحفظ الملف بصيغة CSV. بشكل افتراضي، [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) هو فاصلة، لذا لا تحدد فاصل إذا كنت تحفظ بصيغة CSV. يرجى ملاحظة: إذا كنت تستخدم النسخة التقييمية وحتى تم تعيين خاصية [**TxtSaveOptions.GetExportAllSheets()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getexportallsheets/) إلى true، فإن البرنامج سيصدر ورقة عمل واحدة فقط.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output text file
    U16String outputFilePath = outDir + u"out.txt";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook data saved to text file successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **كيفية حفظ ملف إلى ملفات نصية مع فاصل مخصص**

تحتوي ملفات النص على بيانات جداول بيانات دون تنسيق. الملف هو نوع ملف نصي عادي يمكن أن يحتوي على بعض الفواصل المخصصة بين بياناته.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';');

    // Save the file with the options
    wb.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **كيفية حفظ ملف إلى تيار**

لحفظ الملفات في تيار، أنشئ كائن *MemoryStream* أو *FileStream* واحفظ الملف في ذلك الكائن تيار عن طريق استدعاء طريقة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) للكائن [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). حدد تنسيق الملف المطلوب باستخدام تعداد [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) عند استدعاء الطريقة [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

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

## **كيفية حفظ ملف إكسل إلى ملفات Html و Mht**
يمكن لـ Aspose.Cells ببساطة حفظ ملف إكسل، JSON، CSV أو ملفات أخرى التي يمكن تحميلها بواسطة Aspose.Cells كملفات .html و .mht.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    Workbook workbook(inputFilePath);

    // Save file to MHTML format
    U16String outputFilePath(u"out.mht");
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully to MHTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **كيفية حفظ ملف إكسل إلى OpenOffice (ODS, SXC, FODS, OTS)**
يمكننا حفظ الملفات في تنسيق مفتوح المكتب: ODS, SXC, FODS, OTS وغيرها.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file
    workbook.Save(u"Out.ods");

    // Save as sxc file
    workbook.Save(u"Out.sxc");

    // Save as fods file
    workbook.Save(u"Out.fods");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **كيفية حفظ ملف إكسل إلى JSON أو XML**

JSON (JavaScript Object Notation) هو تنسيق ملف مفتوح المعايير لمشاركة البيانات التي تستخدم النص القابل للقراءة من قبل الإنسان لتخزين ونقل البيانات. يتم تخزين ملفات JSON باستخدام الامتداد .json. يتطلب JSON تنسيقًا أقل وهو بديل جيد لـ XML. يتم استخلاص JSON من JavaScript ولكنه تنسيق بيانات مستقل عن اللغة. تدعم العديد من لغات البرمجة الحديثة مولد وتجزئة JSON. application/json هو نوع الوسائط المستخدم لـ JSON.

تدعم Aspose.Cells حفظ الملفات في JSON أو XML.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output json file
    U16String outputFilePath = outDir + u"book1.json";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **مواضيع متقدمة**
- [ضبط مستوى ضغط الورقة العمل](/cells/ar/cpp/adjust-workbook-compression-level/)
- [حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم](/cells/ar/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [حفظ الملف في كائن الاستجابة](/cells/ar/cpp/saving-file-to-response-object/)
{{< app/cells/assistant language="cpp" >}}
