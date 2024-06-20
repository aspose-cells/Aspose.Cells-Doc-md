---
title: حفظ الملفات في Python
type: docs
weight: 20
url: /ar/java/saving-files-in-python/
---

## **Aspose.Cells - حفظ الملفات**
### **حفظ الملف في موقع معين**
إذا كان المطورون بحاجة إلى حفظ ملفاتهم باستخدام **Aspose.Cells Java for Python** إلى موقع تخزين ما ، فيمكنهم ببساطة تحديد اسم الملف (مع مسار تخزينه الكامل) وتنسيق الملف المرغوب (باستخدام تعداد الـ**FileFormatType**) أثناء استدعاء الطريقة **save** من كائن **Workbook**.

**كود Python**

{{< highlight python >}}

 fileFormatType = self.FileFormatType


#Creating an Workbook object with an Excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save in default (Excel2003) format

workbook.save(self.dataDir + "book.default.out.xls")

#Save in Excel2003 format

workbook.save(self.dataDir + "book.out.xls", fileFormatType.EXCEL_97_TO_2003)

#Save in Excel2007 xlsx format

workbook.save(self.dataDir + "book.out.xlsx", fileFormatType.XLSX)

#Save in SpreadsheetML format

workbook.save(self.dataDir + "book.out.xml", fileFormatType.EXCEL_2003_XML)

#Print Message

print("<BR>")

print("Worksheets are saved successfully.")

{{< /highlight >}}

تنزيل **حفظ الملف (Aspose.Cells)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
