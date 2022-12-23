---
title: SpreadsheetML-XLSX ، XML
type: docs
weight: 10
url: /ar/java/spreadsheetml-xlsx-xml/
---
## **حول SpreadsheetML**
SpreadsheetML هو اسم لمجموعة من التنسيقات المبنية على XML لوثائق جداول البيانات. هناك عدة إصدارات من SpreadsheetML:

1. تم تقديم إصدار SpreadsheetML 2003 في Microsoft Word 2003. كان SpreadsheetML خطوة مهمة بحلول Microsoft نحو فتح تنسيق المستند.
1. [Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML) هو التنسيق الجديد المستند إلى XML والذي تم تقديمه في تطبيقات Office 2007 Microsoft. Office Open XML هو تنسيق حاوية للعديد من لغات الترميز القائمة على XML. SpreadsheetML version 2007 هي لغة الترميز المستخدمة بواسطة Microsoft Office Excel 2007 لتخزين مستنداته.
1. Microsoft يقوم Excel 2010 والإصدارات الأحدث بتخزين المستندات في SpreadsheetML الإصدار 2010 كما هو محدد في معيار OOXML المحدث.
## **SpreadsheetML في Aspose.Cells**
تتوفر ثلاث "إصدارات" من SpreadsheetML:

|**SpreadsheetML “نسخة”**|**المعيار / المواصفات المعمول بها**|**معتمد في Aspose.Cells for Java**|
|:- |:- |:- |
|Microsoft Excel 2003|[Microsoft Excel 2003 XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|نعم|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|نعم|
|Microsoft Excel 2010 والإصدارات الأحدث|OOXML ISO / IEC DIS 29500|نعم|
غالبًا ما تأتي مستندات OOXML SpreadsheetML كملفات XLSX ، وهي عبارة عن حزم ZIP. بالإضافة إلى XLSX. يوفر Aspose.Cells دعمًا شاملاً لتحميل وحفظ وتحويل مستندات SpreadsheetML. مثل هذا التنفيذ الشامل ممكن لأن Aspose.Cells تم تصميمه مع وضع بنية Microsoft في الاعتبار لمستندات Excel (ومن المعروف أن SpreadsheetML يحاكي التمثيل الداخلي لوثائق Excel Microsoft).

**مستند XLSX تم إنشاؤه بواسطة Aspose.Cells وفتح في Microsoft Excel** 

![ما يجب القيام به: image_بديل_نص](spreadsheetml-xlsx-xml_1.png)

**المستند XLSX الذي تم إنشاؤه بواسطة Aspose.Cells يتبع اتفاقية Open Packaging Convention ويمكن فتحه في تطبيق يدعم ZIP** 

![ما يجب القيام به: image_بديل_نص](spreadsheetml-xlsx-xml_2.png)
## **OOXML مفتوح ، لماذا استخدم Aspose.Cells؟**
صحيح أن تقنية Office Open XML تجعل من الممكن إنشاء معالجة المستندات وإنشاء التطبيقات باستخدام فئات XML فقط دون الاعتماد على مكتبات الطرف الثالث مثل Aspose.Cells. ومع ذلك ، فإننا نعتقد بشدة أنه لا يزال من المفيد جدًا استخدام Aspose.Cells عندما يكون لديك للتعامل مع مستندات OOXML ، بدلاً من العمل من خلال XML أو المكتبات الأخرى.

يبلغ طول مواصفات OOXML عدة آلاف من الصفحات. أن تكون منفتحًا ومعيارًا لا يعني أن تكون بسيطًا. لمعالجة أو إنشاء مستندات OOXML بشكل صحيح ، يجب على المرء الاستثمار في تعلم التنسيق جيدًا.

بالإضافة إلى تسهيل معالجة المستندات الصالحة وإنشاءها بشكل صحيح ، يوفر Aspose.Cells الميزات المهمة التالية التي لن تكون لديك عند العمل مع ملفات OOXML مباشرةً عبر XML أو مكتبات أخرى تابعة لجهات خارجية:

- تحويلات الجودة بين العديد من تنسيقات Excel الشائعة ، بما في ذلك التحويل إلى PDF و HTML و TIFF والطباعة.
- القدرة على إنشاء مستندات من أجزاء ، من مستند واحد أو عدة مستندات ، مع دمج البيانات تلقائيًا عن طريق التنسيق الأسلوبي والمخططات والرسومات.
- وظائف عالية المستوى ، مثل استيراد البيانات من مصادر بيانات مختلفة بما في ذلك Array و ArrayList و DataTable و DataColumn و DataGrid و DataView و DataReader أو تصدير البيانات لملء DataTable أو صفيف بسطر واحد فقط من التعليمات البرمجية.
- محرك حساب الصيغة القوي الذي يدعم تقريبًا جميع وظائف Excel القياسية والمتقدمة Microsoft.

تأمل المثال التالي. تحتوي بعض الخلايا على النص "Hello World" بخط غامق. تخيل الآن أنك بحاجة إلى كتابة برنامج يبحث عن جميع العبارات "Hello World" في ورقة العمل ويستبدلها بـ "Goodbye Earth".
## **جزء من مستند Office Open XML**
**XML**

{{< highlight "csharp" >}}

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

يعد تنفيذ عملية بحث واستبدال بسيطة في مستند Office Open XML أمرًا صعبًا.

**نصيحتنا:** تذكر أن الفتح والمعيار لا يعني البساطة والاستخدام Aspose.Cells.
