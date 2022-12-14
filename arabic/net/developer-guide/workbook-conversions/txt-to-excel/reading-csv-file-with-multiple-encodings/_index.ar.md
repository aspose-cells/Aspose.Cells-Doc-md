---
title: قراءة ملف CSV بترميزات متعددة
type: docs
weight: 200
url: /ar/net/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}}

في بعض الأحيان ، يحتوي ملف CSV الخاص بك على ترميزات متعددة (Unicode ، ANSI ، UTF8 ، UTF7 ، إلخ). يسمح لك Aspose.Cells بتحميل ملفات CSV هذه وتحويلها إلى تنسيقات أخرى ، على سبيل المثال ، PDF أو XLSX.

{{% /alert %}}

 يوفر Aspose.Cells ملف[**TxtLoadOptions.SMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)الخاصية التي تحتاج إلى تعيينها**حقيقي** لتحميل ملف CSV الخاص بك مع ترميزات متعددة بشكل صحيح.

 تُظهر لقطة الشاشة التالية نموذج ملف CSV يحتوي على سطرين. السطر الأول في**ANSI** الترميز والسطر الثاني في**يونيكود** التشفير

|**ملف الإدخال**|
|:- |
|![ما يجب القيام به: image_بديل_نص](reading-csv-file-with-multiple-encodings_1.png)|

 تُظهر لقطة الشاشة التالية ملف XLSX المحول من ملف CSV أعلاه دون تعيين ملف[**TxtLoadOptions.SMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) الملكية ل**حقيقي**. كما ترى ، لم يتم تحويل نص Unicode بشكل صحيح.

|**ملف الإخراج 1: لم يتم إجراء أي تكييف للترميز المتعدد**|
|:- |
|![ما يجب القيام به: image_بديل_نص](reading-csv-file-with-multiple-encodings_2.png)|

 تُظهر لقطة الشاشة التالية ملف XSLX المحول من ملف CSV أعلاه بعد تعيين ملف[**TxtLoadOptions.SMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) الملكية ل**حقيقي**. كما ترى ، يتم الآن تحويل نص Unicode بشكل صحيح.

|**ملف الإخراج 2: تم تعيين IsMultiEncoded على true**|
|:- |
|![ما يجب القيام به: image_بديل_نص](reading-csv-file-with-multiple-encodings_3.png)|

يوجد أدناه نموذج التعليمات البرمجية الذي يحول ملف CSV أعلاه إلى تنسيق XLSX بشكل صحيح.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## مقالات ذات صلة

- [فتح ملفات CSV](/cells/ar/net/opening-files-with-different-formats/#opening-csv-files)
