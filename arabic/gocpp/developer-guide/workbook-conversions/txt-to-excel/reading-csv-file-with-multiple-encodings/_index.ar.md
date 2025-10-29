---
title: قراءة ملف CSV مع ترميزات متعددة باستخدام Golang عبر C++
linktitle: قراءة ملف CSV بترميزات متعددة
type: docs
weight: 200
url: /ar/go-cpp/reading-csv-file-with-multiple-encodings/
description: تعلم كيفية قراءة ملفات CSV ذات الترميزات المتعددة باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، يحتوي ملف CSV الخاص بك على ترميزات متعددة (Unicode، ANSI، UTF8، UTF7، إلخ). تتيح لك Aspose.Cells تحميل مثل هذه الملفات وتحويلها إلى تنسيقات أخرى، على سبيل المثال، PDF أو XLSX.

{{% /alert %}}

توفر Aspose.Cells الخاصية [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/)، والتي تحتاج إلى ضبطها على **true** لتحميل ملف CSV الخاص بك مع ترميزات متعددة بشكل صحيح.

 تظهر الصورة التالية مثالاً على ملف CSV يحتوي على سطرين. السطر الأول بالترميز **ANSI** والسطر الثاني بالترميز **Unicode**.

|**ملف الإدخال**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

 تظهر الصورة التالية ملف XLSX الذي تم تحويله من ملف CSV أعلاه دون ضبط الخاصية [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/) على **true**. كما ترى، لم يتم تحويل النص Unicode بشكل صحيح.

|**ملف الإخراج 1: لم يتم اتخاذ إجراءات للتعامل مع الترميز المتعدد**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

تُظهر لقطة الشاشة التالية ملف XLSX الذي تم تحويله من ملف CSV أعلاه بعد تعيين خاصية [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/) إلى **صحيح**. كما ترى، النص اليونيكود يُحوّل الآن بشكل صحيح.

|**ملف الإخراج 2: تم تعيين IsMultiEncoded على true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

أدناه الكود النموذجي الذي يحول ملف CSV أعلاه إلى صيغة XLSX بشكل صحيح.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadingCsvFileWithMultipleEncodings.go" >}}
## مقالات ذات صلة

- [فتح ملفات CSV](/cells/ar/cpp/opening-files-with-different-formats/#opening-csv-files)
