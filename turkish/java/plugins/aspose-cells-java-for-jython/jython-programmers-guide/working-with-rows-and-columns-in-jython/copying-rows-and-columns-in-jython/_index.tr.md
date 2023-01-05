---
title: Jython'da Satırları ve Sütunları Kopyalamak
type: docs
weight: 30
url: /tr/java/copying-rows-and-columns-in-jython/
---
## **Aspose.Cells - Satırları ve Sütunları Kopyalama**
 Belgeleri kullanarak eklemek için**Jython için Aspose.Cells Java**. Burada örnek kodu görebilirsiniz.

**Jython Kodu**

{{< highlight "java" >}}

 aspose-cells'ten içe aktarma Ayarları

com.aspose.cells'ten içe aktarma Çalışma Kitabı

sınıf RowsAndColumns:

 kesin__içinde__(kendisi):



 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'



 # Satırları Kopyalama

 self.copy_rows()

 # Sütunları Kopyalama

 self.kopya_sütunları()



 def copy_rows(dataDir):

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

 # Bir Çalışma Kitabı nesnesini excel dosya yoluna göre başlatma

 çalışma kitabı = Çalışma Kitabı(dataDir + 'Book1.xls')

 Excel dosyasındaki ilk çalışma sayfasına erişim

 çalışma sayfası = çalışma kitabı.getWorksheets().get(0)

 # Veriler, biçimlendirmeler, resimler ve çizim nesneleri ile ikinci satırı kopyalayın

 # çalışma sayfasındaki 12. satıra.

 worksheet.getCells().copyRow(worksheet.getCells(),1,11)

 # Değiştirilen Excel dosyasını varsayılan (yani Excel 2003) biçiminde kaydetme

 workbook.save(dataDir + "Rows.xls'yi Kopyala")

 "Satırları Başarıyla Kopyala" yazdırın.



 def kopya_sütunları(dataDir):

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

 # Bir Çalışma Kitabı nesnesini excel dosya yoluna göre başlatma

 çalışma kitabı = Çalışma kitabı()

 Excel dosyasındaki ilk çalışma sayfasına erişim

 çalışma sayfası = çalışma kitabı.getWorksheets().get(0)

 # Başlık satırlarına bazı veriler koyun (A1:A4)

 ben = 0

 ben iken< 5:

            worksheet.getCells().get(i, 0).setValue("Header Row #i")






        # Put some detail data (A5:A999)

        i = 5

        while i < 1000:

            worksheet.getCells().get(i, 0).setValue("Detail Row #i")



        # Create another Workbook.

        workbook1 = Workbook()

        # Get the first worksheet in the book.

        worksheet1 = workbook1.getWorksheets().get(0)

        # Copy the first column from the first worksheet of the first workbook into

        # the first worksheet of the second workbook.

        worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

        # Autofit the column.

        worksheet1.autoFitColumn(2)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Copy Columns.xls")

        print "Copy Columns Successfully." 




if __name__ == '__main__':        

    RowsAndColumns()

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Belgeleri Ekleyin (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
