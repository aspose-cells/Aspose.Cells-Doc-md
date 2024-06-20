---
title: Aspose.Cells in Jython herunterladen und konfigurieren
type: docs
weight: 10
url: /de/java/download-and-configure-aspose-cells-in-jython/
---

## **Herunterladen**

**Beispielsdownloads von Social-Coding-Websites**

Die folgenden Versionen von laufenden Beispielen sind zum Download auf allen unten genannten Social-Coding-Sites verfügbar:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**Download Aspose.Cells for Java-Komponente**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

## **Installation**

- Platziere die heruntergeladene Aspose.Cells for Java-JAR-Datei im "lib"-Verzeichnis.
- Ersetze "your-lib" durch den heruntergeladenen JAR-Dateinamen in der _*init*_.py-Datei.

## **Verwendung**

Du kannst das HelloWorld-Dokument mit folgendem Beispielcode erstellen:

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
