+++
title = "Managing Page Breaks in Ruby" 
description = "" 
weight = 24729 
+++

Aspose.Cells for Java : Managing Page Breaks in Ruby  

# Aspose.Cells for Java : Managing Page Breaks in Ruby


## Aspose.Cells - Managing Page Breaks

##### Adding Page Breaks

To add page breaks using **Aspose.Cells Java for Ruby**, call **add\_page\_breaks** method of **pagebreaks** module. Below you can see code example.

**Ruby Code**

{{< code lang="cs" >}}
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
{{< /code >}}

##### Clearing All Page Breaks

To clear all page breaks using **Aspose.Cells Java for Ruby**, call **clear\_all\_page\_breaks** method of **pagebreaks** module. Below you can see code example.

**Ruby Code**

{{< code lang="cs" >}}
def clear_all_page_breaks(workbook)
    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()
    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format
    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."
end 
{{< /code >}}

##### Removeing Specific Page Break

To remove specific page break using **Aspose.Cells Java for Ruby**, call **remove\_page\_break** method of **pagebreaks** module. Below you can see code example.

**Ruby Code**

{{< code lang="cs" >}}
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
{{< /code >}}

## Download Running Code

Download **Managing Page Breaks (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)

