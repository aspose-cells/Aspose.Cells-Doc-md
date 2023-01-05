---
title: Elektronik Tablo veya Çalışma Kitabında kullanılan Yazı Tiplerinin Listesini Alın
type: docs
weight: 20
url: /tr/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
## **Olası Kullanım Senaryoları**

İşleme amacıyla çalışma kitabınızda kullanılan yazı tiplerini bilmek genellikle gereklidir. Çalışma kitabınızı PDF veya görüntüye dönüştürdüğünüzde, Aspose.Cells, gerekli tüm yazı tiplerinin sisteminizde yüklü olmasını veya bilgisayarınızda mevcut olmasını gerektirir.**yazı dizini**Aspose.Cells gerekli yazı tipini bulamazsa, onu sisteminizde veya yazı tipi dizininizde bulunan ve gerçek yazı tipinizi değiştirebilecek başka bir uygun yazı tipiyle değiştirmeye çalışır. Bu sadece PDF veya resimlerin istenmeyen bir şekilde oluşturulmasına neden olmakla kalmaz, aynı zamanda uygun yazı tiplerini bulmak için işlem süresi alır.

Bu tür durumlarla başa çıkabilmek için, çalışma kitabınızda hangi yazı tiplerinin kullanıldığını bilmeli, ardından Windows ortamında bu yazı tiplerini sisteminize yüklemeli veya Windows veya Linux ortamında yazı tipleri dizininize yerleştirmelisiniz.

 Aspose.Cells şunları sağlar:**[Workbook.GetFonts](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getfonts)**çalışma kitabınızda veya elektronik tablonuzda kullanılan tüm yazı tiplerinin listesini döndüren yöntem.

## **Elektronik Tablo veya Çalışma Kitabında kullanılan Yazı Tiplerinin Listesini Alın**

 Aşağıdaki örnek kod, kaynak excel dosyasını yükler ve içinde kullanılan yazı tiplerinin listesini alır. Gösterim amacıyla bazı sahte yazı tiplerinin eklendiği bir sahte çalışma sayfasına sahiptir. Kod, çalışma kitabının içindeki tüm yazı tiplerini yazdırdığında, bu sahte yazı tiplerini de yazdırır. Aşağıdaki ekran görüntüsü[örnek excel dosyası](25395211.xlsx) ve sahte yazı tiplerinin nasıl listelendiği.

![yapılacaklar:resim_alternatif_metin](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-GetListOfFontsUsedInSpreadsheetOrWorkbook.cs" >}}

## **Konsol Çıkışı**

 Verilen ile çalıştırıldığında yukarıdaki örnek kodun konsol çıktısı aşağıdadır.[örnek excel dosyası](25395211.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0]]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black]]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128]]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104]]

{{< /highlight >}}
