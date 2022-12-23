---
title: Birleşme ve Ayrılma Cells
type: docs
weight: 140
url: /tr/java/merging-and-unmerging-cells/
---
{{% alert color="primary" %}}

Her satırda veya sütunda her zaman aynı sayıda hücre olmasını istemezsiniz. Örneğin, birkaç sütuna yayılan bir hücreye başlık koymak isteyebilirsiniz. Veya bir fatura oluşturuyorsanız, toplam için daha az sütun isteyebilirsiniz. İki veya daha fazla hücreden bir hücre yapmak için bunları birleştirin. Microsoft Excel, kullanıcıların elektronik tabloyu istedikleri gibi yapılandırmak için hücreleri seçmesine ve birleştirmesine olanak tanır.

**Microsoft Excel'de soldaki hücreler olarak biçimlendirilmiş bir hücre aralığını birleştirmenin ve ardından bölmenin sonucu** 

![yapılacaklar:resim_alternatif_metin](merging-and-unmerging-cells_1.png)

Aspose.Cells bu özelliği destekler ve ayrıca bir çalışma sayfasındaki hücreleri birleştirebilir. Birleştirilmiş hücreleri de ayırabilir veya bölebilirsiniz. Birleştirilmiş bir hücrenin hücre referansı, orijinal olarak seçilen aralıktaki sol üst hücrenin referansıdır.

Hücreler birleştirildiğinde yalnızca sol üst hücredeki verilerin tutulduğunu unutmayın. Aralıktaki diğer hücrelerde veri varsa, o veri silinir.

Biçimlendirme de aynı şekilde referans hücreyi temel alır, böylece hücreleri birleştirdiğinizde, aralıktaki sol üst hücrenin biçimlendirme ayarları birleştirilen hücreye uygulanır. Hücre bölündüğünde, yeni hücreler orijinal biçim ayarlarını korur.

{{% /alert %}}

## **Cells'i bir Çalışma Sayfasında birleştirme.**

### **Microsoft Excel'i kullanma**

Aşağıdaki adımlarda, Microsoft Excel kullanılarak çalışma sayfasındaki hücrelerin nasıl birleştirileceği açıklanmaktadır.

1. İstediğiniz verileri aralık içinde en sol üstteki hücreye kopyalayın.
1. Birleştirmek istediğiniz hücreleri seçin.
1.  Bir satır veya sütundaki hücreleri birleştirmek ve hücre içeriğini ortalamak için,**Birleştir ve Ortala** üzerindeki simge**biçimlendirme** araç çubuğu.

### **Aspose.Cells'i kullanma**

 bu[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) sınıfın görev için bazı yararlı yöntemleri vardır. Örneğin, yöntem[**birleştirmek()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) hücreleri, belirli bir hücre aralığındaki tek bir hücrede birleştirir.

Aşağıdaki çıktı, aşağıdaki kod yürütüldükten sonra oluşturulur.

**Hücreler (C6:E7) birleştirildi** 

![yapılacaklar:resim_alternatif_metin](merging-and-unmerging-cells_2.png)

#### **Kod Örneği**

Aşağıdaki örnek, bir çalışma sayfasındaki hücrelerin (C6:E7) nasıl birleştirileceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **Ayrılıyor (Bölünüyor) Birleştirildi Cells**

### **Microsoft Excel'i kullanma**

Aşağıdaki adımlarda, birleştirilmiş hücrelerin Microsoft Excel kullanılarak nasıl bölüneceği açıklanmaktadır.

1.  Birleştirilmiş hücreyi seçin.
 Hücreler birleştirildiğinde,**Birleştir ve Ortala** üzerinde seçilir**biçimlendirme** araç çubuğu.
1.  Tıklamak**Birleştir ve Ortala** üzerinde**biçimlendirme** araç çubuğu.

#### **Aspose.Cells'i kullanma**

 bu[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) sınıfın adında bir yöntemi var[**birleştirmeyi kaldır()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int)) hücreleri orijinal hallerine böler. Yöntem, birleştirilmiş hücre aralığındaki hücre referansını kullanarak hücreleri ayırır.

#### **Kod Örneği**

Aşağıdaki örnek, birleştirilmiş hücrelerin nasıl bölüneceğini gösterir (C6). Örnek, önceki örnekte oluşturulan dosyayı kullanır ve birleştirilmiş hücreleri böler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **İlgili Makaleler**

- [Birleştirilmiş hücreleri bulma ve bölme](/cells/tr/java/detect-merged-cells-in-a-worksheet/).
- [Range.merge() ve Range.unMerge() yöntemlerini kullanarak bir hücre aralığını birleştirme ve bölme](/cells/tr/java/merge-or-unmerge-range-of-cells/).

