---
title: Hello World en Jython
type: docs
weight: 10
url: /fr/java/hello-world-in-jython/
---

## **Aspose.Cells - Hello World**
Pour ajouter des documents en utilisant **Aspose.Cells Java for Jython**. Vous pouvez voir ici le code d'exemple.

**Code Jython**

{{< highlight java >}}

 from asposewords import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import ImportFormatMode

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
## **Télécharger le code en cours d'exécution**
Téléchargez **Ajouter des documents (Aspose.Cells)** à partir de n'importe lequel des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/quickstart/HelloWorld.py)
