---
title: Ruby'de Çalışma Sayfalarını Yönetme
type: docs
weight: 10
url: /tr/java/managing-worksheets-in-ruby/
---
## **Aspose.Cells - Çalışma Sayfalarını Yönetme**
### **Çalışma Sayfalarını Yeni Bir Excel Dosyasına Ekleme**
Çalışma Sayfası'nı kullanarak yeni bir Excel dosyasına eklemek için**Yakut için Aspose.Cells Java** , aramanız yeterli**add_worksheet** yöntemi**YönetimÇalışma Sayfaları** modül.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def add_worksheet()

    # Instantiating a Workbook object

    workbook = Rjb::import('com.aspose.cells.Workbook').new

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book.out.xls")

    puts "Sheet added successfully."

end 

{{< /highlight >}}
### **Tasarımcı Elektronik Tablosuna Çalışma Sayfaları Ekleme**
Bir tasarımcı elektronik tablosuna çalışma sayfaları ekleme süreci, Excel dosyasının zaten oluşturulmuş olması ve çalışma sayfasını eklemeden önce bu Excel dosyasını açmamız gerekmesi dışında, yukarıdaki yaklaşımla tamamen aynıdır.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def add_worksheet_to_designer_spreadsheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book1.out.xls")

end  

{{< /highlight >}}
### **Sayfa Adını Kullanarak Çalışma Sayfalarına Erişme**
 Kullanarak çalışma sayfasına sayfa adına göre erişmek için**Yakut için Aspose.Cells Java** , aramanız yeterli**get_worksheet** yöntemi**YönetimÇalışma Sayfaları** modül.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def get_worksheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Accessing a worksheet using its sheet name

    worksheet = workbook.getWorksheets().get("Sheet1")

    puts worksheet.to_string

end

{{< /highlight >}}
### **Sayfa Adını Kullanarak Çalışma Sayfalarını Kaldırma**
 Çalışma sayfasını kullanarak sayfa adına göre kaldırmak için**Yakut için Aspose.Cells Java** , aramanız yeterli**remove_worksheet_by_name** yöntemi**YönetimÇalışma Sayfaları** modül.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def remove_worksheet_by_name()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt("Sheet1")



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end


{{< /highlight >}}
### **Sayfa Dizini Kullanarak Çalışma Sayfalarını Kaldırma**
 Çalışma sayfasını kullanarak sayfa dizinine göre kaldırmak için**Yakut için Aspose.Cells Java** , aramanız yeterli**remove_worksheet_by_index** yöntemi**YönetimÇalışma Sayfaları** modül.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def remove_worksheet_by_index()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt(0)



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end 

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Çalışma Sayfalarını Yönetme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
