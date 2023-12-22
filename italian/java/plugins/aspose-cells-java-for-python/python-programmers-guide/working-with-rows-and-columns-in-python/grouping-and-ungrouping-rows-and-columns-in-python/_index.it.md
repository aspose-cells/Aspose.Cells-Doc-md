---
title: Raggruppamento e separazione di righe e colonne in Python
type: docs
weight: 40
url: /it/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: Scopri come raggruppare e separare righe e colonne tramite Aspose.Cells for Python tramite Java API.
keywords: How to Group and Ungroup Rows and Columns in Python Via Java, Group Rows and Columns using Python Via Java, Python Via Java Ungroup Rows and Columns. 
---
##  **Gestione del raggruppamento e della separazione di righe e colonne in Aspose.Cells for Python via Java**
###  **Come raggruppare righe e colonne in Python**
È possibile raggruppare righe o colonne chiamando i metodi groupRows e groupColumns della collection Cells. Entrambi i metodi accettano i seguenti parametri:

- Indice della prima riga/colonna, la prima riga o colonna del gruppo.
- Indice dell'ultima riga/colonna, l'ultima riga o colonna del gruppo.
- È nascosto, un parametro booleano che specifica se nascondere o meno le righe/colonne dopo il raggruppamento.

**Python Cod**

{{< highlight "python" >}}

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
###  **Come separare righe e colonne utilizzando Python**
Separa righe o colonne raggruppate chiamando i metodi UngroupRows e UngroupColumns della raccolta Cells. Entrambi i metodi accettano gli stessi parametri:

- Indice della prima riga o colonna, la prima riga/colonna da separare.
- Indice dell'ultima riga o colonna, l'ultima riga/colonna da separare.

**Python Cod**

{{< highlight "python" >}}

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
##  **Scarica il codice in esecuzione**
 Scaricamento**Raggruppa e separa righe e colonne (Aspose.Cells)**da uno qualsiasi dei siti di social coding indicati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
