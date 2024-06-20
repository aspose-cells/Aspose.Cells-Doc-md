---
title: Hücreleri Birleştirme ve Ayırma
type: docs
weight: 60
url: /tr/net/aspose-cells-gridweb/merge-and-unmerge-cells/
keywords: GridWeb, birleştir,ayır
description: Bu makale, GridWeb de hücreleri birleştirme/ayırma konusunu tanıtır.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb, hücreleri tek büyük bir hücreye birleştirmenizi sağlayan kullanışlı bir özellik içermektedir. Bu konu, hücreleri programlı olarak nasıl birleştireceğinizi açıklar.

{{% /alert %}} 
## **Hücreleri Birleştirme**
Çoklu hücreyi bir çalışma sayfasındaki tek bir hücreye Cells koleksiyonunun Merge yöntemini çağırarak birleştirin. Merge yöntemini çağırırken birleştirilecek hücre aralığını belirtin.

{{% alert color="primary" %}} 

Birden fazla hücreyi birleştirirseniz ve her hücre veri içeriyorsa, birleştirme sonrasında aralıktaki sol üst hücrenin içeriği elde tutulur. Diğer hücrelerdeki veriler kaybolmaz. Hücreleri ayırırsanız, her hücre kendi verilerini geri alır.

{{% /alert %}} 

**Dört hücre tek bir hücreye birleştirildi** 

![todo:image_alt_text](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **Hücreleri Ayırma**
Hücreleri ayırmak için, Merge yönteminin aynı parametreleri alan ve hücreleri ayırma işlemini gerçekleştiren Cells koleksiyonunun UnMerge yöntemini kullanın.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
