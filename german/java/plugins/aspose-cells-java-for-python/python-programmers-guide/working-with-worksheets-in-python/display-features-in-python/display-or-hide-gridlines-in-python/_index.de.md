---
title: Gitternetzlinien anzeigen oder ausblenden in Python
type: docs
weight: 10
url: /de/java/display-or-hide-gridlines-in-python/
---
## **Aspose.Cells - Rasterlinien anzeigen/ausblenden**
### **Ausblenden von Gitternetzlinien**
 Arbeitsblatt ausblenden mit**Aspose.Cells Java für Rubin** , Anruf**Rasterlinien ausblenden** Modul.

**Python Code**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

# Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
### **Rasterlinien sichtbar machen**
Um Rasterlinien sichtbar zu machen, verwenden Sie die setGridlinesVisible(true)-Methode der Worksheet-Klasse.

**Python Code**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Rasterlinien anzeigenausblenden (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
