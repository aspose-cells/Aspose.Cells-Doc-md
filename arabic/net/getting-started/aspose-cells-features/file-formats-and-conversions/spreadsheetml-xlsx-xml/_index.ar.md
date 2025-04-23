---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /ar/net/spreadsheetml-xlsx-xml/
---

## **حول ملف تعريف جدول البيانات**
SpreadsheetML هو اسم لعائلة من تنسيقات الوثائق الإلكترونية المعتمدة على XML. هناك عدة إصدارات من SpreadsheetML:

1. تم تقديم نسخة SpreadsheetML 2003 في Microsoft Word 2003. كانت SpreadsheetML خطوة مهمة من قبل Microsoft نحو جعل تنسيق الوثيقة مفتوحًا.
1. [Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML) هو التنسيق الجديد القائم على XML الذي تم تقديمه في تطبيقات Microsoft Office 2007. Office Open XML هو تنسيق حاوية لعدة لغات ترميز قائمة على XML مخصصة. إن تنسيق SpreadsheetML الإصدار 2007 هو لغة العلامات التي تستخدمها Microsoft Office Excel 2007 لتخزين وثائقها.
1. يخزن Microsoft Excel 2010 الوثائق في إصدار SpreadsheetML 2010 كما هو محدد في المعيار المحدث لـ OOXML.
## **SpreadsheetML في Aspose.Cells**
هناك ثلاث "إصدارات" من SpreadsheetML المتاحة:

|**"إصدار" SpreadsheetML**|**المواصفة/المعيار القابلة للتطبيق**|**المدعومة في Aspose.Cells for .NET**|
| :- | :- | :- |
|Microsoft Excel 2003|[XML Microsoft Excel 2003](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|نعم|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|نعم|
|Microsoft Excel 2010|OOXML ISO/IEC DIS 29500|نعم|
|Microsoft Excel 2013|OOXML ISO/IEC DIS 29500|نعم|
تأتي وثائق OOXML SpreadsheetML في معظم الأحيان كملفات XLSX، والتي هي حزم ZIP. بالإضافة إلى XLSX، يوفر Aspose.Cells دعمًا شاملاً لتحميل وحفظ وتحويل وثائق SpreadsheetML. هذا التنفيذ الشامل ممكن لأن Aspose.Cells تم تصميمها مع هيكل وثائق Microsoft Excel في الاعتبار (ويُعرف أن SpreadsheetML يحاكي التمثيل الداخلي لوثائق Microsoft Excel).
### **OOXML مفتوح، لماذا استخدام Aspose.Cells؟**
من الصحيح أن تكنولوجيا Office Open XML تجعل من الممكن بناء تطبيقات معالجة الوثائق وإنشائها باستخدام فئات XML فقط دون الاعتماد على مكتبات الأطراف الثالثة مثل Aspose.Cells. ومع ذلك، نعتقد بشدة أنه من المفيد للغاية استخدام Aspose.Cells عندما يتعين عليك التعامل مع وثائق OOXML، بدلاً من العمل من خلال XML أو مكتبات أخرى.

مواصفة OOXML تحتوي على عدة آلاف من الصفحات. كونها مفتوحة ومعيارية لا يعني أن تكون بسيطة. لكي يتم معالجة أو إنشاء وثائق OOXML بشكل صحيح، يجب على الشخص الاستثمار في تعلم التنسيق جيدًا.

بالإضافة إلى جعلها أسهل في معالجة وإنشاء وثائق صحيحة، يوفر Aspose.Cells الميزات الهامة التالية التي لن تكون متاحة عند العمل مع ملفات OOXML مباشرة عبر XML أو مكتبات الأطراف الثالثة الأخرى:

- تحويلات بجودة عالية بين العديد من تنسيقات Excel الشهيرة، بما في ذلك التحويل إلى PDF، HTML، TIFF والطباعة.
- القدرة على بناء وثائق من شظايا، من وثيقة واحدة أو متعددة، مع دمج البيانات تلقائيًا من خلال التنسيق الأنيق، والرسوم البيانية والرسومات.
- وظائف عالية المستوى، مثل استيراد البيانات من مصادر بيانات مختلفة بما في ذلك مصفوفة، ArrayList، DataTable، DataColumn، DataGrid، DataView و DataReader أو تصدير البيانات لملء DataTable أو مصفوفة بسطر واحد من الكود.
- محرك حساب الصيغ القوي الذي يدعم معظم وظائف Microsoft Excel القياسية والمتقدمة تقريبًا.

اعتبر المثال التالي. بعض الخلايا تحتوي على نص "مرحباً بالعالم" بخط عريض. الآن تخيل أنك بحاجة إلى كتابة برنامج يبحث عن جميع عبارات "مرحباً بالعالم" في ورق العمل ويستبدلها بـ"وداعًا أرضًا".
### **جزء من مستند Office Open XML**
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


تنفيذ عملية البحث والاستبدال حتى في مستند Office Open XML صعب. نصيحتنا: تذكّر أن الانفتاح والتوحيد لا يعنيان البساطة، واستخدام Aspose.Cells.
{{< app/cells/assistant language="csharp" >}}
