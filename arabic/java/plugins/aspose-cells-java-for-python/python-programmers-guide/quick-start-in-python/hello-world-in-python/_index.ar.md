---
title: Hello World في Python
type: docs
weight: 10
url: /ar/java/hello-world-in-python/
---
## **Aspose.Cells - Hello World**
Hello World باستخدام Aspose.Cells Java في Python ، ما عليك سوى استدعاء طريقة HelloWorld () لفئة المستند وتحديد المستند الثاني الذي سيتم إلحاقه في النهاية.

**Python كود**

{{< highlight "java" >}}

 workbook = self.Workbook()

sheet = workbook.getWorksheets().get(0)

cell = sheet.getCells().get("A1")

cell.setValue("Hello World!")

file_format_type = self.FileFormatType

workbook.save(self.dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )

print "Document has been saved, please check the output file.";

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**Hello World (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
