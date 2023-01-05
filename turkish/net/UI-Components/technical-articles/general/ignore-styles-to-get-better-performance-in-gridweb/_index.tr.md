---
title: GridWeb'de daha iyi performans elde etmek için stilleri yok sayın
type: docs
weight: 1060
url: /tr/net/aspose-cells-gridweb/ignorestylewithnodata
description: Bu makalede, Aspose.Cells.GridWeb kitaplığı için daha iyi performans elde etmek üzere IgnoreStyleWithNoData'nın nasıl kullanılacağı açıklanmaktadır.
keywords: performance
---
## **Olası Kullanım Senaryoları**
 Lütfen kullan[GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata)çalışma kitabından daha az gerekli satır/sütun yükleme özelliği.
 
## **Çalışma Kitabını Yüklerken Daha İyi Performans Elde Edin**
 lütfen kontrol ediniz[örnek excel dosyası](largerowswithstyle.xlsx) 

IgnoreStyleWithNoData = true olarak ayarlandığında;

Görüldüğü gibi 15'e kadar olan satırları ve L'ye kadar olan sütunları gösterir, Hücrelerde veri olmayan son sürekli satır ve sütunları göstermez.Böylece yükleme süresi kısalır.

![yoksay stiliyle çalışma kitabı](ignorestyletrue.png)


IgnoreStyleWithNoData = false olarak ayarlandığında;(varsayılan değer false'tur)

Gördüğünüz gibi, çok daha fazla satır (500'e kadar) ve sütunlar (CZ'ye kadar) gösterir.

16. satırdan 500. satıra kadar bazı hücreler boder stilini ayarladı, ancak hücreler veri içermiyor.

M sütunundan CZ sütununa kadar bazı hücreler boder stilini ayarladı, ancak hücreler veri içermiyor.

![yoksayma stili olmadan çalışma kitabı](ignorestylefalse.png)
 
 
 