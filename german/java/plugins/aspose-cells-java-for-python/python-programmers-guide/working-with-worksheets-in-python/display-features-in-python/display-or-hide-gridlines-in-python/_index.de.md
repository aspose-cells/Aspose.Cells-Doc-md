---
title: Gitterlinien in Python anzeigen oder ausblenden
type: docs
weight: 10
url: /de/java/display-or-hide-gridlines-in-python/
description: Erfahren Sie, wie Sie Gitterlinien über Aspose.Cells for Python über Java API ein- oder ausblenden.
keywords: How to Display or Hide Gridlines in Python Via Java, Display or Hide Gridlines using Python Via Java, Python Show or Hide Gridlines. 
---
##  **Aspose.Cells – So zeigen Sie Gitterlinien an oder verbergen sie**
###  **So verbergen Sie Gitterlinien**
 Arbeitsblatt ausblenden mit**Aspose.Cells Java für Ruby**, rufen Sie **displayhidegridlines auf** Modul.

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
###  **So zeigen Sie Gitterlinien an**
Um Gitternetzlinien sichtbar zu machen, verwenden Sie die Methode setGridlinesVisible(true) der Worksheet-Klasse.

**Python Code**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
##  **Laden Sie Running Code herunter**
 Herunterladen**DisplayHideGridlines (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
