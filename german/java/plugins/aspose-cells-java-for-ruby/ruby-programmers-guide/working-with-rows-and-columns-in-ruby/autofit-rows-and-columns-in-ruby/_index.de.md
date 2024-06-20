---
title: Zeilen und Spalten in Ruby automatisch anpassen
type: docs
weight: 20
url: /de/java/autofit-rows-and-columns-in-ruby/
---

## **Aspose.Cells - Zeilen und Spalten automatisch anpassen**
### **Zeile automatisch anpassen**
Der einfachste Ansatz zum automatischen Anpassen der Breite und Höhe einer Zeile besteht darin, die Methode autoFitRow der Klasse Worksheet aufzurufen. Die Methode autoFitRow nimmt einen Zeilenindex (der Zeile, die angepasst werden soll) als Parameter an.

**Ruby-Code**

{{< highlight ruby >}}

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
### **Spalte automatisch anpassen**
Der einfachste Weg, die Breite und Höhe einer Spalte automatisch anzupassen, besteht darin, die Methode autoFitColumn der Klasse Worksheet aufzurufen. Die Methode autoFitColumn erhält den Spaltenindex (der Spalte, die gerade angepasst wird) als Parameter.

**Ruby-Code**

{{< highlight ruby >}}

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
## **Laufenden Code herunterladen**
Laden Sie **Autofit Rows and Columns (Aspose.Cells)** von einer der unten genannten sozialen Plattformen herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
