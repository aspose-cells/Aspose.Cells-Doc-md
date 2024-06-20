---
title: Ruby de Satırları ve Sütunları Otomatik Daraltma
type: docs
weight: 20
url: /tr/java/autofit-rows-and-columns-in-ruby/
---

## **Aspose.Cells - Satırları ve Sütunları Otomatik Daraltma**
### **Satır Otomatik Daraltma**
Bir satırın genişliğini ve yüksekliğini otomatik ayarlamanın en basit yolu Worksheet sınıfının autoFitRow metodunu çağırmaktır. autoFitRow metodu, (yeniden boyutlandırılacak olan satırın) bir satır indeksi olarak bir parametre alır.

**Ruby Kodu**

{{< highlight ruby >}}

 def autofit_row()

        data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



        # Instantiating a Workbook object by excel file path

        workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        # Auto-fitting the 3rd row of the worksheet

        worksheet.autoFitRow(2)

        # Auto-fitting the 3rd row of the worksheet based on the contents in a range of

        # cells (from 1st to 9th column) within the row

        #worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(data_dir + "Autofit Row.xls")

        puts "Autofit Row Successfully."

    end

{{< /highlight >}}
### **Sütun Otomatik Daraltma**
Bir sütunun genişliğini ve yüksekliğini otomatik boyutlandırmanın en kolay yolu Worksheet sınıfının autoFitColumn metodunu çağırmaktır. autoFitColumn metodu, (yeniden boyutlandırılacak olan sütunun) bir sütun indeksini parametre olarak alır.

**Ruby Kodu**

{{< highlight ruby >}}

 def autofit_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Auto-fitting the 4th column of the worksheet

    worksheet.autoFitColumn(3)

    # Auto-fitting the 4th column of the worksheet based on the contents in a range of

    # cells (from 1st to 9th row) within the column

    #worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Autofit Column.xls")

    puts "Autofit Column Successfully."

end

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Satırları ve Sütunları Otomatik Daraltma (Aspose.Cells)** dosyasını indirebilirsiniz:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
