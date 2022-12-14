---
title: قراءة ملف CSV بترميزات متعددة
type: docs
weight: 70
url: /ar/java/read-csv-file-with-multiple-encodings/
---
## **Aspose.Cells - قراءة ملف CSV بترميزات متعددة**
في وقت ما ، يحتوي ملف CSV الخاص بك على ترميزات متعددة (Unicode ، ANSI ، UTF8 ، UTF7 ، إلخ). يسمح لك Aspose.Cells بتحميل ملفات CSV هذه وتحويلها إلى تنسيقات أخرى ، على سبيل المثال PDF أو XLSX.

**Java**

{{< highlight "java" >}}

 //Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(dataDir + "MultiEncoded.csv", options);

//Save it in XLSX format

workbook.save(dataDir + "EncodedNewFile_Out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[قراءة ملف CSV بترميزات متعددة](/cells/ar/java/reading-csv-file-with-multiple-encodings).

{{% /alert %}}
