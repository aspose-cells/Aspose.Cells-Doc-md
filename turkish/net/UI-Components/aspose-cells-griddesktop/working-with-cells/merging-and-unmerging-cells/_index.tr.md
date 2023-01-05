---
title: GridDesktop'ta Cells'i Birleştirme ve Ayrılma
linktitle: Birleşme ve Ayrılma Cells
type: docs
weight: 90
url: /tr/net/merging-and-unmerging-cells-griddesktop/
---
{{% alert color="primary" %}} 

Bu konuda, bir çalışma sayfasının hücrelerini birleştirmenin ve ayırmanın yararlı bir özelliğini tartışacağız. Bu özellik, verilerin okunabilirliğini artırmak için bazı satırları veya sütunları yaymamız gereken durumlarda kullanışlıdır.

{{% /alert %}} 
## **Birleştirme Cells**
Hücreleri tek bir büyük hücrede birleştirmek için lütfen aşağıdaki adımları izleyin:

-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Oluşturmak**Cells aralığı** birleştirilecek
- **Birleştirmek** büyük bir hücreye hücre aralığı

 Kullanabilirsiniz**Birleştirmek** yöntemi**Çalışma kağıdı** hücreleri birleştirmek için. Ancak, kullanılarak bir hücre aralığı tanımlanabilir.**Hücre Aralığı** nesne.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **Ayrılıyor Cells**
Büyük bir hücreyi birçok hücreye ayırmak için lütfen aşağıdaki adımları izleyin:

-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
- Ayrılması gereken birleştirilmiş hücreye erişin
- **ayır** birleştirilmiş hücrenin konumunu kullanarak büyük hücreyi birçok hücreye

 Kullanabilirsiniz**ayır** yöntemi**Çalışma kağıdı** konumunu kullanarak bir hücreyi ayırmak için.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

Hücreleri tek bir hücrede birleştirdiğinizde, sol üstteki hücrenin (hücre aralığındaki) biçimlendirme ayarları birleştirilen hücreye uygulanır, ancak hücre birleştirilmediğinde, birleştirilmemiş tüm hücreler biçimlendirme ayarlarını korur.

{{% /alert %}}
