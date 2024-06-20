---
title: Raggruppamento e sraggruppamento di righe e colonne in Ruby
type: docs
weight: 40
url: /it/java/grouping-and-ungrouping-rows-and-columns-in-ruby/
---

## **Aspose.Cells - Gestione del raggruppamento di righe e colonne**
### **Raggruppamento di righe e colonne**
È possibile raggruppare righe o colonne chiamando i metodi groupRows e groupColumns della collezione Cells. Entrambi i metodi accettano i seguenti parametri:

- Indice della prima riga/colonna, la prima riga o colonna nel gruppo.
- Indice dell'ultima riga/colonna, l'ultima riga o colonna nel gruppo.
- È nascosto, un parametro booleano che specifica se nascondere o meno righe/colonne dopo il raggruppamento.

**Codice Ruby**

{{< highlight ruby >}}

 def group_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Grouping first six rows (from 0 to 5) and making them hidden by passing true

    cells.groupRows(0,5,true)

    # Grouping first three columns (from 0 to 2) and making them hidden by passing true

    cells.groupColumns(0,2,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Group Rows And Columns.xls")

    puts "Group Rows And Columns Successfully."

end  

{{< /highlight >}}
### **Sganciare Righe e Colonne**
Sraggruppare righe o colonne raggruppate chiamando i metodi UngroupRows e UngroupColumns della collezione Cells. Entrambi i metodi accettano gli stessi parametri:

- Indice della prima riga o colonna, la prima riga/colonna da sraggruppare.
- Indice dell'ultima riga o colonna, l'ultima riga/colonna da sraggruppare.

**Codice Ruby**

{{< highlight ruby >}}

 def ungroup_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Group Rows And Columns.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Ungrouping first six rows (from 0 to 5)

    cells.ungroupRows(0,5)

    # Ungrouping first three columns (from 0 to 2)

    cells.ungroupColumns(0,2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Ungroup Rows And Columns.xls")

    puts "Ungroup Rows And Columns Successfully."

end

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica il **Raggruppamento & Sraggruppamento Righe & Colonne (Aspose.Cells)** da qualunque dei siti di codice sociale di seguito menzionati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
