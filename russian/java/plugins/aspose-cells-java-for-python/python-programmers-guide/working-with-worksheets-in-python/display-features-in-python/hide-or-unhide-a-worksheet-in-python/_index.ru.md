---
title: Скрыть или показать рабочий лист в Python
type: docs
weight: 50
url: /ru/java/hide-or-unhide-a-worksheet-in-python/
---
## **Aspose.Cells - Скрыть или показать рабочий лист**
### **Скрытие рабочего листа**
 Чтобы скрыть рабочий лист, используя Aspose.Cells Java для Ruby, вызовите**скрыть рабочий лист** модуль.

**Python Код**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the first worksheet of the Excel file

worksheet.setVisible(True)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Отображение рабочего листа**
Разработчики могут сделать рабочий лист видимым, установив*установитьвидимый(* *истинный* *)*метод**Рабочий лист**учебный класс.

**Python Код**

{{< highlight "python" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Скрыть или показать рабочий лист (Aspose.Cells)** с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
