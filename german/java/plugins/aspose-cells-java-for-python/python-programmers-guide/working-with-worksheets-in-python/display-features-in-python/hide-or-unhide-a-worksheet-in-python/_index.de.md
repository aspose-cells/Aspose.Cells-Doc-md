---
title: Arbeitsblatt in Python ausblenden oder einblenden
type: docs
weight: 50
url: /de/java/hide-or-unhide-a-worksheet-in-python/
---

## **Aspose.Cells - Arbeitsblatt ausblenden oder einblenden**
### **Arbeitsblatt ausblenden**
Um ein Arbeitsblatt mit Aspose.Cells Java für Ruby auszublenden, rufen Sie das Modul **hideunhideworksheet** auf.

**Python-Code**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Hiding the first worksheet of the Excel file

worksheet.setVisible(True)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Ein Arbeitsblatt anzeigen**
Entwickler können ein Arbeitsblatt sichtbar machen, indem sie die Methode *setVisible(* *true* *)* der Klasse **Worksheet** setzen.

**Python-Code**

{{< highlight python >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Arbeitsblatt ausblenden oder einblenden (Aspose.Cells)** von einer der unten genannten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
