---
title: Tabs anzeigen oder ausblenden in Python
type: docs
weight: 30
url: /de/java/display-or-hide-tabs-in-python/
---
## **Aspose.Cells – Tabs ausblenden anzeigen**
### **Registerkarten ausblenden**
 Tabs ausblenden mit**Aspose.Cells Java für Rubin** , Anruf**Tabs ausblenden** Modul.

**Python Code**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Registerkarten sichtbar machen**
Machen Sie Registerkarten mit der setSheetTabBarHidden(false)-Methode der Workbook-Klasse sichtbar.

**Python Code**

{{< highlight "python" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Hello World (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
