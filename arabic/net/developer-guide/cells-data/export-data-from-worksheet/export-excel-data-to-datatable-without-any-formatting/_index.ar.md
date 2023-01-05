---
title: تصدير بيانات Excel إلى DataTable دون أي تنسيق
type: docs
weight: 280
url: /ar/net/export-excel-data-to-datatable-without-any-formatting/
---
{{% alert color="primary" %}}

في بعض الأحيان ، يرغب المستخدمون في تصدير بيانات Excel إلى جدول بيانات دون أي تنسيق. على سبيل المثال ، إذا كانت بعض الخلايا لها قيمة 0.012345 وتم تنسيقها لعرض منزلتين عشريتين ، فعندما يقوم المستخدم بتصدير بيانات Excel إلى جدول بيانات ، سيتم تصديرها كـ 0.01 وليس 0.012345. للتعامل مع هذه المشكلة ، قدمت Aspose.Cells[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) التي يمكن أن تأخذ إحدى هذه القيم الثلاث

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

 إذا كنت ستضبطه على[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy)، ثم سيتم تصدير البيانات دون أي تنسيق.

{{% /alert %}}

## عينة من الرموز

 يوضح النموذج التالي استخدام[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)لتصدير بيانات Excel مع وبدون أي تنسيق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **إخراج وحدة التحكم**

يوجد أدناه إخراج تصحيح وحدة التحكم لنموذج التعليمات البرمجية أعلاه

{{< highlight "java" >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
