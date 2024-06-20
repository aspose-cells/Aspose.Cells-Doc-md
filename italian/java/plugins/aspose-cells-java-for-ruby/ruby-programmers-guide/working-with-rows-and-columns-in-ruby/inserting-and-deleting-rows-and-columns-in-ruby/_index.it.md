---
title: Inserimento ed eliminazione di righe e colonne in Ruby
type: docs
weight: 60
url: /it/java/inserting-and-deleting-rows-and-columns-in-ruby/
---

## **Aspose.Cells - Gestione delle righe/colonne**
### **Inserimento di una riga**
Inserire una riga in qualsiasi posizione chiamando il metodo insertRows della collezione Cells. Il metodo insertRows prende l'indice della riga in cui verrà inserita la nuova riga come primo argomento e il numero di righe da inserire come secondo argomento.

**Codice Ruby**

{{< highlight ruby >}}

 def insert_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Row.xls")

    puts "Insert Row Successfully."

end   

{{< /highlight >}}
### **Inserimento di Più Righe**
Per inserire più righe nel foglio di lavoro, chiamare il metodo insertRows della collezione Cells. Il metodo insertRows prende due parametri:

- Indice di riga, l'indice della riga da cui saranno inserite le nuove righe.
- Numero di righe, numero totale di righe che devono essere inserite.

**Codice Ruby**

{{< highlight ruby >}}

 def insert_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,10)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Multiple Rows.xls")

    puts "Insert Multiple Rows Successfully."

end

{{< /highlight >}}
### **Eliminazione di una riga**
Per eliminare una riga in qualsiasi posizione, chiamare il metodo deleteRows della collezione Cells. Il metodo DeleteRows prende due parametri:

- Indice riga, l'indice della riga da cui partiranno le eliminazioni.
- Numero di righe, numero totale di righe che devono essere eliminate.

**Codice Ruby**

{{< highlight ruby >}}

 def delete_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 3rd row from the worksheet

    worksheet.getCells().deleteRows(2,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Row.xls")

    puts "Delete Row Successfully."

end

{{< /highlight >}}
### **Eliminazione di Più Righe**
Per eliminare più righe da un foglio di lavoro, chiamare il metodo deleteRows della collezione Cells. Il metodo DeleteRows prende due parametri:

- Indice riga, l'indice della riga da cui partiranno le eliminazioni.
- Numero di righe, numero totale di righe che devono essere eliminate.

**Codice Ruby**

{{< highlight ruby >}}

 def delete_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 10 rows from the worksheet starting from 3rd row

    worksheet.getCells().deleteRows(2,10,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Multiple Rows.xls")

    puts "Delete Multiple Rows Successfully."

end 

{{< /highlight >}}
### **Inserimento di una colonna**
Gli sviluppatori possono anche inserire una colonna nel foglio di lavoro in qualsiasi posizione chiamando il metodo insertColumns della collezione Cells. Il metodo insertColumns prende due parametri:

- Indice della colonna, l'indice della colonna da cui verrà inserita la colonna
- Numero di colonne, numero totale di colonne che devono essere inserite

**Codice Ruby**

{{< highlight ruby >}}

 def insert_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a column into the worksheet at 2nd position

    worksheet.getCells().insertColumns(1,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Column.xls")

    puts "Insert Column Successfully."

end  

{{< /highlight >}}
### **Eliminare una colonna**
Per eliminare una colonna dal foglio di lavoro in qualsiasi posizione, chiamare il metodo deleteColumns della collezione Cells. Il metodo deleteColumns richiede i seguenti parametri:

- Indice della colonna, l'indice della colonna da cui verrà eliminata la colonna.
- Numero di colonne, numero totale di colonne che devono essere eliminate.
- Spostare celle, parametro booleano per indicare se spostare le celle a sinistra dopo l'eliminazione.

**Codice Ruby**

{{< highlight ruby >}}

 def delete_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting a column from the worksheet at 2nd position

    worksheet.getCells().deleteColumns(1,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Column.xls")

    puts "Delete Column Successfully."

end   

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Gestione righe/colonne (Aspose.Cells)** da uno qualsiasi dei siti di codice sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
