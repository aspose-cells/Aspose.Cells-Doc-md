---
title: قم بإلغاء حماية ورقة العمل في Python
type: docs
weight: 20
url: /ar/java/unprotect-a-worksheet-in-python/
---
## **Aspose.Cells - إلغاء حماية ورقة العمل**
 لحماية ورقة العمل باستخدام**Aspose.Cells Java لـ Python** ، مكالمة**unotect_worksheet** طريقة**الحماية** وحدة.

**Python كود**

{{< highlight "java" >}}

 filesFormatType = self.FileFormatType

# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

protection = worksheet.getProtection()

# The following 3 methods are only for Excel 2000 and earlier formats

protection.setAllowEditingContent(False)

protection.setAllowEditingObject(False)

protection.setAllowEditingScenario(False)

# Unprotecting the worksheet

worksheet.unprotect()

\# Save the excel file.

workbook.save(self.dataDir + "output.xls", filesFormatType.EXCEL_97_TO_2003)

# Print Message

print "Worksheet unprotected successfully."

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**إلغاء حماية ورقة العمل (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
