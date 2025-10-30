---
title: Hücreler için Stil Al ve Ayarla
description: Aspose.Cells for Node.js via C++ te veri biçimlendirme ve stil yapmanın yollarını keşfedin; metin biçimlendirme, sayı biçimlendirme, tarih biçimlendirme ve diğer stil seçenekleri dahil. Kılavuzumuz, profesyonel görünümlü ve çekici biçimlendirmelerle elektronik tablo oluşturmanıza yardımcı olacaktır.
keywords: Aspose.Cells for Node.js via C++, veri biçimlendirme, stil verme, metin biçimlendirme, sayı biçimlendirme, tarih biçimlendirme, stil seçenekleri, tablolar, çekici biçimlendirme, profesyonel görünümlü.
linktitle: Stil
type: docs
weight: 50
url: /tr/nodejs-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for Node.js via C++, hücreleri biçimlendirmek için iki yeni yöntem tanıttı: Cell.getStyle ve Cell.setStyle. Bu makale, Cell.getStyle/setStyle yaklaşımını inceleyerek, en uygun tekniği değerlendirmenize yardımcı olur.

{{% /alert %}} 
## **Hücreleri Biçimlendirme**
Bir hücreyi biçimlendirmenin iki yolu vardır, aşağıda gösterildiği gibi.
### **getStyle() kullanımı**
Aşağıdaki kod parçasıyla, biçimlendirme sırasında her hücre için bir Style nesnesi başlatılır. Birçok hücre biçimlendiriliyorsa, büyük miktarda bellek tüketilir çünkü Style nesnesi büyük bir nesnedir. Bu Style nesneleri, Workbook.save yöntemi çağrılana kadar serbest bırakılmaz.

**JavaScript**

{{< highlight javascript >}}
cell.getStyle().getFont().setIsBold(true);
{{< /highlight >}}
### **setStyle() kullanımı**
İlk yaklaşım kolay ve açıktır, peki neden ikinci yaklaşımı ekledik?

Bellek kullanımını optimize etmek için ikinci yaklaşımı ekledik. Cell.getStyle yöntemiyle bir Style nesnesi alındıktan sonra, üzerinde değişiklik yapın ve Cell.setStyle yöntemiyle bu hücreye yeniden ayarlayın. Bu Style nesnesi korunmayacak ve JavaScript'in çöp toplayıcısı, kullanılmayan bu nesneyi toplayacaktır.

Cell.setStyle yöntemini çağırırken, Style nesnesi her hücre için kaydedilmez. Bunun yerine, bu Style nesnesi, kullanılabilir olup olmadığını görmek için iç Style nesne havuzuyla karşılaştırılır. Sadece mevcut olanlardan farklı olan Style nesneleri, her Workbook nesnesinde saklanır. Bu, her Excel dosyası için birkaç yüz Style nesnesi olmasını sağlar, binlerce yerine. Her hücre için, yalnızca Style nesne havuzuna erişim için bir indeks korunur.

**JavaScript**

{{< highlight javascript >}}
let style = cell.getStyle();

style.getFont().setIsBold(true);

cell.setStyle(style);
{{< /highlight >}}

## **Gelişmiş Konular**
- [CellsFactory sınıfını kullanarak Stil nesnesi oluşturma](/cells/tr/nodejs-cpp/create-style-object-using-cellsfactory-class/)
- [Mevcut Bir Stilü Değiştirme](/cells/tr/nodejs-cpp/modify-an-existing-style/)
- [Stil Nesnelerini Yeniden Kullanma](/cells/tr/nodejs-cpp/reusing-style-objects/)
- [Dahili Stilleri Kullanma](/cells/tr/nodejs-cpp/using-built-in-styles/)

{{< app/cells/assistant language="nodejs-cpp" >}}
