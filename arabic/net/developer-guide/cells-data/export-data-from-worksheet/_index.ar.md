---
title: تصدير البيانات من ورقة العمل في .NET
linktitle: تصدير البيانات من ورقة العمل
type: docs
weight: 180
url: /ar/net/export-data-from-worksheet/
description: تشرح هذه المقالة كيفية تصدير البيانات أو استيرادها من ورقة العمل إلى جدول البيانات باستخدام C#.
---
## ملخص

تشرح هذه المقالة كيفية تصدير بيانات ورقة العمل إلى DataTable باستخدام C#. وتغطي الموضوعات التالية

_شكل_: **اكسل**
- [C# Excel إلى DataTable](#csharp-excel-to-datatable)
- [C# تحويل Excel إلى DataTable](#csharp-convert-excel-to-datatable)
- [C# قم باستيراد Excel إلى DataTable](#csharp-import-excel-to-datatable)
- [C# تصدير إلى DataTable من Excel](#csharp-export-to-datatable-from-excel)

_شكل_: **XLS**
- [C# XLS إلى DataTable](#csharp-xls-to-datatable)
- [C# قم بتحويل XLS إلى DataTable](#csharp-convert-xls-to-datatable)
- [C# استيراد XLS إلى DataTable](#csharp-import-xls-to-datatable)
- [C# تصدير إلى DataTable من XLS](#csharp-export-to-datatable-from-xls)

_شكل_: **XLSX**
- [C# XLSX إلى DataTable](#csharp-xlsx-to-datatable)
- [C# قم بتحويل XLSX إلى DataTable](#csharp-convert-xlsx-to-datatable)
- [C# استيراد XLSX إلى DataTable](#csharp-import-xlsx-to-datatable)
- [C# تصدير إلى DataTable من XLSX](#csharp-export-to-datatable-from-xlsx)

_شكل_: **ODS**
- [C# ODS إلى DataTable](#csharp-ods-to-datatable)
- [C# قم بتحويل ODS إلى DataTable](#csharp-convert-ods-to-datatable)
- [C# استيراد ODS إلى DataTable](#csharp-import-ods-to-datatable)
- [C# تصدير إلى DataTable من ODS](#csharp-export-to-datatable-from-ods)

## **C# تصدير بيانات Excel**

{{% alert color="primary" %}}

تتناول هذه المقالة بعض تقنيات تصدير البيانات التي يمكن للمطورين الوصول إليها من خلال Aspose.Cells.

{{% /alert %}}

## **تصدير البيانات من ورقة العمل**

 لا يسهّل Aspose.Cells المستخدمين فقط لاستيراد البيانات إلى أوراق العمل من مصادر البيانات الخارجية ولكن أيضًا يسمح لهم بتصدير بيانات ورقة العمل الخاصة بهم إلى[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) . كما نعلم ذلك[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) هو جزء من ADO.NET ويستخدم للاحتفاظ بالبيانات. بمجرد تخزين البيانات في ملف[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) يمكن استخدامه بأي طريقة حسب متطلبات المستخدمين. يمكن للمطورين أيضًا تخزين هذه البيانات (المخزنة بتنسيق[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ) مباشرة إلى قاعدة بيانات إذا رغبوا في ذلك. لذلك ، يمكننا أن نرى أنه يصبح من السهل على المطورين معالجة بيانات ورقة العمل إذا تم تصديرها إلى ملف[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **تصدير البيانات إلى DataTable باستخدام Aspose.Cells**

 يمكن للمطورين بسهولة تصدير بيانات ورقة العمل الخاصة بهم إلى ملف[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) عن طريق استدعاء أي منهما[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) أو[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)صف دراسي. يتم استخدام كلتا الطريقتين في سيناريوهات مختلفة ، والتي تمت مناقشتها أدناه بمزيد من التفصيل.

## **الأعمدة التي تحتوي على بيانات مكتوبة بقوة**

نعلم أن جدول البيانات يخزن البيانات على شكل سلسلة من الصفوف والأعمدة. إذا كانت جميع القيم في أعمدة ورقة العمل مكتوبة بقوة (وهذا يعني أن جميع القيم في عمود يجب أن تحتوي على نفس نوع البيانات) ، فيمكننا تصدير محتوى ورقة العمل عن طريق استدعاء[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) صف دراسي.[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) تأخذ الطريقة المعلمات التالية لتصدير بيانات ورقة العمل كملف[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)موضوع:

- **رقم الصف**، سيتم تصدير رقم صف بيانات الخلية الأولى من.
- **رقم العمود**، رقم العمود للخلية الأولى التي سيتم تصدير البيانات منها.
- **عدد الصفوف**، عدد الصفوف المطلوب تصديرها.
- **عدد الأعمدة**، عدد الأعمدة المطلوب تصديرها.
- **تصدير أسماء الأعمدة** ، خاصية منطقية تشير إلى ما إذا كان يجب تصدير البيانات الموجودة في الصف الأول من ورقة العمل كأسماء أعمدة من[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)أم لا.

_الخطوات: تصدير البيانات إلى DataTable_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>خطوات:</em> Excel إلى DataTable في C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>خطوات:</em> XLS إلى DataTable في C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>خطوات:</em> XLSX إلى DataTable في C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>خطوات:</em> ODS إلى DataTable في C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>خطوات:</em> قم بتحويل Excel إلى DataTable في C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>خطوات:</em>حول XLS إلى DataTable في C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>خطوات:</em>حول XLSX إلى DataTable في C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>خطوات:</em>حول ODS إلى DataTable في C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>خطوات:</em> قم باستيراد Excel إلى DataTable في C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>خطوات:</em> قم باستيراد XLS إلى DataTable في C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>خطوات:</em> قم باستيراد XLSX إلى DataTable في C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>خطوات:</em> قم باستيراد ODS إلى DataTable في C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>خطوات:</em> تصدير إلى DataTable من Excel في C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>خطوات:</em> تصدير إلى DataTable من XLS في C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>خطوات:</em> تصدير إلى DataTable من XLSX في C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>خطوات:</em> تصدير إلى DataTable من ODS في C#</strong></a>

_خطوات التعليمات البرمجية:_

1.  قم بتحميل ملف Excel بتنسيق[دفتر العمل](https://reference.aspose.com/cells/net/aspose.cells/workbook/) موضوع.
   - [دفتر العمل](https://reference.aspose.com/cells/net/aspose.cells/workbook/) يمكن للكائن تحميل تنسيقات ملفات Excel ، مثل XLS ، XLSX ، XLSM ، ODS إلخ.
 3. يقبل الأول[ورقة عمل](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) في ملف Excel.
 4. اختر منطقة التصدير الخاصة بك ، على سبيل المثال 7 صفوف وعمودين بدءًا من الخلية الأولى في**جدول البيانات**.
 5. الاستخدام[ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) طريقة لتصدير البيانات إلى DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **الأعمدة التي تحتوي على بيانات غير مكتوبة بشدة**

 إذا لم يتم كتابة جميع القيم في أعمدة ورقة العمل بشكل قوي (وهذا يعني أن القيم الموجودة في عمود قد تحتوي على أنواع بيانات مختلفة) ، فيمكننا تصدير محتوى ورقة العمل عن طريق استدعاء[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) صف دراسي.[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)تأخذ الطريقة نفس مجموعة المعلمات مثل تلك الخاصة بـ[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)طريقة لتصدير بيانات ورقة العمل كملف[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)موضوع.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **نطاق التصدير مع العلم لتخطي اسم العمود**

يمكن تصدير البيانات من نطاق إلى[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) حيث تتوفر علامة لتخطي صف الرأس في البيانات المصدرة. يصدر الكود التالي نطاقًا من البيانات إلى[**جدول البيانات**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) مع حجة[**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) الذي يحتوي على[**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) علَم. تم تعيينه على**حقيقي** إذا كانت معلومات الرأس موجودة ، فلن يتم تضمينها في البيانات وتعيينها إلى**خاطئة** إذا لم يكن هناك رأس ، فسيتم اعتبار جميع الصفوف بيانات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **موضوعات مسبقة**
- [تصدير بيانات Excel إلى DataTable دون أي تنسيق](/cells/ar/net/export-excel-data-to-datatable-without-any-formatting/)
- [تصدير HTML سلسلة قيمة Cells إلى DataTable](/cells/ar/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [تصدير بيانات الصفوف المرئية من ورقة العمل](/cells/ar/net/export-visible-rows-data-from-worksheet/)
- [تجاهل الأعمدة المخفية أثناء تصدير بيانات ورقة العمل إلى جدول البيانات](/cells/ar/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [أعد تسمية الأعمدة المكررة تلقائيًا أثناء تصدير بيانات ورقة العمل](/cells/ar/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
