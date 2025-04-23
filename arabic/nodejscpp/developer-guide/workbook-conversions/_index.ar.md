---  
title: تحويل Excel إلى Pdf، صورة وصيغ أخرى  
linktitle: تحويل المصنفات  
type: docs  
weight: 65  
url: /ar/nodejs-cpp/convert-workbook-to-different-formats/  
description: تحويل ملفات Excel إلى Word، Excel، PowerPoint، PDF، CSV، JPG، HTML، MHT، ODS، BMP، PNG، SVG، TIFF، XPS، JSON، SQL، XML والمزيد باستخدام Node.js عبر C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells تدعم تحويل بين العديد من الصيغ. من الناحية التقنية، التحويل يعني تحميل جدول عمل في تنسيق ملف معين وحفظه في تنسيق آخر.  
{{% /alert %}}  

## **تحويل مصنف Excel إلى PDF**  
تستخدم ملفات PDF على نطاق واسع لتبادل المستندات بين المؤسسات والقطاعات الحكومية والأفراد. إنها صيغة مستند قياسية وغالبًا ما يُطلب من مطوري البرامج أن يجدوا طريقة لتحويل ملفات Microsoft Excel إلى مستندات PDF.  

تدعم Aspose.Cells تحويل ملفات Excel إلى PDF وتحافظ على دقة الرؤية العالية في التحويل.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save("output.pdf");
```  

## **تحويل مصنف Excel إلى JPG**  
يدعم Aspose.Cells تحويل ملفات Excel إلى JPG. يوضح مثال الكود أدناه كيفية حفظ مصنف كصورة JPG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Convert workbook to JPG image.
workbook.save("Image1.jpg");
```  

## **تحويل مصنف Excel إلى صورة**  
يدعم Aspose.Cells تحويل ملفات Excel إلى صور. يوضح مثال الكود أدناه كيفية حفظ مصنف كصور.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const book = new AsposeCells.Workbook(filePath);

// Convert workbook to BMP image.
book.save("Image1.bmp");
// Convert workbook to JPG image.
book.save("Image1.jpg");
// Convert workbook to Png image.
book.save("Image1.png");
// Convert workbook to EMF image.
book.save("Image1.emf");
// Convert workbook to GIF image.
book.save("Image1.gif");
```  

## **تحويل دفتر العمل في Excel إلى XPS**  
تتكون صيغة مستند XPS من ترميز XML منظم يحدد تخطيط المستند والمظهر البصري لكل صفحة، جنبًا إلى جنب مع قواعد العرض لتوزيع المستندات وأرشفتها وعرضها ومعالجتها وطباعتها.  

لغة الوسوم لـ XPS هي جزء من XAML مما يسمح لها بدمج عناصر الرسومات الناقلة في المستندات، باستخدام XAML لتسمية عناصر Windows Presentation Foundation (WPF) البدائية. يتم وصف العناصر المستخدمة من حيث المسارات والبدائيات الهندسية الأخرى.  

ملف XPS هو في الواقع أرشيف ZIP يستخدم ترميز Unicode باستخدام الاتفاقات الخاصة بالتغليف المفتوح، يحتوي على الملفات التي تشكل المستند. تشمل هذه ملف ترميز XML لكل صفحة، ونصوص، وخطوط مضمنة، وصور بترا، ورسومات ناقلة 2D، بالإضافة إلى معلومات إدارة الحقوق الرقمية. يمكن فحص محتويات ملف XPS ببساطة عن طريق فتحه في تطبيق يدعم ملفات ZIP.  

ابتداءً من Aspose.Cells 6.0.0، يتم دعم تحويل ملفات Microsoft Excel إلى XPS.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);


// Render the sheet to xps            
const options = new AsposeCells.XpsSaveOptions();
const sheetSet = new AsposeCells.SheetSet([sheet.getIndex()]);
options.setSheetSet(sheetSet);
workbook.save(path.join(dataDir, "out_printingxps.out.xps"), options);


// Export the whole workbook to XPS
workbook.save(path.join(dataDir, "out_whole_printingxps.out.xps"), new AsposeCells.XpsSaveOptions());
```  

