---
title: Çalışma Sayfasında Hyperlinkleri Yönetme
type: docs
weight: 90
url: /tr/net/aspose-cells-griddesktop/manage-hyperlinks-in-a-worksheet/
keywords: GridDesktop,hyper,link,hyperlink,hyperlinks
description: Bu makale, GridDesktop ta hyperlink ile çalışmayı nasıl tanıtacağınızı açıklar.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop kullanarak, bir çalışma sayfasındaki hücrelerde depolanan basit değerlere hyperlink eklemek de mümkündür. Diyelim ki bazı hücrelerde, kullanıcıları bir web sayfasında daha detaylı bilgilerle ilişkilendirmek istediğiniz değerleriniz olsun. Bu durumda, bir kullanıcı hücreye tıkladığında o sayfaya yönlendirilmesi istenir. Bu konuda, geliştiricilerin çalışma sayfalarında hyperlink ekleyip değiştirebilmeleri konusunu açıklayacağız.

{{% /alert %}} 
## **Hyperlinkler Ekleme**
Aspose.Cells.GridDesktop kullanarak bir hücreye bağlantı eklemek için lütfen aşağıdaki adımları izleyin:

- **Form**'unuza Aspose.Cells.GridDesktop kontrolünü ekleyin
- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- Bağlantı eklenecek çalışsayfadaki istenen **Hücre**'ye erişin
- Bağlantı eklenmek istenen hücreye bir değer ekleyin
- Bağlantı uygulanacak hücreyi belirterek **Çalışsayfa**'ya **Bağlantı** ekleyin

**Çalışsayfa** nesnesindeki **Bağlantılar** koleksiyonu, aşırı yüklenmiş bir **Ekle** yöntemi sağlar. Geliştiriciler, belirli ihtiyaçlarına göre **Ekle** yönteminin herhangi bir aşırı yüklenmiş sürümünü kullanabilir.

Aşağıdaki kod, çalışsayfanın **B2** ve **C3** hücrelerine bağlantı ekleyecektir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **Bağlantıları Erişme**
Bir hücreye bağlantı eklendikten sonra, bağlantıya erişilmesi ve çalışma zamanında değiştirilmesi de gerekebilir. Bunun için geliştiriciler, Basitleştirilmiş Çalışsayfa'nın **Bağlantılar** koleksiyonundan bağlantıya basitçe erişebilirler ve bağlanacak hücreyi belirterek bağlantıyı değiştirebilirler (hücre adını veya satır ve sütun numarası olarak konumunu kullanarak). Bağlantıya erişildiğinde geliştiriciler, çalışma zamanında URL'sini değiştirebilirler.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **Bağlantıları Kaldırma**
Mevcut bir bağlantıyı kaldırmak için, geliştiriciler basitçe istenen çalışma sayfasına erişebilir ve ardından **Bağlantılar** koleksiyonundan bağlantıyı belirterek (adını veya satır ve sütun numarasını kullanarak) bağlantıyı **Kaldırabilir**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

Eğer bir hücreye bağlantı eklemek istiyorsanız ve bu bağlantının değer yerine hücredeki bağlantı URL'sinin görüntülenmesini istiyorsanız, hücreye herhangi bir değer eklemeyin ve bağlantıyı basitçe ekleyin. Bunu yaparak hücre bağlantılı olacak ve bağlantı URL'si aynı zamanda hücrede değeri olarak da görüntülenecektir.

{{% /alert %}}
