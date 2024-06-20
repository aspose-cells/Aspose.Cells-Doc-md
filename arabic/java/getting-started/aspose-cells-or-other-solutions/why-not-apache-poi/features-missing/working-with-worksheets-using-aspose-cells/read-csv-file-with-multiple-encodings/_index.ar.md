---
title: قراءة ملف CSV بعدة ترميزات
type: docs
weight: 70
url: /ar/java/read-csv-file-with-multiple-encodings/
---

## **Aspose.Cells - قراءة ملف CSV بعدة ترميزات**
أحيانًا، يحتوي ملف الـ CSV الخاص بك على ترميزات متعددة (يونيكود، ANSI، UTF8، UTF7 إلخ). Aspose.Cells تسمح لك بتحميل مثل هذه الملفات الـ CSV وتحويلها إلى صيغ أخرى، على سبيل المثال PDF أو XLSX.

**Java**

{{< highlight java >}}

 //Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(dataDir + "MultiEncoded.csv", options);

//Save it in XLSX format

workbook.save(dataDir + "EncodedNewFile_Out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
## **تحميل رمز التشغيل**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [قراءة ملف CSV بعدة ترميزات](/cells/ar/java/reading-csv-file-with-multiple-encodings).

{{% /alert %}}
