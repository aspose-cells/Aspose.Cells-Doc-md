---
title: Ruby de Bir Çalışma Sayfasının Korumasını Kaldırma
type: docs
weight: 20
url: /tr/java/unprotect-a-worksheet-in-ruby/
---

## **Aspose.Cells - Bir Çalışma Sayfasının Korumasını Kaldırma**
**Aspose.Cells Java için Ruby** kullanarak bir çalışma sayfasını korumak için **protection** modülünün **unprotect_worksheet** yöntemini çağırın.

**Ruby Kodu**

{{< highlight ruby >}}

 def unprotect_worksheet()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    worksheet = worksheets.get(0)

    protection = worksheet.getProtection()

    # The following 3 methods are only for Excel 2000 and earlier formats

    protection.setAllowEditingContent(false)

    protection.setAllowEditingObject(false)

    protection.setAllowEditingScenario(false)

    # Unprotecting the worksheet with a password

    worksheet.unprotect("1234")



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Unprotect Worksheet.xls")

    puts "Unprotect a Worksheet, please check the output file."

end   

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi bir sosyal kodlama sitesinden **Bir Çalışma Sayfasını Korumasız Bırakma (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/protection.rb)
