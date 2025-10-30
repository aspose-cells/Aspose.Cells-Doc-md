---
title: Bir Elektronik Tablo veya Çalışma Kitabında Kullanılan Yazı Tiplerinin Listesini Alın
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir Python kütüphanesidir. Bir elektronik tablo veya çalışma kitabında kullanılan yazı tiplerinin listesini almayı destekler, kullanıcılara belgede kullanılan yazı tipi bilgilerini edinme imkanı sağlar. Bu makale, Aspose.Cells for Python via .NET kütüphanesini kullanarak yazı tipi listesini nasıl alacağınızı gösterecek.
keywords: Aspose.Cells for Python via .NET, Elektronik Tablo, Çalışma Kitabı, Yazı Tipi, Liste
type: docs
weight: 20
url: /tr/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Olası Kullanım Senaryoları**

Çalışma kitabınızda kullanılan yazı tiplerini bilmek sıklıkla gereklidir. Çalışma kitabınızı PDF veya görsel formatına dönüştürdüğünüzde, Aspose.Cells for Python via .NET tüm gereken yazı tiplerinin sisteminizde yüklü veya **yazı tipi dizininde** bulunmasını ister. Gerekli yazı tipi bulunamadığında, sisteminizde veya yazı tipi dizininizde bulunan başka uygun bir yazı tipi ile değiştirmeye çalışır. Bu, PDF veya görsellerin istenmeyen şekilde render edilmesine neden olmanın yanı sıra, uygun yazı tiplerinin bulunması için işlem süresini de artırır.

Bu tür durumlarla başa çıkmak için, çalışma kitabınızda kullanılan yazı tiplerini bilmeli, sonra Windows ortamında sisteminize yükleyin veya Windows veya Linux ortamında yazı tiplerinizin bulunduğu dizine yerleştirin.

Aspose.Cells for Python via .NET, çalışma kitabınızda kullanılan tüm yazı tiplerinin listesini döndüren `[**Workbook.get_fonts**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_fonts)` yöntemini sağlar.

## **Bir Elektronik Tablo veya Çalışma Kitabında Kullanılan Yazı Tiplerinin Listesini Alın**

Aşağıdaki örnek kod, kaynak excel dosyasını yükler ve içinde kullanılan yazı tiplerinin listesini alır. İçinde bazı yanıltıcı yazı tiplerinin bulunduğu sahte bir çalışma sayfası vardır. Kod, çalışma kitabındaki tüm yazı tiplerini yazdırdığında, o sahte yazı tiplerini de yazdırır. Aşağıdaki ekran görüntüsü, [örnek excel dosyasını](25395211.xlsx) ve sahte yazı tiplerinin nasıl listelendiğini gösterir.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetListOfFontsUsedInSpreadsheetOrWorkbook.py" >}}

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

{{< app/cells/assistant language="python-net" >}}
