---
title: العلامات الذكية في الرؤوس والتذييلات | Aspose.Cells for Node.js via Java
linktitle: علامات ذكية في الرأس والتذييل | Aspose.Cells for Node.js via Java
description: ضع نوايا العلامات الذكية في رؤوس وتذييلات الصفحات باستخدام صيغة الأقواس المزدوجة والخاصية WorkbookDesigner.setEnableHeaderFooterMarkers مع مصادر بيانات JSON، واربط الصور عبر URI للبيانات، في Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells for Node.js via Java, العلامات الذكية, رؤوس الصفحات, تذييلات الصفحات, علامات الرأس والتذييل, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, صفوف JSON, ربط البيانات, صورة, URI للبيانات, JavaScript
type: docs
weight: 196
url: /ar/nodejs-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
تحتوي رؤوس وتذييلات الصفحات عادةً على بيانات تعريفية للتقارير مثل عنوان التقرير، فترة التقرير، المؤلف، والقسم. عندما تكون هذه المعلومات موجودة بالفعل في مصدر البيانات المستخدم لملء المصنف، فإن تكرارها يدويًا يخلق تكرارًا غير ضروري.  
الصيغة الكلاسيكية للعلامات الذكية، `&=Source.Field`، تُعالج في خلايا جسم ورقة عمل. إذا وضعت علامة كلاسيكية في رأس أو تذييل عبر `PageSetup.setHeader` أو `PageSetup.setFooter`، فإنها تبقى نصًا حرفيًا لأن سلاسل الرأس والتذييل ليست جزءًا من شبكة خلايا ورقة العمل التي يمسحها `WorkbookDesigner.process()`.  
بدءًا من **Aspose.Cells for Node.js via Java 26.11**، تجعل الخاصية `WorkbookDesigner.setEnableHeaderFooterMarkers`، والتي تكون `false` افتراضيًا، وظيفة `process()` تحل المستبدلات المكتوبة كـ `<<Source.Field>>` في سلاسل أقسام الرأس والتذييل. استدعِ `designer.setEnableHeaderFooterMarkers(true)` قبل استدعاء `process()`. تستخدم مستبدلات الرأس والتذييل نفس مصدر البيانات الذي يُستخدم للعلامات في الجسم.  
كل رأس وتذييل يحتوي على ثلاثة أقسام يمكن عنونتها:
- القسم `0` هو القسم الأيسر.
- القسم `1` هو القسم المتوسط.
- القسم `2` هو القسم الأيمن.  
استخدم `PageSetup.setHeader(int section, String value)` و `PageSetup.setFooter(int section, String value)` لكتابة هذه الأقسام. بعد المعالجة، استخدم `PageSetup.getHeader(int section)` و `PageSetup.getFooter(int section)` لاسترجاع النص المكتمل.

{{% alert color="primary" %}}
مستبدل مثل `<<Source.Field>>` يُدخل قيمة الحقل كنص في سلسلة القسم. تُربط الصور باللاحقة `(picture)` وقيمة URI للبيانات.  
{{% /alert %}}

