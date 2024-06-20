---
title: Python da Dosyaları Kaydetme
type: docs
weight: 20
url: /tr/java/saving-files-in-python/
---

## **Aspose.Cells - Dosyaları Kaydetme**
### **Dosyayı belirli bir konuma kaydetme**
Geliştiriciler, dosyalarını **Aspose.Cells Java for Python** kullanarak bir depolama konumuna kaydetmek istiyorlarsa, sadece **Workbook** nesnesinin **save** yöntemini çağırırken dosya adını (tam depolama yolunu içeren) ve istenen dosya biçimini ( **FileFormatType** numaralama kullanarak) belirtebilirler.

**Python Kodu**

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

Aşağıda belirtilen herhangi bir sosyal kodlama sitesinden **Dosya Kaydetme (Aspose.Cells)**'i indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
