---
title: Geri Al ve Yinele Özelliğini Kullanma
type: docs
weight: 120
url: /tr/net/using-undo-and-redo-feature/
---
{{% alert color="primary" %}} 

GridDesktop'ın Geri Al/Yinele özelliği çok kullanışlıdır. Ad, işlevselliğini kendisi açıklar, bir çalışma sayfasındaki son işlemleri geri almanıza/yeniden yapmanıza olanak tanır. Örneğin, bir formül yanlışlıkla silinirse veya bir hücrede aslında istemediğiniz bir veriyi düzenlerseniz, bu eylemler, kontrol tarafından sağlanan Geri Al ve Yinele işlemleri kullanılarak düzeltilebilir.

{{% /alert %}} 
## **Geri Alma ve Yineleme İşlemini Gerçekleştirme**
Aşağıdaki API'ler görev için kullanılabilir. Açıklama her API ile verilmiştir, lütfen kontrol ediniz.

- **GridDesktop.EnableUndo** - nitelik: Geri Al işlevinin etkin olup olmadığını gösterir, varsayılan değer "yanlış" tır.
- **Yöneticiyi Geri Al** – class: Geri alma/yineleme işlemini yönetmek için kullanılır.
- **GridDesktop.UndoManager** – öznitelik: örneğini alır**Yöneticiyi Geri Al** nesne.
- **Geri AlManager.Geri Al** – method: Bir geri alma işlemi gerçekleştirir.
- **UndoManager.Redo -** method: Redo işlemini gerçekleştirir.
- **UndoManager.ClearStack** – method: Geri alma/yineleme yığınını temizler.
- **UndoManager.UndoStepsCount** – öznitelik: Mevcut mevcut geri alma adımlarının sayısını alır.
- **UndoManager.RedoStepsCount** – öznitelik: Mevcut mevcut yineleme adımlarının sayısını alır.
- **UndoManager.UndoStackSize** – nitelik: Geri alma yığın boyutunu alır/ayarlar.
### **Geri alma**
Aşağıdaki örnek kod, GridDesktop API kullanılarak Geri Al işleminin nasıl uygulanacağını gösterir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **Yeniden yap**
Aşağıdaki örnek kod, GridDesktop API kullanılarak Redo işleminin nasıl uygulanacağını gösterir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

Şu anda, geri alma/yineleme işlemi, bir hücre değerindeki değişikliği ifade eder.

{{% /alert %}}
