---
title: Excel to PDF Conversion in Jython
type: docs
weight: 50
url: /java/excel-to-pdf-conversion-in-jython/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Excel to PDF Conversion**
To convert documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

{{< highlight java >}}
from aspose-cells import Settings
from com.aspose.cells import Workbook
from com.aspose.cells import SaveFormat

class Excel2PdfConversion:
    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithFiles/Excel2PdfConversion/'

        saveFormat = SaveFormat
        workbook = Workbook(dataDir + "Book1.xls")
        # Save the document in PDF format
        workbook.save(dataDir + "OutBook1.pdf", saveFormat.PDF)
        # Print message
        print "\n Excel to PDF conversion performed successfully."

if __name__ == '__main__':
    Excel2PdfConversion()
{{< /highlight >}}

## **Download Runnable Code**
Download **Excel to PDF Conversion (Aspose.Cells)** from any of the below-mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/Excel2PdfConversion.py)
