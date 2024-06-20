---
title: قراءة ملف CSV بترميزات متعددة
type: docs
weight: 200
url: /ar/python-net/reading-csv-file-with-multiple-encodings/
description: قراءة ملف CSV بعدة ترميزات باستخدام Aspose.Cells لواجهة برمجة التطبيقات لـ Python via .NET API.
keywords: قراءة ملف CSV بعدة ترميزات في Python، تحويل ملف CSV بعدة ترميزات إلى Excel في Python via NET، تحويل ملف CSV بعدة ترميزات إلى xlsx في Python، تحميل ملف CSV بعدة ترميزات إلى ملف Excel.
---

{{% alert color="primary" %}}

في بعض الأحيان، يحتوي ملف CSV الخاص بك على ترميزات متعددة (Unicode، ANSI، UTF8، UTF7، إلخ). تسمح Aspose.Cells لك بتحميل مثل هذه الملفات CSV وتحويلها إلى تنسيقات أخرى، على سبيل المثال PDF أو XLSX.

{{% /alert %}}

توفر Aspose.Cells خاصية [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) التي يجب أن تقوم بضبطها على **true** لتحميل ملف CSV الخاص بك بترميزات متعددة بشكل صحيح.

يوضح اللقطة الشاشية التالية ملف CSV عينة يحتوي على سطرين. السطر الأول بترميز **ANSI** والسطر الثاني بترميز **Unicode**.

|**ملف الإدخال**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

توضح اللقطة الشاشية التالية ملف XLSX المحول من ملف CSV المذكور أعلاه من دون ضبط خاصية [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) على **true**. كما ترون، لم يتم تحويل النص Unicode بشكل صحيح.

|**ملف الإخراج 1: لم يتم اتخاذ إجراءات للتعامل مع الترميز المتعدد**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

توضح اللقطة الشاشية التالية ملف XSLX المحول من ملف CSV المذكور أعلاه بعد ضبط خاصية [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) على **true**. كما ترون، تم تحويل النص Unicode بشكل صحيح الآن.

|**ملف الإخراج 2: تم تعيين IsMultiEncoded على true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

أدناه الكود النموذجي الذي يحول ملف CSV أعلاه إلى صيغة XLSX بشكل صحيح.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
