---
title: Hücreler için Stil Al ve Ayarla
description: Metin biçimlendirme, sayı biçimlendirme, tarih biçimlendirme ve diğer biçimlendirme seçenekleri dahil olmak üzere Aspose.Cells for .NET de veri biçimlendirme ve stil uygulamanın yolunu keşfedin. Rehberimiz, çekici biçimlendirmeyle profesyonel görünümlü elektronik tablolar oluşturmanıza yardımcı olacaktır.
keywords: Aspose.Cells for .NET, veri biçimlendirme, stil, metin biçimlendirme, sayı biçimlendirme, tarih biçimlendirme, stil seçenekleri, elektronik tablolar, çekici biçimlendirme, profesyonel görünümlü.
linktitle: Stil
type: docs
weight: 50
url: /tr/net/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2, hücreleri biçimlendirmek için iki yeni yöntem tanıttı: Cell.GetStyle ve Cell.SetStyle. Bu makale, Cell.GetStyle/SetStyle yaklaşımını inceleyerek hangi teknikten en iyi şekilde yararlanacağınıza karar vermenize yardımcı olur.

{{% /alert %}} 
## **Hücreleri Biçimlendirme**
Bir hücreyi biçimlendirmenin iki yolu vardır, aşağıda gösterildiği gibi.
### **GetStyle() Kullanarak**
Aşağıdaki kod parçasını kullanarak, bir hücre biçimlendirilirken her bir hücre için bir Stil nesnesi oluşturulur. Eğer birçok hücre biçimlendiriliyorsa, büyük miktarda bellek tüketilir çünkü Stil nesnesi büyük bir nesnedir. Bu Stil nesneleri Workbook.Save yöntemi çağrıldığında serbest bırakılmaz.



**C#**

{{< highlight csharp >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
### **SetStyle() Kullanarak**
İlk yaklaşım kolay ve açıktır, peki neden ikinci yaklaşımı ekledik?

İkinci yaklaşımı bellek kullanımını optimize etmek için ekledik. Hücre.GetStyle yöntemini kullanarak bir Stil nesnesi alıp, onu değiştirip Hücre.SetStyle yöntemini kullanarak geri bu hücreye ayarlamak. Bu Stil nesnesi saklanmaz ve .NET GC ona referans olmadığında onu toplar.

Hücre.SetStyle yöntemi çağrıldığında, Stil nesnesi her bir hücre için saklanmaz. Bunun yerine bu Stil nesnesi içsel bir Stil nesnesi havuzuyla karşılaştırılır ve yeniden kullanılıp kullanılamayacağı kontrol edilir. Yalnızca mevcut olanlardan farklı olan Stil nesneleri her bir Workbook nesnesi için saklanır. Bu, her Excel dosyası için yalnızca birkaç yüz Stil nesnesi olduğu anlamına gelir, binlerce değil. Her bir hücre için yalnızca bir Stil nesnesi havuzuna bir indeks saklanır.



**C#**

{{< highlight csharp >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

## **Gelişmiş Konular**
- [CellsFactory sınıfını kullanarak Stil nesnesi oluşturma](/cells/tr/net/create-style-object-using-cellsfactory-class/)
- [Mevcut Bir Stilü Değiştirme](/cells/tr/net/modify-an-existing-style/)
- [Stil Nesnelerini Yeniden Kullanma](/cells/tr/net/reusing-style-objects/)
- [Dahili Stilleri Kullanma](/cells/tr/net/using-built-in-styles/)


