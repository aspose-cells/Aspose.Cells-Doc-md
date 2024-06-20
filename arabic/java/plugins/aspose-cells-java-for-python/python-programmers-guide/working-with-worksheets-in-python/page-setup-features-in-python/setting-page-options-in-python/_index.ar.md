---
title: ضبط خيارات الصفحة في Python
type: docs
weight: 10
url: /ar/java/setting-page-options-in-python/
---

## **Aspose.Cells - ضبط خيارات الصفحة**
### **اتجاه الصفحة**
لتطبيق إعدادات اتجاه الصفحة باستخدام **Aspose.Cells Java for Ruby**، ادعو إلى الاستدعاء **page_orientation** لوحدة **pagesetup**.

**كود Python**

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
### **عامل التحليل**
لتطبيق تحجيم باستخدام **Aspose.Cells Java for Python**, اطلب الطريقة **scaling** من وحدة **pagesetup**.

**كود Python**

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
## **تحميل رمز التشغيل**
تحميل **خيارات صفحة الإعداد (Aspose.Cells)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
