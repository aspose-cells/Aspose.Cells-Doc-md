---
title: Impostazione delle opzioni della pagina in Python
type: docs
weight: 10
url: /it/java/setting-page-options-in-python/
---
## **Aspose.Cells - Impostazione Opzioni Pagina**
### **Orientamento della pagina**
 Per applicare le impostazioni di orientamento della pagina utilizzando**Aspose.Cells Java per Rubino** , chiamata**orientamento_pagina** metodo di**impostazione della pagina** modulo.

**Python Cod**

{{< highlight "java" >}}

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
### **Fattore di scala**
 Per applicare il ridimensionamento utilizzando**Aspose.Cells Java for Python** , chiamata**ridimensionamento** metodo di**impostazione della pagina** modulo.

**Python Cod**

{{< highlight "python" >}}

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
## **Scarica il codice in esecuzione**
 Scaricamento**Impostazione opzioni pagina (Aspose.Cells)** da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
