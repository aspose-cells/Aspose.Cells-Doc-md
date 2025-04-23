---
title: تصدير بيانات Excel إلى DataTable دون أي تنسيق
type: docs
weight: 280
url: /ar/net/export-excel-data-to-datatable-without-any-formatting/
description: تعلم كيفية تصدير بيانات Excel إلى DataTable دون أي تنسيق من خلال واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: تصدير بيانات Excel إلى DataTable دون أي تنسيق، تحديد استراتيجية قيمة الخلية، إضافة استراتيجية التنسيق عند تصدير البيانات إلى DataTable. 
---

{{% alert color="primary" %}}

أحيانًا يرغب المستخدمون في تصدير بيانات Excel إلى جدول بيانات دون أي تنسيق. على سبيل المثال، إذا كانت لديهم خلية بها قيمة 0.012345 وكانت مهيأة لعرض رقمين عشريين، فعند تصدير بيانات Excel إلى جدول بيانات، سيتم تصديرها على أنها 0.01 وليس كـ 0.012345. للتعامل مع هذه المشكلة، قدمت Aspose.Cells [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) خاصية التي يمكن أن تأخذ إحدى هذه القيم

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

إذا قمت بتعيينها إلى [**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy)، فسيتم تصدير البيانات دون أي تنسيق.

{{% /alert %}}

## كود عينة

يشرح العينة التالية استخدام خاصية [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) لتصدير بيانات الإكسل مع وبدون أي تنسيق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **مخرجات الوحدة**

أدناه هو إخراج تصحيح الوحدة النمطية لكود العينة أعلاه

{{< highlight java >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
