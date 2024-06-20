---
title: Преобразование Excel в файлы PDF в Python
type: docs
weight: 20
url: /ru/java/converting-excel-to-pdf-files-in-python/
---

## **Aspose.Cells - Преобразование Excel в Pdf**
Для преобразования Excel в файл Pdf с использованием Aspose.Cells for Java в Python просто вызовите метод excel_to_pdf() модуля Converter.

**Код Python**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **Скачать работающий код**
Загрузить **Преобразование Excel в PDF (Aspose.Cells)** с любого из нижеприведенных сайтов для социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
