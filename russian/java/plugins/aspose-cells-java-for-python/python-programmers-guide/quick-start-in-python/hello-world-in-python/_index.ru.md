---
title: Привет, мир на Python
type: docs
weight: 10
url: /ru/java/hello-world-in-python/
---

## **Aspose.Cells - Hello World**
Hello World с использованием Aspose.Cells Java в Python, просто вызовите метод HelloWorld() класса Document и укажите второй документ для присоединения в конце.

**Код Python**

{{< highlight java >}}

 workbook = self.Workbook()

sheet = workbook.getWorksheets().get(0)

cell = sheet.getCells().get("A1")

cell.setValue("Hello World!")

file_format_type = self.FileFormatType

workbook.save(self.dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )

print "Document has been saved, please check the output file.";

{{< /highlight >}}
## **Скачать работающий код**
Загрузить **Hello World (Aspose.Cells)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
