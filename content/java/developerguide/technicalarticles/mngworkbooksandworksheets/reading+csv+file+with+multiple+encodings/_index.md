---
title : "Reading CSV File with Multiple Encodings" 
description : "" 
weight : 16428 
toc : false
type: docs
url: /java/developerguide/technicalarticles/mngworkbooksandworksheets/reading+csv+file+with+multiple+encodings/
---

# Aspose.Cells for Java : Reading CSV File with Multiple Encodings


Sometime, your CSV file contains multiple Encodings (Unicode, ANSI, UTF8, UTF7 etc). Aspose.Cells allows you to load such CSV files and converting them into other formats, for example PDF or XLSX.

Aspose.Cells provides the `TxtLoadOptions.setMultiEncoded()` method, which you need to set to **true** to load your CSV file with multiple encodings properly.

The following screenshot shows a sample CSV file which contains two lines. The first line is in **ANSI** encoding and the second line is in **Unicode** encoding

**Input file**  
![image](https://docs2.aspose.com/cells/java/attachments/5276653/5473048.png)

The following screenshot shows the XLSX file converted from the above CSV file without setting the `TxtLoadOptions.setMultiEncoded()` method to true. As you can see, the Unicode text was not converted properly.

**Output file 1: no accommodation made for multiple encoding**  
![image](https://docs2.aspose.com/cells/java/attachments/5276653/5473049.png)

The following screenshot shows the XSLX file converted from the above CSV file after setting the `TxtLoadOptions.setMultiEncoded()` method to true. As you can see, the Unicode text is now converted properly.

**Output file 2: IsMultiEncoded is set to true**  
![image](https://docs2.aspose.com/cells/java/attachments/5276653/5473059.png)

Below is the sample code that converts the above CSV file into XLSX format properly.

**Java**

String filePath = "F:\\\\Downloads\\\\MutliEncoded.csv";//Set Multi Encoded Property to TrueTxtLoadOptions options = new TxtLoadOptions();options.setMultiEncoded(true);//Load the CSV file into WorkbookWorkbook workbook = new Workbook(filePath, options);//Save it in XLSX formatworkbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

