---
title: Geri Al ve Yeniden Yap Özelliğini Kullanma
type: docs
weight: 120
url: /tr/net/aspose-cells-griddesktop/use-undo-and-redo-feature/
keywords: GridDesktop, geri al, yeniden yap
description: Bu makale, GridDesktop ta geri alma ve yeniden yapma özelliğini tanıtıyor.
---

{{% alert color="primary" %}} 

GridDesktop'ın Geri Al/Yeniden Yap özelliği çok kullanışlıdır. Adı zaten işlevselliğini açıklıyor, çalışma sayfasında son yapılan işlem(ler)i geri alma/yeniden yapma olanağı sağlar. Örneğin, bir formül yanlışlıkla silinirse veya aslında istemediğiniz bir hücrede veri düzenlerseniz, kontrol tarafından sağlanan Geri Al ve Yeniden Yap işlemlerini kullanarak bu işlemleri düzeltebilirsiniz.

{{% /alert %}} 
## **Geri Alma ve Yeniden Yapma İşlemi Gerçekleştirme**
Görev için aşağıdaki API'ler mevcuttur. Her API ile ilgili açıklama verilmiştir, lütfen bunları kontrol edin.

- **GridDesktop.EnableUndo** - öznitelik: Geri alma işlevinin etkin olup olmadığını gösterir, varsayılan değer "false"dır.
- **UndoManager** – sınıf: Geri alma/yeniden yapma işlemini yönetmek için kullanılır.
- **GridDesktop.UndoManager** – öznitelik: **UndoManager** nesnesinin örneğini alır.
- **UndoManager.Undo** – yöntem: Geri alma işlemi gerçekleştirir.
- **UndoManager.Redo** – yöntem: Yeniden yapma işlemi gerçekleştirir.
- **UndoManager.ClearStack** – yöntem: Geri alma/yeniden yapma yığınını temizler.
- **UndoManager.UndoStepsCount** – öznitelik: Mevcut kullanılabilir geri alma adım sayısını alır.
- **UndoManager.RedoStepsCount** – öznitelik: Mevcut kullanılabilir yeniden yapma adım sayısını alır.
- **UndoManager.UndoStackSize** – öznitelik: Geri alma yığınını alır/ayarlar.
### **Geri Alma**
Aşağıdaki örnek kod, GridDesktop API'sını kullanarak Geri Alma işlemini nasıl uygulayacağınızı göstermektedir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **Yeniden Yap**
Aşağıdaki örnek kod, GridDesktop API'sını kullanarak Yeniden Yap işlemini nasıl uygulayacağınızı göstermektedir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

Şu anda, geri alma/yeniden yapma işlemi bir hücre değerindeki değişikliği ifade etmektedir.

{{% /alert %}}
