---
title: Elektronik Tablo veya Çalışma Kitabında kullanılan Yazı Tiplerinin Listesini Alın
type: docs
weight: 20
url: /tr/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
## **Olası Kullanım Senaryoları**

 İşleme amacıyla çalışma kitabınızda kullanılan yazı tiplerini bilmek genellikle gereklidir. Çalışma kitabınızı PDF veya görüntüye dönüştürdüğünüzde, Aspose.Cells, gerekli tüm yazı tiplerinin sisteminizde yüklü olmasını veya bilgisayarınızda mevcut olmasını gerektirir.**yazı dizini**Aspose.Cells gerekli yazı tipini bulamazsa, onu sisteminizde veya yazı tipi dizininizde bulunan ve gerçek yazı tipinizi değiştirebilecek başka bir uygun yazı tipiyle değiştirmeye çalışır. Bu sadece PDF veya resimlerin istenmeyen bir şekilde oluşturulmasına neden olmakla kalmaz, aynı zamanda uygun yazı tiplerini bulmak için işlem süresi alır.

Bu tür durumlarla başa çıkabilmek için, çalışma kitabınızda hangi yazı tiplerinin kullanıldığını bilmeli, ardından Windows ortamında bu yazı tiplerini sisteminize yüklemeli veya Windows veya Linux ortamında yazı tipleri dizininize yerleştirmelisiniz.

 Aspose.Cells şunları sağlar:[Workbook.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts()) çalışma kitabınızda veya elektronik tablonuzda kullanılan tüm yazı tiplerinin listesini döndüren yöntem.

## **Elektronik Tablo veya Çalışma Kitabında kullanılan Yazı Tiplerinin Listesini Alın**

Aşağıdaki örnek kod, kaynak excel dosyasını yükler ve içinde kullanılan yazı tiplerinin listesini alır. Gösterim amacıyla bazı sahte yazı tiplerinin eklendiği bir sahte çalışma sayfasına sahiptir. Kod, çalışma kitabının içindeki tüm yazı tiplerini yazdırdığında, bu sahte yazı tiplerini de yazdırır. Aşağıdaki ekran görüntüsü[örnek excel dosyası](sampleGetFonts.xlsx) ve sahte yazı tiplerinin nasıl listelendiği.

![yapılacaklar:resim_alternatif_metin](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **Konsol Çıkışı**

 Verilen ile çalıştırıldığında yukarıdaki örnek kodun konsol çıktısı aşağıdadır.[örnek excel dosyası](sampleGetFonts.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]{{< /highlight >}}
