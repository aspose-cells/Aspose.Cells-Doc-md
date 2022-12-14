---
title: Abriendo Archivos en Python
type: docs
weight: 10
url: /es/java/opening-files-in-python/
---
## **Aspose.Cells - Apertura de archivos en Python**
Para abrir un archivo usando Aspose.Cells Java en Python, simplemente invoque el método openfile() de la clase Document y especifique el segundo documento para agregarlo al final.

**Código Python**

{{< highlight "java" >}}

 fileFormatType = self.FileFormatType

\# 1. Opening from path

\# Creatin an Workbook object with an Excel file path

workbook1 = self.Workbook(self.dataDir + "Book1.xls")

print "Workbook opened using path successfully.";

\# 2 Opening workbook from stream

# Create a Stream object

fstream = self.FileInputStream(self.dataDir + "Book2.xls")

# Creating an Workbook object with the stream object

workbook2 = self.Workbook(fstream)

fstream.close()

print ("Workbook opened using stream successfully.");

\# 3.

\# Opening Microsoft Excel 97 Files

# Createing and EXCEL_97_TO_2003 LoadOptions object

loadOptions1 = self.LoadOptions(fileFormatType.EXCEL_97_TO_2003)

# Creating an Workbook object with excel 97 file path and the loadOptions object

workbook3 = self.Workbook(self.dataDir + "Book_Excel97_2003.xls", loadOptions1)

\# Print message

print("Excel 97 Workbook opened successfully.");

\# 4.

\# Opening Microsoft Excel 2007 XLSX Files

# Createing and XLSX LoadOptions object

loadOptions2 = self.LoadOptions(fileFormatType.XLSX)

# Creating an Workbook object with 2007 xlsx file path and the loadOptions object

workbook4 = self.Workbook(self.dataDir + "Book_Excel2007.xlsx", loadOptions2)

\# Print message

print ("Excel 2007 Workbook opened successfully.")


\# 5.

\# Opening SpreadsheetML Files

# Creating and EXCEL_2003_XML LoadOptions object

loadOptions3 = self.LoadOptions(fileFormatType.EXCEL_2003_XML)

# Creating an Workbook object with SpreadsheetML file path and the loadOptions object

workbook5 = self.Workbook(self.dataDir + "Book3.xml", loadOptions3)

\# Print message

print ("SpreadSheetML format workbook has been opened successfully.");

\# 6.

\# Opening CSV Files

# Creating and CSV LoadOptions object

loadOptions4 = self.LoadOptions(fileFormatType.CSV)

# Creating an Workbook object with CSV file path and the loadOptions object

workbook6 = self.Workbook(self.dataDir + "Book_CSV.csv", loadOptions4)

\# Print message

print ("CSV format workbook has been opened successfully.")


\# 7.

\# Opening Tab Delimited Files

\# Creating and TAB_DELIMITED LoadOptions object

loadOptions5 = self.LoadOptions(fileFormatType.TAB_DELIMITED);

\# Creating an Workbook object with Tab Delimited text file path and the loadOptions object

workbook7 = self.Workbook(self.dataDir + "Book1TabDelimited.txt", loadOptions5)

\# Print message

print("<br />");

print ("Tab Delimited workbook has been opened successfully.");



\# 8.

\# Opening Encrypted Excel Files

\# Creating and EXCEL_97_TO_2003 LoadOptions object

loadOptions6 = self.LoadOptions(fileFormatType.EXCEL_97_TO_2003)

\# Setting the password for the encrypted Excel file

loadOptions6.setPassword("1234")

\# Creating an Workbook object with file path and the loadOptions object

workbook8 = self.Workbook(self.dataDir + "encryptedBook.xls", loadOptions6)

\# Print message

print("<br />");

print ("Encrypted workbook has been opened successfully.");

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Archivo de apertura (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
