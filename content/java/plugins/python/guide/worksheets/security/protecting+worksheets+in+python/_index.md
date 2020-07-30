---
title : "Protecting Worksheets in Python" 
description : "" 
weight : 24776 
toc : false
type: docs
url: /java/plugins/python/guide/worksheets/security/protecting+worksheets+in+python/
---

# Aspose.Cells for Java : Protecting Worksheets in Python


## Aspose.Cells - Protecting Worksheets

To protect worksheet using **Aspose.Cells Java for Python**, call **protect\_worksheet** method of **protection** module.

**Python Code**

#Instantiating a Excel object by excel file pathexcel = self.Workbook(self.dataDir + "Book1.xls")#Accessing the first worksheet in the Excel fileworksheets = excel.getWorksheets()worksheet = worksheets.get(0)protection = worksheet.getProtection()#The following 3 methods are only for Excel 2000 and earlier formatsprotection.setAllowEditingContent(False)protection.setAllowEditingObject(False)protection.setAllowEditingScenario(False)#Protects the first worksheet with a password "1234"protection.setPassword("1234")#Saving the modified Excel file in default formatexcel.save(self.dataDir + "output.xls")#Print Messageprint "Sheet protected successfully."

## Download Running Code

Download **Protecting Worksheets (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

