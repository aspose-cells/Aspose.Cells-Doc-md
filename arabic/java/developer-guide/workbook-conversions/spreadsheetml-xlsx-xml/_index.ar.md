---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /ar/java/spreadsheetml-xlsx-xml/
---

## **حول ملف تعريف جدول البيانات**
SpreadsheetML هو اسم لعائلة من تنسيقات الوثائق الإلكترونية المعتمدة على XML. هناك عدة إصدارات من SpreadsheetML:

1. تم تقديم نسخة SpreadsheetML 2003 في Microsoft Word 2003. كانت SpreadsheetML خطوة مهمة من قبل Microsoft نحو جعل تنسيق الوثيقة مفتوحًا.
1. [Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML) هو التنسيق الجديد القائم على XML الذي تم تقديمه في تطبيقات Microsoft Office 2007. Office Open XML هو تنسيق حاوية لعدة لغات ترميز قائمة على XML مخصصة. إن تنسيق SpreadsheetML الإصدار 2007 هو لغة العلامات التي تستخدمها Microsoft Office Excel 2007 لتخزين وثائقها.
1. يقوم Microsoft Excel 2010 والإصدارات اللاحقة بتخزين المستندات في إصدار 2010 من جدول بيانات ML كما هو محدد في معيار OOXML المحدث.
## **SpreadsheetML في Aspose.Cells**
هناك ثلاث "إصدارات" من SpreadsheetML المتاحة:

|**جدول بيانات ML 'الإصدار'**|**المواصفة/المواصفة المطبقة**|**مدعوم في Aspose.Cells for Java**|
| :- | :- | :- |
|Microsoft Excel 2003|[XML Microsoft Excel 2003](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|نعم|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|نعم|
|Microsoft Excel 2010 والإصدارات اللاحقة|OOXML ISO/IEC DIS 29500|نعم|
مستندات OOXML لجدول بيانات ML في الغالب تأتي كملفات XLSX، وهي حزم ZIP. بالإضافة إلى XLSX، توفر Aspose.Cells دعمًا واسعًا لتحميل وحفظ وتحويل مستندات جدول البيانات ML. إن تنفيذًا شاملاً كهذا ممكن بسبب تصميم Aspose.Cells بتصوير هيكل مستندات Microsoft Excel (ومعروف أن جدول بيانات ML يحاكي التمثيل الداخلي لمستندات Microsoft Excel).

**يتم إنشاء مستند XLSX بواسطة Aspose.Cells ويتم فتحه في Microsoft Excel** 

![todo:image_alt_text](spreadsheetml-xlsx-xml_1.png)

**المستند XLSX الذي تم إنشاؤه بواسطة Aspose.Cells يتبع اتفاقية التغليف المفتوح ويمكن فتحه في تطبيق قادر على ضغط الملفات** 

![todo:image_alt_text](spreadsheetml-xlsx-xml_2.png)
## **OOXML مفتوح، لماذا استخدام Aspose.Cells؟**
من الصحيح أن تكنولوجيا Office Open XML تجعل من الممكن بناء تطبيقات معالجة الوثائق وإنشائها باستخدام فئات XML فقط دون الاعتماد على مكتبات الأطراف الثالثة مثل Aspose.Cells. ومع ذلك، نعتقد بشدة أنه من المفيد للغاية استخدام Aspose.Cells عندما يتعين عليك التعامل مع وثائق OOXML، بدلاً من العمل من خلال XML أو مكتبات أخرى.

مواصفة OOXML تحتوي على عدة آلاف من الصفحات. كونها مفتوحة ومعيارية لا يعني أن تكون بسيطة. لكي يتم معالجة أو إنشاء وثائق OOXML بشكل صحيح، يجب على الشخص الاستثمار في تعلم التنسيق جيدًا.

بالإضافة إلى جعلها أسهل في معالجة وإنشاء وثائق صحيحة، يوفر Aspose.Cells الميزات الهامة التالية التي لن تكون متاحة عند العمل مع ملفات OOXML مباشرة عبر XML أو مكتبات الأطراف الثالثة الأخرى:

- تحويلات ذات جودة جيدة بين العديد من صيغ Excel الشائعة، بما في ذلك التحويل إلى PDF، HTML، TIFF، والطباعة.
- القدرة على بناء وثائق من أجزاء، من وثيقة واحدة أو متعددة، مع دمج البيانات تلقائيًا بالتنسيق الأسلوبي، والرسوم البيانية، والجرافيك.
- وظائف عالية المستوى، مثل استيراد البيانات من مصادر بيانات مختلفة بما في ذلك النصف، ArrayList، DataTable، DataColumn، DataGrid، DataView، و DataReader أو تصدير البيانات لملء جدول بيانات أو نصف فقط سطر من الكود.
- محرك حساب الصيغ القوي الذي يدعم معظم وظائف Microsoft Excel القياسية والمتقدمة تقريبًا.

اعتبر المثال التالي. بعض الخلايا تحتوي على نص "مرحباً بالعالم" بخط عريض. الآن تخيل أنك بحاجة إلى كتابة برنامج يبحث عن جميع عبارات "مرحباً بالعالم" في ورق العمل ويستبدلها بـ"وداعًا أرضًا".
## **جزء من مستند Office Open XML**
**XML**

{{< highlight csharp >}}

 <?xml version="1.0" encoding="UTF-8" standalone="yes" ?>

\- <worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">

  <dimension ref="A1:M184" />

\- <sheetViews>

\- <sheetView tabSelected="1" workbookViewId="0">

  <selection activeCell="H27" sqref="H27" />

  </sheetView>

  </sheetViews>

  <sheetFormatPr defaultRowHeight="15" />

\- <sheetData>

\- <row r="1" spans="1:7">

\- <c r="A1" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="11" spans="1:7">

\- <c r="D11" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="15" spans="1:7">

\- <c r="G15" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="21" spans="2:7">

\- <c r="G21" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="25" spans="2:7">

\- <c r="F25" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="31" spans="2:7">

\- <c r="B31" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="34" spans="6:13">

\- <c r="M34" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="38" spans="6:13">

\- <c r="F38" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="117" spans="8:8">

\- <c r="H117" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="184" spans="8:8">

\- <c r="H184" s="1" t="s">

  <v>0</v>

  </c>

  </row>

  </sheetData>

  <pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3" />

</worksheet>



{{< /highlight >}}

تنفيذ عملية البحث والاستبدال حتى تكون الأمور بسيطة في مستند Office Open XML صعبة.

**نصيحتنا:** تذكر أن الانفتاح والمعيار لا يعني بالضرورة البساطة، واستخدم Aspose.Cells.
