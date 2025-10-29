---
title: تقليم الصفوف والأعمدة الفارغة الرائدة أثناء تصدير الجداول الجدولية إلى تنسيق CSV
type: docs
weight: 100
url: /ar/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: تقليص الصفوف والأعمدة الفارغة الرائدة أثناء تصدير جداول البيانات إلى تنسيق CSV باستخدام API Aspose.Cells للبايثون via .NET.
keywords: تقليص الصفوف والأعمدة الفارغة الرائدة أثناء تصدير جداول البيانات إلى تنسيق CSV بواسطة Python، تقليص الصفوف والأعمدة الفارغة الرائدة أثناء حفظ جداول البيانات بتنسيق CSV في Python via NET، تقليص الصفوف والأعمدة الفارغة عند تصدير جدول البيانات إلى تنسيق CSV بواسطة Python.
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يحتوي ملف Excel أو CSV الخاص بك على أعمدة أو صفوف فارغة رئيسية. على سبيل المثال، تأمل هذا السطر

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

هنا تكون الأعمدة الثلاثة الأولى فارغة. عند فتح مثل هذا الملف CSV في Microsoft Excel، فإن Microsoft Excel يتجاهل هذه الأعمدة الرئيسية والصفوف.

بشكل افتراضي، لا تقوم Aspose.Cells for Python via .NET بتجاهل الأعمدة الفارغة الرائدة والصفوف عند الحفظ ولكن إذا كنت ترغب في إزالتها تمامًا كما يفعل Microsoft Excel، فإن Aspose.Cells for Python via .NET توفر خاصية [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/). يُرجى ضبطها إلى **true** وسيتم التخلص من كافة الأعمدة الفارغة الرائدة والصفوف عند الحفظ.

{{% alert color="primary" %}}

قبل إصدار Aspose.Cells for Python via .NET 20.4، كان القيمة الافتراضية لـ [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) هي **false**. منذ إصدار 20.4، القيمة الافتراضية لـ [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) هي **true**.

{{% /alert %}}

## **تقليص الصفوف والأعمدة الخالية أثناء تصدير جداول البيانات إلى تنسيق CSV**

الكود النموذجي التالي يقوم بتحميل [ملف الإكسيل المصدر](sampleTrimBlankColumns.xlsx) الذي يحتوي على عمودين فارغين رائدين. يقوم أولاً بحفظ ملف الإكسيل في تنسيق CSV دون أي تغييرات ومن ثم يضبط الخاصية [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) على **true** ويحفظه مرة أخرى. توضح اللقطة [ملف الإكسيل المصدر](sampleTrimBlankColumns.xlsx)، [ملف CSV الناتج بدون تقليم](outputWithoutTrimBlankColumns.csv)، و[ملف CSV الناتج بالتقليم](outputTrimBlankColumns.csv).

![todo:image_alt_text](result.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
{{< app/cells/assistant language="python-net" >}}
