---
title: Enregistrement de fichiers en Python
type: docs
weight: 20
url: /fr/java/saving-files-in-python/
---

## **Aspose.Cells - Enregistrement de fichiers**
### **Enregistrer le fichier à un emplacement**
Si les développeurs doivent enregistrer leurs fichiers en utilisant **Aspose.Cells Java pour Python** à un emplacement de stockage spécifique, ils peuvent simplement spécifier le nom du fichier (avec son chemin de stockage complet) et le format de fichier souhaité (en utilisant l'énumération **FileFormatType**) lors de l'appel de la méthode **save** de l'objet **Workbook**.

**Code Python**

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

Téléchargez **Enregistrement de fichier (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
