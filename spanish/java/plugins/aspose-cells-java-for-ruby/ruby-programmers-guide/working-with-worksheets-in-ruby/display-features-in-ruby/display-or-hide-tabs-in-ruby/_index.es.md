---
title: Mostrar u ocultar pestañas en Ruby
type: docs
weight: 40
url: /es/java/display-or-hide-tabs-in-ruby/
---

## **Aspose.Cells - Mostrar u Ocultar Pestañas**
### **Ocultar pestañas**
Para ocultar pestañas usando **Aspose.Cells Java para Ruby**, llama al módulo **displayhidetabs**.

**Código Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Hacer pestañas visibles**
Haz visibles las pestañas con el método setSheetTabBarHidden(false) de la clase Workbook.

**Código Ruby**

{{< highlight ruby >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Ocultar o Mostrar o Esconder Pestañas (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
