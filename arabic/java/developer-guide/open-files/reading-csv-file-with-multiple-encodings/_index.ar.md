---
title: قراءة ملف CSV بترميزات متعددة
type: docs
weight: 140
url: /ar/java/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}} 

في وقت ما ، يحتوي ملف CSV الخاص بك على ترميزات متعددة (Unicode ، ANSI ، UTF8 ، UTF7 ، إلخ). يسمح لك Aspose.Cells بتحميل ملفات CSV هذه وتحويلها إلى تنسيقات أخرى ، على سبيل المثال PDF أو XLSX.

{{% /alert %}} 

 يوفر Aspose.Cells طريقة TxtLoadOptions.setMultiEncoded () ، والتي تحتاج إلى ضبطها على**حقيقي** لتحميل ملف CSV الخاص بك مع ترميزات متعددة بشكل صحيح.

 تُظهر لقطة الشاشة التالية نموذج ملف CSV يحتوي على سطرين. السطر الأول في**ANSI** الترميز والسطر الثاني في**يونيكود** التشفير

**ملف الإدخال** 

![ما يجب القيام به: image_بديل_نص](reading-csv-file-with-multiple-encodings_1.png)

تُظهر لقطة الشاشة التالية ملف XLSX المحول من ملف CSV أعلاه دون ضبط طريقة TxtLoadOptions.setMultiEncoded () على القيمة true. كما ترى ، لم يتم تحويل نص Unicode بشكل صحيح.

**ملف الإخراج 1: لم يتم إجراء أي تكييف للترميز المتعدد** 

![ما يجب القيام به: image_بديل_نص](reading-csv-file-with-multiple-encodings_2.png)

تُظهر لقطة الشاشة التالية ملف XSLX المحول من ملف CSV أعلاه بعد تعيين طريقة TxtLoadOptions.setMultiEncoded () على القيمة true. كما ترى ، يتم الآن تحويل نص Unicode بشكل صحيح.

**ملف الإخراج 2: تم تعيين IsMultiEncoded على true** 

![ما يجب القيام به: image_بديل_نص](reading-csv-file-with-multiple-encodings_3.png)

يوجد أدناه نموذج التعليمات البرمجية الذي يحول ملف CSV أعلاه إلى تنسيق XLSX بشكل صحيح.

**Java**

{{< highlight "csharp" >}}

 String filePath = "F:\\Downloads\\MutliEncoded.csv";

//Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(filePath, options);

//Save it in XLSX format

workbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
