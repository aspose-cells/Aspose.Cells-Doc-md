---
title: Regolazione dell'altezza della riga e della larghezza della colonna in Python
type: docs
weight: 10
url: /it/java/adjusting-row-height-and-column-width-in-python/
keywords: create XLSX in Python, create XLS in Python, XLS python, XLSX python, row height python, column width python, Excel pytho
description: Usa Python Excel API per creare file Excel in Python. Regola l'altezza della riga e la larghezza della colonna in XLSX o XLS nelle tue applicazioni Python senza MS Office.
---
## **Fogli di calcolo Excel in Python - Regolazione dell'altezza della riga e della larghezza della colonna**
### **Impostazione dell'altezza della riga**
Con Aspose.Cells, è possibile impostare l'altezza di una singola riga in Python chiamando il metodo setRowHeight della raccolta Cells. Il metodo setRowHeight accetta i seguenti parametri:

- **Indice di riga**, l'indice della riga di cui stai modificando l'altezza.
- **Altezza della riga**, l'altezza della riga da applicare alla riga.

**Python Cod**

{{< highlight "python" >}}

 def set_row_height(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the height of the second row to 13

cells.setRowHeight(1, 13)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Row Height.xls")

print "Set Row Height Successfully." 

{{< /highlight >}}
### **Impostazione della larghezza della colonna**
Impostare la larghezza di una colonna chiamando il metodo setColumnWidth della raccolta Cells. Il metodo setColumnWidth accetta i seguenti parametri:

- **Indice di colonna**, l'indice della colonna di cui stai modificando la larghezza.
- **Larghezza della colonna**, la larghezza della colonna desiderata.

**Python Cod**

{{< highlight "python" >}}

 def set_column_width(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the width of the second column to 17.5

cells.setColumnWidth(1, 17.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Column Width.xls")

print "Set Column Width Successfully." 

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scaricamento**Regolazione dell'altezza della riga e della larghezza della colonna (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
