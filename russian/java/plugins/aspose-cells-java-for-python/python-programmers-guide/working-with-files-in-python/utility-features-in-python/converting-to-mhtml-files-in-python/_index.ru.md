---
title: Преобразование в файлы MHTML в Python
type: docs
weight: 30
url: /ru/java/converting-to-mhtml-files-in-python/
---
## **Aspose.Cells — Преобразование в MHTML**
Чтобы преобразовать рабочий лист в файл MHTML, используя Aspose.Cells for Java в Python, просто вызовите рабочий лист_к_Метод mhtml() модуля Converter.

**Python Код**

{{< highlight "java" >}}

 saveFormat = self.SaveFormat

# Specify the file path

filePath = self.dataDir + "Book1.xlsx"

# Specify the HTML saving options

sv = self.HtmlSaveOptions(saveFormat.M_HTML)

# Instantiate a workbook and open the template XLSX file

wb = self.Workbook(filePath)

# Save the MHT file

wb.save(filePath + ".out.mht", sv)

\# Print message

print "Excel to MHTML conversion performed successfully."

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Преобразование в MHTML (Aspose.Cells)** с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
