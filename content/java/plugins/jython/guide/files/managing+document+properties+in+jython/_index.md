---
title : "Managing Document Properties in Jython" 
description : "" 
weight : 20793 
toc : false
type: docs
url: /java/plugins/jython/guide/files/managing+document+properties+in+jython/
---

# Aspose.Cells for Java : Managing Document Properties in Jython


## Aspose.Cells - Managing Document Properties

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookclass ManagingDocumentProperties:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithFiles/ManagingDocumentProperties/'        workbook = Workbook(dataDir + "Book1.xls")        #Retrieve a list of all custom document properties of the Excel file        customProperties = workbook.getWorksheets().getCustomDocumentProperties()        #Accessing a custom document property by using the property index        #customProperty1 = customProperties.get(3)        #Accessing a custom document property by using the property name        customProperty2 = customProperties.get("Owner")        #Adding a custom document property to the Excel file        publisher = customProperties.add("Publisher", "Aspose")        #Save the file        workbook.save(dataDir + "Test\_Workbook.xls")        #Removing a custom document property        customProperties.remove("Publisher")        #Save the file        workbook.save(dataDir + "Test\_Workbook\_RemovedProperty.xls")        # Print message        print "Excel file's custom properties accessed successfully." if \_\_name\_\_ == '\_\_main\_\_':            ManagingDocumentProperties()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithFiles/ManagingDocumentProperties.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ManagingDocumentProperties.py)

