---
title: تقليم الصفوف والأعمدة الفارغة الرائدة أثناء تصدير الجداول الجدولية إلى تنسيق CSV
type: docs
weight: 100
url: /ar/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يحتوي ملف Excel أو CSV الخاص بك على أعمدة أو صفوف فارغة رئيسية. على سبيل المثال، تأمل هذا السطر

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

هنا تكون الأعمدة الثلاثة الأولى فارغة. عند فتح مثل هذا الملف CSV في Microsoft Excel، فإن Microsoft Excel يتجاهل هذه الأعمدة الرئيسية والصفوف.

بشكل افتراضي، لا تقوم Aspose.Cells بتجاهل الأعمدة والصفوف الفارغة الرائدة عند الحفظ ولكن إذا كنت ترغب في إزالتها تمامًا كما يفعل Microsoft Excel، فإن Aspose.Cells توفر الخاصية  [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn). يرجى ضبطها على **true** ثم سيتم تجاهل كل الصفوف والأعمدة الفارغة الرائدة عند الحفظ.

{{% alert color="primary" %}}

قبل إصدار Aspose.Cells for .NET 20.4، كان القيمة الافتراضية للخاصية [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) هي **false**. منذ إصدار 20.4، أصبحت القيمة الافتراضية للخاصية [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) هي **true**.

{{% /alert %}}

## **تقليص الصفوف والأعمدة الخالية أثناء تصدير جداول البيانات إلى تنسيق CSV**

الكود النموذجي التالي يقوم بتحميل [ملف الإكسيل المصدر](sampleTrimBlankColumns.xlsx) الذي يحتوي على عمودين فارغين رائدين. يقوم أولاً بحفظ ملف الإكسيل في تنسيق CSV دون أي تغييرات ومن ثم يضبط الخاصية [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) على **true** ويحفظه مرة أخرى. توضح اللقطة [ملف الإكسيل المصدر](sampleTrimBlankColumns.xlsx)، [ملف CSV الناتج بدون تقليم](outputWithoutTrimBlankColumns.csv)، و[ملف CSV الناتج بالتقليم](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
