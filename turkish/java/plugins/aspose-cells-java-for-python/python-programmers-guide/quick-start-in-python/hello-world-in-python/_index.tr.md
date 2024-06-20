---
title: Python da Merhaba Dünya
type: docs
weight: 10
url: /tr/java/hello-world-in-python/
---

## **Aspose.Cells - Hello World**
Python'da Aspose.Cells Java kullanarak Merhaba Dünya, sadece Document sınıfının HelloWorld() yöntemini çağırın ve sona eklemek için ikinci belgeyi belirtin.

**Python Kodu**

{{< highlight java >}}

 workbook = self.Workbook()

sheet = workbook.getWorksheets().get(0)

cell = sheet.getCells().get("A1")

cell.setValue("Hello World!")

file_format_type = self.FileFormatType

workbook.save(self.dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )

print "Document has been saved, please check the output file.";

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi bir sosyal kodlama sitesinden **Merhaba Dünya (Aspose.Cells)**'ı indirin

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
