---
title: Birleştir ve Ayır Cells
type: docs
weight: 60
url: /tr/net/merge-and-unmerge-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb, hücreleri tek bir büyük hücrede birleştirmenizi sağlayan kullanışlı bir yardımcı program özelliğine sahiptir. Bu konu, hücrelerin program aracılığıyla nasıl birleştirileceğini açıklar.

{{% /alert %}} 
## **Birleştirme Cells**
Cells koleksiyonunun Merge yöntemini çağırarak bir çalışma sayfasındaki birden çok hücreyi tek bir hücrede birleştirin. Merge yöntemi çağrılırken birleştirilecek hücre aralığını belirtin.

{{% alert color="primary" %}} 

Birden çok hücreyi birleştirirseniz ve her hücre veri içeriyorsa, birleştirmeden sonra yalnızca aralıktaki sol üst hücrenin içeriği korunur. Diğer hücrelerdeki veriler kaybolmaz. Hücreleri ayırırsanız, her hücre kendi verilerini kurtarır.

{{% /alert %}} 

**Dört hücre tek hücrede birleştirildi** 

![yapılacaklar:resim_alternatif_metin](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **Ayrılıyor Cells**
Hücreleri ayırmak için, Merge yöntemiyle aynı parametreleri alan ve hücrelerin ayrılmasını gerçekleştiren Cells koleksiyonunun UnMerge yöntemini kullanın.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
