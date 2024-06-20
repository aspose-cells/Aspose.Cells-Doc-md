---
title: Bir Hücrenin Değerine Erişme ve Değiştirme
type: docs
weight: 20
url: /tr/net/aspose-cells-griddesktop/accessing-and-modifying-the-value-of-a-cell/
keywords: GridDesktop,cell,modify cell,get cell,modify cell value,get cell value
description: Bu makale, GridDesktop teki Çalışsayfadaki hücre değerini (GridCell) nasıl alacağınızı ve değiştireceğinizi tanıtır.
---

{{% alert color="primary" %}} 

Önceki konumuzda, çalışsayfadaki hücrelere erişimden bahsettik. Bu konuda, geliştiricilere nasıl erişip hücre değerlerini API'sini kullanarak nasıl değiştirebileceklerini göstermek için bu konuyu sadece o konuya genişleteceğiz.

{{% /alert %}} 
## **Aspose.Cells.GridDesktop Kullanarak Hücre Değerine Erişme ve Değiştirme**
Bir hücrenin değerine erişmeden ve değiştirmeden önce, hücrelere nasıl erişileceğini bilmemiz gerekmektedir. Bir çalışsayfanın hücrelerine erişmenin üç yaklaşımı vardır. Bu üç yaklaşım hakkında daha fazla bilgi için lütfen [Bir Çalışsayfadaki Hücrelere Erişim](/cells/tr/net/accessing-cells-in-a-worksheet/) sayfasına bakın.

Her hücrenin Value adında bir özelliği vardır. Dolayısıyla, bir hücreye eriştikten sonra, geliştiriciler, hücrenin içeriğine erişip değiştirmek için Value özelliğinin içeriğine erişebilirler.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**ÖNEMLİ:** Bir hücrenin değerini değiştirmek için Value özelliğini kullanmak, tek veya birkaç hücrenin değerini ayarlamak için iyi bir yaklaşımdır. Eğer birçok hücrenin değerlerini ayarlamanız gerekiyorsa, bu yaklaşımın performansı iyi olmayacaktır. Bu nedenle, birçok hücrenin değerlerini ayarlamak için uygulamalarınızın performansını artırmak için hücrenin **SetCellValue** yöntemini kullanmalısınız. **SetCellValue** yöntemini kullanarak yukarıdaki kod parçasının modifiye edilmiş bir versiyonu aşağıda gösterilmektedir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
