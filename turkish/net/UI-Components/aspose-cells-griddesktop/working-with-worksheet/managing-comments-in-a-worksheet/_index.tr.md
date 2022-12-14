---
title: Bir Çalışma Sayfasındaki Yorumları Yönetme
type: docs
weight: 110
url: /tr/net/managing-comments-in-a-worksheet/
---
{{% alert color="primary" %}} 

MS Excel'de, kullanıcıların hücrelere yorum eklemesine izin veren yorumlar özelliğini biliyor olmalısınız. Bu özellik, kullanıcılara hücrelere değer girmek üzereyken bazı bilgiler verilmesi gerektiğinde yardımcı olur. Bir kullanıcı, fare imlecini yorum yapılan bir hücreye getirdiğinde, kullanıcıya bazı bilgiler sağlamak için küçük bir açılır mesaj görüntülenir. Geliştiriciler, Aspose.Cells.GridDesktop kullanarak hücreler üzerinde yorumlar oluşturabilir. Bu konumuzda bu özelliğin kullanımını detaylı bir şekilde anlatacağız.

{{% /alert %}} 
## **Yorum Ekleme**
Aspose.Cells.GridDesktop kullanarak bir hücreye yorum eklemek için lütfen aşağıdaki adımları izleyin:

-  Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Ekle**Yorum** yorumun ekleneceği hücreyi (adını veya satır ve sütun numarasını kullanarak) belirterek çalışma sayfasına ekleyin.

 Aşağıdaki kod, şuraya yorum ekleyecektir:**b2** ve**b4** çalışma sayfasının hücreleri.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


**Yorumlar** koleksiyonunda**Çalışma kağıdı** nesne aşırı yükleme sağlar**Ekle** yöntem. Geliştiriciler, herhangi bir aşırı yüklenmiş sürümünü kullanabilir**Ekle** özel ihtiyaçlarına göre yöntem.
## **Yorumlara Erişim**
Çalışma sayfasındaki mevcut bir yoruma erişmek ve üzerinde değişiklik yapmak için geliştiriciler, çalışma sayfasından yoruma erişebilir.**Yorumlar** koleksiyonu**Çalışma kağıdı** yorumun eklendiği hücreyi belirterek (hücre adını veya satır ve sütun numarası cinsinden konumunu kullanarak). Yoruma erişildikten sonra, geliştiriciler çalışma zamanında Metnini değiştirebilir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **Yorumları Kaldırma**
 Mevcut bir yorumu kaldırmak için, geliştiriciler basitçe istenen bir çalışma sayfasına erişebilir ve ardından**Kaldırmak** gelen yorum**Yorumlar** koleksiyonu**Çalışma kağıdı** Yorum içeren hücreyi (adını veya satır ve sütun numarasını kullanarak) belirterek.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
