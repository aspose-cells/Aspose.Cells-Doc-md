---
title: Golang ile C++ kullanarak Bir Tablo veya Çalışma Kitabında Kullanılan Yazı Tipleri Listesi Alın
linktitle: Yazı Tipleri Listesi Alma
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir C++ kitaplığıdır. Bir elektronik tabloda veya çalışma kitabında kullanılan yazı tiplerinin listesini alma desteği sağlar ve belgeye kullanılan yazı tipi bilgilerini edinmenize olanak tanır. Bu makale, Aspose.Cells kütüphanesini kullanarak yazı tipi listesini nasıl alacağınızı gösterecektir.
keywords: Aspose.Cells, Elektronik Tablo, Çalışma Kitabı, Yazı Tipi, Liste
type: docs
weight: 20
url: /tr/go-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Olası Kullanım Senaryoları**

Bazen, bir belgenin düzenlenmesi için kullanılan yazı tiplerini bilmek önemli olabilir. Elektronik tablonuzu PDF veya resim formatına dönüştürdüğünüzde, Aspose.Cells tüm gerekli yazı tiplerinin sisteminize yüklü olmasını veya **yazı tipleri dizininde** bulunmasını gerektirir. Aspose.Cells, gereken yazı tipini bulamazsa, gerçek yazı tipinizi başka uygun bir yazı tipi ile değiştirmeye çalışır. Bu, sadece istenmeyen şekilde PDF veya görüntülerin işlenmesine neden olmakla kalmaz, aynı zamanda uygun yazı tiplerini bulma süresi de alır.

Bu tür durumlarla başa çıkmak için, çalışma kitabınızda kullanılan yazı tiplerini bilmeli, sonra Windows ortamında sisteminize yükleyin veya Windows veya Linux ortamında yazı tiplerinizin bulunduğu dizine yerleştirin.

Aspose.Cells, çalışma kitabınızda veya elektronik tablonuzda kullanılan tüm yazı tiplerinin listesini döndüren [**Workbook.GetFonts**](https://reference.aspose.com/cells/go-cpp/workbook/getfonts/) yöntemini sağlar.

## **Bir Elektronik Tablo veya Çalışma Kitabında Kullanılan Yazı Tiplerinin Listesini Alın**

Aşağıdaki örnek kod, kaynak excel dosyasını yükler ve içinde kullanılan yazı tiplerinin listesini alır. İçinde bazı yanıltıcı yazı tiplerinin bulunduğu sahte bir çalışma sayfası vardır. Kod, çalışma kitabındaki tüm yazı tiplerini yazdırdığında, o sahte yazı tiplerini de yazdırır. Aşağıdaki ekran görüntüsü, [örnek excel dosyasını](25395211.xlsx) ve sahte yazı tiplerinin nasıl listelendiğini gösterir.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAListOfFontsUsedInASpreadsheetOrWorkbook.go" >}}
## **Konsol Çıktısı**

Yukarıdaki örnek excel dosyasıyla çalıştırıldığında, yukarıdaki örnek kodun konsol çıktısı şöyle görünür.

{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

{{< /highlight >}}
