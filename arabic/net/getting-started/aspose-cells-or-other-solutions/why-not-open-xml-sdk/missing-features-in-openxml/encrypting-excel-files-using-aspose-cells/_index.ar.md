---
title: تشفير ملفات Excel باستخدام Aspose.Cells
type: docs
weight: 30
url: /ar/net/encrypting-excel-files-using-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) يتيح لك تشفير وحماية كلمة مرور لجداول البيانات خاصتك. يستخدم خوارزميات تقدمها مزود خدمات التشفير، أو CSP، مجموعة من الخوارزميات التشفيرية ذات الخصائص المختلفة. يعتبر CSP الافتراضي هو 'متوافق مع Office 97/2000' أو 'التشفير الضعيف (XOR)'. من المهم اختيار طول المفتاح التشفيري الصحيح. بعض CSPs لا تدعم أكثر من 40 أو 56 بت. يُعتبر ذلك تشفيرًا ضعيفًا. بالنسبة للتشفير القوي، يتطلب طول مفتاح أدنى قدره 128 بت. يحتوي نظام التشغيل Microsoft Windows على CSPs تقدم أنواع تشفير قوية أيضًا، على سبيل المثال 'موفر خدمات التشفير القوي من مايكروسوفت'. على سبيل المثال، 128 بت تشفير هو ما يستخدمه البنوك لتشفير الاتصال بأنظمتها للخدمات المصرفية عبر الإنترنت.

تسمح Aspose.Cells لك بتشفير وحماية ملفات Microsoft Excel بنوع التشفير الذي ترغب فيه.

{{% /alert %}} 
## **استخدام Microsoft Excel**
لضبط إعدادات تشفير الملف في Microsoft Excel (هنا Microsoft Excel 2003):

١. من قائمة **الأدوات**, حدد **خيارات**.
   يظهر حوار.
١. حدد علامة التبويب **الأمان**.
1. أدخل كلمة مرور وانقر **متقدم** 
   **الحوار للاختيارات** 

![todo:image_alt_text](encrypting-excel-files-using-aspose-cells_1.png)




١. اختر نوع التشفير وقم بتأكيد كلمة المرور. 

   **مربع حوار نوع التشفير** 

![todo:image_alt_text](encrypting-excel-files-using-aspose-cells_2.png)



## **التشفير مع Aspose.Cells**
المثال التالي يوضح كيفية تشفير وحماية ملف Excel بكلمة مرور باستخدام واجهة برمجة التطبيقات Aspose.Cells.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string srcFileName = FilePath + "Encrypting Excel Files.xlsx";

string destFileName = FilePath + "Result Encrypting Excel Files.xlsx";

//Open an excel file.

Workbook workbook = new Workbook(srcFileName);

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR, 40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save(destFileName);

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
## **تحميل رمز عينة**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Encrypting%20Excel%20Files)

{{< app/cells/assistant language="csharp" >}}
