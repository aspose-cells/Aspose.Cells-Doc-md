---
title: Ruby'de Çalışma Sayfalarını Kopyalama ve Taşıma
type: docs
weight: 10
url: /tr/java/copying-and-moving-worksheets-in-ruby/
---
## **Aspose.Cells - Çalışma Sayfalarını Kopyalama ve Taşıma**
### **Çalışma Kitabındaki Çalışma Sayfalarını Kopyalama**
 Çalışma sayfasını kullanarak kopyalamak için**Yakut içinde Aspose.Cells for Java** , aramak**kopya_çalışma sayfası** yöntemi**kopya çalışma sayfaları** modül. Aşağıda kod örneğini görebilirsiniz.

**Yakut Kodu**

{{< highlight "ruby" >}}

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
### **Çalışma Sayfalarını Çalışma Kitabı İçinde Taşıma**
 Çalışma sayfasını kullanarak taşımak için**Yakut içinde Aspose.Cells for Java** , aramak**move_worksheet** yöntemi**kopya çalışma sayfaları** modül. Aşağıda kod örneğini görebilirsiniz.

**Yakut Kodu**

{{< highlight "ruby" >}}

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
İndirmek**Çalışma Sayfalarını Kopyalama ve Taşıma (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
