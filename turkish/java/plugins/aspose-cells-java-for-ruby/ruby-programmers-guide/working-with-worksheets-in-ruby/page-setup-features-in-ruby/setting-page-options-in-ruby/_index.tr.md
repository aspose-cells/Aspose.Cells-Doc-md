---
title: Ruby'de Sayfa Seçeneklerini Ayarlama
type: docs
weight: 10
url: /tr/java/setting-page-options-in-ruby/
---
## **Aspose.Cells - Ayar Sayfası Seçenekleri**
### **Sayfa yönlendirmesi**
 kullanarak sayfa yönü ayarlarını uygulamak için**Yakut için Aspose.Cells Java** , aramak**Sayfa yönlendirmesi** yöntemi**sayfa ayarı** modül.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def page_orientation()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    sheet = worksheets.get(sheet_index)

    # Setting the orientation to Portrait

    page_setup = sheet.getPageSetup()

    page_orientation_type = Rjb::import('com.aspose.cells.PageOrientationType')

    page_setup.setOrientation(page_orientation_type.PORTRAIT)



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Page Orientation.xls")

    puts "Set page orientation, please check the output file."

end   

{{< /highlight >}}
### **Ölçekleme faktörü**
 kullanarak ölçekleme uygulamak için**Yakut için Aspose.Cells Java** , aramak**ölçekleme** yöntemi**sayfa ayarı** modül.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def scaling()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    sheet = worksheets.get(sheet_index)

    # Setting the scaling factor to 100

    page_setup = sheet.getPageSetup()

    page_setup.setZoom(100)



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Scaling.xls")

    puts "Set scaling, please check the output file."

end


{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Ayar Sayfası Seçenekleri (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagesetup.rb)
