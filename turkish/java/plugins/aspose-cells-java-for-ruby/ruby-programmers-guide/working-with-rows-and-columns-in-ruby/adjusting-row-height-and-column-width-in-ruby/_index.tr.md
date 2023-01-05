---
title: Ruby'de Satır Yüksekliğini ve Sütun Genişliğini Ayarlama
type: docs
weight: 10
url: /tr/java/adjusting-row-height-and-column-width-in-ruby/
---
## **Aspose.Cells - Satır Yüksekliğini ve Sütun Genişliğini Ayarlama**
### **Satır Yüksekliğini Ayarlama**
Cells koleksiyonunun setRowHeight yöntemini çağırarak tek bir satırın yüksekliğini ayarlamak mümkündür. setRowHeight yöntemi aşağıdaki parametreleri alır:

- **Satır dizini**, yüksekliğini değiştirdiğiniz satırın dizini.
- **Satır yüksekliği**, satıra uygulanacak satır yüksekliği.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def set_row_height()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Setting the height of the second row to 13

    cells.setRowHeight(1, 13)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Set Row Height.xls")

    puts "Set Row Height Successfully."

end

{{< /highlight >}}
### **Sütun Genişliğini Ayarlama**
Cells koleksiyonunun setColumnWidth yöntemini çağırarak bir sütunun genişliğini ayarlayın. setColumnWidth yöntemi aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliğini değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, istenen sütun genişliği.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def set_column_width()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Setting the width of the second column to 17.5

    cells.setColumnWidth(1, 17.5)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Set Column Width.xls")

    puts "Set Column Width Successfully."

end

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Satır Yüksekliğini ve Sütun Genişliğini Ayarlama (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
