---
title: Hücreler için Stil Al ve Ayarla
description: Aspose.Cells for Python via .NET kullanarak veri biçimlendirme ve stil verme işlemlerini, metin biçimlendirme, sayı biçimlendirme, tarih biçimlendirme ve diğer stil seçenekleri dahil olmak üzere nasıl yapacağınızı öğrenin. Kılavuzumuz, profesyonel görünümlü ve çekici biçimlendirmeli tablolar oluşturmanıza yardımcı olacak.
keywords: Aspose.Cells for Python via .NET, veri biçimlendirmesi, stil, metin biçimlendirmesi, sayı biçimlendirmesi, tarih biçimlendirmesi, stil seçenekleri, elektronik tablolar, çekici biçimlendirme, profesyonel görünümlü.
linktitle: Stil
type: docs
weight: 50
url: /tr/python-net/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET, hücre biçimlendirmeleri için iki yeni yöntem tanıttı: Cell.GetStyle ve Cell.SetStyle. Bu makale, hangi tekniğin size en uygun olduğunu anlamanız için Cell.GetStyle/SetStyle yöntemini inceler.

{{% /alert %}} 

## **Hücreleri Biçimlendirme**
Bir hücreyi biçimlendirmenin iki yolu vardır, aşağıda gösterildiği gibi.

### **GetStyle() Kullanarak**
Aşağıdaki kod parçasını kullanarak, bir hücre biçimlendirilirken her bir hücre için bir Stil nesnesi oluşturulur. Eğer birçok hücre biçimlendiriliyorsa, büyük miktarda bellek tüketilir çünkü Stil nesnesi büyük bir nesnedir. Bu Stil nesneleri Workbook.Save yöntemi çağrıldığında serbest bırakılmaz.


**Python**

{{< highlight python >}}

cell.get_style().font.is_bold = True

{{< /highlight >}}

### **SetStyle() Kullanarak**
İlk yaklaşım kolay ve açıktır, peki neden ikinci yaklaşımı ekledik?

İkinci yaklaşımı bellek kullanımını optimize etmek için ekledik. Hücre.GetStyle yöntemini kullanarak bir Stil nesnesi alıp, onu değiştirip Hücre.SetStyle yöntemini kullanarak geri bu hücreye ayarlamak. Bu Stil nesnesi saklanmaz ve .NET GC ona referans olmadığında onu toplar.

Hücre.SetStyle yöntemi çağrıldığında, Stil nesnesi her bir hücre için saklanmaz. Bunun yerine bu Stil nesnesi içsel bir Stil nesnesi havuzuyla karşılaştırılır ve yeniden kullanılıp kullanılamayacağı kontrol edilir. Yalnızca mevcut olanlardan farklı olan Stil nesneleri her bir Workbook nesnesi için saklanır. Bu, her Excel dosyası için yalnızca birkaç yüz Stil nesnesi olduğu anlamına gelir, binlerce değil. Her bir hücre için yalnızca bir Stil nesnesi havuzuna bir indeks saklanır.



**Python**

{{< highlight python >}}

style = cell.get_style()
style.font.is_bold = True
cell.set_style(style)

{{< /highlight >}}

## **Gelişmiş Konular**
- [CellsFactory sınıfını kullanarak Stil nesnesi oluşturma](/cells/tr/python-net/create-style-object-using-cellsfactory-class/)
- [Mevcut Bir Stilü Değiştirme](/cells/tr/python-net/modify-an-existing-style/)
- [Stil Nesnelerini Yeniden Kullanma](/cells/tr/python-net/reusing-style-objects/)
- [Dahili Stilleri Kullanma](/cells/tr/python-net/using-built-in-styles/)


{{< app/cells/assistant language="python-net" >}}
