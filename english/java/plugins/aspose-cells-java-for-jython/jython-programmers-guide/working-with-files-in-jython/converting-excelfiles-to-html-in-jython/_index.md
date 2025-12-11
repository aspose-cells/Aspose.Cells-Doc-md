---
title: Converting Excel Files to HTML in Jython
type: docs
weight: 10
url: /java/converting-excelfiles-to-html-in-jython/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Converting Excel Files to HTML**
To convert documents using **Aspose.Cells for Java in Jython**. Here is an example.

**Jython Code**

{{< highlight java >}}
from aspose-cells import Settings
from com.aspose.cells import Workbook
from com.aspose.cells import SaveFormat


class ConvertingExcelFilesToHtml:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingExcelFilesToHtml/'

        saveFormat = SaveFormat
        workbook = Workbook(dataDir + "Book1.xls")

        # Save the document in HTML format
        workbook.save(dataDir + "OutBook1.html", saveFormat.HTML)

        # Print message
        print "\n Excel to HTML conversion performed successfully."

if __name__ == '__main__':
    ConvertingExcelFilesToHtml()
{{< /highlight >}}

## **Download Runnable Code**
Download **Converting Excel Files to HTML (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingExcelFilesToHtml.py)
