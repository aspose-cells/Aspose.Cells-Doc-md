---
title: Ruby'de Satırları ve Sütunları Gruplandırma ve Grubu Çözme
type: docs
weight: 40
url: /tr/java/grouping-and-ungrouping-rows-and-columns-in-ruby/
---
## **Aspose.Cells - Satırlar ve Sütunların Grup Yönetimi**
### **Satırları ve Sütunları Gruplama**
Cells koleksiyonunun groupRows ve groupColumns yöntemlerini çağırarak satırları veya sütunları gruplamak mümkündür. Her iki yöntem de aşağıdaki parametreleri alır:

- İlk satır/sütun dizini, gruptaki ilk satır veya sütun.
- Son satır/sütun dizini, gruptaki son satır veya sütun.
- Gizlidir, gruplamadan sonra satırların/sütunların gizlenip gizlenmeyeceğini belirten bir Boolean parametresidir.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def group_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Grouping first six rows (from 0 to 5) and making them hidden by passing true

    cells.groupRows(0,5,true)

    # Grouping first three columns (from 0 to 2) and making them hidden by passing true

    cells.groupColumns(0,2,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Group Rows And Columns.xls")

    puts "Group Rows And Columns Successfully."

end  

{{< /highlight >}}
### **Satırları ve Sütunları Çözme**
Cells koleksiyonunun UngroupRows ve UngroupColumns yöntemlerini çağırarak gruplandırılmış satırların veya sütunların grubunu çözün. Her iki yöntem de aynı parametreleri alır:

- İlk satır veya sütun dizini, grubu çözülecek ilk satır/sütun.
- Son satır veya sütun dizini, grubu çözülecek son satır/sütun.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def ungroup_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Group Rows And Columns.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Ungrouping first six rows (from 0 to 5)

    cells.ungroupRows(0,5)

    # Ungrouping first three columns (from 0 to 2)

    cells.ungroupColumns(0,2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Ungroup Rows And Columns.xls")

    puts "Ungroup Rows And Columns Successfully."

end

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Satırları ve Sütunları Gruplandırma ve Grubu Çözme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
