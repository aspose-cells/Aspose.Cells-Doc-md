---
title: تحويل إكسل إلى PDF، صورة، وصيغ أخرى باستخدام C++
linktitle: تحويل المصنفات
type: docs
weight: 65
url: /ar/cpp/convert-workbook-to-different-formats/
description: تحويل ملفات إكسل إلى Word، Excel، PowerPoint، PDF، CSV، JPG، HTML، MHT، ODS، BMP، PNG، SVG، TIFF، XPS، JSON، SQL، XML، والمزيد باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يدعم Aspose.Cells التحويل بين العديد من الصيغ. تقنياً، يعني التحويل تحميل ملف معالجة واحد بصيغة معينة وحفظه بصيغة أخرى.

{{% /alert %}}

## **تحويل مصنف Excel إلى PDF**

ملفات PDF مستخدمة على نطاق واسع لتبادل الوثائق بين المؤسسات والقطاعات الحكومية والأفراد. هو صيغة وثيقة قياسية، وغالباً ما يُطلب من مطوري البرامج إيجاد طريقة لتحويل ملفات إكسل إلى وثائق PDF.

تدعم Aspose.Cells تحويل ملفات Excel إلى PDF وتحافظ على دقة الرؤية العالية في التحويل.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Instantiate the Workbook object and open an Excel file
    Workbook workbook(u"Book1.xlsx");

    // Save the document in PDF format
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    std::cout << "Excel file converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحويل مصنف Excel إلى JPG**
Aspose.Cells تدعم تحويل ملفات Excel إلى JPG.
يظهر المثال التالي كيفية حفظ مصنف كصورة.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"Book1.xlsx");
    Workbook book(inputFilePath);

    U16String outputFilePath(u"Image1.jpg");
    book.Save(outputFilePath, SaveFormat::Jpg);

    std::cout << "Workbook converted to JPG image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحويل مصنف Excel إلى صورة**
Aspose.Cells تدعم تحويل ملفات Excel إلى صور.
يظهر المثال التالي كيفية حفظ مصنف كصور.

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook(srcDir + u"Book1.xlsx");

    workbook.Save(outDir + u"Image1.bmp", SaveFormat::Bmp);
    workbook.Save(outDir + u"Image1.jpg", SaveFormat::Jpg);
    workbook.Save(outDir + u"Image1.png", SaveFormat::Png);
    workbook.Save(outDir + u"Image1.emf", SaveFormat::Emf);
    workbook.Save(outDir + u"Image1.gif", SaveFormat::Gif);

    std::cout << "Workbook converted to images successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحويل دفتر العمل في Excel إلى XPS**

تتكون صيغة مستند XPS من ترميز XML منظم يحدد تخطيط المستند والمظهر البصري لكل صفحة، جنبًا إلى جنب مع قواعد العرض لتوزيع المستندات وأرشفتها وعرضها ومعالجتها وطباعتها.

لغة ترميز للمستندات XPS هي مجموعة فرعية من XAML، مما يسمح لها بدمج عناصر الرسومات والمتجهات في المستندات، باستخدام XAML لعلامة عناصر Windows Presentation Foundation (WPF). العناصر المستخدمة موصوفة من حيث المسارات وغيرها من الأشكال الهندسية.

ملف XPS هو في الواقع أرشيف ZIP يونيكودي يستخدم قواعد التعبئة المفتوحة، ويحتوي على الملفات التي تشكل المستند. وتشمل هذه ملف ترميز XML لكل صفحة، نص، خطوط مدمجة، صور نقطية، رسومات متجهة ثنائية الأبعاد، بالإضافة إلى معلومات إدارة الحقوق الرقمية. يمكن فحص محتويات ملف XPS ببساطة عن طريق فتحه في تطبيق يدعم ملفات ZIP.

ابتداءً من Aspose.Cells 6.0.0، يتم دعم تحويل ملفات Microsoft Excel إلى XPS.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xls";
    Workbook workbook(inputFilePath);

    Worksheet sheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    SheetRender sr(sheet, options);
    sr.ToImage(0, outDir + u"out_image.png");

    XpsSaveOptions xpsOptions;
    workbook.Save(outDir + u"out_whole_printingxps.out.xps", xpsOptions);

    std::cout << "Files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحويل إكسل إلى Ods، Sxc، وFods (OpenOffice / LibreOffice Calc)**
يدعم Aspose.Cells تحويل ملفات إكسل إلى ملفات Ods، Sxc، وFods. يوضح مثال الكود أدناه كيفية تحويل [قالب](book1.xlsx) إلى ملفات Ods، Sxc، وفودس.

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

