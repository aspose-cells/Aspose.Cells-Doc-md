---
title: Proteger hojas de trabajo en Ruby
type: docs
weight: 10
url: /es/java/protecting-worksheets-in-ruby/
---
## **Aspose.Cells - Hojas de trabajo de protección**
 Para proteger la hoja de trabajo usando**Aspose.Cells Java para rubí** , llamada**proteger_hoja de trabajo** método de**proteccion** módulo.

**código rubí**

{{< highlight "ruby" >}}

 def protect_worksheet()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    worksheet = worksheets.get(0)

    protection = worksheet.getProtection()

    # The following 3 methods are only for Excel 2000 and earlier formats

    protection.setAllowEditingContent(false)

    protection.setAllowEditingObject(false)

    protection.setAllowEditingScenario(false)

    # Protects the first worksheet with a password "1234"

    protection.setPassword("1234")



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Protect Worksheet.xls")

    puts "Protect a Worksheet, please check the output file."

end   

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Hojas de trabajo de protección (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/protection.rb)
