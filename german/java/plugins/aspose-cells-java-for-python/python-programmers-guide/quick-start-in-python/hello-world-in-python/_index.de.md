---
title: Hallo Welt in Python
type: docs
weight: 10
url: /de/java/hello-world-in-python/
---

## **Aspose.Cells - Hello World**
Hallo Welt mit Aspose.Cells Java in Python, rufen Sie einfach die Methode HelloWorld() der Dokumentenklasse auf und geben Sie das zweite Dokument an, das am Ende angehängt werden soll.

**Python-Code**

{{< highlight java >}}

 workbook = self.Workbook()

sheet = workbook.getWorksheets().get(0)

cell = sheet.getCells().get("A1")

cell.setValue("Hello World!")

file_format_type = self.FileFormatType

workbook.save(self.dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )

print "Document has been saved, please check the output file.";

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Hello World (Aspose.Cells)** von einer der unten genannten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
