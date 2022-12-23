---
title: Copia di righe e colonne in Jython
type: docs
weight: 30
url: /it/java/copying-rows-and-columns-in-jython/
---
## **Aspose.Cells - Copia di righe e colonne**
 Per aggiungere documenti utilizzando**Aspose.Cells Java per Jython**. Qui puoi vedere il codice di esempio.

**Codice Jython**

{{< highlight "java" >}}

 dalle impostazioni di importazione delle celle aspose

da com.aspose.cells importa cartella di lavoro

classe RowsAndColumns:

 def__dentro__(se stesso):



 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'



 # Copia di righe

 self.copy_rows()

 # Copia di colonne

 self.copia_colonne()



 def copia_righe(dataDir):

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

 # Creazione di un'istanza di un oggetto cartella di lavoro in base al percorso del file excel

 cartella di lavoro = Cartella di lavoro(dataDir + 'Libro1.xls')

 Accesso al primo foglio di lavoro nel file Excel

 foglio di lavoro = workbook.getWorksheets().get(0)

 # Copia la seconda riga con dati, formattazioni, immagini e oggetti di disegno

 # alla dodicesima riga del foglio di lavoro.

 foglio di lavoro.getCells().copyRow(foglio di lavoro.getCells(),1,11)

 # Salvataggio del file Excel modificato nel formato predefinito (ovvero Excel 2003).

 workbook.save(dataDir + "Copy Rows.xls")

 print "Copia le righe con successo."



 def copia_colonne(dataDir):

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

 # Creazione di un'istanza di un oggetto cartella di lavoro in base al percorso del file excel

 cartella di lavoro = cartella di lavoro()

 Accesso al primo foglio di lavoro nel file Excel

 foglio di lavoro = workbook.getWorksheets().get(0)

 # Inserisci alcuni dati nelle righe di intestazione (A1: A4)

 io = 0

 mentre io< 5:

            worksheet.getCells().get(i, 0).setValue("Header Row #i")






        # Put some detail data (A5:A999)

        i = 5

        while i < 1000:

            worksheet.getCells().get(i, 0).setValue("Detail Row #i")



        # Create another Workbook.

        workbook1 = Workbook()

        # Get the first worksheet in the book.

        worksheet1 = workbook1.getWorksheets().get(0)

        # Copy the first column from the first worksheet of the first workbook into

        # the first worksheet of the second workbook.

        worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

        # Autofit the column.

        worksheet1.autoFitColumn(2)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Copy Columns.xls")

        print "Copy Columns Successfully." 




if __name__ == '__main__':        

    RowsAndColumns()

{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scaricamento**Aggiungi documenti (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
