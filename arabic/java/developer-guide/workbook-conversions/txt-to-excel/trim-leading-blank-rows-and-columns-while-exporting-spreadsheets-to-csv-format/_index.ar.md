---
title: تقليم الصفوف والأعمدة الفارغة الرائدة أثناء تصدير الجداول الجدولية إلى تنسيق CSV
type: docs
weight: 50
url: /ar/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يحتوي ملف Excel أو CSV الخاص بك على أعمدة أو صفوف فارغة رئيسية. على سبيل المثال، تأمل هذا السطر

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

هنا تكون الأعمدة الثلاثة الأولى فارغة. عند فتح مثل هذا الملف CSV في Microsoft Excel، فإن Microsoft Excel يتجاهل هذه الأعمدة الرئيسية والصفوف.

بشكل افتراضي، لا تقوم Aspose.Cells بتجاهل الأعمدة والصفوف الفارغة الرائدة عند الحفظ ولكن إذا كنت ترغب في إزالتها تمامًا كما يفعل Microsoft Excel، فإن Aspose.Cells توفر الخاصية  [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn). يرجى ضبطها على **true** ثم سيتم تجاهل كل الصفوف والأعمدة الفارغة الرائدة عند الحفظ.

{{% alert color="primary" %}}

قبل إصدار Aspose.Cells for .NET 20.4، كان القيمة الافتراضية للخاصية [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) هي **false**. منذ إصدار 20.4، أصبحت القيمة الافتراضية للخاصية [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) هي **true**.

{{% /alert %}}

## **تقليص الصفوف والأعمدة الخالية أثناء تصدير جداول البيانات إلى تنسيق CSV**

يحمل الكود العيني العيني التالي ملف إكسيل المصدر الذي يحتوي على عمودين فارغين رئيسيين. يحفظ الملف الإكسيل أولاً في تنسيق CSV دون أي تغييرات ثم يضبط الخاصية [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) إلى **true** ويحفظه مرة أخرى. توضح اللقطة الشاشية ملف الفئران الأولي [ملف إكسيل المصدر](sampleTrimBlankColumns.xlsx)، [ملف CSV الناتج بدون قص الأعمدة الفارغة](outputWithoutTrimBlankColumns.csv) و ملف CSV الناتج مع القص](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
{{< app/cells/assistant language="java" >}}
