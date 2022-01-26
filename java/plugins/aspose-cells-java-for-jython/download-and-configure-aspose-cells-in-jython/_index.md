---
title: Download and Configure Aspose.Cells in Jython
type: docs
weight: 10
url: /java/download-and-configure-aspose-cells-in-jython/
---

## **Downloading**

**Download Examples from social coding websites**

Following releases of running examples are available to download on all of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**Download Aspose.Cells for Java component**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

## **Installing**

- Place downloaded Aspose.Cells for Java jar file into "lib" directory.
- Replace "your-lib" with the downloaded jar filename in _*init*_.py file.

## **Using**

You can create HelloWorld document using following example code:

{{< highlight java >}}

 from aspose-cells  import Settings

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



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':

    HelloWorld()

{{< /highlight >}}
