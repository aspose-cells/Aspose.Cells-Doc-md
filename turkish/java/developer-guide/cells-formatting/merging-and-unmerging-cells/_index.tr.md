---
title: Hücreleri Birleştirme ve Ayırma
type: docs
weight: 140
url: /tr/java/merging-and-unmerging-cells/
---

{{% alert color="primary" %}}

Her zaman her satır veya sütunda aynı hücre sayısını istemezsiniz. Örneğin, birkaç sütunu kapsayan bir başlık koymak isteyebilirsiniz. Veya bir fatura oluştururken toplam için daha az sütun isteyebilirsiniz. İki veya daha fazla hücreden bir hücre oluşturmak için onları birleştirin. Microsoft Excel kullanıcıları, istedikleri şekilde elektronik tabloyu yapılandırmak için hücreleri seçip birleştirebilirler.

Hücrelerin bir araya getirilmesinin ardından biçimlendirilen hücrelerin, Microsoft Excel'deki sol hücrelerin sonucu 

![todo:image_alt_text](merging-and-unmerging-cells_1.png)

Aspose.Cells bu özelliği destekler ve bir çalışma sayfasındaki hücreleri birleştirebilir. Birleştirilen hücreleri ayrıştırabilir veya bölebilirsiniz de. Birleştirilmiş bir hücrenin hücre başvurusu, başlangıçta seçilen aralıktaki sol üst hücrenin başvurusudur.

Hücreler birleştirildiğinde, sadece sol üst hücredeki veriler saklanır. Eğer aralıktaki diğer hücrelerde veri varsa, o veri silinir.

Benzer şekilde, biçimlendirme referans hücreye dayalıdır, bu nedenle hücreleri birleştirdiğinizde, aralıktaki sol üst hücrenin biçimlendirme ayarları birleştirilmiş hücreye uygulanır. Hücre bölündüğünde, yeni hücreler orijinal format ayarlarını korur.

{{% /alert %}}

## **Bir Çalışma Sayfasında Hücreleri Birleştirme.**

### **Microsoft Excel Kullanımı**

Aşağıdaki adımlar, Microsoft Excel kullanarak çalışma sayfasındaki hücreleri nasıl birleştireceğinizi açıklar.

1. İstenen veriyi aralıktaki en sol üst hücreye kopyalayın.
2. Birleştirmek istediğiniz hücreleri seçin.
3. Bir satır veya sütunda hücreleri birleştirmek ve hücre içeriğini ortalamak için, **Biçimlendirme** araç çubuğundaki **Birleştir ve Ortala** simgesine tıklayın.

### **Aspose.Cells Kullanımı**

**[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)** sınıfı, görev için bazı yararlı yöntemlere sahiptir. Örneğin, **[**merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int))** yöntemi, hücreleri belirtilen hücre aralığı içinde tek bir hücreye birleştirir.

Aşağıdaki çıktı, aşağıdaki kodun çalıştırılmasından sonra oluşturulur.

**Hücreler (C6:E7) birleştirildi** 

![todo:image_alt_text](merging-and-unmerging-cells_2.png)

#### **Kod Örneği**

Aşağıdaki örnek, bir çalışsheet'te (C6:E7) hücrelerin nasıl birleştirileceğini göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **Hücreleri Ayırma (Birleştirmeyi Bölmek)**

### **Microsoft Excel Kullanımı**

Aşağıdaki adımlar, Microsoft Excel kullanarak birleştirilmiş hücreleri nasıl ayıracağınızı açıklar.

1. Birleştirilmiş hücreyi seçin. 
   Hücreler birleştirildiğinde, **Birleştir ve Ortala**, **Biçimlendirme** araç çubuğunda seçilidir.
1. **Biçimlendirme** araç çubuğunda **Birleştir ve Ortala**'ya tıklayın.

#### **Aspose.Cells Kullanımı**

**[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)** sınıfı, **[**unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int))** adlı bir yönteme sahiptir. Bu yöntem, hücreleri birleştirilmiş hücre aralığındaki hücre başvurusunu kullanarak ayrıştırır.

#### **Kod Örneği**

Aşağıdaki örnek, birleştirilmiş hücreleri (C6) nasıl ayıracağınızı göstermektedir. Örnek, önceki örnekte oluşturulan dosyayı kullanır ve birleştirilmiş hücreleri ayırır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **İlgili Makaleler**

- [Birleştirilmiş hücreleri bulma ve ayırma](/cells/tr/java/detect-merged-cells-in-a-worksheet/).
- [Aralık.merge() ve Aralık.unMerge() yöntemlerini kullanarak bir hücre aralığını birleştirme ve ayırma](/cells/tr/java/merge-or-unmerge-range-of-cells/).

