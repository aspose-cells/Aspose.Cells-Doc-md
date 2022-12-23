---
title: Çalışma Sayfasındaki Resimleri Yönetme
type: docs
weight: 100
url: /tr/net/managing-pictures-in-a-worksheet/
---
{{% alert color="primary" %}} 

İnsanların çoğu, bir resmin her şeyi kelimelerden daha iyi açıklayabileceğine inanır. Bu yüzden Aspose.Cells.GridDesktop insanların bu inancını gerçekleştirmek için çalışma sayfalarına resim eklenmesini desteklemektedir. Bu konuda, çalışma sayfalarına resim ekleme ve değiştirme hakkında konuşacağız.

{{% /alert %}} 
## **Resim Ekleme**
Aspose.Cells.GridDesktop kullanarak bir hücreye köprü eklemek için lütfen aşağıdaki adımları izleyin:

-  Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Eklemek**Resim** resmin dosya yolunu ve resmin ekleneceği hücre adını belirterek çalışma sayfasına

**resimler** koleksiyonunda**Çalışma kağıdı** nesne aşırı yükleme sağlar**Eklemek** yöntem. Geliştiriciler, herhangi bir aşırı yüklenmiş sürümünü kullanabilir**Eklemek** özel ihtiyaçlarına göre yöntem. Bu aşırı yüklenmiş sürümlerini kullanarak**Eklemek** yöntemiyle, dosyadan, akıştan veya**resim** nesne.

Çalışma sayfalarına resim eklemek için örnek kod aşağıdadır.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **Resimlere Erişme**
 Çalışma sayfasındaki mevcut bir resme erişmek ve üzerinde değişiklik yapmak için, geliştiriciler resme**resimler** koleksiyonu**Çalışma kağıdı** resmin eklendiği hücreyi (hücre adını veya satır ve sütun numarası cinsinden konumunu kullanarak) belirterek. Resme erişildikten sonra, geliştiriciler çalışma zamanında Resmini değiştirebilir.

Bir çalışma sayfasındaki resimlere erişmek ve bunları değiştirmek için örnek kod aşağıdadır.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **Resimleri Kaldırma**
 Mevcut bir resmi kaldırmak için, geliştiriciler basitçe istenen bir çalışma sayfasına erişebilir ve ardından**Kaldırmak** gelen resim**resimler** koleksiyonu**Çalışma kağıdı** resmi içeren hücreyi (adını veya satır ve sütun numarasını kullanarak) belirterek.

Aşağıdaki kodda resimlerin çalışma sayfasından nasıl çıkarılacağı gösterilmektedir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
