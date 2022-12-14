---
title: Преобразование файлов Excel в HTML в Python
type: docs
weight: 10
url: /ru/java/converting-excel-files-to-html-in-python/
---
## **Aspose.Cells - Преобразование файла Excel в HTML**
Чтобы преобразовать Excel в HTML, используя Aspose.Cells for Java в Python, просто вызовите рабочий лист_к_html() модуля Converter.

**Python Код**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Преобразование файла Excel в HTML (Aspose.Cells)** с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
