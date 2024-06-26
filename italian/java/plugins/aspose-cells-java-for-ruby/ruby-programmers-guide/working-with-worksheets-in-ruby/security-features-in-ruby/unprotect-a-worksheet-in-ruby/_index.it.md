---
title: Sblocca un foglio di lavoro in Ruby
type: docs
weight: 20
url: /it/java/unprotect-a-worksheet-in-ruby/
---

## **Aspose.Cells - Sbloccare un foglio di lavoro**
Per proteggere il foglio di lavoro utilizzando **Aspose.Cells Java per Ruby**, chiama il metodo **unprotect_worksheet** del modulo **protection**.

**Codice Ruby**

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
## **Scarica il codice in esecuzione**
Scarica **Sbloccare un foglio di lavoro (Aspose.Cells)** da uno dei siti di codice sociale di seguito indicati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/protection.rb)
