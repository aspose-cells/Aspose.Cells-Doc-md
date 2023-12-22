---
title: تصدير بيانات Excel إلى DataTable دون أي تنسيق
type: docs
weight: 280
url: /ar/net/export-excel-data-to-datatable-without-any-formatting/
description: تعرف على كيفية تصدير بيانات Excel إلى DataTable دون أي تنسيق من خلال Aspose.Cells for .NET API.
keywords: Export Excel Data to DataTable without any Formatting, Specify Cell Value Format Strategy, Add Format Strategy When Exporting Data to DataTable. 
---
{{% alert color="primary" %}}

في بعض الأحيان يرغب المستخدمون في تصدير بيانات Excel إلى جدول بيانات دون أي تنسيق. على سبيل المثال، إذا كانت بعض الخلايا تحتوي على قيمة 0.012345 وتم تنسيقها لعرض منزلتين عشريتين، فعندما يقوم المستخدم بتصدير بيانات Excel إلى جدول بيانات، سيتم تصديرها كـ 0.01 وليس كـ 0.012345. للتعامل مع هذه المشكلة تم توفير Aspose.Cells[**تصديرTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) الخاصية التي يمكن أن تأخذ إحدى هذه القيم الثلاث

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

 إذا قمت بتعيينه على[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy)، ثم سيتم تصدير البيانات دون أي تنسيق.

{{% /alert %}}

##  عينة من الرموز

 النموذج التالي يشرح استخدام[**تصديرTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)خاصية تصدير بيانات Excel مع وبدون أي تنسيق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

##  **إخراج وحدة التحكم**

يوجد أدناه إخراج تصحيح وحدة التحكم لنموذج التعليمات البرمجية أعلاه

{{< highlight "java" >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
