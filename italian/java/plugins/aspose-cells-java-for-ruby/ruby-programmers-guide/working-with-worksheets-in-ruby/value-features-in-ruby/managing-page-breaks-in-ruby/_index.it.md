---
title: Gestione delle interruzioni di pagina in Ruby
type: docs
weight: 20
url: /it/java/managing-page-breaks-in-ruby/
---
## **Aspose.Cells - Gestione interruzioni di pagina**
### **Aggiunta di interruzioni di pagina**
 Per aggiungere interruzioni di pagina utilizzando**Aspose.Cells Java per Ruby** , chiamata**add_page_breaks** metodo di**interruzioni di pagina** modulo. Di seguito puoi vedere un esempio di codice.

**Codice Rubino**

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
### **Cancellazione di tutte le interruzioni di pagina**
 Per cancellare tutte le interruzioni di pagina utilizzando**Aspose.Cells Java per Ruby** , chiamata**cancella_tutte_le_interruzioni_di_pagina** metodo di**interruzioni di pagina** modulo. Di seguito puoi vedere un esempio di codice.

**Codice Rubino**

{{< highlight "ruby" >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **Rimozione di un'interruzione di pagina specifica**
 Per rimuovere un'interruzione di pagina specifica utilizzando**Aspose.Cells Java per Ruby** , chiamata**remove_page_break** metodo di**interruzioni di pagina** modulo. Di seguito puoi vedere un esempio di codice.

**Codice Rubino**

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
## **Scarica il codice in esecuzione**
Scarica**Gestione interruzioni di pagina (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
