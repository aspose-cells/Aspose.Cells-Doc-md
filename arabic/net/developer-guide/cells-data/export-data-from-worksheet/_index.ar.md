---
title: تصدير البيانات من ورقة العمل في .NET
linktitle: تصدير البيانات من ورقة العمل
type: docs
weight: 180
url: /ar/net/export-data-from-worksheet/
description: يشرح هذا المقال كيفية تصدير أو استيراد البيانات من ورقة العمل إلى DataTable باستخدام C#.
keywords: C# تصدير البيانات من ورقة العمل، C# تصدير البيانات إلى DataTable، أعمدة تحتوي على بيانات من نوع محدد بشكل قوي، أعمدة تحتوي على بيانات من نوع غير محدد بشكل قوي، C# تصدير المدى مع راية لتخطي اسم العمود، كيفية تصدير المدى مع رأس.
---

## نظرة عامة

يشرح هذا المقال كيفية تصدير بيانات ورقة العمل إلى DataTable باستخدام C#. يغطي المواضيع التالية

_التنسيق_: **Excel**
- [تحويل C# Excel إلى DataTable](#csharp-excel-to-datatable)
- [تحويل C# Excel إلى DataTable](#csharp-convert-excel-to-datatable)
- [تحميل C# Excel إلى DataTable](#csharp-import-excel-to-datatable)
- [تصدير إلى DataTable من Excel باستخدام C#](#csharp-export-to-datatable-from-excel)

_التنسيق_: **XLS**
- [C# XLS إلى DataTable](#csharp-xls-to-datatable)
- [تحويل C# XLS إلى DataTable](#csharp-convert-xls-to-datatable)
- [تحميل C# XLS إلى DataTable](#csharp-import-xls-to-datatable)
- [تصدير إلى DataTable من XLS باستخدام C#](#csharp-export-to-datatable-from-xls)

_التنسيق_: **XLSX**
- [C# XLSX إلى DataTable](#csharp-xlsx-to-datatable)
- [تحويل C# XLSX إلى DataTable](#csharp-convert-xlsx-to-datatable)
- [تحميل C# XLSX إلى DataTable](#csharp-import-xlsx-to-datatable)
- [تصدير إلى DataTable من XLSX باستخدام C#](#csharp-export-to-datatable-from-xlsx)

_التنسيق_: **ODS**
- [C# ODS إلى DataTable](#csharp-ods-to-datatable)
- [تحويل C# ODS إلى DataTable](#csharp-convert-ods-to-datatable)
- [تحميل C# ODS إلى DataTable](#csharp-import-ods-to-datatable)
- [تصدير إلى DataTable من ODS باستخدام C#](#csharp-export-to-datatable-from-ods)

## **كيفية تصدير بيانات Excel باستخدام C#**

{{% alert color="primary" %}}

يركز هذا المقال على بعض تقنيات تصدير البيانات التي يمتلك المطورون الوصول إليها من خلال Aspose.Cells.

{{% /alert %}}

## **كيفية تصدير البيانات من ورق العمل**

Aspose.Cells لا تسهل فقط على مستخدميها استيراد البيانات إلى أوراق العمل من مصادر بيانات خارجية ولكنها تسمح لهم أيضًا بتصدير بيانات أوراقهم العمل إلى كائن [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8). كما نعلم أن [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) جزء من ADO.NET ويتم استخدامه لعقد البيانات. بمجرد أن تُخزن البيانات في [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ، يمكن استخدامها بأي طريقة وفقًا لمتطلبات المستخدمين. يمكن للمطورين أيضًا تخزين هذه البيانات (المخزنة في [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)) مباشرة في قاعدة بيانات إذا أرادوا. لذلك ، يمكننا أن نرى أنه يصبح من الأسهل بالنسبة للمطورين تلاعب ببيانات الورقة العمل إذا تم تصديرها إلى [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **كيفية تصدير البيانات إلى جدول بيانات باستخدام Aspose.Cells**

يمكن للمطورين تصدير بيانات أوراق العمل بسهولة إلى كائن [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) من خلال استدعاء إما [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) أو [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) من فئة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). كلا الطريقتين تستخدم في سيناريوهات مختلفة ، والتي يتم مناقشتها أدناه بمزيد من التفاصيل.

## **الأعمدة التي تحتوي على بيانات مكونة من نوع واحد**

نحن نعلم أن جدول البيانات يخزن البيانات كسلسلة من الصفوف والأعمدة. إذا كانت جميع القيم في أعمدة ورقة العمل من نوع محدد (وهذا يعني أن جميع القيم في العمود يجب أن تكون لها نفس نوع البيانات) ، فيمكننا تصدير محتوى ورقة العمل عن طريق استدعاء الطريقة [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) من فئة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). تأخذ الطريقة [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) المعلمات التالية لتصدير بيانات ورقة العمل ككائن [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8):

- **رقم الصف** ، رقم الصف للبيانات التي سيتم تصديرها منها الخلية الأولى.
- **رقم العمود** ، رقم العمود للخلية الأولى التي سيتم تصدير البيانات منها.
- **عدد الصفوف** ، عدد الصفوف المراد تصديرها.
- **عدد الأعمدة** ، عدد الأعمدة المراد تصديرها.
- **تصدير أسماء الأعمدة** ، خاصية بوليانية تشير إلى ما إذا كان ينبغي تصدير البيانات في الصف الأول من ورقة العمل كأسماء للأعمدة للكائن [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) أم لا.

_خطوات: تصدير البيانات إلى جدول بيانات_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>خطوات:</em> Excel to DataTable in C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>خطوات:</em> XLS to DataTable in C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>خطوات:</em> XLSX to DataTable in C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>خطوات:</em> ODS to DataTable in C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>خطوات:</em> Convert Excel to DataTable in C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>خطوات:</em> Convert XLS to DataTable in C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>خطوات:</em> Convert XLSX to DataTable in C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>خطوات:</em> Convert ODS to DataTable in C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>خطوات:</em> Import Excel to DataTable in C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>خطوات:</em> Import XLS to DataTable in C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>خطوات:</em> Import XLSX to DataTable in C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>خطوات:</em> Import ODS to DataTable in C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>خطوات:</em> Export to DataTable from Excel in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>خطوات:</em> Export to DataTable from XLS in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>خطوات:</em> Export to DataTable from XLSX in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>خطوات:</em> Export to DataTable from ODS in C#</strong></a>

_خطوات الكود:_

1. قم بتحميل ملف Excel الخاص بك في [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/) الكائن.
   - يمكن لكائن [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/) تحميل تنسيقات ملف Excel مثل XLS, XLSX, XLSM, ODS وما إلى ذلك.
3. الوصول إلى الورقة العمل الأولى [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) في ملف Excel.
4. اختيار منطقة التصدير الخاصة بك مثل 7 صفوف و 2 أعمدة تبدأ من الخلية الأولى من **DataTable**.
5. استخدام [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) الطريقة لتصدير البيانات إلى DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **الأعمدة التي تحتوي على بيانات غير مكونة من نوع واحد**

إذا كانت جميع القيم في الأعمدة لورقة العمل غير مكتوبة بشكل قوي (وهذا يعني أن القيم في العمود قد تحتوي على أنواع بيانات مختلفة) ثم يمكننا تصدير محتوى ورقة العمل عن طريق استدعاء الطريقة [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) من الصنف [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). الطريقة [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) تأخذ نفس مجموعة من المعاملات كما في الطريقة [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) لتصدير بيانات ورقة العمل ككائن [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **كيفية تصدير المدى مع رأس**

يمكن تصدير البيانات من مدى إلى [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) حيث تكون هناك علم متاح لتجاهل صف الرأس في البيانات المصدرة. يتم تصدير مجموعة البيانات التالية إلى [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) بمعطى [**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) والذي يحتوي على علم [**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname). يتم ضبطه على **true** إذا كانت هناك معلومات رأس، لذا لن تتم إدراجها في البيانات وضبطه على **false** إذا لم يكن هناك رأس ويجب اعتبار كل الصفوف بأنها بيانات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **مواضيع متقدمة**
- [تصدير بيانات Excel إلى جدول البيانات دون أي تنسيق](/cells/ar/net/export-excel-data-to-datatable-without-any-formatting/)
- [تصدير قيمة سلسلة HTML للخلايا إلى جدول البيانات](/cells/ar/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [تصدير بيانات الصفوف المرئية من ورقة العمل](/cells/ar/net/export-visible-rows-data-from-worksheet/)
- [تجاهل الأعمدة المخفية أثناء تصدير بيانات ورقة العمل إلى جدول البيانات](/cells/ar/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [إعادة تسمية الأعمدة المكررة تلقائيًا أثناء تصدير بيانات ورقة العمل](/cells/ar/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
{{< app/cells/assistant language="csharp" >}}
