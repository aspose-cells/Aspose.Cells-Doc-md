---
title: Cell Değerine Erişme ve Değiştirme
type: docs
weight: 20
url: /tr/net/accessing-and-modifying-the-value-of-a-cell/
---
{{% alert color="primary" %}} 

Bir önceki konumuzda, bir çalışma sayfasının hücrelerine erişme konusunu ele almıştık. Bu başlıkta, geliştiricilere API veya Aspose.Cells.GridDesktop kullanarak hücrelerin değerlerine nasıl erişebileceklerini ve bunları değiştirebileceklerini göstermek için bu konuyu genişleteceğiz.

{{% /alert %}} 
## **Aspose.Cells.GridDesktop kullanarak Cell Değerine Erişin ve Değiştirin**
 Bir hücreye erişmeden ve değerini değiştirmeden önce, hücrelere nasıl erişeceğimizi bilmeliyiz. Bir çalışma sayfasının hücrelerine erişmek için üç yaklaşım vardır. Bu üç yaklaşım hakkında daha fazla ayrıntı için lütfen[Bir Çalışma Sayfasında Cells'e erişme.](/cells/tr/net/accessing-cells-in-a-worksheet/)

Her hücrenin Value adlı bir özelliği vardır. Böylece, bir hücreye erişildiğinde, geliştiriciler bir hücrenin değerine erişmek ve değerini değiştirmek için Value özelliğinin içeriğine erişebilir ve içeriğini değiştirebilir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**ÖNEMLİ:**Değerini değiştirmek için bir hücrenin Value özelliğini kullanmak, tek veya birkaç hücrenin değerini ayarlamak için iyi bir yaklaşımdır. Birçok hücrenin değerlerini ayarlamanız gerekiyorsa, bu yaklaşımın performansı iyi olmaz. Bu nedenle, birçok hücrenin değerlerini ayarlamak için kullanmalısınız.**Hücre Değerini Ayarla** uygulamalarınızın performansını artırmak için hücre yöntemi. Yukarıdaki kod parçacığının değiştirilmiş bir sürümü kullanılarak**Hücre Değerini Ayarla** yöntem aşağıda gösterilmiştir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
