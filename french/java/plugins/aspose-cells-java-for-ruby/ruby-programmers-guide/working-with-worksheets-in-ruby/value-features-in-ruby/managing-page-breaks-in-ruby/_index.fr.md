---
title: Gestion des sauts de page dans Ruby
type: docs
weight: 20
url: /fr/java/managing-page-breaks-in-ruby/
---
## **Aspose.Cells - Gestion des sauts de page**
### **Ajouter des sauts de page**
 Pour ajouter des sauts de page à l'aide de**Aspose.Cells Java pour rubis** , appel**add_page_breaks** méthode de**sauts de page** module. Ci-dessous, vous pouvez voir un exemple de code.

**Code rubis**

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
### **Effacer tous les sauts de page**
 Pour effacer tous les sauts de page à l'aide de**Aspose.Cells Java pour rubis** , appel**clear_all_page_breaks** méthode de**sauts de page** module. Ci-dessous, vous pouvez voir un exemple de code.

**Code rubis**

{{< highlight "ruby" >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **Suppression d'un saut de page spécifique**
 Pour supprimer un saut de page spécifique à l'aide de**Aspose.Cells Java pour rubis** , appel**remove_page_break** méthode de**sauts de page** module. Ci-dessous, vous pouvez voir un exemple de code.

**Code rubis**

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
## **Télécharger le code d'exécution**
Télécharger**Gestion des sauts de page (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
