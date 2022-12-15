---
title: Çalışma Sayfasını Jython'da SVG'ye Dönüştürme
type: docs
weight: 40
url: /tr/java/converting-worksheet-to-svg-in-jython/
---
## **Aspose.Cells - Çalışma Sayfasını SVG'ye Dönüştürme**
 Belgeleri kullanarak eklemek için**Jython için Aspose.Cells Java**. Burada örnek kodu görebilirsiniz.

**Jython Kodu**

{{< highlight "java" >}}

 aspose-cells'ten içe aktarma Ayarları

com.aspose.cells'ten içe aktarma Çalışma Kitabı

com.aspose.cells'den ImageFormat'ı içe aktarın

com.aspose.cells'den ImageOrPrintOptions'ı içe aktarın

com.aspose.cells'den SheetRender'ı içe aktarın

com.aspose.cells'den SaveFormat'ı içe aktarın



sınıf ConvertingWorksheetToSVG:

 kesin__içinde__(kendisi):

 dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingWorksheetToSVG/'



 saveFormat = SaveFormat

 çalışma kitabı = Çalışma Kitabı(dataDir + "Kitap1.xls")

 #Her çalışma sayfasını tek bir sayfada svg formatına dönüştür.

 imgOptions = ImageOrPrintOptions()

 imgOptions.setSaveFormat(saveFormat.SVG)

 imgOptions.setOnePagePerSheet(Doğru)

 #Her çalışma sayfasını svg formatına dönüştür

 SheetCount = workbook.getWorksheets().getCount()

 #for(i=0; ben<sheetCount; i++)

        for i in range(sheetCount):



            sheet = workbook.getWorksheets().get(i)

            sr = SheetRender(sheet, imgOptions)

            pageCount = sr.getPageCount()

            #for (k = 0 k < pageCount k++)

            for k in range(pageCount):



                #Output the worksheet into Svg image format

                sr.toImage(k, dataDir + sheet.getName() + ".out.svg")





        # Print message

        print "Excel to SVG conversion completed successfully."



if __name__ == '__main__':        

    ConvertingWorksheetToSVG()

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Belgeleri Ekleyin (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingWorksheetToSVG.py)
