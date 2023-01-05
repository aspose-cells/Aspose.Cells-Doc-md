---
title: Управление разрывами страниц в Ruby
type: docs
weight: 20
url: /ru/java/managing-page-breaks-in-ruby/
---
## **Aspose.Cells - Управление разрывами страниц**
### **Добавление разрывов страниц**
 Чтобы добавить разрывы страниц с помощью**Aspose.Cells Java для рубина** , вызов**add_page_breaks** метод**разрывы страниц** модуль. Ниже вы можете увидеть пример кода.

**Рубиновый код**

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
### **Удаление всех разрывов страниц**
 Чтобы очистить все разрывы страниц с помощью**Aspose.Cells Java для рубина** , вызов**clear_all_page_breaks** метод**разрывы страниц** модуль. Ниже вы можете увидеть пример кода.

**Рубиновый код**

{{< highlight "ruby" >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **Удаление определенного разрыва страницы**
 Чтобы удалить определенный разрыв страницы, используя**Aspose.Cells Java для рубина** , вызов**remove_page_break** метод**разрывы страниц** модуль. Ниже вы можете увидеть пример кода.

**Рубиновый код**

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
## **Скачать рабочий код**
Скачать**Управление разрывами страниц (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
