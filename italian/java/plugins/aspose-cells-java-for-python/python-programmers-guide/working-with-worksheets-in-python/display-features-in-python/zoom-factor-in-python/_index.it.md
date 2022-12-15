---
title: Fattore di zoom in Python
type: docs
weight: 80
url: /it/java/zoom-factor-in-python/
---
## **Aspose.Cells - Fattore di ingrandimento**
 Per impostare il fattore di zoom utilizzando**Aspose.Cells Giava for Python** , semplicemente invocare**Fattore di zoom** modulo.

**Codice Pitone**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Zoom factor set to 75% for sheet 1, please check the output document."

{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scarica**Fattore di zoom (Aspose.Cells)** da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
