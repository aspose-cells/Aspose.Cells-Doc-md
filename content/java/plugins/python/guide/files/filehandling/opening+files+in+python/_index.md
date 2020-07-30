---
title : "Opening Files in Python" 
description : "" 
weight : 24747 
toc : false
type: docs
url: /java/plugins/python/guide/files/filehandling/opening+files+in+python/
---

# Aspose.Cells for Java : Opening Files in Python


## Aspose.Cells - Opening Files in Python

To open a file using Aspose.Cells Java in Python, simply invoke the openfile() method of Document class and specify the second document to append at end.

**Python Code**

fileFormatType = self.FileFormatType# 1. Opening from path# Creatin an Workbook object with an Excel file pathworkbook1 = self.Workbook(self.dataDir + "Book1.xls")print "Workbook opened using path successfully.";# 2 Opening workbook from stream#Create a Stream objectfstream = self.FileInputStream(self.dataDir + "Book2.xls")#Creating an Workbook object with the stream objectworkbook2 = self.Workbook(fstream)fstream.close()print ("Workbook opened using stream successfully.");# 3.# Opening Microsoft Excel 97 Files#Createing and EXCEL\_97\_TO\_2003 LoadOptions objectloadOptions1 = self.LoadOptions(fileFormatType.EXCEL\_97\_TO\_2003)#Creating an Workbook object with excel 97 file path and the loadOptions objectworkbook3 = self.Workbook(self.dataDir + "Book\_Excel97\_2003.xls", loadOptions1)# Print messageprint("Excel 97 Workbook opened successfully.");# 4.# Opening Microsoft Excel 2007 XLSX Files#Createing and XLSX LoadOptions objectloadOptions2 = self.LoadOptions(fileFormatType.XLSX)#Creating an Workbook object with 2007 xlsx file path and the loadOptions objectworkbook4 = self.Workbook(self.dataDir + "Book\_Excel2007.xlsx", loadOptions2)# Print messageprint ("Excel 2007 Workbook opened successfully.")# 5.# Opening SpreadsheetML Files#Creating and EXCEL\_2003\_XML LoadOptions objectloadOptions3 = self.LoadOptions(fileFormatType.EXCEL\_2003\_XML)#Creating an Workbook object with SpreadsheetML file path and the loadOptions objectworkbook5 = self.Workbook(self.dataDir + "Book3.xml", loadOptions3)# Print messageprint ("SpreadSheetML format workbook has been opened successfully.");# 6.# Opening CSV Files#Creating and CSV LoadOptions objectloadOptions4 = self.LoadOptions(fileFormatType.CSV)#Creating an Workbook object with CSV file path and the loadOptions objectworkbook6 = self.Workbook(self.dataDir + "Book\_CSV.csv", loadOptions4)# Print messageprint ("CSV format workbook has been opened successfully.")# 7.# Opening Tab Delimited Files# Creating and TAB\_DELIMITED LoadOptions objectloadOptions5 = self.LoadOptions(fileFormatType.TAB\_DELIMITED);# Creating an Workbook object with Tab Delimited text file path and the loadOptions objectworkbook7 = self.Workbook(self.dataDir + "Book1TabDelimited.txt", loadOptions5)# Print messageprint("<br />");print ("Tab Delimited workbook has been opened successfully.");# 8.# Opening Encrypted Excel Files# Creating and EXCEL\_97\_TO\_2003 LoadOptions objectloadOptions6 = self.LoadOptions(fileFormatType.EXCEL\_97\_TO\_2003)# Setting the password for the encrypted Excel fileloadOptions6.setPassword("1234")# Creating an Workbook object with file path and the loadOptions objectworkbook8 = self.Workbook(self.dataDir + "encryptedBook.xls", loadOptions6)# Print messageprint("<br />");print ("Encrypted workbook has been opened successfully.");

## Download Running Code

Download **Opening File (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

