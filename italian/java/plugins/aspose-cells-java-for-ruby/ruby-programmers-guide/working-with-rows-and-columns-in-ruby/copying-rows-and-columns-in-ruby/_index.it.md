---
title: Copiare righe e colonne in Ruby
type: docs
weight: 30
url: /it/java/copying-rows-and-columns-in-ruby/
---
## **Aspose.Cells - Copia di righe e colonne**
### **Copia di righe**
Aspose.Cells fornisce il metodo copyRow della classe Cells. Questo metodo copia tutti i tipi di dati inclusi formule, valori, commenti, formati di cella, celle nascoste, immagini e altri oggetti di disegno dalla riga di origine alla riga di destinazione.

Il metodo copyRow accetta i seguenti parametri:

- l'oggetto sorgente Cells,
- l'indice della riga di origine e
- l'indice della riga di destinazione.

**Codice Rubino**

{{< highlight "ruby" >}}

 def copy_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Copy the second row with data, formattings, images and drawing objects

    # to the 12th row in the worksheet.

    worksheet.getCells().copyRow(worksheet.getCells(),1,11)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Rows.xls")

    puts "Copy Rows Successfully."

end

{{< /highlight >}}
### **Copia di colonne**
Aspose.Cells fornisce il metodo copyColumn della classe Cells, questo metodo copia tutti i tipi di dati, incluse formule - con riferimenti aggiornati - e valori, commenti, formati di celle, celle nascoste, immagini e altri oggetti di disegno dalla colonna di origine alla colonna di destinazione.

Il metodo copyColumn accetta i seguenti parametri:

- l'oggetto sorgente Cells,
- indice della colonna di origine e
- l'indice della colonna di destinazione.

**Codice Rubino**

{{< highlight "ruby" >}}

 def copia_colonne()

dati_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/dati/'



# Creazione di un'istanza di un oggetto cartella di lavoro in base al percorso del file excel

cartella di lavoro = Rjb::import('com.aspose.cells.Workbook').new

# Accesso al primo foglio di lavoro nel file Excel

foglio di lavoro = workbook.getWorksheets().get(0)

# Inserisci alcuni dati nelle righe di intestazione (A1: A4)

io = 0

 mentre io< 5

        worksheet.getCells().get(i, 0).setValue("Header Row #{i}")

        i +=1

    end

    # Put some detail data (A5:A999)

    i = 5

    while i < 1000

        worksheet.getCells().get(i, 0).setValue("Detail Row #{i}")

        i +=1

    end

    # Create another Workbook.

    workbook1 = Rjb::import('com.aspose.cells.Workbook').new

    # Get the first worksheet in the book.

    worksheet1 = workbook1.getWorksheets().get(0)

    # Copy the first column from the first worksheet of the first workbook into

    # the first worksheet of the second workbook.

    worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

    # Autofit the column.

    worksheet1.autoFitColumn(2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Columns.xls")

    puts "Copy Columns Successfully."

end

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scaricamento**Copia di righe e colonne (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
