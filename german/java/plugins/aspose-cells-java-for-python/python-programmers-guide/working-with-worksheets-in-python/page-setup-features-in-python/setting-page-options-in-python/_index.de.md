---
title: Seitenoptionen in Python einstellen
type: docs
weight: 10
url: /de/java/setting-page-options-in-python/
---

## **Aspose.Cells - Seitenoptionen einstellen**
### **Seitenausrichtung**
Um Seitenausrichtungseinstellungen unter Verwendung von **Aspose.Cells Java für Ruby** anzuwenden, rufen Sie einfach die Methode **page_orientation** des Moduls **pagesetup** auf.

**Python-Code**

{{< highlight java >}}

 def page_orientation(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook()

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

sheet = worksheets.get(sheet_index)

\# Setting the orientation to Portrait

page_setup = sheet.getPageSetup()

page_orientation_type = self.PageOrientationType

page_setup.setOrientation(page_orientation_type.PORTRAIT)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Page_Orientation.xls")

print "Set page orientation, please check the output file."


{{< /highlight >}}
### **Maßstab**
Um die Skalierung mit **Aspose.Cells Java for Python** anzuwenden, rufen Sie die Methode **scaling** des Moduls **pagesetup** auf.

**Python-Code**

{{< highlight python >}}

 def scaling(self):        

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

sheet = worksheets.get(sheet_index)

\# Setting the scaling factor to 100

page_setup = sheet.getPageSetup()

page_setup.setZoom(100)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Scaling.xls")

print "Set scaling, please check the output file."

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Seitenoptionen einstellen (Aspose.Cells)** von einer der unten genannten sozialen Code-Seiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
