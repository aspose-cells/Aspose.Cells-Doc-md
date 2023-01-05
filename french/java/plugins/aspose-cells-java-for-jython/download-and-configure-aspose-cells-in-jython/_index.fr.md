---
title: Télécharger et configurer Aspose.Cells dans Jython
type: docs
weight: 10
url: /fr/java/download-and-configure-aspose-cells-in-jython/
---
## **Téléchargement**

**Télécharger des exemples à partir de sites Web de codage social**

Les versions suivantes des exemples d'exécution sont disponibles en téléchargement sur tous les sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**Télécharger le composant Aspose.Cells for Java**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

## **Installation**

- Placez le fichier jar Aspose.Cells for Java téléchargé dans le répertoire "lib".
- Remplacez "votre-lib" par le nom du fichier jar téléchargé dans le fichier _*init*_.py.

## **En utilisant**

Vous pouvez créer un document HelloWorld à l'aide de l'exemple de code suivant :

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
