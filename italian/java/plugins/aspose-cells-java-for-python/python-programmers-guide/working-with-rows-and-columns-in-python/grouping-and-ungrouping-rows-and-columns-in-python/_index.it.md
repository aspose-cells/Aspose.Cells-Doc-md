---
title: Raggruppamento e sraggruppamento di righe e colonne in Python
type: docs
weight: 40
url: /it/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: Scopri come raggruppare e sraggruppare righe e colonne tramite Aspose.Cells per l API di Python Via Java.
keywords: Come raggruppare e sraggruppare righe e colonne in Python Via Java, raggruppare righe e colonne con Python Via Java, sraggruppare righe e colonne con Python Via Java. 
---

## **Gestione del raggruppamento e dello sraggruppamento delle righe e delle colonne in Aspose.Cells per Python via Java**
### **Come raggruppare righe e colonne in Python**
È possibile raggruppare righe o colonne chiamando i metodi groupRows e groupColumns della collezione Cells. Entrambi i metodi accettano i seguenti parametri:

- Indice della prima riga/colonna, la prima riga o colonna nel gruppo.
- Indice dell'ultima riga/colonna, l'ultima riga o colonna nel gruppo.
- È nascosto, un parametro booleano che specifica se nascondere o meno righe/colonne dopo il raggruppamento.

**Codice Python**

{{< highlight python >}}

 def group_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Grouping first six rows (from 0 to 5) and making them hidden by passing true

cells.groupRows(0,5,True)

\# Grouping first three columns (from 0 to 2) and making them hidden by passing true

cells.groupColumns(0,2,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Group Rows And Columns.xls")

print "Group Rows And Columns Successfully." 

{{< /highlight >}}
### **Come sraggruppare righe e colonne utilizzando Python**
Sraggruppare righe o colonne raggruppate chiamando i metodi UngroupRows e UngroupColumns della collezione Cells. Entrambi i metodi accettano gli stessi parametri:

- Indice della prima riga o colonna, la prima riga/colonna da sraggruppare.
- Indice dell'ultima riga o colonna, l'ultima riga/colonna da sraggruppare.

**Codice Python**

{{< highlight python >}}

 def ungroup_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Group Rows And Columns.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Ungrouping first six rows (from 0 to 5)

cells.ungroupRows(0,5)

\# Ungrouping first three columns (from 0 to 2)

cells.ungroupColumns(0,2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Ungroup Rows And Columns.xls")

print "Ungroup Rows And Columns Successfully." 

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica il **Raggruppamento & Sraggruppamento Righe & Colonne (Aspose.Cells)** da qualunque dei siti di codice sociale di seguito menzionati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
