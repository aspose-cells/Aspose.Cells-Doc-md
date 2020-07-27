+++
title = "Zoom Factor in Python" 
description = "" 
weight = 24772 
+++

Aspose.Cells for Java : Zoom Factor in Python  

# Aspose.Cells for Java : Zoom Factor in Python


## Aspose.Cells - Zoom Factor

To set Zoom Factor using **Aspose.Cells Java for Python**, simply invoke **ZoomFactor** module.

**Python Code**

workbook = self.Workbook(self.dataDir + "Book1.xls")#Accessing the first worksheet in the Excel fileworksheets = workbook.getWorksheets()worksheet = worksheets.get(0)#Setting the zoom factor of the worksheet to 75worksheet.setZoom(75)#Saving the modified Excel file in default formatworkbook.save(self.dataDir + "output.xls")# Print messageprint "Zoom factor set to 75% for sheet 1, please check the output document."

## Download Running Code

Download **Zoom Factor (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

