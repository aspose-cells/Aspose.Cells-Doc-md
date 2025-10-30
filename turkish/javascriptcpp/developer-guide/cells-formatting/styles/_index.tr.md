---
title: Hücreler için Stil Al ve Ayarla
description: Veri biçimlendirme ve stil uygulama işlemlerinin nasıl gerçekleştirileceğini, metin biçimlendirme, sayı biçimlendirme, tarih biçimlendirme ve diğer stil seçenekleri dahil olmak üzere C++ ile JavaScript üzerinden öğreneceksiniz. Rehberimiz, profesyonel görünümlü elektronik tablolar oluşturmanıza yardımcı olacaktır.
keywords: Aspose.Cells for JavaScript üzerinden C++ ile veri biçimlendirme, stil uygulama, metin biçimlendirme, sayı biçimlendirme, tarih biçimlendirme, stil seçenekleri, elektronik tablolar, çekici biçimlendirme, profesyonel görünümlü.
linktitle: Stil
type: docs
weight: 50
url: /tr/javascript-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for JavaScript ile C++ kullanılarak hücre biçimlendirme için iki yeni yöntem tanıtıldı: Cell.style ve Cell.style. Bu makale, hangi yöntemin size en uygun olduğunu belirlemenize yardımcı olmak için Cell.style/yöntem yaklaşımını incelemektedir.

{{% /alert %}} 
## **Hücreleri Biçimlendirme**
Bir hücreyi biçimlendirmenin iki yolu vardır, aşağıda gösterildiği gibi.
### **Stil kullanımı**
Aşağıdaki kod parçasıyla, biçimlendirme sırasında her hücre için bir Style nesnesi başlatılır. Birçok hücre biçimlendiriliyorsa, büyük miktarda bellek tüketilir çünkü Style nesnesi büyük bir nesnedir. Bu Style nesneleri, Workbook.save yöntemi çağrılana kadar serbest bırakılmaz.

**JavaScript**

{{< highlight javascript >}}
cell.style.font.isBold = true;
{{< /highlight >}}
### **Stil kullanımı**
İlk yaklaşım kolay ve açıktır, peki neden ikinci yaklaşımı ekledik?

İkinci yaklaşımı, bellek kullanımını optimize etmek için ekledik. Style nesnesini almak için Cell.style özelliğini kullandıktan sonra, onu değiştirin ve tekrar bu hücreye atamak için Cell.style özelliğini kullanın. Bu Style nesnesi korunmayacak ve JavaScript'in çöp toplayıcısı onu referans olmadığı zaman toplayacaktır.

Cell.style özelliğini atadığınızda, Style nesnesi her hücre için kaydedilmez. Bunun yerine, bu Style nesnesi, yeniden kullanılabilir olup olmadığını görmek için dahili bir Style nesnesi havuzuyla karşılaştırılır. Sadece farklı olan Style nesneleri, her Çalışma Kitabı nesnesinde saklanır. Bu, her Excel dosyası için binlerce yerine birkaç yüz Style nesnesi olduğu anlamına gelir. Her hücre için sadece Stillık nesne havuzuna bir indeks saklanır.

**JavaScript**

{{< highlight javascript >}}
let style = cell.style;

style.font.isBold = true;

cell.style = style;
{{< /highlight >}}

## **Gelişmiş Konular**
- [CellsFactory sınıfını kullanarak Stil nesnesi oluşturma](/cells/tr/javascript-cpp/create-style-object-using-cellsfactory-class/)
- [Mevcut Bir Stilü Değiştirme](/cells/tr/javascript-cpp/modify-an-existing-style/)
- [Stil Nesnelerini Yeniden Kullanma](/cells/tr/javascript-cpp/reusing-style-objects/)
- [Dahili Stilleri Kullanma](/cells/tr/javascript-cpp/using-built-in-styles/)
