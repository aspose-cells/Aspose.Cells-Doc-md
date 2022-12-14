---
title: تقليم الصفوف والأعمدة الفارغة البادئة أثناء تصدير جداول البيانات إلى تنسيق CSV
type: docs
weight: 50
url: /ar/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---
## **سيناريوهات الاستخدام الممكنة**

في بعض الأحيان ، يحتوي ملف Excel أو CSV على أعمدة أو صفوف فارغة بادئة. على سبيل المثال ، ضع في اعتبارك هذا الخط

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

هنا تكون الخلايا أو الأعمدة الثلاثة الأولى فارغة. عند فتح ملف CSV في Microsoft Excel ، يتجاهل Microsoft Excel هذه الصفوف والأعمدة الفارغة البادئة.

 بشكل افتراضي ، لا يتجاهل Aspose.Cells الأعمدة والصفوف الفارغة البادئة عند الحفظ ولكن إذا كنت تريد إزالتها تمامًا مثل Microsoft Excel ، فإن Aspose.Cells يوفر**[TxtSaveOptions.TrimLeadingBlankRowAndColumn] (https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)** منشأه. يرجى ضبطه على**حقيقي**وبعد ذلك سيتم تجاهل جميع الصفوف والأعمدة الفارغة عند الحفظ.

{{% alert color="primary" %}}

 قبل إصدار Aspose.Cells for .NET 20.4 ، كانت القيمة الافتراضية لـ**[TxtSaveOptions.TrimLeadingBlankRowAndColumn] (https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)** كنت**خاطئة** . منذ الإصدار 20.4 ، القيمة الافتراضية لـ**[TxtSaveOptions.TrimLeadingBlankRowAndColumn] (https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)** هو**حقيقي.**

{{% /alert %}}

## **تقليم الصفوف والأعمدة الفارغة البادئة أثناء تصدير جداول البيانات إلى تنسيق CSV**

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف Excel المصدر الذي يحتوي على عمودين فارغين بادئين. يقوم أولاً بحفظ ملف Excel بتنسيق CSV دون أي تغييرات ثم يتم تعيينه**[TxtSaveOptions.TrimLeadingBlankRowAndColumn] (https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)** الملكية ل**حقيقي** ويحفظه مرة أخرى. تظهر لقطة الشاشة ملف[ملف اكسل المصدر](sampleTrimBlankColumns.xlsx), [إخراج ملف CSV دون تقليم](outputWithoutTrimBlankColumns.csv)، و ال[إخراج ملف CSV مع التشذيب](outputTrimBlankColumns.csv).

![ما يجب القيام به: image_بديل_نص](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
