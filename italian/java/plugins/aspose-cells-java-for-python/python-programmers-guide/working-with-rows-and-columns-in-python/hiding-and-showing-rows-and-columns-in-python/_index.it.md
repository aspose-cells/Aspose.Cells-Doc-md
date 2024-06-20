---
title: Nascondere e mostrare righe e colonne in Python
type: docs
weight: 50
url: /it/java/hiding-and-showing-rows-and-columns-in-python/
description: Scopri come nascondere e mostrare righe e colonne tramite Aspose.Cells per l API di Python Via Java.
keywords: Come nascondere e mostrare righe e colonne in Python tramite Java, nascondere righe e colonne utilizzando Python tramite Java, mostrare righe e colonne tramite Python tramite Java. 
---

## **Aspose.Cells - Controllo della visibilità di righe e colonne**
### **Come nascondere righe e colonne**
Gli sviluppatori possono nascondere una riga o colonna chiamando rispettivamente i metodi HideRow e HideColumn della collezione Cells. Entrambi i metodi accettano l'indice di riga/colonna come parametro per nascondere la riga o colonna specifica.

**Codice Ruby**

{{< highlight ruby >}}

 def hide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Hiding the 3rd row of the worksheet

cells.hideRow(2)

\# Hiding the 2nd column of the worksheet

cells.hideColumn(1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Hide Rows And Columns.xls")

print "Hide Rows And Columns Successfully." 

{{< /highlight >}}
### **Come mostrare righe e colonne**
Gli sviluppatori possono mostrare qualsiasi riga o colonna nascosta chiamando rispettivamente i metodi UnhideRow e UnhideColumn della collezione Cells. Entrambi i metodi accettano due parametri:

- **Indice di riga o colonna** - l'indice di una riga o colonna che viene utilizzato per mostrare la riga o colonna specifica.
- **Altezza riga o larghezza colonna** - l'altezza della riga o la larghezza della colonna assegnata alla riga o alla colonna dopo che è stata mostrata.

**Codice Ruby**

{{< highlight ruby >}}

 def unhide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Unhiding the 3rd row and setting its height to 13.5

cells.unhideRow(2,13.5)

\# Unhiding the 2nd column and setting its width to 8.5

cells.unhideColumn(1,8.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Unhide Rows And Columns.xls")

print "Unhide Rows And Columns Successfully." 

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Controllo della visibilità delle righe e delle colonne (Aspose.Cells)** da uno dei siti di codifica sociali di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
