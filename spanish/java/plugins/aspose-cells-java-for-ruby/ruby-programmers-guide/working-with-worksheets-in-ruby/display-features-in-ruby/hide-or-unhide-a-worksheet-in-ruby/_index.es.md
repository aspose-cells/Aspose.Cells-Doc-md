---
title: Ocultar o mostrar una hoja de trabajo en Ruby
type: docs
weight: 60
url: /es/java/hide-or-unhide-a-worksheet-in-ruby/
---
## **Aspose.Cells - Ocultar o mostrar una hoja de trabajo**
### **Ocultar una hoja de trabajo**
 Para ocultar la hoja de trabajo usando Aspose.Cells Java para Ruby, llame**ocultarunhideworksheet** módulo.

**código rubí**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Hiding the first worksheet of the Excel file

worksheet.setVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Mostrando una hoja de trabajo**
Los desarrolladores pueden hacer que una hoja de trabajo sea visible configurando el*establecerVisible(* *verdadero* *)*metodo de la**Hoja de cálculo**clase.

**código rubí**

{{< highlight "ruby" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Ocultar o mostrar una hoja de trabajo (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
