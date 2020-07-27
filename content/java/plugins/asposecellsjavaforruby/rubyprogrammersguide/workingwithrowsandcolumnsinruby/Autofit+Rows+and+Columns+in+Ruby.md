+++
title = "Autofit Rows and Columns in Ruby" 
description = "" 
weight = 20732 
+++

Aspose.Cells for Java : Autofit Rows and Columns in Ruby  

# Aspose.Cells for Java : Autofit Rows and Columns in Ruby


## Aspose.Cells - Autofit Rows and Columns

##### Autofit Row

The most straight-forward approach to auto-sizing the width and height of a row is to call the`Worksheet`class'`autoFitRow`method. The`autoFitRow`method takes a row index (of the row to be resized) as a parameter.

**Ruby Code**

{{< code lang="cs" >}}
def autofit_row()
        data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
        
        # Instantiating a Workbook object by excel file path
        workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file
        worksheet = workbook.getWorksheets().get(0)

        # Auto-fitting the 3rd row of the worksheet
        worksheet.autoFitRow(2)

        # Auto-fitting the 3rd row of the worksheet based on the contents in a range of
        # cells (from 1st to 9th column) within the row
        #worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

        # Saving the modified Excel file in default (that is Excel 2003) format
        workbook.save(data_dir + "Autofit Row.xls")

        puts "Autofit Row Successfully."
    end
{{< /code >}}

##### Autofit Column

The easiest way to auto-size the width and height of a column is to call the`Worksheet`class'`autoFitColumn`method. The`autoFitColumn`method takes the column index (of the column about to be resized) as a parameter.

**Ruby Code**

{{< code lang="cs" >}}
def autofit_column()
    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
    
    # Instantiating a Workbook object by excel file path
    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file
    worksheet = workbook.getWorksheets().get(0)

    # Auto-fitting the 4th column of the worksheet
    worksheet.autoFitColumn(3)

    # Auto-fitting the 4th column of the worksheet based on the contents in a range of
    # cells (from 1st to 9th row) within the column
    #worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

    # Saving the modified Excel file in default (that is Excel 2003) format
    workbook.save(data_dir + "Autofit Column.xls")

    puts "Autofit Column Successfully."
end
{{< /code >}}

## Download Running Code

Download **Autofit Rows and Columns (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)

