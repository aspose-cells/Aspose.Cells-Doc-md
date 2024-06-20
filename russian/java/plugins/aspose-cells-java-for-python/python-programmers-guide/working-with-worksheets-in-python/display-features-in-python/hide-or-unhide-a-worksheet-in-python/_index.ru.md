---
title: Скрыть или отобразить лист в Python
type: docs
weight: 50
url: /ru/java/hide-or-unhide-a-worksheet-in-python/
---

## **Aspose.Cells - Скрыть или показать лист**
### **Скрыть лист**
Чтобы скрыть лист с помощью Aspose.Cells Java для Ruby, вызовите модуль **hideunhideworksheet**.

**Код Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Hiding the first worksheet of the Excel file

worksheet.setVisible(True)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Показать лист**
Разработчики могут сделать лист видимым, установив метод *setVisible(* *true* *)* класса **Worksheet**.

**Код Python**

{{< highlight python >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Скрыть или отобразить лист (Aspose.Cells)** с любого из упомянутых ниже сайтов для социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
