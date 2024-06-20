---
title: Сохранение файлов в Python
type: docs
weight: 20
url: /ru/java/saving-files-in-python/
---

## **Aspose.Cells - Сохранение Файлов**
### **Сохранение файла в выбранное место**
Если разработчикам нужно сохранить их файлы с использованием **Aspose.Cells Java для Python** в определенное место хранения, то они могут просто указать имя файла (с полным путем к его хранению) и желаемый формат файла (используя перечисление **FileFormatType**) при вызове метода **save** объекта **Workbook**.

**Код Python**

{{< highlight python >}}

 fileFormatType = self.FileFormatType


#Creating an Workbook object with an Excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save in default (Excel2003) format

workbook.save(self.dataDir + "book.default.out.xls")

#Save in Excel2003 format

workbook.save(self.dataDir + "book.out.xls", fileFormatType.EXCEL_97_TO_2003)

#Save in Excel2007 xlsx format

workbook.save(self.dataDir + "book.out.xlsx", fileFormatType.XLSX)

#Save in SpreadsheetML format

workbook.save(self.dataDir + "book.out.xml", fileFormatType.EXCEL_2003_XML)

#Print Message

print("<BR>")

print("Worksheets are saved successfully.")

{{< /highlight >}}

Скачать **Сохранение файла (Aspose.Cells)** с любого из нижеперечисленных сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
