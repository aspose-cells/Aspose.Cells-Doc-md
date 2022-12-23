---
title: Python'de bir Çalışma Sayfasının korumasını kaldırın
type: docs
weight: 20
url: /tr/java/unprotect-a-worksheet-in-python/
---
## **Aspose.Cells - Bir Çalışma Sayfasının korumasını kaldırın**
 Çalışma sayfasını kullanarak korumak için**Aspose.Cells Java for Python** , Arama**unprotect_worksheet** yöntemi**koruma** modül.

**Python Kod**

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
## **Çalışan Kodu İndir**
 İndirmek**Bir Çalışma Sayfasının korumasını kaldırın (Aspose.Cells)** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
