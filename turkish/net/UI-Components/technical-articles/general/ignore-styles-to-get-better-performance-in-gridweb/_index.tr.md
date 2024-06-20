---
title: Daha İyi Performans İçin Stilleri Yoksay GridWeb
type: docs
weight: 1060
url: /tr/net/aspose-cells-gridweb/ignorestylewithnodata
description: Bu makale, daha iyi performans elde etmek için GridWeb de IgnoreStyleWithNoData nın nasıl kullanılacağını açıklar.
keywords: GridWeb,performance
---

## **Olası Kullanım Senaryoları**
[GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata) özelliğini kullanarak çalışma kitabından gerekli olan daha az satır/sütun yüklemek için lütfen.

## **Çalışma Kitabı Yüklenirken Daha İyi Performans Elde Edin**
Lütfen [örnek excel dosyasını](largerowswithstyle.xlsx) kontrol edin 

IgnoreStyleWithNoData = true; olarak ayarlandığında

Görebileceğiniz gibi, satırlar (15'e kadar) ve sütunlar (L'ye kadar) gösterilir, hücresiz son sürekli satırları ve sütunları göstermeyecektir. Bu nedenle yükleme süresi daha kısa olacaktır.

![ignore stil ile çalışma kitabı](ignorestyletrue.png)


IgnoreStyleWithNoData = false olarak ayarlandığında;(varsayılan değer false'dur)

Görebileceğiniz gibi, 500 sıra ve CZ sütuna kadar çok daha fazla satır ve sütun gösteriyor

16. satırdan 500. satıra kadar, bazı hücrelerin kenarlık stili ayarlanmış ancak hücreler veri içermiyor

M sütunundan CZ sütununa kadar, bazı hücrelerin kenarlık stili ayarlanmış ancak hücreler veri içermiyor

![ignorestylefalse.png](ignorestylefalse.png)



