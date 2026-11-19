---
title: العلامات الذكية في رؤوس وتذييلات الصفحات | Aspose.Cells .NET
linktitle: علامات ذكية في الرأس والتذييل | Aspose.Cells
description: ضع عناصر نائبة للعلامات الذكية في رؤوس وتذييلات الصفحات باستخدام صيغة الأقواس المزدوجة ومفتاح WorkbookDesigner.EnableHeaderFooterMarkers مع مصادر بيانات DataTable أو JSON، وربط الصور عبر عناوين URI للبيانات، في Aspose.Cells for .NET.
keywords: Aspose.Cells, العلامات الذكية, رؤوس, تذييلات, علامات الرؤوس والتذييلات, EnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, SetHeader, SetFooter, SetJsonDataSource, DataTable, ربط البيانات, صورة, URI للبيانات, C#
type: docs
weight: 196
url: /ar/net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **السيناريوهات المحتملة للاستخدام**
عادةً ما تحتوي رؤوس وتذييلات الصفحات على بيانات تعريفية للتقرير مثل عنوان التقرير، فترة التقرير، المؤلف، والقسم. عندما تكون هذه المعلومات موجودة بالفعل في مصدر البيانات المستخدم لتعبئة المصنف، فإن تكرارها يدويًا يخلق تكرارًا غير ضروري.  
يتم معالجة صيغة العلامة الذكية الكلاسيكية، `&=Source.Field`، في خلايا جسم ورقة العمل. إذا وضعت علامة كلاسيكية في رأس أو تذييل عبر `PageSetup.SetHeader` أو `PageSetup.SetFooter`، فإنها تظل نصًا حرفيًا لأن سلاسل الرؤوس والتذييلات ليست جزءًا من شبكة خلايا ورقة العمل التي يمررها `WorkbookDesigner.Process()`.  
بدءًا من **Aspose.Cells for .NET 26.11**، يتحكم مفتاح `WorkbookDesigner.EnableHeaderFooterMarkers`، الذي يكون `false` بشكل افتراضي، في جعل `Process()` يحل العناصر النائبة المكتوبة كـ `<<Source.Field>>` في سلاسل أقسام الرؤوس والتذييلات — قم بتعيينه إلى `true` قبل استدعاء `Process()`. تستخدم عناصر النائب في الرؤوس والتذييلات نفس مصدر البيانات مثل علامات الجسم.  

كل رأس وتذييل يحتوي على ثلاثة أقسام يمكن الإشارة إليها:  
- القسم `0` هو القسم الأيسر.  
- القسم `1` هو القسم الأوسط.  
- القسم `2` هو القسم الأيمن.  

استخدم `PageSetup.SetHeader(int section, string value)` و `PageSetup.SetFooter(int section, string value)` لكتابة هذه الأقسام. بعد المعالجة، استخدم `PageSetup.GetHeader(int section)` و `PageSetup.GetFooter(int section)` لاسترجاع النص المكتمل.

{{% alert color="primary" %}}
العنصر النائب مثل `<<Source.Field>>` يدرج قيمة الحقل كنص داخل سلسلة القسم. يتم ربط الصور باللاحقة `(picture)` وقيمة URI للبيانات.
{{% /alert %}}

## **تمكين علامات الرؤوس/التذييلات باستخدام DataTable**
استخدام التسلسل التالي لحل العناصر النائبة في الرؤوس والتذييلات باستخدام `DataTable` في **Aspose.Cells for .NET 26.11**:
1. إنشاء كائن `Workbook` والحصول على أول `Worksheet` له عند الفهرس `0`.  
2. اكتب العناصر النائبة `<<Source.Field>>` في أقسام الرؤوس والتذييلات المطلوبة باستخدام `PageSetup.SetHeader` و `PageSetup.SetFooter`.  
3. إنشاء `DataTable` يكون اسم جدولها مطابقًا للبادئة المصدر المستخدمة في العناصر النائبة. على سبيل المثال، جدول باسم `node` يدعم العناصر النائبة مثل `<<node.Name>>`.  
4. إنشاء كائن `WorkbookDesigner` للمصنف.  
5. تعيين `designer.EnableHeaderFooterMarkers` إلى `true` قبل المعالجة.  
6. إرفاق الجدول باستخدام `designer.SetDataSource(table)`.  
7. استدعاء `designer.Process()`.  
8. بعد المعالجة، لا تكون العناصر النائبة موجودة بعد الآن في نص الرأس أو التذييل. استخدم `GetHeader` و `GetFooter` لاسترجاع سلاسل الأقسام المكتملة.

