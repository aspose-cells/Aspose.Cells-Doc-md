---
title: قص الصفوف والأعمدة الفارغة قبل التصدير إلى CSV مع Golang عبر C++
linktitle: تقليم الصفوف والأعمدة الفارغة في البداية
type: docs
weight: 100
url: /ar/go-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: تعلم كيف تقليم الصفوف والأعمدة الفارغة في البداية أثناء تصدير جداول البيانات إلى تنسيق CSV باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يكون لملف Excel أو CSV الخاص بك أعمدة أو صفوف فارغة في البداية. على سبيل المثال، فكر في السطر التالي:

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

هنا تكون الأعمدة الثلاثة الأولى فارغة. عند فتح مثل هذا الملف CSV في Microsoft Excel، فإن Microsoft Excel يتجاهل هذه الأعمدة الرئيسية والصفوف.

بشكل افتراضي، لا تقوم Aspose.Cells بتجاهل الأعمدة والصفوف الفارغة الرائدة عند الحفظ ولكن إذا كنت ترغب في إزالتها تمامًا كما يفعل Microsoft Excel، فإن Aspose.Cells توفر الخاصية  [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/). يرجى ضبطها على **true** ثم سيتم تجاهل كل الصفوف والأعمدة الفارغة الرائدة عند الحفظ.

{{% alert color="primary" %}}

قبل إصدار Aspose.Cells for C++ 20.4، كانت القيمة الافتراضية لـ [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) هي **false**. منذ إصدار 20.4، القيمة الافتراضية لـ [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) هي **true.**

{{% /alert %}}

## **تقليص الصفوف والأعمدة الخالية أثناء تصدير جداول البيانات إلى تنسيق CSV**

الكود النموذجي التالي يقوم بتحميل [ملف الإكسيل المصدر](sampleTrimBlankColumns.xlsx) الذي يحتوي على عمودين فارغين رائدين. يقوم أولاً بحفظ ملف الإكسيل في تنسيق CSV دون أي تغييرات ومن ثم يضبط الخاصية [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) على **true** ويحفظه مرة أخرى. توضح اللقطة [ملف الإكسيل المصدر](sampleTrimBlankColumns.xlsx)، [ملف CSV الناتج بدون تقليم](outputWithoutTrimBlankColumns.csv)، و[ملف CSV الناتج بالتقليم](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCsvFormat.go" >}}
