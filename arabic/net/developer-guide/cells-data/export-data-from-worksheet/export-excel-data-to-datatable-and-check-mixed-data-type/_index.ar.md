---
title: تصدير بيانات Excel إلى DataTable والتحقق من نوع البيانات المختلطة
type: docs
weight: 280
url: /ar/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: تعرف على كيفية تصدير بيانات Excel إلى DataTable والتحقق من نوع البيانات المختلطة من خلال Aspose.Cells for .NET API.
keywords: Export Excel Data to DataTable and Check Mixed Data Type, Export Workbook Data to DataTable and Check Mixed Data Type, Export Data to DataTable and Check Mixed Data Type, Export Worksheet Data to DataTable and Check Mixed Data Type.
---
##  **سيناريوهات الاستخدام المحتملة**
 إذا كان العمود يحتوي على بيانات من أنواع مختلفة، فسيطرح البرنامج استثناء النوع عند تصدير البيانات إلى DataTable. لتصدير جدول البيانات، بشكل افتراضي، يقوم Aspose.Cells بتقييم نوع البيانات للقيم بناءً على القيمة (الخلية) الأولى في العمود. لذا، إذا كانت القيمة رقمًا، فهذا يعني أن نوع بيانات العمود سيكون رقميًا، وهو أمر معقول. إذا كانت القيمة الأولى عبارة عن رقم ولكن هناك بيانات أو قيم أبجدية رقمية في العمود، فيجب تعيين نوع بيانات سلسلة. للتعامل معها، يرجى استخدام[التحميل الزائد لـ ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) الذي يتضمن[تصديرDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) ومحاولة تعيين[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) سمة منطقية إلى "صحيح" إذا كان العمود يحتوي على قيم رقمية وسلسلة لتجنب الخطأ.

##  **تصدير بيانات Excel إلى DataTable والتحقق من نوع البيانات المختلطة**

 النموذج التالي يشرح استخدام[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/)خاصية تصدير بيانات Excel إلى جدول البيانات. الرجاء مراجعة[عينة من ملف إكسل](sample.xlsx)ولقطة الشاشة وإخراج وحدة التحكم كمرجع.

###  **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

###  **لقطة شاشة**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

###  **إخراج وحدة التحكم**

يوجد أدناه إخراج تصحيح وحدة التحكم لنموذج التعليمات البرمجية أعلاه

{{< highlight "java" >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
