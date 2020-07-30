---
title : "Managing Document Properties in Python" 
description : "" 
weight : 24755 
toc : false
type: docs
url: /java/plugins/python/guide/files/utility/managing+document+properties+in+python/
---

# Aspose.Cells for Java : Managing Document Properties in Python


## Aspose.Cells - Managing Document Properties

Developers can make use of the**Index**or**Name**of the property to get a specific property from a **custom\_properties**collection as demonstrated below in the example.

**Python Code**

workbook = self.Workbook(self.dataDir + "Book1.xls")#Retrieve a list of all custom document properties of the Excel filecustomProperties = workbook.getWorksheets().getCustomDocumentProperties()#Accessing a custom document property by using the property index#customProperty1 = customProperties.get(3)#Accessing a custom document property by using the property namecustomProperty2 = customProperties.get("Owner")#Adding a custom document property to the Excel filepublisher = customProperties.add("Publisher", "Aspose")#Save the fileworkbook.save(self.dataDir + "Test\_Workbook.xls")#Removing a custom document propertycustomProperties.remove("Publisher")#Save the fileworkbook.save(self.dataDir + "Test\_Workbook\_RemovedProperty.xls")# Print messageprint "Excel file's custom properties accessed successfully."

## Download Running Code

Download **Hello World (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

