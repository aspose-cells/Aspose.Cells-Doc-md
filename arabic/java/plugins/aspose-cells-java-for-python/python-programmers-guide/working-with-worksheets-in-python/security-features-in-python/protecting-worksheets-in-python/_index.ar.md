---
title: حماية الصفحات في Python
type: docs
weight: 10
url: /ar/java/protecting-worksheets-in-python/
---

## **Aspose.Cells - حماية ورقة عمل**
لحماية صفحة العمل باستخدام **Aspose.Cells Java for Python**, اتصل بطريقة **protect_worksheet** من وحدة **protection**.

**كود Python**

{{< highlight java >}}

 #Instantiating a Excel object by excel file path

excel = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = excel.getWorksheets()

worksheet = worksheets.get(0)

protection = worksheet.getProtection()

#The following 3 methods are only for Excel 2000 and earlier formats

protection.setAllowEditingContent(False)

protection.setAllowEditingObject(False)

protection.setAllowEditingScenario(False)

#Protects the first worksheet with a password "1234"

protection.setPassword("1234")

#Saving the modified Excel file in default format

excel.save(self.dataDir + "output.xls")

#Print Message

print "Sheet protected successfully."

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **حماية الصفحات (Aspose.Cells)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
