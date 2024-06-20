---
title: Salvataggio File in Python
type: docs
weight: 20
url: /it/java/saving-files-in-python/
---

## **Aspose.Cells - Salvataggio dei file**
### **Salvataggio file in una determinata posizione**
Se gli sviluppatori hanno bisogno di salvare i propri file utilizzando **Aspose.Cells Java per Python** in una posizione di storage specifica, possono semplicemente specificare il nome del file (con il percorso di storage completo) e il formato desiderato del file (usando l'enumerazione **FileFormatType**) durante la chiamata del metodo **save** dell'oggetto **Workbook**.

**Codice Python**

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

Scarica **Salvataggio File (Aspose.Cells)** da uno qualsiasi dei siti di codice sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
