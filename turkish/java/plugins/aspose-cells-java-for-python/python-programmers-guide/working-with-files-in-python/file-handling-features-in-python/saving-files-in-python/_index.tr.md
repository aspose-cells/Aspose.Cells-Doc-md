---
title: Dosyaları Python'de Kaydetme
type: docs
weight: 20
url: /tr/java/saving-files-in-python/
---
## **Aspose.Cells - Dosyaları Kaydetme**
### **Dosyayı bir konuma kaydetme**
 Geliştiricilerin dosyalarını kullanarak kaydetmeleri gerekiyorsa**Aspose.Cells Java için Python** bir depolama konumuna daha sonra dosya adını (tam depolama yolu ile birlikte) ve istenen dosya formatını (kullanarak) belirtebilirler.**Dosya Biçimi Türü**numaralandırma) çağrılırken**kaydetmek**yöntemi**Çalışma kitabı**nesne.

**Python Kod**

{{< highlight "python" >}}

 fileFormatType = self.FileFormatType


# Creating an Workbook object with an Excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save in default (Excel2003) format

workbook.save(self.dataDir + "book.default.out.xls")

# Save in Excel2003 format

workbook.save(self.dataDir + "book.out.xls", fileFormatType.EXCEL_97_TO_2003)

# Save in Excel2007 xlsx format

workbook.save(self.dataDir + "book.out.xlsx", fileFormatType.XLSX)

# Save in SpreadsheetML format

workbook.save(self.dataDir + "book.out.xml", fileFormatType.EXCEL_2003_XML)

# Print Message

print("<BR>")

print("Worksheets are saved successfully.")

{{< /highlight >}}

 İndirmek**Dosyayı Kaydetme (Aspose.Cells)** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
