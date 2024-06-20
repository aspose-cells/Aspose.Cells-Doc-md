---
title: Ruby de Çalışma Sayfalarını Kopyalama ve Taşıma
type: docs
weight: 10
url: /tr/java/copying-and-moving-worksheets-in-ruby/
---

## **Aspose.Cells - Çalışma Sayfalarını Kopyalama ve Taşıma**
### **Çalışma Kitabı İçinde Çalışma Sayfalarını Kopyalama**
**Aspose.Cells for Java in Ruby** kullanarak çalışma sayfasını kopyalamak için **copyworksheets** modülünün **copy_worksheet** yöntemini çağırın. Aşağıda kod örneğini görebilirsiniz.

**Ruby Kodu**

{{< highlight ruby >}}

 def copy_worksheet(workbook)

    # Create a Worksheets object with reference to the sheets of the Workbook.

    sheets = workbook.getWorksheets()

    # Copy data to a new sheet from an existing sheet within the Workbook.

    sheets.addCopy("Sheet1")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Copy Worksheet.xls")

    puts "Copy worksheet, please check the output file."

end 

{{< /highlight >}}
### **Çalışma Kitabı İçinde Çalışma Sayfalarını Taşıma**
Ruby kullanarak **Aspose.Cells for Java kullanarak** çalışma sayfasını taşımak için, **copyworksheets** modülünün **move_worksheet** yöntemini çağırın. Aşağıda örnek kodu görebilirsiniz.

**Ruby Kodu**

{{< highlight ruby >}}

 def move_worksheet(workbook)

    # Get the first worksheet in the book.

    sheet = workbook.getWorksheets().get(0)

    # Move the first sheet to the third position in the workbook.

    sheet.moveTo(2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Move Worksheet.xls")

    puts "Move worksheet, please check the output file."

end 

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıdaki sosyal kodlama sitelerinden herhangi birinden **Kopyalama ve Taşıma Çalışma Sayfalarını (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
