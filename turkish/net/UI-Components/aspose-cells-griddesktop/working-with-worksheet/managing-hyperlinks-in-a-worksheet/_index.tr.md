---
title: Çalışma Sayfasında Köprüleri Yönetme
type: docs
weight: 90
url: /tr/net/managing-hyperlinks-in-a-worksheet/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop kullanarak, bir çalışma sayfasının hücrelerinde saklanan basit değerlere köprüler eklemek de mümkündür. Diyelim ki bazı hücrelerde, bir web sayfasındaki daha ayrıntılı bilgilerle ilişkilendirmek istediğiniz bazı değerleriniz olabilir. Bu durumda, o hücreye bir köprü eklenmesi arzu edilir, böylece bir kullanıcı hücreye tıklarsa o web sayfasına yönlendirilir. Bu konuda, geliştiricilerin çalışma sayfalarına köprüleri nasıl ekleyebileceklerini ve değiştirebileceklerini açıklayacağız.

{{% /alert %}} 
## **Köprü Ekleme**
Aspose.Cells.GridDesktop kullanarak bir hücreye köprü eklemek için lütfen aşağıdaki adımları izleyin:

-  Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  İstenilen erişim**Cell** köprülenecek çalışma sayfasında
- Köprülenecek hücreye bir miktar değer ekleyin
-  Eklemek**köprü** köprünün uygulanacağı hücre adını belirterek çalışma sayfasına

**köprüler** koleksiyonunda**Çalışma kağıdı** nesne aşırı yükleme sağlar**Eklemek** yöntem. Geliştiriciler, herhangi bir aşırı yüklenmiş sürümünü kullanabilir**Eklemek** özel ihtiyaçlarına göre yöntem.

 Aşağıdaki kod, bir köprü ekleyecektir**B2** ve**C3** çalışma sayfasının hücreleri.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **Köprülere Erişim**
Bir hücreye köprü eklendiğinde, çalışma zamanında köprüye erişmek ve köprüyü değiştirmek de gerekebilir. Bunu yapmak için, geliştiriciler köprüye yalnızca**köprüler** koleksiyonu**Çalışma kağıdı** köprünün eklendiği hücreyi belirterek (hücre adını veya satır ve sütun numarası cinsinden konumunu kullanarak). Köprüye erişildikten sonra, geliştiriciler çalışma zamanında URL'sini değiştirebilir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **Köprüleri Kaldırma**
 Mevcut bir köprüyü kaldırmak için, geliştiriciler basitçe istenen bir çalışma sayfasına erişebilir ve ardından**Kaldırmak** gelen köprü**köprüler** koleksiyonu**Çalışma kağıdı** köprülü hücreyi belirterek (adını veya satır ve sütun numarasını kullanarak).



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

Bir hücreye köprü eklemek istiyorsanız ve hücrede bir değer yerine köprü URL'sini görüntülemek istiyorsanız, hücreye herhangi bir değer eklemeyin ve köprüyü o hücreye ekleyin. Bunu yaptığınızda, hücre köprülenecek ve köprü URL'si de hücrede değeri olarak görüntülenecektir.

{{% /alert %}}