```csharp
using System;
using System.Data;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.PageSetup.SetHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.PageSetup.SetFooter(1, "Prepared by <<node.Author>>");
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Columns.Add("Author");
table.Rows.Add("Q4 2026", "Aspose.Cells");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
Console.WriteLine("Footer: " + worksheet.PageSetup.GetFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.Save("HeaderFooterSmartMarkers.xlsx");
```

## **استخدام مصدر بيانات JSON**
يمكنك استخدام JSON بدلاً من `DataTable` عندما تكون بيانات التقرير متاحة بالفعل بصيغة JSON. استدعِ `WorkbookDesigner.SetJsonDataSource(string name, string json)` لإرفاق المصدر.  
المعامل `name` له نفس دور اسم `DataTable`. على سبيل المثال، الاسم `node` يدعم العناصر النائبة مثل `<<node.Company>>` و `<<node.Title>>`.  
مرّر بيانات الصف مباشرة إلى `SetJsonDataSource`:
- مصفوفة صفوف، مثل مصفوفة JSON تحتوي على كائن صف واحد أو أكثر، مدعومة.  
- يمكن أيضًا تمرير كائن صف واحد مباشرة.  
- لا تُغلف الصفوف تحت مفتاح علوي مسمى مثل `{"rows":[...]}`. هذه الغلاف ليست الشكل المتوقع لمدخلات الصفوف لهذا سير العمل.  

