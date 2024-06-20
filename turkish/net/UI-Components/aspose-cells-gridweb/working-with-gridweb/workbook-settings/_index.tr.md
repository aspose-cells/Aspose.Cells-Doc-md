---
title: Çalışma Sayfası İçin Ayarlar
type: docs
weight: 250
url: /tr/net/aspose-cells-gridweb/aspose-cells-gridweb/workbook-settings/
description: Bu makale, GridWeb de çalışma sayfası ayarlarını açıklar.
keywords: GridWeb, ayarlar
---


GridWorkbookSettings'ı belirterek ayarlayabileceğimiz bazı ayarlarımız vardır:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/GridWorkbookSettings)

|**Ad** |**Açıklama** |
| :- | :- |
|MaxIteration |Döngüsel bir referansı çözmek için maksimum iterasyon sayısını alır veya ayarlar, varsayılan değer 100'dür. |
|Iteration | Döngüsel referansları çözmek için iterasyon kullanılıp kullanılmayacağını ayarlar. |
|ForceFullCalculate | Her bir hesaplama tetiklendiğinde her seferinde tamamen hesaplanıp hesaplanımamasını ayarlar veya alır. |
|CreateCalcChain | Hesaplanmış formüller zinciri oluşturulup oluşturulmayacağını ayarlar veya alır. Varsayılan olarak false. |
|ReCalculateOnOpen | Dosya açılırken tüm formüllerin tekrar hesaplanıp hesaplanmayacağını ayarlar veya alır. |
|PrecisionAsDisplayed | Bu çalışma kitabındaki hesaplamaların, sayıların gösterildiği şekildeki hassasiyet kullanılarak yapılıp yapılmayacağını belirtir. |
|Date1904 | İş kitabının 1904 tarih sistemini kullanıp kullanmadığını temsil eden bir değeri alır veya ayarlar. |
|CheckCustomNumberFormat | Tarz.Custom ayarlarken özel sayı biçimini kontrol etmek için alır veya ayarlar. |
|Author |Dosyanın yazarını alır ve ayarlar. |



Örneğin, aşağıdaki kod, Dosya'nın açılması sırasında hesaplamanın durdurulması için ReCalculateOnOpen özelliğini false olarak ayarlar:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 aşağıdaki kod, dosyanın yazarını ayarlar:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}


