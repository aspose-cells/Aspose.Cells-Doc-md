---
title: Bir Çalışma Sayfasında Resimleri Yönetme
type: docs
weight: 100
url: /tr/net/aspose-cells-griddesktop/manage-pictures-in-a-worksheet/
keywords: GridDesktop, resim, resimler
description: Bu makale, GridDesktop ta çalışsayfasındaki resimlerle nasıl çalışılacağını tanıtır.
---

{{% alert color="primary" %}} 

Çoğu insan, bir resmin birkaç kelimeyi daha iyi açıklayabileceğine inanır. Bu nedenle Aspose.Cells.GridDesktop, insanların bu inancını gerçekleştirmek için çalışsayfasına resim eklemeyi destekler. Bu konuda, çalışsayfalarına resim eklemek ve bu resimleri yönetmek konusunu tartışacağız.

{{% /alert %}} 
## **Resim Ekleme**
Aspose.Cells.GridDesktop kullanarak bir hücreye bağlantı eklemek için lütfen aşağıdaki adımları izleyin:

- **Form**'unuza Aspose.Cells.GridDesktop kontrolünü ekleyin
- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- **Resim'in işleneceği dosya yolunu ve resmin ekleneceği hücre adını belirterek** çalışsayfaya **Resim** ekleyin

**Çalışsayfa** nesnesindeki **Resimler** koleksiyonu, aşırı yüklenmiş bir **Ekle** yöntemi sağlar. Geliştiriciler, belirli ihtiyaçlarına göre **Ekle** yönteminin herhangi bir aşırı yüklenmiş sürümünü kullanabilir. Bu aşırı yüklenmiş **Ekle** yöntemlerini kullanarak, dosyadan, akıştan veya **Resim** nesnesinden resim eklemek mümkündür.

Aşağıda, çalışsayfalara resim eklemek için örnek kod bulunmaktadır.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **Resimlere Erişme**
Çalışsayfadaki mevcut bir resme erişmek ve değiştirmek için, geliştiriciler resmi basitçe **Resimler** koleksiyonundan erişebilir. Resmi eklenen hücreyi belirterek (hücre adını veya satır ve sütun numarası olarak konumunu kullanarak). Resme erişildiğinde geliştiriciler, çalışma zamanında resmin İmgesini değiştirebilirler.

Aşağıda, bir çalışma sayfasındaki resimlere erişmek ve değiştirmek için örnek kod bulunmaktadır.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **Resimleri Kaldırma**
Mevcut bir resmi kaldırmak için, geliştiriciler basitçe istenen çalışma sayfasına erişebilir ve ardından resmin bulunduğu hücreyi belirterek **Resimler** koleksiyonundan resmi **Kaldırabilir**.

Aşağıdaki kodda, çalışma sayfasından resimleri nasıl kaldıracağınız gösterilmektedir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
