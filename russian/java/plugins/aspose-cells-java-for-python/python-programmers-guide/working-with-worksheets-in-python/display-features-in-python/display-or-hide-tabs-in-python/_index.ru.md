---
title: Отобразить или скрыть вкладки в Python
type: docs
weight: 30
url: /ru/java/display-or-hide-tabs-in-python/
---

## **Aspose.Cells - Display Hide вкладки**
### **Скрытие вкладок**
Чтобы скрыть вкладки с помощью **Aspose.Cells Java для Ruby**, вызовите модуль **displayhidetabs**.

**Код Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Отображение вкладок**
Сделайте вкладки видимыми с помощью метода setSheetTabBarHidden(false) класса Workbook.

**Код Python**

{{< highlight python >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Скачать работающий код**
Загрузить **Hello World (Aspose.Cells)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
