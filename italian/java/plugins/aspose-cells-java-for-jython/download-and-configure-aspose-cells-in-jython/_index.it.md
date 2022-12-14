---
title: Scarica e configura Aspose.Cells in Jython
type: docs
weight: 10
url: /it/java/download-and-configure-aspose-cells-in-jython/
---
## **Download**

**Scarica esempi da siti Web di social coding**

Le seguenti versioni di esempi in esecuzione sono disponibili per il download su tutti i siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**Scarica il componente Aspose.Cells for Java**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

## **Installazione**

- Posiziona il file jar Aspose.Cells for Java scaricato nella directory "lib".
- Sostituisci "your-lib" con il nome del file jar scaricato nel file _*init*_.py.

## **Usando**

Puoi creare un documento HelloWorld utilizzando il seguente codice di esempio:

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
