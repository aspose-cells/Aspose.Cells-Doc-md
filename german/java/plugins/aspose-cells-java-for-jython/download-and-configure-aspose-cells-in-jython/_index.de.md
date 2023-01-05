---
title: Laden Sie Aspose.Cells in Jython herunter und konfigurieren Sie es
type: docs
weight: 10
url: /de/java/download-and-configure-aspose-cells-in-jython/
---
## **wird heruntergeladen**

**Laden Sie Beispiele von Social-Coding-Websites herunter**

Die folgenden Versionen von Laufbeispielen stehen auf allen unten genannten Social-Coding-Sites zum Download zur Verfügung:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**Laden Sie die Komponente Aspose.Cells for Java herunter**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

## **Installieren**

- Platzieren Sie die heruntergeladene JAR-Datei Aspose.Cells for Java im Verzeichnis „lib“.
- Ersetzen Sie „your-lib“ durch den heruntergeladenen JAR-Dateinamen in der Datei _*init*_.py.

## **Verwenden**

Sie können ein HelloWorld-Dokument mit folgendem Beispielcode erstellen:

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
