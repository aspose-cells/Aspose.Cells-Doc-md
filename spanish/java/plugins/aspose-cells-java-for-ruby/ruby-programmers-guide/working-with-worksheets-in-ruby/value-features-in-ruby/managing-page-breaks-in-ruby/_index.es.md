---
title: Gestión de saltos de página en Ruby
type: docs
weight: 20
url: /es/java/managing-page-breaks-in-ruby/
---
## **Aspose.Cells - Gestión de saltos de página**
### **Adición de saltos de página**
 Para agregar saltos de página usando**Aspose.Cells Java para rubí** , llamada**add_page_breaks** método de**saltos de página** módulo. A continuación puede ver un ejemplo de código.

**código rubí**

{{< highlight "ruby" >}}

 def add_page_breaks(workbook)

    worksheets = workbook.getWorksheets()

    worksheet = worksheets.get(0)

    h_page_breaks = worksheet.getHorizontalPageBreaks()

    h_page_breaks.add("Y30")



    v_page_breaks = worksheet.getVerticalPageBreaks()

    v_page_breaks.add("Y30")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Add Page Breaks.xls")

    puts "Add page breaks, please check the output file."

end   

{{< /highlight >}}
### **Borrar todos los saltos de página**
 Para borrar todos los saltos de página usando**Aspose.Cells Java para rubí** , llamada**clear_all_page_breaks** método de**saltos de página** módulo. A continuación puede ver un ejemplo de código.

**código rubí**

{{< highlight "ruby" >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **Eliminación de un salto de página específico**
 Para eliminar un salto de página específico usando**Aspose.Cells Java para rubí** , llamada**remove_page_break** método de**saltos de página** módulo. A continuación puede ver un ejemplo de código.

**código rubí**

{{< highlight "ruby" >}}

 def remove_page_break(workbook)

    worksheets = workbook.getWorksheets()

    worksheet = worksheets.get(0)



    h_page_breaks = worksheet.getHorizontalPageBreaks()

    h_page_breaks.removeAt(0)



    v_page_breaks = worksheet.getVerticalPageBreaks()

    v_page_breaks.removeAt(0)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Remove Page Break.xls")

    puts "Remove page break, please check the output file."

end 

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Gestión de saltos de página (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
