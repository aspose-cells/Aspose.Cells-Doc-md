---
title: Spara filer i Python
type: docs
weight: 20
url: /sv/java/saving-files-in-python/
---

## **Aspose.Cells - Spara filer**
### **Spara filen på en viss plats**
Om utvecklare behöver spara sina filer med **Aspose.Cells Java för Python** till någon lagringsplats kan de enkelt ange filnamnet (med dess fullständiga lagringsväg) och önskat filformat (med hjälp av **FileFormatType** uppräkning) när de anropar **save** metoden för **Workbook** objektet.

**Python-kod**

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

Ladda ned **Spara fil (Aspose.Cells)** från någon av nedan angivna sociala kodningssidor:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
