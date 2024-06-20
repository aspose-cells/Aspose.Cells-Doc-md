---
title: Registerkarten in Python einblenden oder ausblenden
type: docs
weight: 30
url: /de/java/display-or-hide-tabs-in-python/
---

## **Aspose.Cells - Anzeigen und Ausblenden von Registerkarten**
### **Registerkarten ausblenden**
Rufen Sie zur Ausblendung von Registerkarten mit **Aspose.Cells Java für Ruby** das Modul **displayhidetabs** auf.

**Python-Code**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Sichtbarkeit von Registerkarten**
Machen Sie Registerkarten mit der Methode setSheetTabBarHidden(false) der Klasse Arbeitsmappe sichtbar.

**Python-Code**

{{< highlight python >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Hello World (Aspose.Cells)** von einer der unten genannten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
