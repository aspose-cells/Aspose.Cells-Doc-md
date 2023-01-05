---
title: Преобразование Excel в файлы PDF в Python
type: docs
weight: 20
url: /ru/java/converting-excel-to-pdf-files-in-python/
---
## **Aspose.Cells - Преобразование Excel в PDF**
Чтобы преобразовать файл Excel в файл Pdf, используя Aspose.Cells for Java в Python, просто вызовите excel_к_pdf() модуля Converter.

**Python Код**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Преобразование Excel в PDF (Aspose.Cells)** с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
