---
title: Gérer les sauts de page en Ruby
type: docs
weight: 20
url: /fr/java/managing-page-breaks-in-ruby/
---

## **Aspose.Cells - Gérer les sauts de page**
### **Ajout de sauts de page**
Pour ajouter des sauts de page en utilisant **Aspose.Cells Java pour Ruby**, appelez la méthode **add_page_breaks** du module **pagebreaks**. Vous pouvez voir ci-dessous un exemple de code.

**Code Ruby**

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
### **Effacement de tous les sauts de page**
Pour effacer tous les sauts de page en utilisant **Aspose.Cells Java pour Ruby**, appelez la méthode **clear_all_page_breaks** du module **pagebreaks**. Vous pouvez voir ci-dessous un exemple de code.

**Code Ruby**

{{< highlight ruby >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **Supprimer un saut de page spécifique**
Pour supprimer un saut de page spécifique en utilisant **Aspose.Cells Java pour Ruby**, appelez la méthode **remove_page_break** du module **pagebreaks**. Vous pouvez voir ci-dessous un exemple de code.

**Code Ruby**

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
## **Télécharger le code en cours d'exécution**
Téléchargez **Gestion des sauts de page (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
