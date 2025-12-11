---  
title: Managing Document Properties in Jython  
type: docs  
weight: 60  
url: /java/managing-document-properties-in-jython/  
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Aspose.Cells - Managing Document Properties**  
To manage document properties using **Aspose.Cells Java for Jython**, see the example code below.  

**Jython Code**  

{{< highlight java >}}  

```java
from aspose-cells import Settings
from com.aspose.cells import Workbook

class ManagingDocumentProperties:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithFiles/ManagingDocumentProperties/'
        workbook = Workbook(dataDir + "Book1.xls")

        # Retrieve a list of all custom document properties of the Excel file
        customProperties = workbook.getWorksheets().getCustomDocumentProperties()

        # Access a custom document property by using the property index
        # customProperty1 = customProperties.get(3)

        # Access a custom document property by using the property name
        customProperty2 = customProperties.get("Owner")

        # Add a custom document property to the Excel file
        publisher = customProperties.add("Publisher", "Aspose")

        # Save the file
        workbook.save(dataDir + "Test_Workbook.xls")

        # Remove a custom document property
        customProperties.remove("Publisher")

        # Save the file
        workbook.save(dataDir + "Test_Workbook_RemovedProperty.xls")

        # Print message
        print "Excel file's custom properties accessed successfully."

if __name__ == '__main__':
    ManagingDocumentProperties()
```  

{{< /highlight >}}  

## **Download Running Code**  
Download **Managing Document Properties (Aspose.Cells)** from any of the below‑mentioned social coding sites:  

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ManagingDocumentProperties.py)
