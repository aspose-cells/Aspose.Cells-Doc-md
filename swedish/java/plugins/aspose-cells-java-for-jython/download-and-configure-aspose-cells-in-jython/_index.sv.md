---
title: Ladda ner och konfigurera Aspose.Cells i Jython
type: docs
weight: 10
url: /sv/java/download-and-configure-aspose-cells-in-jython/
---
## **Laddar ner**

**Ladda ner exempel från webbplatser för social kodning**

Följande versioner av löpande exempel finns att ladda ner på alla nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**Ladda ner komponenten Aspose.Cells for Java**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

## **Installerar**

- Placera den nedladdade Aspose.Cells for Java jar-filen i "lib"-katalogen.
- Ersätt "your-lib" med det nedladdade jar-filnamnet i filen _*init*_.py.

## **Använder sig av**

Du kan skapa HelloWorld-dokument med följande exempelkod:

{{< highlight "java" >}}

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