يمكن لمصدر JSON واحد تعبئة كلا نمطي العلامات أثناء استدعاء `Process()` نفسه. يمكنه حل علامة كلاسيكية `&=` في خلية جسم ورقة عمل وعناصر نائبة بصيغة الأقواس المزدوجة `<<>>` في أقسام الرؤوس والتذييلات. لا يزال عليك تمكين `EnableHeaderFooterMarkers` لكي يتم حل العناصر النائبة في الرؤوس والتذييلات.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.PageSetup.SetHeader(0, "<<node.Company>>");
worksheet.PageSetup.SetHeader(2, "Page <<node.Title>>");
worksheet.Cells["A1"].PutValue("&=node.Company");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
designer.Process();
Console.WriteLine("Left: " + worksheet.PageSetup.GetHeader(0));
Console.WriteLine("Right: " + worksheet.PageSetup.GetHeader(2));
Console.WriteLine("Body: " + worksheet.Cells["A1"].StringValue);
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.Save("HeaderFooterJsonMarkers.xlsx");
```

## **دلالات المفتاح ومصدر الصفوف المتعددة**
`EnableHeaderFooterMarkers` يكون `false` بشكل افتراضي، يتحكم هذا المفتاح فقط في عناصر النائب `<<Source.Field>>` في الرؤوس والتذييلات. عندما يكون المفتاح مُعطَّلًا، يظل `Process()` يحل علامات الجسم الكلاسيكية `&=`، لكن العنصر النائب `<<Source.Field>>` في رأس أو تذييل يظل نصًا حرفيًا.  
قسم الرأس أو التذييل هو سلسلة واحدة، وليس شريطًا متكررًا. إذا كان مصدر البيانات يحتوي على عدة صفوف، فإن الصف الأول يزود قيم الرؤوس والتذييلات. بمجرد الحل، تصبح القيم نصًا عاديًا للرأس أو التذييل. تبقى هذه القيم في المصنف بعد استدعاء `Save` وتظهر عند تحميل المصنف المحفوظ مرة أخرى.  

المثال التالي ينشئ مصنفين باستخدام نفس `DataTable` المتعدد الصفوف لمقارنة سلوك الإيقاف والتمكين. يترك `plainDesigner` العنصر النائب دون تغيير، بينما يقوم `enabledDesigner` بحله باستخدام الصف الأول.

```csharp
using System;
using System.Data;
using Aspose.Cells;
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Rows.Add("First Row");
table.Rows.Add("Second Row");
// Without the switch the placeholder stays literal text
Workbook plainWorkbook = new Workbook();
Worksheet plainSheet = plainWorkbook.Worksheets[0];
plainSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
plainDesigner.SetDataSource(table);
plainDesigner.Process();
// With the switch on, the FIRST row of a multi-row source wins
Workbook enabledWorkbook = new Workbook();
Worksheet enabledSheet = enabledWorkbook.Worksheets[0];
enabledSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
enabledDesigner.EnableHeaderFooterMarkers = true;
enabledDesigner.SetDataSource(table);
enabledDesigner.Process();
Console.WriteLine("Without switch: " + plainSheet.PageSetup.GetHeader(1));
Console.WriteLine("With switch: " + enabledSheet.PageSetup.GetHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.Save("HeaderFooterMarkersEnabled.xlsx");
```

## **ربط صورة في رأس أو تذييل**
اللاحقة `(picture)` تربط صورة في قسم الرأس أو التذييل. اكتب `<<node.logo(picture)>>` حيث يجب أن تظهر الصورة، وقدم قيمة الحقل كـ URI للبيانات — البادئة `data:image/png;base64,` يليها نص Base64 لبتات الصورة. سلسلة Base64 عارية بدون البادئة `data:` لا تُدرج صورة.  

بعد `Process()`:
1. العنصر النائب يتم استبداله بـ `&G`، وهو رمز الصورة القياسي في الرؤوس والتذييلات. لأن العلامة تتحول إلى رمز داخل سلسلة القسم، يمكن أن تكون جزءًا من نص أطول مثل `Logo: <<node.logo(picture)>>`.  
2. بتات الصورة يتم تضمينها في المصنف كجزء وسائط مرفق بطبقة الرسم للرأس/التذييل في ورقة العمل تلك، وبالتالي تُطبع الصورة مع الرأس أو التذييل.

```csharp
using System;
using System.Data;
using System.IO;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.PageSetup.SetHeader(1, "Logo: <<node.logo(picture)>>");
DataTable table = new DataTable("node");
table.Columns.Add("logo");
table.Rows.Add("data:image/png;base64," + Convert.ToBase64String(File.ReadAllBytes("logo.png")));
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
// This prints:
// Header: Logo: &G
workbook.Save("HeaderFooterPicture.xlsx");
```

الرمز `&G` المطبوع هو كود الصورة الذي يفسره Excel عند عرض الرأس — الآن توجد بتات `logo.png` داخل `HeaderFooterPicture.xlsx`، وتُطبع الصورة مكان الكود.  
لاستخدام العلامات الذكية في الرؤوس والتذييلات، اكتب العناصر النائبة `<<Source.Field>>` في أقسام الرأس أو التذييل اليسرى والوسطى واليمنى باستخدام `SetHeader` و `SetFooter`. عيّن `EnableHeaderFooterMarkers` إلى `true` على `WorkbookDesigner` قبل استدعاء `Process()`، وقدم القيم إما عبر `SetDataSource(DataTable)` أو `SetJsonDataSource`. اقرأ الأقسام المكتملة باستخدام `GetHeader` و `GetFooter`. يمكن لنفس مصدر البيانات تعبئة علامات الجسم والعناصر النائبة في الرؤوس أو التذييلات في عملية معالجة واحدة. أضف اللاحقة `(picture)` مع قيمة URI للبيانات لربط صورة في قسم.

## **مقالات ذات صلة**
- [العرض المتسلسل للخلية الواحدة للعلامة الذكية](/cells/ar/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="csharp" >}}