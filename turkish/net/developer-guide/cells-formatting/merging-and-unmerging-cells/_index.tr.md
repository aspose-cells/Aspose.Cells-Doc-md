---
title: Birleşme ve Ayrılma Cells
type: docs
weight: 190
url: /tr/net/merging-and-unmerging-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells bu özelliği destekler ve ayrıca bir çalışma sayfasındaki hücreleri birleştirebilir. Birleştirilmiş hücreleri de ayırabilir veya bölebilirsiniz. Birleştirilmiş bir hücrenin hücre referansı, orijinal seçili aralıktaki sol üst hücrenin referansıdır.

{{% /alert %}} 
## **Giriş**
Her satırda veya sütunda her zaman aynı sayıda hücre olmasını istemezsiniz. Örneğin, birkaç sütuna yayılan bir hücreye başlık koymak isteyebilirsiniz. Veya bir fatura oluşturuyorsanız, toplam için daha az sütun isteyebilirsiniz. İki veya daha fazla hücreden bir hücre yapmak için bunları birleştirin. Microsoft Excel, kullanıcıların elektronik tabloyu istedikleri gibi yapılandırmak için dosyaları seçip birleştirmesine olanak tanır.

{{% alert color="primary" %}} 

Hücreler birleştirildiğinde yalnızca sol üst hücrelerdeki verilerin tutulduğunu unutmayın. Aralıktaki diğer hücrelerde veri varsa bu veri silinir.
Biçimlendirme de aynı şekilde referans hücreyi temel alır, böylece hücreleri birleştirdiğinizde, aralıktaki sol üst hücrenin biçimlendirme ayarları birleştirilen hücreye uygulanır. Hücre bölündüğünde, yeni hücreler orijinal biçim ayarlarını korur.

{{% /alert %}} 
## **Cells'i Çalışma Sayfasında Birleştirme**
### **Cells'i Microsoft Excel'de birleştirme**
Aşağıdaki adımlarda MS Excel kullanılarak çalışma sayfasındaki hücrelerin nasıl birleştirileceği açıklanmaktadır.

1. İstediğiniz verileri aralık içinde en sol üstteki hücreye kopyalayın.
1. Birleştirmek istediğiniz hücreleri seçin.
1.  Bir satır veya sütundaki hücreleri birleştirmek ve hücre içeriğini ortalamak için,**Birleştir ve Ortala** üzerindeki simge**biçimlendirme** araç çubuğu.
### **Cells ile Aspose.Cells birleştirme**
Aspose.Cells.Cells Sınıfı, görev için bazı yararlı yöntemlere sahiptir. Örneğin, Merge() yöntemi, hücreleri belirli bir aralıktaki tek bir hücrede birleştirir.

Aşağıdaki örnek, bir çalışma sayfasındaki hücrelerin (C6:E7) nasıl birleştirileceğini gösterir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
## **Ayrılıyor (Bölünüyor) Birleştirildi Cells**
### **Microsoft Excel'i kullanma**
Aşağıdaki adımlarda, birleştirilmiş hücrelerin Microsoft Excel kullanılarak nasıl bölüneceği açıklanmaktadır.

1. Birleştirilmiş hücreyi seçin.
 Hücreler birleştirildiğinde,**Birleştir ve Ortala** üzerinde seçilir**biçimlendirme** araç çubuğu.
1.  Tıklamak**Birleştir ve Ortala** üzerinde**biçimlendirme** araç çubuğu.
### **Aspose.Cells'i kullanma**
Aspose.Cells.Cells sınıfı, hücreleri orijinal durumlarına bölen UnMerge() adlı bir yönteme sahiptir. Yöntem, birleştirilmiş hücre aralığındaki hücre referansını kullanarak hücreleri ayırır.

Aşağıdaki örnek, birleştirilmiş hücrelerin nasıl bölüneceğini gösterir (C6). Örnek, önceki örnekte oluşturulan dosyayı kullanır ve birleştirilmiş hücreleri böler.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


## **ileri konular**
- [Çalışma Sayfasında Birleştirilmiş Cells'i Algıla](/cells/tr/net/detect-merged-cells-in-a-worksheet/)
