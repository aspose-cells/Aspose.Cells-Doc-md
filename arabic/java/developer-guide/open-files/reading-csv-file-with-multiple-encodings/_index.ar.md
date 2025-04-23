---
title: قراءة ملف CSV بترميزات متعددة
type: docs
weight: 140
url: /ar/java/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}} 

أحيانًا، يحتوي ملف الـ CSV الخاص بك على ترميزات متعددة (يونيكود، ANSI، UTF8، UTF7 إلخ). Aspose.Cells تسمح لك بتحميل مثل هذه الملفات الـ CSV وتحويلها إلى صيغ أخرى، على سبيل المثال PDF أو XLSX.

{{% /alert %}} 

توفر Aspose.Cells طريقة TxtLoadOptions.setMultiEncoded()، التي تحتاج إلى تعيينها إلى **true** لتحميل ملف الـ CSV الخاص بك بترميزات متعددة بشكل صحيح.

تُظهر اللقطة الشاشية التالية ملف CSV عينة يحتوي على سطرين. السطر الأول بترميز **ANSI** والسطر الثاني بترميز **يونيكود**

**الملف الداخلي** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)

تُظهر اللقطة الشاشية التالية ملف XLSX تم تحويله من ملف CSV أعلاه دون تعيين طريقة TxtLoadOptions.setMultiEncoded() إلى قيمة صحيحة. كما تلاحظ، لم يتم تحويل النص اليونيكود بشكل صحيح.

**الملف الناتج 1: لم يتم إجراء أي تكيف للترميز المتعدد** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)

تُظهر اللقطة الشاشية التالية ملف XSLX تم تحويله من ملف CSV أعلاه بعد تعيين طريقة TxtLoadOptions.setMultiEncoded() إلى قيمة صحيحة. كما تلاحظ، تم تحويل النص اليونيكود بشكل صحيح الآن.

**الملف الناتج 2: IsMultiEncoded تم تعيين قيمتها إلى true** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)

أدناه الكود النموذجي الذي يحول ملف CSV أعلاه إلى صيغة XLSX بشكل صحيح.

**Java**

{{< highlight csharp >}}

 String filePath = "F:\\Downloads\\MutliEncoded.csv";

//Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(filePath, options);

//Save it in XLSX format

workbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