## **تمكين مستبدلات الرأس/التذييل باستخدام بيانات صفوف JSON**
استخدم التسلسل التالي لحل مستبدلات الرأس والتذييل ببيانات صفوف JSON في **Aspose.Cells for Node.js via Java 26.11**:
1. أنشئ كائن `Workbook` واحصل على أول `Worksheet` له عبر `workbook.getWorksheets().get(0)`.
2. اكتب المستبدلات `<<Source.Field>>` في أقسام الرأس والتذييل المطلوبة باستخدام `PageSetup.setHeader` و `PageSetup.setFooter`.
3. جهّز بيانات الصفوف كمصفوفة JSON من كائنات الصف، واختر اسم مصدر يطابق البادئة المستخدمة في المستبدلات. على سبيل المثال، مصدر باسم `node` يدعم مستبدلات مثل `<<node.Name>>`. الكائنات والمصفوفات العادية في JavaScript لا تُربط على هذه المنصة — JSON هو الشكل الجدولي المدعوم.
4. أنشئ كائن `WorkbookDesigner` للمصنف.
5. استدعِ `designer.setEnableHeaderFooterMarkers(true)` قبل المعالجة.
6. أرفق JSON عبر `designer.setJsonDataSource("node", '[{"Name":"...","Author":"..."}]')`.
7. استدعِ `designer.process()`.
8. بعد المعالجة، لا تُظهر المستبدلات بعد الآن في نص الرأس أو التذييل. استخدم `getHeader` و `getFooter` لاسترجاع سلاسل الأقسام المكتملة.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource(
  "node",
  '[{"Name":"Q4 2026","Author":"Aspose.Cells"}]'
);
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
console.log("Footer: " + worksheet.getPageSetup().getFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx");
```

## **استخدام مصدر بيانات JSON**
عندما تكون بيانات التقرير متاحة بالفعل كـ JSON، يمكن لاستدعاء واحد لـ `setJsonDataSource` تزويد كل أنماط العلامات. استدعِ `WorkbookDesigner.setJsonDataSource(String name, String json)` لإرفاق المصدر.  
المعامل `name` هو اسم المصدر المستخدم في المستبدلات. على سبيل المثال، الاسم `node` يدعم مستبدلات مثل `<<node.Company>>` و `<<node.Title>>`.  
مرّر بيانات الصف مباشرة إلى `setJsonDataSource`:
- مصفوفة صفوف، مثل مصفوفة JSON تحتوي على كائن صف واحد أو أكثر، مدعومة.
- يمكن أيضًا تمرير كائن صف واحد مباشرة.
- لا تقم بلف الصفوف تحت مفتاح علوي مسمى مثل `{"rows":[...]}`. هذا الغلاف ليس الشكل المتوقع للبيانات الموجهة للصفوف لهذا سير العمل.  
يمكن لمصدر JSON واحد تعبئة كلا نمطي العلامات أثناء نفس استدعاء `process()`. يمكنه حل علامة كلاسيكية `&=` في خلية جسم ورقة عمل ومستبدلات مزدوجة الأقواس `<<>>` في أقسام الرأس والتذييل. يجب أن تظل تستدعي `designer.setEnableHeaderFooterMarkers(true)` لحل مستبدلات الرأس والتذييل.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
worksheet.getCells().get("A1").putValue("&=node.Company");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]');
designer.process();
console.log("Left: " + worksheet.getPageSetup().getHeader(0));
console.log("Right: " + worksheet.getPageSetup().getHeader(2));
console.log("Body: " + worksheet.getCells().get("A1").getStringValue());
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx");
```

## **دلالات المفتاح وتعدد صفوف المصدر**
`setEnableHeaderFooterMarkers` تكون `false` افتراضيًا، وتتحكم هذه الخاصية فقط في مستبدلات الرأس والتذييل `<<Source.Field>>`. عندما يكون المفتاح معطلًا، يستمر `process()` في حل علامات الجسم الكلاسيكية `&=`، لكن مستبدل `<<Source.Field>>` في رأس أو تذييل يبقى نصًا حرفيًا.  
القسم في الرأس أو التذييل هو سلسلة واحدة، ليست شريطًا متكررًا. إذا كان مصدر البيانات يحتوي على عدة صفوف، فإن الصف الأول يزود قيم الرأس والتذييل. بعد الحل، تصبح القيم نصًا عاديًا في الرأس أو التذييل. تظل هذه القيم في المصنف بعد استدعاء `save` وتظهر عند تحميل المصنف المحفوظ مرة أخرى.  
المثال التالي ينشئ مصنفين على نفس مصدر JSON متعدد الصفوف لتوضيح السلوك عندما يكون المفتاح معطلًا ومُفعلًا. يترك `plainDesigner` المستبدلات دون تغيير، بينما يحل `enabledDesigner` المستبدلات باستخدام الصف الأول.

```javascript
const AsposeCells = require("aspose.cells");
const table = '[{"Name":"First Row"},{"Name":"Second Row"}]';
// Without the switch the placeholder stays literal text
const plainWorkbook = new AsposeCells.Workbook();
const plainSheet = plainWorkbook.getWorksheets().get(0);
plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const plainDesigner = new AsposeCells.WorkbookDesigner(plainWorkbook);
plainDesigner.setJsonDataSource("node", table);
plainDesigner.process();
// With the switch on, the FIRST row of a multi-row source wins
const enabledWorkbook = new AsposeCells.Workbook();
const enabledSheet = enabledWorkbook.getWorksheets().get(0);
enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const enabledDesigner = new AsposeCells.WorkbookDesigner(enabledWorkbook);
enabledDesigner.setEnableHeaderFooterMarkers(true);
enabledDesigner.setJsonDataSource("node", table);
enabledDesigner.process();
console.log("Without switch: " + plainSheet.getPageSetup().getHeader(1));
console.log("With switch: " + enabledSheet.getPageSetup().getHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
```

## **ربط صورة في رأس أو تذييل**
اللاحقة `(picture)` تربط صورة في قسم رأس أو تذييل. اكتب `<<node.logo(picture)>>` حيث تريد ظهور الصورة، وقدم قيمة الحقل كـ URI للبيانات — البادئة `data:image/png;base64,` تليها النص Base64 لبايتات الصورة. سلسلة Base64 منفردة دون البادئة `data:` لا تُدرج صورة.  
بعد `process()`:
1. تُستبدل المستبدل بـ `&G`، وهو رمز الصورة القياسي للرأس والتذييل. لأن العلامة تصبح شفرة داخل سلسلة القسم، يمكن أن تتواجد داخل نص أطول مثل `Logo: <<node.logo(picture)>>`.
2. تُدمج بايتات الصورة في المصنف كجزء وسائط يُرفق بطبقة رسم الرأس/التذييل لتلك ورقة العمل، لذا تُطبع الصورة مع الرأس أو التذييل.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
const table = [
    {
        logo: "data:image/png;base64," + fs.readFileSync("logo.png").toString("base64")
    }
];
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", JSON.stringify(table));
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
// This prints:
// Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx");
```

يُطبع الرمز `&G` كرمز صورة يفسره Excel عند عرض الرأس — الآن بايتات `logo.png` تعيش داخل `HeaderFooterPicture.xlsx`، وتطبع الصورة مكان الرمز. لاستخدام علامات الرأس والتذييل الذكية، اكتب مستبدلات `<<Source.Field>>` في الأقسام اليسرى، المتوسطة، واليمنى للرأس أو التذييل باستخدام `setHeader` و `setFooter`. استدعِ `designer.setEnableHeaderFooterMarkers(true)` قبل استدعاء `process()`، وزوّد القيم عبر `designer.setJsonDataSource(name, json)`. اقرأ الأقسام المكتملة باستخدام `getHeader` و `getFooter`. يمكن لنفس مصدر البيانات تعبئة علامات الجسم ومستبدلات الرأس أو التذييل في تمريرة معالجة واحدة. أضف اللاحقة `(picture)` مع قيمة URI للبيانات لربط صورة في قسم.

## **مقالات ذات صلة**
- [العرض المتعدد للخلية الواحدة باستخدام SmartMarker](/cells/ar/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="nodejs-java" >}}