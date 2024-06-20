---
title: Ruby de Çalışma Sayfalarını Yönetme
type: docs
weight: 10
url: /tr/java/managing-worksheets-in-ruby/
---

## **Aspose.Cells - Çalışma Sayfalarını Yönetme**
### **Yeni bir Excel Dosyasına Çalışsayfalar Ekleme**
Yeni bir Excel dosyasına çalışma sayfası eklemek için **Aspose.Cells Java for Ruby** kullanarak, **MangingWorksheets** modülünün **add_worksheet** yöntemini çağırın.

**Ruby Kodu**

{{< highlight ruby >}}

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
### **Tasarımcı Çalışsayfalara Çalışsayfalar Ekleme**
Tasarımcı e-tabloya çalışma sayfaları eklemek süreci tamamen yukarıdaki yaklaşımla aynıdır, tek farkı Excel dosyasının zaten oluşturulmuş olması ve çalışma sayfasını eklemeden önce bu Excel dosyasını açmamız gerektiği.

**Ruby Kodu**

{{< highlight ruby >}}

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
### **Sayfa Adını Kullanarak Çalışsayfalara Erişme**
**Aspose.Cells Java for Ruby** kullanarak, **MangingWorksheets** modülünün **get_worksheet** yöntemini çağırarak sayfa adına göre çalışma sayfasına erişin.

**Ruby Kodu**

{{< highlight ruby >}}

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
### **Sayfa Adını Kullanarak Çalışsayfaları Kaldırma**
**Aspose.Cells Java for Ruby** kullanarak, **MangingWorksheets** modülünün **remove_worksheet_by_name** yöntemini çağırarak sayfa adına göre çalışma sayfasını kaldırın.

**Ruby Kodu**

{{< highlight ruby >}}

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
### **Sayfa Dizinini Kullanarak Çalışma Sayfalarını Kaldırma**
**Aspose.Cells Java for Ruby** kullanarak, **MangingWorksheets** modülünün **remove_worksheet_by_index** yöntemini çağırarak sayfa indeksine göre çalışma sayfasını kaldırın.

**Ruby Kodu**

{{< highlight ruby >}}

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
Herhangi bir sosyal kodlama sitesinden **Yönetim Çalışma Sayfalarını (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
