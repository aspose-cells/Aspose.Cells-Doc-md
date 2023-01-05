---
title: Ruby'de Satırları ve Sütunları Kopyalamak
type: docs
weight: 30
url: /tr/java/copying-rows-and-columns-in-ruby/
---
## **Aspose.Cells - Satırları ve Sütunları Kopyalama**
### **Satırları Kopyalama**
Aspose.Cells, Cells sınıfının copyRow yöntemini sağlar. Bu yöntem, formüller, değerler, yorumlar, hücre formatları, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kaynak satırdan hedef satıra kopyalar.

copyRow yöntemi aşağıdaki parametreleri alır:

- kaynak Cells nesnesi,
- kaynak satır dizini ve
- hedef satır dizini.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def copy_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Copy the second row with data, formattings, images and drawing objects

    # to the 12th row in the worksheet.

    worksheet.getCells().copyRow(worksheet.getCells(),1,11)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Rows.xls")

    puts "Copy Rows Successfully."

end

{{< /highlight >}}
### **Sütunları Kopyalama**
Aspose.Cells, Cells sınıfının copyColumn yöntemini sağlar; bu yöntem, güncellenmiş referanslarla formüller ve değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kaynak sütundan hedef sütuna kopyalar.

copyColumn yöntemi aşağıdaki parametreleri alır:

- kaynak Cells nesnesi,
- kaynak sütun dizini ve
- hedef sütun dizini.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def kopya_sütunlar()

veri_dir = Dosya.diradı(Dosya.diradı(Dosya.diradı(__DOSYA__))) + '/veri/'



# Bir Çalışma Kitabı nesnesini excel dosya yoluna göre başlatma

çalışma kitabı = Rjb::import('com.aspose.cells.Workbook').new

# Excel dosyasındaki ilk çalışma sayfasına erişim

çalışma sayfası = çalışma kitabı.getWorksheets().get(0)

# Başlık satırlarına bazı veriler koyun (A1:A4)

ben = 0

 ben iken< 5

        worksheet.getCells().get(i, 0).setValue("Header Row #{i}")

        i +=1

    end

    # Put some detail data (A5:A999)

    i = 5

    while i < 1000

        worksheet.getCells().get(i, 0).setValue("Detail Row #{i}")

        i +=1

    end

    # Create another Workbook.

    workbook1 = Rjb::import('com.aspose.cells.Workbook').new

    # Get the first worksheet in the book.

    worksheet1 = workbook1.getWorksheets().get(0)

    # Copy the first column from the first worksheet of the first workbook into

    # the first worksheet of the second workbook.

    worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

    # Autofit the column.

    worksheet1.autoFitColumn(2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Columns.xls")

    puts "Copy Columns Successfully."

end

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Satırları ve Sütunları Kopyalama (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
