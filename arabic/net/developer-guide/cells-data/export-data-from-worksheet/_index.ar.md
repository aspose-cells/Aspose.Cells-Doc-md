---
title: تصدير البيانات من ورقة العمل في .NET
linktitle: تصدير البيانات من ورقة العمل
type: docs
weight: 180
url: /ar/net/export-data-from-worksheet/
description: تشرح هذه المقالة كيفية تصدير البيانات أو استيرادها من ورقة العمل إلى جدول البيانات باستخدام C#.
keywords: C# Export Data from Worksheet, C# Export Data to DataTable, Columns Containing Strongly Typed Data, Columns Containing Non-Strongly Typed Data, C# Export Range with flag to skip column name
---
##  ملخص

تشرح هذه المقالة كيفية تصدير بيانات ورقة العمل الخاصة بك إلى DataTable باستخدام C#. وهي تغطي المواضيع التالية

 _شكل_:**اكسل**
- [C# إكسل إلى DataTable](#csharp-excel-to-datatable)
- [C# تحويل Excel إلى DataTable](#csharp-convert-excel-to-datatable)
- [C# استيراد Excel إلى DataTable](#csharp-import-excel-to-datatable)
- [C# تصدير إلى DataTable من Excel](#csharp-export-to-datatable-from-excel)

 _شكل_:**XLS**
- [C# XLS إلى DataTable](#csharp-xls-to-datatable)
- [C# تحويل XLS إلى DataTable](#csharp-convert-xls-to-datatable)
- [C# استيراد XLS إلى DataTable](#csharp-import-xls-to-datatable)
- [C# تصدير إلى DataTable من XLS](#csharp-export-to-datatable-from-xls)

 _شكل_:**XLSX**
- [C# XLSX إلى DataTable](#csharp-xlsx-to-datatable)
- [C# تحويل XLSX إلى DataTable](#csharp-convert-xlsx-to-datatable)
- [C# استيراد XLSX إلى DataTable](#csharp-import-xlsx-to-datatable)
- [C# تصدير إلى DataTable من XLSX](#csharp-export-to-datatable-from-xlsx)

 _شكل_:**ODS**
- [C# ODS إلى DataTable](#csharp-ods-to-datatable)
- [C# تحويل ODS إلى DataTable](#csharp-convert-ods-to-datatable)
- [C# استيراد ODS إلى DataTable](#csharp-import-ods-to-datatable)
- [C# تصدير إلى DataTable من ODS](#csharp-export-to-datatable-from-ods)

##  **كيفية تصدير بيانات Excel باستخدام C#**

{{% alert color="primary" %}}

تتناول هذه المقالة بعض تقنيات تصدير البيانات التي يمكن للمطورين الوصول إليها من خلال Aspose.Cells.

{{% /alert %}}

##  **كيفية تصدير البيانات من ورقة العمل**

 Aspose.Cells لا يسهل على مستخدميه استيراد البيانات إلى أوراق العمل من مصادر البيانات الخارجية فحسب، بل يسمح لهم أيضًا بتصدير بيانات ورقة العمل الخاصة بهم إلى[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) . كما نعلم ذلك[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) هو جزء من ADO.NET ويستخدم للاحتفاظ بالبيانات. بمجرد تخزين البيانات في ملف[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ، ويمكن استخدامه بأي شكل من الأشكال وفقا لمتطلبات المستخدمين. يمكن للمطورين أيضًا تخزين هذه البيانات (المخزنة في[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ) مباشرة إلى قاعدة البيانات إذا رغبوا في ذلك. لذلك، يمكننا أن نرى أنه يصبح من الأسهل على المطورين التعامل مع بيانات ورقة العمل إذا تم تصديرها إلى ملف[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

##  **كيفية تصدير البيانات إلى DataTable باستخدام Aspose.Cells**

 يمكن للمطورين بسهولة تصدير بيانات ورقة العمل الخاصة بهم إلى ملف[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) الكائن عن طريق الاتصال إما[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) أو[**تصديرDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)فصل. يتم استخدام كلا الطريقتين في سيناريوهات مختلفة، والتي سيتم مناقشتها أدناه بمزيد من التفاصيل.

##  **الأعمدة التي تحتوي على بيانات مكتوبة بقوة**

 نحن نعلم أن جدول البيانات يخزن البيانات كسلسلة من الصفوف والأعمدة. إذا كانت جميع القيم الموجودة في أعمدة ورقة العمل مكتوبة بقوة (وهذا يعني أن جميع القيم الموجودة في العمود يجب أن تحتوي على نفس نوع البيانات)، فيمكننا تصدير محتوى ورقة العمل عن طريق استدعاء الأمر[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) فصل.[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) تأخذ الطريقة المعلمات التالية لتصدير بيانات ورقة العمل بتنسيق[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)هدف:

- *رقم الصف**، سيتم تصدير رقم صف بيانات الخلية الأولى منه.
- *رقم العمود**، رقم عمود الخلية الأولى التي سيتم تصدير البيانات منها.
- *عدد الصفوف**، عدد الصفوف المراد تصديرها.
- *عدد الأعمدة**، عدد الأعمدة المراد تصديرها.
- *تصدير أسماء الأعمدة**، وهي خاصية منطقية تشير إلى ما إذا كان يجب تصدير البيانات الموجودة في الصف الأول من ورقة العمل كأسماء أعمدة في[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)أم لا.

_الخطوات: تصدير البيانات إلى DataTable_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>خطوات:</em> Excel إلى DataTable في C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>خطوات:</em> XLS إلى DataTable في C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>خطوات:</em> XLSX إلى DataTable في C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>خطوات:</em> ODS إلى DataTable في C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>خطوات:</em> تحويل Excel إلى DataTable في C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>خطوات:</em> تحويل XLS إلى DataTable في C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>خطوات:</em> تحويل XLSX إلى DataTable في C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>خطوات:</em> تحويل ODS إلى DataTable في C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>خطوات:</em> استيراد Excel إلى DataTable في C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>خطوات:</em> استيراد XLS إلى DataTable في C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>خطوات:</em> استيراد XLSX إلى DataTable في C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>خطوات:</em> استيراد ODS إلى DataTable في C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>خطوات:</em> تصدير إلى DataTable من Excel في C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>خطوات:</em> تصدير إلى DataTable من XLS في C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>خطوات:</em> تصدير إلى DataTable من XLSX في C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>خطوات:</em> تصدير إلى DataTable من ODS في C#</strong></a>

_خطوات الكود:_

1.  قم بتحميل ملف Excel الخاص بك[دفتر العمل](https://reference.aspose.com/cells/net/aspose.cells/workbook/) هدف.
   - [دفتر العمل](https://reference.aspose.com/cells/net/aspose.cells/workbook/) يمكن للكائن تحميل تنسيقات ملفات Excel، على سبيل المثال XLS، XLSX، XLSM، ODS وما إلى ذلك.
 3. الوصول إلى الأول[ورقة عمل](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) في ملف اكسيل .
4. اختر منطقة التصدير الخاصة بك، على سبيل المثال، 7 صفوف وعمودين بدءًا من الخلية الأولى في *DataTable**.
 5. استخدم[ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) طريقة تصدير البيانات إلى DataTable

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

##  **الأعمدة التي تحتوي على بيانات غير مكتوبة بقوة**

 إذا لم تتم كتابة جميع القيم الموجودة في أعمدة ورقة العمل بقوة (وهذا يعني أن القيم الموجودة في العمود قد تحتوي على أنواع بيانات مختلفة)، فيمكننا تصدير محتوى ورقة العمل عن طريق استدعاء الأمر[**تصديرDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) فصل.[**تصديرDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)تأخذ الطريقة نفس مجموعة المعلمات مثل تلك الخاصة بـ[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)طريقة لتصدير بيانات ورقة العمل كملف[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)هدف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

##  **كيفية تصدير النطاق مع العلم لتخطي اسم العمود**

 يمكن تصدير البيانات من نطاق إلى[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) حيث تتوفر علامة لتخطي صف الرأس في البيانات المصدرة. يقوم الكود التالي بتصدير نطاق من البيانات إلى[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) مع حجة[**خيارات التصدير**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) الذي يحتوي على[**اسم عمود التصدير**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) علَم. تم ضبطه على**حقيقي** إذا كانت معلومات الرأس موجودة، فلن يتم تضمينها في البيانات وتعيينها على**خطأ شنيع** إذا لم يكن هناك رأس، فسيتم اعتبار كافة الصفوف كبيانات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

##  **مواضيع متقدمة**
- [تصدير بيانات Excel إلى DataTable دون أي تنسيق](/cells/ar/net/export-excel-data-to-datatable-without-any-formatting/)
- [تصدير HTML قيمة سلسلة Cells إلى DataTable](/cells/ar/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [تصدير بيانات الصفوف المرئية من ورقة العمل](/cells/ar/net/export-visible-rows-data-from-worksheet/)
- [تجاهل الأعمدة المخفية أثناء تصدير بيانات ورقة العمل إلى جدول البيانات](/cells/ar/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [إعادة تسمية الأعمدة المكررة تلقائيًا أثناء تصدير بيانات ورقة العمل](/cells/ar/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
