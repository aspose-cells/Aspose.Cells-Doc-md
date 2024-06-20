---
title: Inserimento e cancellazione di righe e colonne in Python
type: docs
weight: 60
url: /it/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: "crea XLSX in Python, crea XLS in Python, XLS python, XLSX python, XLT python, XLTX python, inserisci riga python, inserisci colonna python, Excel python"
description: Usa Python Excel API per creare fogli Excel in Python. Inserisci o elimina righe da XLSX o XLS nelle tue applicazioni Python senza MS Office.
---

## **Crea fogli Excel in Python - Gestione Righe/Colonne**
### **Inserimento di una riga**
Inserisci una riga in qualsiasi posizione chiamando il metodo insertRows della collezione Cells. Il metodo insertRows prende l'indice della riga in cui verrà inserita la nuova riga come primo argomento e il numero di righe da inserire come secondo argomento. Di seguito sono riportati i passaggi:

- Carica il workbook XLS o XLSX
- Accedi al foglio di lavoro
- Inserisci la riga
- Salvare come cartella di lavoro XLS o XLSX

**Codice Python**

{{< highlight python >}}

 def insert_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Row.xls")

print "Insert Row Successfully." 

{{< /highlight >}}
### **Inserimento di Più Righe**
Per inserire più righe nel foglio di lavoro, chiamare il metodo insertRows della collezione Cells. Il metodo insertRows prende due parametri:

- Indice di riga, l'indice della riga da cui saranno inserite le nuove righe.
- Numero di righe, numero totale di righe che devono essere inserite.

**Codice Python**

{{< highlight python >}}

 def insert_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,10)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Multiple Rows.xls")

print "Insert Multiple Rows Successfully." 


{{< /highlight >}}
### **Eliminazione di una riga**
Per eliminare una riga in qualsiasi posizione, chiamare il metodo deleteRows della collezione Cells. Il metodo DeleteRows prende due parametri:

- Indice riga, l'indice della riga da cui partiranno le eliminazioni.
- Numero di righe, numero totale di righe che devono essere eliminate.

**Codice Python**

{{< highlight python >}}

 def delete_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 3rd row from the worksheet

worksheet.getCells().deleteRows(2,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Row.xls")

print "Delete Row Successfully." 

{{< /highlight >}}
### **Eliminazione di Più Righe**
Per eliminare più righe da un foglio di lavoro, chiamare il metodo deleteRows della collezione Cells. Il metodo DeleteRows prende due parametri:

- Indice riga, l'indice della riga da cui partiranno le eliminazioni.
- Numero di righe, numero totale di righe che devono essere eliminate.

**Codice Python**

{{< highlight python >}}

 def delete_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 10 rows from the worksheet starting from 3rd row

worksheet.getCells().deleteRows(2,10,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Multiple Rows.xls")

print "Delete Multiple Rows Successfully." 


{{< /highlight >}}
### **Inserimento di una colonna**
Gli sviluppatori possono anche inserire una colonna nel foglio di lavoro in qualsiasi posizione chiamando il metodo insertColumns della collezione Cells. Il metodo insertColumns prende due parametri:

- Indice della colonna, l'indice della colonna da cui verrà inserita la colonna
- Numero di colonne, numero totale di colonne che devono essere inserite

**Codice Python**

{{< highlight python >}}

 def insert_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a column into the worksheet at 2nd position

worksheet.getCells().insertColumns(1,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Column.xls")

print "Insert Column Successfully." 


{{< /highlight >}}
### **Eliminare una colonna**
Per eliminare una colonna dal foglio di lavoro in qualsiasi posizione, chiamare il metodo deleteColumns della collezione Cells. Il metodo deleteColumns richiede i seguenti parametri:

- Indice della colonna, l'indice della colonna da cui verrà eliminata la colonna.
- Numero di colonne, numero totale di colonne che devono essere eliminate.
- Spostare celle, parametro booleano per indicare se spostare le celle a sinistra dopo l'eliminazione.

**Codice Python**

{{< highlight python >}}

 def delete_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting a column from the worksheet at 2nd position

worksheet.getCells().deleteColumns(1,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Column.xls")

print "Delete Column Successfully." 


{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Gestione righe/colonne (Aspose.Cells)** da uno qualsiasi dei siti di codice sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
