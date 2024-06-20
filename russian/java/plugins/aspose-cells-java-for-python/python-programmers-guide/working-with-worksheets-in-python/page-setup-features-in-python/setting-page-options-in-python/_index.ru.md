---
title: Установка параметров страницы в Python
type: docs
weight: 10
url: /ru/java/setting-page-options-in-python/
---

## **Aspose.Cells - Настройка параметров страницы**
### **Ориентация страницы**
Чтобы применить параметры ориентации страницы с использованием Aspose.Cells Java для Ruby, вызовите метод page_orientation модуля pagesetup.

**Код Python**

{{< highlight java >}}

 def page_orientation(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook()

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

sheet = worksheets.get(sheet_index)

\# Setting the orientation to Portrait

page_setup = sheet.getPageSetup()

page_orientation_type = self.PageOrientationType

page_setup.setOrientation(page_orientation_type.PORTRAIT)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Page_Orientation.xls")

print "Set page orientation, please check the output file."


{{< /highlight >}}
### **Фактор масштабирования**
Для применения масштабирования с использованием **Aspose.Cells Java для Python** вызовите метод **scaling** модуля **pagesetup**.

**Код Python**

{{< highlight python >}}

 def scaling(self):        

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

sheet = worksheets.get(sheet_index)

\# Setting the scaling factor to 100

page_setup = sheet.getPageSetup()

page_setup.setZoom(100)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Scaling.xls")

print "Set scaling, please check the output file."

{{< /highlight >}}
## **Скачать работающий код**
Загрузить **Установка параметров страницы (Aspose.Cells)** с любого из упомянутых ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
