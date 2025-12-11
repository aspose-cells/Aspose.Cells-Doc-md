---
title: Download and Configure Aspose.Cells in Jython
type: docs
weight: 10
url: /java/download-and-configure-aspose-cells-in-jython/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Downloading**

**Download Examples from social coding websites**

The following runnable example releases are available for download on the social coding sites listed below:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**Download Aspose.Cells for Java component**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

## **Installing**

- Place the downloaded Aspose.Cells for Java JAR file into the **lib** directory.  
- Replace `"your-lib"` with the downloaded JAR filename in the `__init__.py` file.

## **Using**

You can create a HelloWorld document using the following example code:

{{< highlight java >}}
from aspose-cells import Settings
from com.aspose.Cells import Document
from com.aspose.Cells import DocumentBuilder

class HelloWorld:
    def __init__(self):
        dataDir = Settings.dataDir + 'quickstart/'

        workbook = Workbook()

        sheet = workbook.getWorksheets().get(0)

        cell = sheet.getCells().get("A1")

        cell.setValue("Hello World!")

        file_format_type = FileFormatType

        workbook.save(dataDir + "HelloWorld.xls", file_format_type.EXCEL_97_TO_2003)

        print "Document has been saved, please check the output file."

if __name__ == '__main__':
    HelloWorld()
{{< /highlight >}}
