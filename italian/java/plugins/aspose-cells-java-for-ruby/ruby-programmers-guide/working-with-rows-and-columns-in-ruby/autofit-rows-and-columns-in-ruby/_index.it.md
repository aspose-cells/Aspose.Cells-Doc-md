---
title: Adatta automaticamente righe e colonne in Ruby
type: docs
weight: 20
url: /it/java/autofit-rows-and-columns-in-ruby/
---
## **Aspose.Cells - Adatta automaticamente righe e colonne**
### **Riga di adattamento automatico**
L'approccio più diretto al ridimensionamento automatico della larghezza e dell'altezza di una riga consiste nel chiamare il metodo autoFitRow della classe Worksheet. Il metodo autoFitRow accetta un indice di riga (della riga da ridimensionare) come parametro.

**Codice Rubino**

{{< highlight "ruby" >}}

 def autofit_row()

        data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



        # Instantiating a Workbook object by excel file path

        workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        # Auto-fitting the 3rd row of the worksheet

        worksheet.autoFitRow(2)

        # Auto-fitting the 3rd row of the worksheet based on the contents in a range of

        # cells (from 1st to 9th column) within the row

        #worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(data_dir + "Autofit Row.xls")

        puts "Autofit Row Successfully."

    end

{{< /highlight >}}
### **Colonna Adatta automaticamente**
Il modo più semplice per ridimensionare automaticamente la larghezza e l'altezza di una colonna consiste nel chiamare il metodo autoFitColumn della classe Worksheet. Il metodo autoFitColumn accetta l'indice di colonna (della colonna che sta per essere ridimensionata) come parametro.

**Codice Rubino**

{{< highlight "ruby" >}}

 def autofit_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Auto-fitting the 4th column of the worksheet

    worksheet.autoFitColumn(3)

    # Auto-fitting the 4th column of the worksheet based on the contents in a range of

    # cells (from 1st to 9th row) within the column

    #worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Autofit Column.xls")

    puts "Autofit Column Successfully."

end

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scaricamento**Adatta automaticamente righe e colonne (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
