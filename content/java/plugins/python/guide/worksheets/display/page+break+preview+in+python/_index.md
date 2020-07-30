---
title : "Page Break Preview in Python" 
description : "" 
weight : 24770 
toc : false
type: docs
url: /java/plugins/python/guide/worksheets/display/page+break+preview+in+python/
---

# Aspose.Cells for Java : Page Break Preview in Python


## Aspose.Cells - Hello World

To set worksheet to page break preview using **Aspose.Cells Java for Python**, simply invoke **PageBreakPreview** module.

**Python Code**

workbook = self.Workbook(self.dataDir + "Book1.xls")#Adding a new worksheet to the Workbook objectworksheets = workbook.getWorksheets()worksheet = worksheets.get(0)#Displaying the worksheet in page break previewworksheet.setPageBreakPreview(True)#Saving the modified Excel file in default formatworkbook.save(self.dataDir + "output.xls")# Print messageprint "Page break preview is enabled for sheet 1, please check the output document." 

## Download Running Code

Download **Page Break Preview (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

