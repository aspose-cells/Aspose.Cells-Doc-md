---
title: Заморозка области в Python
type: docs
weight: 40
url: /ru/java/freeze-panes-in-python/
---

## **Aspose.Cells - Заморозить области**
Для замораживания областей в документе электронной таблицы с использованием **Aspose.Cells Java for Python** просто вызовите модуль **FreezePanes**.

**Код Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "book.out.xls")

#Print Message

print "Panes freeze successfull."

{{< /highlight >}}
## **Скачать работающий код**
Загрузить **Hello World (Aspose.Cells)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
