---
title: Ausblenden oder Einblenden eines Arbeitsblatts in Python
type: docs
weight: 50
url: /de/java/hide-or-unhide-a-worksheet-in-python/
---
## **Aspose.Cells – Ausblenden oder Einblenden eines Arbeitsblatts**
### **Ausblenden eines Arbeitsblatts**
 Um das Arbeitsblatt mit Aspose.Cells Java für Ruby auszublenden, rufen Sie an**verbergenarbeitsblatt einblenden** Modul.

**Python Code**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the first worksheet of the Excel file

worksheet.setVisible(True)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Anzeigen eines Arbeitsblatts**
Entwickler können ein Arbeitsblatt sichtbar machen, indem sie das festlegen*setVisible(* *wahr* *)*Methode der**Arbeitsblatt**Klasse.

**Python Code**

{{< highlight "python" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Ein Arbeitsblatt ein- oder ausblenden (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
