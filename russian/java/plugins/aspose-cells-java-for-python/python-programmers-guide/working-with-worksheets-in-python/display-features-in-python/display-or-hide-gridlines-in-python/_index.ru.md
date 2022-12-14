---
title: Показать или скрыть линии сетки в Python
type: docs
weight: 10
url: /ru/java/display-or-hide-gridlines-in-python/
---
## **Aspose.Cells - Показать скрыть линии сетки**
### **Скрытие линий сетки**
 Чтобы скрыть рабочий лист, используя**Aspose.Cells Java для рубина** , вызов**displayhidegridlines** модуль.

**Python Код**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

# Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
### **Делаем линии сетки видимыми**
Чтобы сделать линии сетки видимыми, используйте метод setGridlinesVisible(true) класса Worksheet.

**Python Код**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**DisplayHideGridlines (Aspose.Cells)** с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
