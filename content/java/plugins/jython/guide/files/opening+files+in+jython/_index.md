---
title : "Opening Files in Jython" 
description : "" 
weight : 20794 
toc : false
type: docs
url: /java/plugins/jython/guide/files/opening+files+in+jython/
---

# Aspose.Cells for Java : Opening Files in Jython


## Aspose.Cells - Opening Files

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import FileFormatTypefrom com.aspose.cells import LoadOptionsfrom java.io import FileInputStreamclass OpeningFiles:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithFiles/OpeningFiles/'                fileFormatType = FileFormatType        # 1. Opening from path        # Creatin an Workbook object with an Excel file path        workbook1 = Workbook(dataDir + "Book1.xls")        print "Workbook opened using path successfully.";                # 2 Opening workbook from stream                #Create a Stream object        fstream = FileInputStream(dataDir + "Book2.xls")        #Creating an Workbook object with the stream object        workbook2 = Workbook(fstream)        fstream.close()        print ("Workbook opened using stream successfully.");                # 3.        # Opening Microsoft Excel 97 Files        #Createing and EXCEL\_97\_TO\_2003 LoadOptions object        loadOptions1 = LoadOptions(fileFormatType.EXCEL\_97\_TO\_2003)        #Creating an Workbook object with excel 97 file path and the loadOptions object        workbook3 = Workbook(dataDir + "Book\_Excel97\_2003.xls", loadOptions1)        # Print message        print("Excel 97 Workbook opened successfully.");                # 4.        # Opening Microsoft Excel 2007 XLSX Files        #Createing and XLSX LoadOptions object        loadOptions2 = LoadOptions(fileFormatType.XLSX)        #Creating an Workbook object with 2007 xlsx file path and the loadOptions object        workbook4 = Workbook(dataDir + "Book\_Excel2007.xlsx", loadOptions2)        # Print message        print ("Excel 2007 Workbook opened successfully.")                        # 5.        # Opening SpreadsheetML Files        #Creating and EXCEL\_2003\_XML LoadOptions object        loadOptions3 = LoadOptions(fileFormatType.EXCEL\_2003\_XML)        #Creating an Workbook object with SpreadsheetML file path and the loadOptions object        workbook5 = Workbook(dataDir + "Book3.xml", loadOptions3)                # Print message        print ("SpreadSheetML format workbook has been opened successfully.");                # 6.        # Opening CSV Files        #Creating and CSV LoadOptions object        loadOptions4 = LoadOptions(fileFormatType.CSV)        #Creating an Workbook object with CSV file path and the loadOptions object        workbook6 = Workbook(dataDir + "Book\_CSV.csv", loadOptions4)        # Print message        print ("CSV format workbook has been opened successfully.")                        # 7.        # Opening Tab Delimited Files        # Creating and TAB\_DELIMITED LoadOptions object        loadOptions5 = LoadOptions(fileFormatType.TAB\_DELIMITED);        # Creating an Workbook object with Tab Delimited text file path and the loadOptions object        workbook7 = Workbook(dataDir + "Book1TabDelimited.txt", loadOptions5)        # Print message        print("<br />");        print ("Tab Delimited workbook has been opened successfully.");        # 8.        # Opening Encrypted Excel Files        # Creating and EXCEL\_97\_TO\_2003 LoadOptions object        loadOptions6 = LoadOptions(fileFormatType.EXCEL\_97\_TO\_2003)        # Setting the password for the encrypted Excel file        loadOptions6.setPassword("1234")        # Creating an Workbook object with file path and the loadOptions object        workbook8 = Workbook(dataDir + "encryptedBook.xls", loadOptions6)        # Print message        print("<br />");        print ("Encrypted workbook has been opened successfully.");                if \_\_name\_\_ == '\_\_main\_\_':            OpeningFiles()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithFiles/OpeningFiles.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/OpeningFiles.py)

