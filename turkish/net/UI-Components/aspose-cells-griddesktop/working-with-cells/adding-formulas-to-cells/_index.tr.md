---
title: Cells'e Formüller Ekleniyor
type: docs
weight: 30
url: /tr/net/adding-formulas-to-cells/
---
{{% alert color="primary" %}} 

Bir hücre yalnızca sayısal bir şekil veya bazı metinler gibi basit bir değer içeremez, aynı zamanda bir hücreye değeri olarak bir formül de ekleyebiliriz. Bazı hesaplamalardan sonra bir hücrenin değerinin belirlenmesi gerektiğinde, hücrede bir formül kullanılır. Bu konuda, bir hücrede uygulanan bir formüle nasıl erişebileceğimizi ve değiştirebileceğimizi tartışacağız.

{{% /alert %}} 
## **Cell'e Formül Ekleme**
 Bir hücreye formül eklemek, önceki konumuzda tartıştığımız gibi, hücrenin değerini ayarlamak gibidir:[Bir Cell Değerine Erişme ve Değeri Değiştirme](/cells/tr/net/accessing-and-modifying-the-value-of-a-cell/) ancak bu durumda, hücrelere sadece basit değerler ekledik. Şimdi formülleri ekleyeceğiz. Geliştiriciler, formüle erişmek ve formülde değişiklik yapmak veya başka bir şekilde değiştirmek için bir hücrenin Value özelliğini kullanabilir.**Hücre Değerini Ayarla** hücre yöntemi, bir hücreye formül eklemek veya değiştirmek için de kullanılabilir.

**ÖNEMLİ:** Value özelliğini kullanma arasındaki temel fark veya**Hücre Değerini Ayarla** bir hücrenin yöntemi, Value özelliğinin çağırmasıdır.**Tüm Formülleri Çalıştır** durumunda olduğu gibi tüm formüllerin değerlerini yeniden hesaplamak için Grid yöntemi**Hücre Değerini Ayarla** yöntem geliştiricilerin araması gerekir**Tüm Formülleri Çalıştır** yöntemi açıkça formüller hücrelere eklendikten sonra. Aslında, kullandığımızda**Hücre Değerini Ayarla** bir hücre yöntemi, daha sonra bu yöntem hücrenin değerini şu şekilde ayarlar:**Formül Türü** sadece ve formülü hesaplamayın. Üstelik arama**Tüm Formülleri Çalıştır**yöntem her zaman gerekli değildir. Bir çalışma sayfasının hücrelerine çok sayıda formül eklemek istiyorsanız, arayabilirsiniz.**Tüm Formülleri Çalıştır** sonunda sadece bir kez yöntem.

 Bir hücreye dize değeri olarak bir formül eklenir. Ayrıca formül yapısı MS Excel'in formül yapısı ile uyumlu olmalıdır. Tüm formüller bir ile başlamalıdır**Eşittir İşareti (=)**.

 Aşağıda verilen örnekte, çalışma sayfasının iki hücresinin değerlerini çarpmak ve sonucu başka bir hücreye kaydetmek için bir formül ekledik.**Tüm Formülleri Çalıştır** yöntem ayrıca sonunda çağrılır.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



Şimdi uygulamayı çalıştırın. Formülün eklendiği hücreye çift tıklarsanız, değerin arka uçta değeri gerçekten hesaplayan formülle değiştirileceğini fark edeceksiniz.

{{% alert color="primary" %}} 

 Aspose.Cells.GridDesktop, MS Excel'in yaygın olarak kullanılan işlevlerinin çoğunu destekler. Desteklenen işlevlerin listesi hakkında daha fazla ayrıntı için lütfen[buraya tıklayın.](/cells/tr/net/list-of-supported-functions/)

{{% /alert %}}
