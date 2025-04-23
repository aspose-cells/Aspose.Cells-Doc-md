---
title: Bir Elektronik Tablo veya Çalışma Kitabında Kullanılan Yazı Tiplerinin Listesini Alın
type: docs
weight: 20
url: /tr/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Olası Kullanım Senaryoları**

Genellikle, çalışma kitabınızda kullanılan yazı tiplerini, dönüştürdüğünüzde PDF veya görüntüye gereksinim duyarsınız. Aspose.Cells, ihtiyaç duyulan tüm yazı tiplerinin sisteminizde yüklü veya **yazı tipleri dizininizde** bulunmasını gerektirir. Aspose.Cells, gereken yazı tipini bulamazsa, sisteminizde veya yazı tipi dizinizde bulunan uygun bir yazı tipi ile değiştirmeye çalışır ve gerçek yazı tipinizi yerine koyabilir. Bu, hem istenmeyen bir PDF veya görüntü oluşturulmasına neden olur hem de uygun yazı tiplerini bulma süresi alır.

Bu tür durumlarla başa çıkmak için, çalışma kitabınızda hangi yazı tiplerinin kullanıldığını bilmelisiniz, ardından bu yazı tiplerini Windows ortamı için sisteminize yükleyin veya Windows veya Linux ortamı için yazı tipi dizininize yerleştirin.

Aspose.Cells, çalışma kitabınızda veya elektronik tablonuzda kullanılan tüm yazı tiplerinin listesini döndüren [Workbook.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts--) metodunu sağlar.

## **Bir Elektronik Tablo veya Çalışma Kitabında Kullanılan Yazı Tiplerinin Listesini Alın**

Aşağıdaki örnek kod, kaynak excel dosyasını yükler ve içinde kullanılan yazı tiplerinin listesini alır. İllüstrasyon amacıyla bazı sahte yazı tipleri eklenmiş sahte bir çalışma tablosuna sahiptir. Kod, çalışma kitabı içindeki tüm yazı tiplerini yazdırdığında, bu sahte yazı tiplerini de yazdırır. Aşağıdaki ekran görüntüsü, [örnek excel dosyasını](sampleGetFonts.xlsx) ve sahte yazı tiplerinin nasıl listelendiğini göstermektedir.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **Konsol Çıktısı**

Verilen [örnek excel dosyası](sampleGetFonts.xlsx) ile birlikte yukarıdaki örnek kodun konsol çıktısı aşağıda bulunmaktadır.

{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