## **تحويل Excel إلى Ods و Sxc و Fods (OpenOffice / LibreOffice Calc)**  
يدعم Aspose.Cells تحويل ملفات Excel إلى ملفات Ods و Sxc و Fods. يوضح مثال الكود أدناه كيفية تحويل [القالب](book1.xlsx) إلى ملفات Ods و Sxc و Fods.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const filePath = path.join(dataDir, "book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Save as ods file 
workbook.save("Out.ods");

// Save as sxc file 
workbook.save("Out.sxc");

// Save as fods file 
workbook.save("Out.fods");
```  

## **تحويل دفتر العمل في إكسل إلى ملفات MHTML**  
تجمع MHTML بين HTML العادي مع الموارد الخارجية (أي المحتوى الذي يتم عادةً الربط به، مثل الصور والرسوم المتحركة والصوت وما إلى ذلك) في ملف واحد. يُستخدمون في الرسائل البريدية بامتداد ملف .mht.  

Aspose.Cells تدعم قراءة وكتابة ملفات MHTML.  

يوضح المثال البرمجي أدناه كيفية حفظ دفتر العمل كملف MHTML.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "Book1.xlsx");

// Specify the HTML Saving Options
const sv = new AsposeCells.HtmlSaveOptions(AsposeCells.SaveFormat.MHtml);

// Instantiate a workbook and open the template XLSX file
const wb = new AsposeCells.Workbook(filePath);

// Save the MHT file
wb.save(`${filePath}.out.mht`, sv);
```  

## **تحويل دفتر العمل في إكسل إلى HTML**  
يوفر API Aspose.Cells دعمًا للتصدير إلى تنسيق HTML. لهذا الغرض، يستخدم Aspose.Cells فئة [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) لتوفير المرونة للتحكم في عدة جوانب من مخرجات HTML.  

يوضح المثال البرمجي أدناه كيفية حفظ دفتر العمل كملف HTML.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  

## **تعيين تفضيلات الصور لتنسيق HTML**  
ابتداءً من الإصدار 8.0.2، كشفت Aspose.Cells عن [**getImageOptions()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getImageOptions--) لفئة [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions)، مما يسمح للمطورين بتحديد تفضيلات الصور عند حفظ جداول البيانات بصيغة HTML.  

أدناه تفاصيل بعض إعدادات الصور التي يمكن تطبيقها،  

- [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/): يحدد نوع الصورة. يرجى ملاحظة أن جميع الأشكال ، بما في ذلك الرسوم البيانية ، يتحولون إلى صور في تنسيق HTML الناتج.   
- [**getQuality()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getQuality--): يحدد جودة الصورة بين 0 و 100، عندما يتم تحديد [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) كـ Jpeg.  
- [**getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--): يحصل أو يحدد الدقة الرأسية للصورة بدقة بالنقاط في البوصة.  
- [**getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--): يحصل أو يحدد الدقة الأفقية للصورة بدقة بالنقاط في البوصة.  
- [**TiffCompression**](https://reference.aspose.com/cells/nodejs-cpp/tiffcompression/): يحصل أو يضبط نوع الضغط للصور عند تحديد [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) كـ Tiff.  
- [**getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--): يشير إذا كان خلفية الصورة يجب أن تكون شفافة عندما يتم تحديد ImageFormat على أنها PNG.  

## **تحويل دفتر العمل إكسل إلى Markdown**  
توفر واجهة برمجة تطبيقات Aspose.Cells دعمًا لتصدير جداول البيانات إلى صيغة Markdown. لتصدير ورقة العمل النشطة إلى Markdown، مرر [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) كوسيط ثاني لطريقة [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). يمكنك أيضًا استخدام فئة [**MarkdownSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/markdownsaveoptions) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى Markdown.  

يُوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى Markdown باستخدام عضو تعداد [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). يرجى مراجعة [ملف Markdown الناتج](md_sample.txt) الذي تم إنشاؤه بواسطة الكود للمرجعية.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir; // Adjust as needed for source directory
const outputDir = dataDir; // Adjust as needed for output directory

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.md"), AsposeCells.SaveFormat.Markdown);
```  

## **تحويل دفتر العمل Excel إلى JSON**  
يدعم Aspose.Cells تحويل مصنف إلى ملف Json (ترميز كائن JavaScript).  

يُوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى Json باستخدام عضو تعداد [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). يرجى مراجعة الكود لتحويل [ملف المصدر](Book1.xlsx) إلى [ملف Json الناتج](Book1.Json) الذي تم إنشاؤه بواسطة الكود للمرجعية.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```  

## **تحويل دفتر العمل إكسل إلى XML**  
Aspose.Cells تدعم تحويل جدول العمل إلى ملف Excel 2003 Spreadsheet XML وبيانات XML نقية.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save as Excel 2003 Spreadsheet XML
workbook.save("Spreadsheet.xml");

// Save as plain XML data
const xmlSaveOptions = new AsposeCells.XmlSaveOptions();
workbook.save("data.xml", xmlSaveOptions);
```  

## **تحويل دفتر العمل إكسل إلى TIFF**  
Aspose.Cells تدعم تحويل جدول العمل إلى ملف TIFF.  

الكود المصغر أدناه يوضّح كيفية تحويل إكسل إلى TIFF:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save file to tiff
workbook.save("out.tiff");
```  

## **تحويل دفتر العمل إكسل إلى DOCX**  
توفر واجهة برمجة تطبيقات Aspose.Cells دعمًا لتحويل جداول البيانات إلى صيغة DOCX. لتصدير المصنف إلى DOCX، مرر [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) كوسيط ثاني لطريقة [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). يمكنك أيضًا استخدام فئة [**DocxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/docxsaveoptions) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى DOCX.  

يُوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى DOCX باستخدام عضو تعداد [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). يرجى مراجعة [ملف DOCX الناتج](Book1.docx) الذي تم إنشاؤه بواسطة الكود للمرجعية.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = dataDir;

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.docx"), AsposeCells.SaveFormat.Docx);
```  

## **تحويل دفتر العمل إكسل إلى PPTX**  
توفر واجهة برمجة تطبيقات Aspose.Cells دعمًا لتحويل جداول البيانات إلى صيغة PPTX. لتصدير المصنف إلى PPTX، مرر [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) كوسيط ثاني لطريقة [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). يمكنك أيضًا استخدام فئة [**PptxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pptxsaveoptions) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى PPTX.  

يُوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى PPTX باستخدام عضو تعداد [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). يرجى مراجعة [ملف PPTX الناتج](Book1.pptx) الذي تم إنشاؤه بواسطة الكود للمرجعية.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = path.join(dataDir, "output/");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.pptx"), AsposeCells.SaveFormat.Pptx);
```  

## **تحويل ملف عمل Excel إلى EPUB**  
توفر واجهة برمجة تطبيقات Aspose.Cells دعمًا لتحويل جداول البيانات إلى صيغة EPUB. لتصدير المصنف إلى EPUB، مرر [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) كوسيط ثاني لطريقة [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). يمكنك أيضًا استخدام فئة [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى Epub.  

يُوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى EPUB باستخدام عضو تعداد [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Save it in EPUB format
workbook.save(path.join(dataDir, "ConvertingToEPUBFiles_out.epub"), AsposeCells.SaveFormat.Epub);
```  

## **تحويل ملف عمل Excel إلى AZW3**  
توفر واجهة برمجة تطبيقات Aspose.Cells دعمًا لتحويل جداول البيانات إلى صيغة AZW3. لتصدير المصنف إلى AZW3، مرر [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) كوسيط ثاني لطريقة [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). يمكنك أيضًا استخدام فئة [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى AZW3.  

يُوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى AZW3 باستخدام عضو تعداد [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in AZW3 format
wb.save(path.join(dataDir, "ConvertingToEPUBFiles_out.azw3"), AsposeCells.SaveFormat.Azw3);
```  

## **مواضيع متقدمة**  
- [تحويل مراجعة XLSB إلى XLSM](/cells/ar/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/)  
- [HTML](/cells/ar/nodejs-cpp/convert-excel-to-html/)  
- [صورة](/cells/ar/nodejs-cpp/convert-excel-to-image/)  
- [Json](/cells/ar/nodejs-cpp/convert-workbook-to-json/)  
- [تحويل مصنف Excel إلى Ods و Sxc و Fods (OpenOffice / LibreOffice calc).](/cells/ar/nodejs-cpp/convert-excel-to-ods/)  
- [Pdf](/cells/ar/nodejs-cpp/convert-excel-workbook-to-pdf/)  
- [تحويل Excel إلى CSV و TSV و Txt](/cells/ar/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/)  
- [تتبع تقدم تحويل الوثائق](/cells/ar/nodejs-cpp/track-document-conversion-progress/)  
- [تحويل CSV، TSV و TXT إلى Excel](/cells/ar/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/)  

