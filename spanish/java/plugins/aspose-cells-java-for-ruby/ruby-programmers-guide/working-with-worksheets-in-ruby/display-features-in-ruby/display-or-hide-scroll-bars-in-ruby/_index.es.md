---
title: Mostrar u ocultar barras de desplazamiento en Ruby
type: docs
weight: 30
url: /es/java/display-or-hide-scroll-bars-in-ruby/
---
## **Aspose.Cells - Mostrar u ocultar barras de desplazamiento**
### **Ocultar barras de desplazamiento**
 Para ocultar las barras de desplazamiento usando**Aspose.Cells Java para rubí** , llamar**mostrar ocultar barras de desplazamiento** módulo.

**código rubí**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false)

\# Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Scroll Bars are now hidden, please check the output file."

{{< /highlight >}}
### **Haciendo visibles las barras de desplazamiento**
Haga visibles las barras de desplazamiento configurando los métodos setVerticalScrollBarHidden() o setHorizontalScrollBarHidden() de la clase Workbook en verdadero.

**código rubí**

{{< highlight "ruby" >}}

 # Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true)

\# Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true)

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Mostrar u ocultar barras de desplazamiento (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)
