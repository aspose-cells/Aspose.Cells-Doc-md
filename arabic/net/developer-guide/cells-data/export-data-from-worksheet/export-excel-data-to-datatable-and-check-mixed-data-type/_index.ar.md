---
title: تصدير بيانات Excel إلى DataTable والتحقق من نوع البيانات المختلطة
type: docs
weight: 280
url: /ar/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: تعلم كيفية تصدير بيانات Excel إلى DataTable والتحقق من نوع البيانات المختلطة من خلال واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: تصدير بيانات Excel إلى DataTable والتحقق من نوع البيانات المختلطة، تصدير بيانات دفتر العمل إلى DataTable والتحقق من نوع البيانات المختلطة، تصدير البيانات إلى DataTable والتحقق من نوع البيانات المختلطة، تصدير بيانات ورقة العمل إلى DataTable والتحقق من نوع البيانات المختلطة.
---

## **سيناريوهات الاستخدام المحتملة**
إذا تحتوي العمود على بيانات من أنواع مختلفة، سيقوم البرنامج بإلقاء استثناء نوع عند تصدير البيانات إلى DataTable. عند تصدير جدول البيانات، يقوم Aspose.Cells بتقييم نوع البيانات للقيم استنادًا إلى القيمة الأولى (خلية) في العمود. لذا، إذا كانت القيمة رقمية، فهذا يعني أن نوع بيانات العمود سيكون رقميًا، وهذا أمر معقول. إذا كانت القيمة الأولى رقمية ولكن هناك بيانات أو قيم أبجدية رقمية في العمود، فيجب تعيين نوع البيانات كسلسلة. للتعامل مع ذلك، يرجى استخدام [تشتيت البيانات الزائدة](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) الذي يتضمن [خيارات تصدير جدول البيانات](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) ومحاولة ضبط [حقل ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) إلى "true" إذا كان لديك عمود يحتوي على قيم رقمية وسلسلة لتجنب الخطأ.

## **تصدير بيانات Excel إلى DataTable والتحقق من نوع البيانات المختلطة**

يشرح العينة التالية استخدام [خيارات تصدير جدول البيانات.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) لتصدير بيانات Excel إلى جدول بيانات. يُرجى الرجوع إلى [ملف Excel العيني](عينة.xlsx)، لقطة الشاشة وإخراج الكونسول للإشارة.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

### **لقطة شاشة**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

### **مخرجات الوحدة**

أدناه هو إخراج تصحيح الوحدة النمطية لكود العينة أعلاه

{{< highlight java >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
