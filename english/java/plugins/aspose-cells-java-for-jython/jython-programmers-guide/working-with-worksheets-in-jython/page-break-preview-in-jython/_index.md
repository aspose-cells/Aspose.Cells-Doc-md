---  
title: Page Break Preview in Jython  
type: docs  
weight: 90  
url: /java/page-break-preview-in-jython/  
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Aspose.Cells - Page Break Preview**  
This example shows how to append documents using **Aspose.Cells for Java with Jython**. Here you can see the sample code.  

**Jython Code**  

{{< highlight java >}}  

```python
from aspose-cells import Settings
from com.aspose.cells import Workbook

class PageBreakPreview:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithWorksheets/PageBreakPreview/'

        workbook = Workbook(dataDir + "Book1.xls")

        # Adding a new worksheet to the Workbook object
        worksheets = workbook.getWorksheets()
        worksheet = worksheets.get(0)

        # Displaying the worksheet in page‑break preview
        worksheet.setPageBreakPreview(True)

        # Saving the modified Excel file in the default format
        workbook.save(dataDir + "output.xls")

        # Print message
        print "Page break preview is enabled for sheet 1, please check the output document."
        
if __name__ == '__main__':
    PageBreakPreview()
```  

{{< /highlight >}}  

## **Download Running Code**  
Download **Append Documents (Aspose.Cells)** from any of the below‑mentioned social‑coding sites:  

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/PageBreakPreview.py)
