---
title: Autoajustar filas y columnas en Ruby
type: docs
weight: 20
url: /es/java/autofit-rows-and-columns-in-ruby/
---
## **Aspose.Cells - Autoajustar filas y columnas**
### **Autoajustar fila**
El enfoque más sencillo para cambiar automáticamente el tamaño del ancho y el alto de una fila es llamar al método autoFitRow de la clase Worksheet. El método autoFitRow toma un índice de fila (de la fila a redimensionar) como parámetro.

**código rubí**

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
### **Columna de ajuste automático**
La forma más fácil de cambiar automáticamente el tamaño del ancho y el alto de una columna es llamar al método autoFitColumn de la clase Worksheet. El método autoFitColumn toma el índice de la columna (de la columna que se va a cambiar de tamaño) como parámetro.

**código rubí**

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
## **Descargar código de ejecución**
Descargar**Autoajustar filas y columnas (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
