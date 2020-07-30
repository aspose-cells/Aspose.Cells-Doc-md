---
title : "Copying and Moving Worksheets in Python" 
description : "" 
weight : 24779 
toc : false
type: docs
url: /java/plugins/python/guide/worksheets/value/copying+and+moving+worksheets+in+python/
---

# Aspose.Cells for Java : Copying and Moving Worksheets in Python


## Aspose.Cells - Copying and Moving Worksheets

##### Copy Worksheets within a Workbook

To copy worksheet using **Aspose.Cells for Java in Ruby**, call **copy\_worksheet** method of **copyworksheets** module. Below you can see code example.

**Python Code**

{{< code lang="cs" >}}
def copy_worksheet(self):  

# Instantiating a Workbook object by excel file path
workbook = self.Workbook(self.dataDir + "Book1.xls")


# Create a Worksheets object with reference to the sheets of the Workbook.
sheets = workbook.getWorksheets()

# Copy data to a new sheet from an existing sheet within the Workbook.
sheets.addCopy("Sheet1")

# Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(self.dataDir + "Copy Worksheet.xls")

print "Copy worksheet, please check the output file."

h5. Move Worksheets within a Workbook


{color:#333333}To move worksheet using{color} {color:#333333}{*}Aspose.Cells for Java in Ruby{*}{color}{color:#333333}, call{color} {color:#333333}{*}move_worksheet{*}{color} {color:#333333}method of{color} {color:#333333}{*}copyworksheets{*}{color} {color:#333333}module. Below you can see code example.{color}

{code:language=python|title= Python Code }

def move_worksheet(self):

# Instantiating a Workbook object by excel file path
workbook = self.Workbook(self.dataDir + "Book1.xls")


# Get the first worksheet in the book.
sheet = workbook.getWorksheets().get(0)

# Move the first sheet to the third position in the workbook.
sheet.moveTo(2)

# Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(self.dataDir + "Move_Worksheet.xls")

print "Move worksheet, please check the output file."
{{< /code >}}

## Download Running Code

Download **Copying and Moving Worksheets (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