## **تحويل دفتر العمل في إكسل إلى ملفات MHTML**

تجمع MHTML بين HTML العادي مع الموارد الخارجية (أي المحتوى الذي يتم عادةً الربط به، مثل الصور والرسوم المتحركة والصوت وما إلى ذلك) في ملف واحد. يُستخدمون في الرسائل البريدية بامتداد ملف .mht.

Aspose.Cells تدعم قراءة وكتابة ملفات MHTML.

يوضح المثال البرمجي أدناه كيفية حفظ دفتر العمل كملف MHTML.

```cpp
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

    // Specify the HTML Saving Options
    HtmlSaveOptions sv(SaveFormat::MHtml);

    // Instantiate a workbook and open the template XLSX file
    Workbook wb(filePath);

    // Save the MHT file
    wb.Save(filePath + u".out.mht", sv);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحويل دفتر العمل في إكسل إلى HTML**

يوفر API Aspose.Cells دعمًا للتصدير إلى تنسيق HTML. لهذا الغرض، يستخدم Aspose.Cells فئة [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) لتوفير المرونة للتحكم في عدة جوانب من مخرجات HTML.

يوضح المثال البرمجي أدناه كيفية حفظ دفتر العمل كملف HTML.

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

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"ConvertingToHTMLFiles_out.html";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in HTML format
    wb.Save(outputFilePath, SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تعيين تفضيلات الصور لتنسيق HTML**

ابتداءً من الإصدار 8.0.2، كشفت Aspose.Cells عن [**GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) لفئة [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/)، مما يسمح للمطورين بتحديد تفضيلات الصور عند حفظ جداول البيانات بصيغة HTML.

فيما يلي تفاصيل بعض إعدادات الصور التي يمكن تطبيقها:

- [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/): يحدد نوع الصورة. يرجى ملاحظة أن جميع الأشكال ، بما في ذلك الرسوم البيانية ، يتحولون إلى صور في تنسيق HTML الناتج.
- [**GetQuality()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getquality/): يحدد جودة الصورة من 0 إلى 100 عند تحديد [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) كـ Jpeg.
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/): يحصل أو يحدد الدقة الرأسية للصورة بدقة بالنقاط في البوصة.
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/): يحصل أو يحدد الدقة الأفقية للصورة بدقة بالنقاط في البوصة.
- [**TiffCompression**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/): يحصل أو يضبط نوع الضغط للصور عند تحديد [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) كـ Tiff.
- [**GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/): يشير إذا كان خلفية الصورة يجب أن تكون شفافة عندما يتم تحديد ImageFormat على أنها PNG.

الكود أدناه يوضح كيفية استخدام [**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) لتحديد تفضيلات مختلفة.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"Book1.xlsx";

    Workbook book(filePath);
    HtmlSaveOptions saveOptions(SaveFormat::Html);

    saveOptions.GetImageOptions().SetImageType(ImageType::Png);

    book.Save(outDir + u"output.html", saveOptions);

    std::cout << "Spreadsheet converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحويل دفتر العمل إكسل إلى Markdown**

يوفر API Aspose.Cells دعمًا للتصدير إلى تنسيق Markdown. لتصدير ورقة العمل النشطة إلى Markdown، مرر [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) كمعامل ثاني لأسلوب [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). يمكنك أيضًا استخدام فئة [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى Markdown.

يعرض المثال التالي كود تصدير ورقة العمل النشطة إلى Markdown باستخدام عضو تعداد [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). الرجاء مراجعة [ملف Markdown الناتج](md_sample.txt) الذي تم توليده بواسطة الكود للرجوع إليه.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Markdown file
    U16String outputFilePath = outDir + u"Book1.md";

    // Create workbook from the input Excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as Markdown
    workbook.Save(outputFilePath, SaveFormat::Markdown);

    std::cout << "Workbook saved as Markdown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحويل دفتر العمل Excel إلى JSON**

يدعم Aspose.Cells تحويل ملف عمل إلى JSON (ترميز كائن جافا سكريبت).

يوضح المثال التالي كود تصدير ورقة العمل النشطة إلى JSON باستخدام عضو تعداد [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). الرجاء مراجعة الكود لتحويل [ملف المصدر](Book1.xlsx) إلى [ملف JSON الناتج](Book1.Json) للمرجعية.

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

## **تحويل دفتر العمل إكسل إلى XML**
Aspose.Cells تدعم تحويل جدول العمل إلى ملف Excel 2003 Spreadsheet XML وبيانات XML نقية.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save as Excel 2003 Spreadsheet XML
    U16String outputFilePath1 = u"Spreadsheet.xml";
    workbook.Save(outputFilePath1);

    // Save as plain XML data
    U16String outputFilePath2 = u"data.xml";
    XmlSaveOptions xmlSaveOptions;
    workbook.Save(outputFilePath2, xmlSaveOptions);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحويل دفتر العمل إكسل إلى TIFF**
Aspose.Cells تدعم تحويل جدول العمل إلى ملف TIFF.

الكود المصغر أدناه يوضّح كيفية تحويل إكسل إلى TIFF:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open a template excel file
    U16String inputFilePath(u"Book1.xlsx");
    Workbook book(inputFilePath);

    // Save file to TIFF
    U16String outputFilePath(u"out.tiff");
    book.Save(outputFilePath);

    std::cout << "File saved successfully to TIFF format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحويل دفتر العمل إكسل إلى DOCX**

يوفر API Aspose.Cells دعمًا لتحويل أوراق العمل إلى صيغة DOCX. لتصدير ملف العمل إلى DOCX، مرر [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) كمعامل ثاني لأسلوب [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). يمكنك أيضًا استخدام فئة [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى DOCX.

يعرض المثال التالي كود تصدير ورقة العمل النشطة إلى DOCX باستخدام عضو تعداد [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). الرجاء مراجعة [ملف DOCX الناتج](Book1.docx) الذي تم توليده بواسطة الكود للمرجعية.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output docx file
    U16String outputFilePath = outDir + u"Book1.docx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save as DOCX
    workbook.Save(outputFilePath, SaveFormat::Docx);

    std::cout << "File saved successfully as DOCX!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحويل دفتر العمل إكسل إلى PPTX**

يدعم API Aspose.Cells تحويل أوراق العمل إلى تنسيق PPTX. لتصدير ملف العمل إلى PPTX، مرر [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) كمعامل ثاني لأسلوب [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). يمكنك أيضًا استخدام فئة [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى PPTX.

يوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى PPTX باستخدام [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) عضو تعداد. يرجى الاطلاع على [ملف PPTX الناتج](Book1.pptx) الذي تم إنشاؤه بواسطة الكود للمرجعية.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output PowerPoint file
    U16String outputFilePath = outDir + u"Book1.pptx";

    // Create workbook from the input Excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as a PowerPoint file
    workbook.Save(outputFilePath, SaveFormat::Pptx);

    std::cout << "Workbook saved as PowerPoint successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحويل ملف عمل Excel إلى EPUB**

توفر واجهة برمجة التطبيقات Aspose.Cells دعمًا لتحويل الجداول إلى صيغة EPUB. لتصدير ملف العمل إلى EPUB، مرر [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) كالمعلمة الثانية لدالة [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). يمكنك أيضًا استخدام فئة [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى EPUB.

يوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى EPUB باستخدام [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) عضو تعداد.

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

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output EPUB file
    U16String outputFilePath = outDir + u"ConvertingToEPUBFiles_out.epub";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in EPUB format
    wb.Save(outputFilePath, SaveFormat::Epub);

    std::cout << "File converted to EPUB format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحويل ملف عمل Excel إلى AZW3**

توفر واجهة برمجة التطبيقات Aspose.Cells دعمًا لتحويل الجداول إلى صيغة AZW3. لتصدير ملف العمل إلى AZW3، مرر [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) كالمعلمة الثانية لدالة [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). يمكنك أيضًا استخدام فئة [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى AZW3.

يوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى AZW3 باستخدام [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) عضو تعداد.

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
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output AZW3 file
    U16String outputFilePath = outDir + u"ConvertingToEPUBFiles_out.azw3";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in AZW3 format
    wb.Save(outputFilePath, SaveFormat::Azw3);

    std::cout << "File converted to AZW3 format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [تحويل مراجعة XLSB إلى XLSM](/cells/ar/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/ar/cpp/convert-excel-to-html/)
- [صورة](/cells/ar/cpp/convert-excel-to-image/)
- [Json](/cells/ar/cpp/convert-workbook-to-json/)
- [تحويل ملف Excel إلى Ods و Sxc و Fods (OpenOffice / LibreOffice calc).](/cells/ar/cpp/convert-excel-to-ods/)
- [Pdf](/cells/ar/cpp/convert-excel-workbook-to-pdf/)
- [تحويل Excel إلى CSV و TSV و Txt](/cells/ar/cpp/convert-excel-to-csv-tsv-and-txt/)
- [تتبع تقدم تحويل الوثائق](/cells/ar/cpp/track-document-conversion-progress/)
- [تحويل CSV و TSV و TXT إلى Excel](/cells/ar/cpp/convert-csv-tsv-and-txt-to-excel/)
