---
title: GridDesktop ta Hücreleri Birleştirme ve Ayırma
linktitle: Hücreleri Birleştirme ve Ayırma
type: docs
weight: 90
url: /tr/net/aspose-cells-griddesktop/merge-and-unmerge-cells-griddesktop/
keywords: GridDesktop, birleştirme, ayırma
description: Bu makale GridDesktop ta birleştirme ve ayırma işlemlerini tanıtıyor.
---

{{% alert color="primary" %}} 

Bu konuda, bir çalışsayfadaki hücreleri birleştirme ve ayırma işlevini tartışacağız. Bu özellik, verilerin okunabilirliğini artırmak için bazı satırları veya sütunları kapsamamız gerektiği durumlarda kullanışlıdır.

{{% /alert %}} 
## **Hücreleri Birleştirme**
Birden çok hücreyi tek büyük hücre haline getirmek için lütfen aşağıdaki adımları izleyin:

- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- Birleştirilecek **Hücre Aralığı** oluşturun
- Hücre aralığını tek büyük hücre haline getirin

Hücreleri birleştirmek için **Worksheet**'in **Birleştir** yöntemini kullanabilirsiniz. Ancak, bir hücre aralığı, **CellRange** nesnesi kullanılarak tanımlanabilir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **Hücreleri Ayırma**
Bir büyük hücreyi birden çok hücreye ayırmak için lütfen aşağıdaki adımları izleyin:

- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- Ayırılması gereken birleşik hücreye erişin
- Ayırılan büyük hücreyi, birleşik hücrenin konumunu kullanarak birden çok hücreye ayırın

Bir hücrenin konumunu kullanarak **Worksheet**'in **Ayır** yöntemini kullanarak hücreleri ayırabilirsiniz.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

Hücreleri tek bir hücreye birleştirdiğinizde, (hücre aralığı içinde) sol üst hücrenin biçimlendirme ayarları birleştirilmiş hücreye uygulanır, ancak hücre ayrılmışsa, tüm ayrılan hücreler kendi biçimlendirme ayarlarını korur.

{{% /alert %}}
