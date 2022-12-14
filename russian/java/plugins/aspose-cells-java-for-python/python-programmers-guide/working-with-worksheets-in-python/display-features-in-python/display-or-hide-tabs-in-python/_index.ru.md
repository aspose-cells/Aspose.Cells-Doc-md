---
title: Показать или скрыть вкладки в Python
type: docs
weight: 30
url: /ru/java/display-or-hide-tabs-in-python/
---
## **Aspose.Cells - Показать скрыть вкладки**
### **Скрытие вкладок**
 Чтобы скрыть вкладки с помощью**Aspose.Cells Java для рубина** , вызов**показать скрыть вкладки** модуль.

**Python Код**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Делаем вкладки видимыми**
Сделайте вкладки видимыми с помощью метода setSheetTabBarHidden(false) класса Workbook.

**Python Код**

{{< highlight "python" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Hello World (Aspose.Cells)** с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
