---
title: Gestionar Saltos de Página en Ruby
type: docs
weight: 20
url: /es/java/managing-page-breaks-in-ruby/
---

## **Aspose.Cells - Gestionar Saltos de Página**
### **Añadir Saltos de Página**
Para añadir saltos de página usando **Aspose.Cells Java para Ruby**, llame al método **add_page_breaks** del módulo **pagebreaks**. A continuación, puede ver un ejemplo de código.

**Código Ruby**

{{< highlight ruby >}}

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
### **Borrar Todos los Saltos de Página**
Para borrar todos los saltos de página usando **Aspose.Cells Java para Ruby**, llame al método **clear_all_page_breaks** del módulo **pagebreaks**. A continuación, puede ver un ejemplo de código.

**Código Ruby**

{{< highlight ruby >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **Eliminar Salto de Página Específico**
Para eliminar un salto de página específico usando **Aspose.Cells Java para Ruby**, llame al método **remove_page_break** del módulo **pagebreaks**. A continuación, puede ver un ejemplo de código.

**Código Ruby**

{{< highlight ruby >}}

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
## **Descargar Código en Ejecución**
Descargar **Gestionando Saltos de Página (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
