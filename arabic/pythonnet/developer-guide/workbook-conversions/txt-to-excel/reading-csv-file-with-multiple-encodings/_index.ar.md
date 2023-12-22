---
title: قراءة CSV ملف مع ترميزات متعددة
type: docs
weight: 200
url: /ar/python-net/reading-csv-file-with-multiple-encodings/
description: قراءة CSV ملف متعدد الترميزات باستخدام Aspose.Cells for Python via .NET API.
keywords: Python Reading CSV File with Multiple Encodings, Convert CSV File with Multiple Encodings to Excel in Python via NET, Python convert CSV File with Multiple Encodings to xlsx, Load CSV File with Multiple Encodings to Excel file.
---
{{% alert color="primary" %}}

في بعض الأحيان، يحتوي ملفك CSV على ترميزات متعددة (Unicode، ANSI، UTF8، UTF7، إلخ). Aspose.Cells يسمح لك بتحميل مثل هذه الملفات CSV وتحويلها إلى صيغ أخرى، على سبيل المثال، PDF أو XLSX.

{{% /alert %}}

 Aspose.Cells يوفر[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) الخاصية التي تحتاج إلى تعيينها**حقيقي** لتحميل ملف CSV الخاص بك بترميزات متعددة بشكل صحيح.

 تعرض لقطة الشاشة التالية نموذج ملف CSV الذي يحتوي على سطرين. السطر الأول موجود**ANSI** الترميز والسطر الثاني في**يونيكود** التشفير

|**ملف الإدخال**|
| :- |
|![ما يجب القيام به:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

تُظهر لقطة الشاشة التالية الملف XLSX الذي تم تحويله من الملف CSV أعلاه دون تعيين[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)الخاصية إلى *صحيح**. كما ترون، لم يتم تحويل نص Unicode بشكل صحيح.

|**ملف الإخراج 1: لم يتم إجراء أي ترتيبات للتشفير المتعدد**|
| :- |
|![ما يجب القيام به:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

 تعرض لقطة الشاشة التالية ملف XSLX المحول من الملف CSV أعلاه بعد تعيين ملف[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)الخاصية إلى *صحيح**. كما ترون، تم الآن تحويل نص Unicode بشكل صحيح.

|**ملف الإخراج 2: تم تعيين IsMultiEncoded على true**|
| :- |
|![ما يجب القيام به:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

يوجد أدناه نموذج التعليمات البرمجية الذي يحول الملف CSV أعلاه إلى تنسيق XLSX بشكل صحيح.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
