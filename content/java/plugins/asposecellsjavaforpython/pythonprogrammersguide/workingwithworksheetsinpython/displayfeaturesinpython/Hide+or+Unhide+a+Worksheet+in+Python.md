+++
title = "Hide or Unhide a Worksheet in Python" 
description = "" 
weight = 24769 
+++

Aspose.Cells for Java : Hide or Unhide a Worksheet in Python  

# Aspose.Cells for Java : Hide or Unhide a Worksheet in Python


## Aspose.Cells - Hide or Unhide a Worksheet

##### Hiding a Worksheet

To hide worksheet using Aspose.Cells Java for Ruby, call **hideunhideworksheet** module.

**Python Code**

workbook = self.Workbook(self.dataDir + "Book1.xls")#Accessing the first worksheet in the Excel fileworksheets = workbook.getWorksheets()worksheet = worksheets.get(0)#Hiding the first worksheet of the Excel fileworksheet.setVisible(True)#Saving the modified Excel file in default (that is Excel 2003) formatworkbook.save(self.dataDir + "output.xls")# Print messageprint "Worksheet 1 is now hidden, please check the output document."

##### Showing a Worksheet

Developers can make a worksheet visible by setting the*setVisible(**true**)*method of the**Worksheet**class.

**Python Code**

\# Displaying the worksheet of the Excel fileworksheet.setVisible(true)

## Download Running Code

Download **Hide or Unhide a Worksheet (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

