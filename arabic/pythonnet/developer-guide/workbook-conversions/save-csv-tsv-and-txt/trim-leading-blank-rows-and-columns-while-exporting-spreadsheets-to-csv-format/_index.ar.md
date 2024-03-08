---
title: اقتطاع الصفوف والأعمدة الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV
type: docs
weight: 100
url: /ar/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: قم بقص الصفوف والأعمدة الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV باستخدام Aspose.Cells for Python via .NET API.
keywords: Python Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format, Trim Leading Blank Rows and Columns while saving excel to CSV format in Python via NET, Python Trim Leading Blank Rows and Columns exporting excel to CSV format.
---
##  **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يحتوي ملف Excel أو CSV على أعمدة أو صفوف فارغة في المقدمة. على سبيل المثال، النظر في هذا الخط

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

هنا تكون الخلايا أو الأعمدة الثلاثة الأولى فارغة. عند فتح ملف CSV في Microsoft Excel، فإن Microsoft Excel يتجاهل هذه الصفوف والأعمدة الفارغة البادئة.

 افتراضيًا، Aspose.Cells for Python via .NET لا يتجاهل الأعمدة والصفوف الفارغة البادئة عند الحفظ، ولكن إذا كنت تريد إزالتها تمامًا كما يفعل Microsoft Excel، فإن Aspose.Cells for Python via .NET يوفر**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** ملكية. يرجى ضبطه على**حقيقي**وبعد ذلك سيتم التخلص من كافة الصفوف والأعمدة الفارغة عند الحفظ.

{{% alert color="primary" %}}

 قبل إصدار Aspose.Cells for Python via .NET 20.4 كانت القيمة الافتراضية لـ**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**كان**خطأ شنيع**. منذ الإصدار 20.4، القيمة الافتراضية **[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** يكون**حقيقي.**

{{% /alert %}}

##  **اقتطاع الصفوف والأعمدة الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[ملف اكسيل المصدر](sampleTrimBlankColumns.xlsx) الذي يحتوي على عمودين فارغين رئيسيين. يقوم أولاً بحفظ ملف Excel بتنسيق CSV دون أي تغييرات ثم يقوم بتعيينه**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** الملكية ل**حقيقي** ويحفظه مرة أخرى. تظهر لقطة الشاشة[ملف اكسيل المصدر](sampleTrimBlankColumns.xlsx), [إخراج الملف CSV بدون تقطيع](outputWithoutTrimBlankColumns.csv)، و ال[ملف الإخراج CSV مع التشذيب](outputTrimBlankColumns.csv).

![ما يجب القيام به:image_alt_text](result.png)

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
