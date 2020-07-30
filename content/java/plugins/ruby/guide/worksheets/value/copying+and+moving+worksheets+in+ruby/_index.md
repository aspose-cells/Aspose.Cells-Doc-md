---
title : "Copying and Moving Worksheets in Ruby" 
description : "" 
weight : 24728 
toc : false
type: docs
url: /java/plugins/ruby/guide/worksheets/value/copying+and+moving+worksheets+in+ruby/
---

# Aspose.Cells for Java : Copying and Moving Worksheets in Ruby


## Aspose.Cells - Copying and Moving Worksheets

##### Copy Worksheets within a Workbook

To copy worksheet using **Aspose.Cells for Java in Ruby**, call **copy\_worksheet** method of **copyworksheets** module. Below you can see code example.

**Ruby Code**

{{< code lang="cs" >}}
def copy_worksheet(workbook)
    # Create a Worksheets object with reference to the sheets of the Workbook.
    sheets = workbook.getWorksheets()

    # Copy data to a new sheet from an existing sheet within the Workbook.
    sheets.addCopy("Sheet1")

    # Saving the modified Excel file in default (that is Excel 2003) format
    workbook.save(@data_dir + "Copy Worksheet.xls")

    puts "Copy worksheet, please check the output file."
end 
{{< /code >}}

##### Move Worksheets within a Workbook

To move worksheet using **Aspose.Cells for Java in Ruby**, call **move\_worksheet** method of **copyworksheets** module. Below you can see code example.

**Ruby Code**

{{< code lang="cs" >}}
def move_worksheet(workbook)
    # Get the first worksheet in the book.
    sheet = workbook.getWorksheets().get(0)

    # Move the first sheet to the third position in the workbook.
    sheet.moveTo(2)

    # Saving the modified Excel file in default (that is Excel 2003) format
    workbook.save(@data_dir + "Move Worksheet.xls")

    puts "Move worksheet, please check the output file."
end 
{{< /code >}}

## Download Running Code

Download **Copying and Moving Worksheets (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)

