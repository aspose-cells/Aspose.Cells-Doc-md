---
title: Çalışsayfada Hiperbağlantıları Yönetme
type: docs
weight: 100
url: /tr/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/
keywords: GridWeb, hyperlink
description: Bu makale, GridWeb de hyperlink ile nasıl çalışılacağını tanıtır.
---

{{% alert color="primary" %}} 

Bu konu Aspose.Cells.GridWeb'de desteklenen bağlantı türlerini ve bunları programlı olarak nasıl yöneteceğinizi tartışmaktadır. Bağlantılar, web URL'lerine bağlantı oluşturmak veya sunucuya postback yapmak için kullanılabilir.

{{% /alert %}} 
## **Hiperbağlantıyla Çalışma**
### **Bağlantı Türleri**
Genellikle, Aspose.Cells.GridWeb tarafından desteklenen aşağıdaki hiperbağlantılar:

- [URL hiperbağlantıları](/cells/tr/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), web URL'lerine bağlanabilen hiperbağlantılar.
- [Metin hiperbağlantıları](/cells/tr/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), metne uygulanan URL hiperbağlantıları.
- [Görüntü hiperbağlantıları](/cells/tr/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), görüntülere uygulanan URL hiperbağlantıları.
- [Hücre işlemi hiperbağlantıları](/cells/tr/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), sunucuya veri gönderen hiperbağlantılar. Bu tür hiperbağlantılar, tıklandığında sunucu taraflı bir etkinlik başlatan bir düğme gibi davranır.

Aşağıdaki bölümler, tüm hiperbağlantı türlerinin ayrıntılı kullanımını açıklar. Ayrıca bağlantılara erişme veya kaldırma konuları da tartışılır.
### **Hyperlinkler Ekleme**

#### **URL Hiperbağlantıları**
URL hiperbağlantıları, genellikle web sitelerinde gördüğünüz basit bağlantılara daha çok benzer. Bir URL hiperbağlantısı, hücrede bir çapa gibi çalışır. Tıkladığınızda web sayfasına gitmek veya yeni bir tarayıcı penceresi açmak gibi işlev görür.

Farklı türde URL hiperbağlantıları bulunmaktadır:

- Metin hiperbağlantıları.
- Resim hiperbağlantıları.

Geliştiriciler, hiperbağlantı için bir resim belirleyebilirler. Eğer bir resim belirtilmemişse, bir metin hiperbağlantısı oluşturulur; aksi halde bir resim hiperbağlantısı oluşturulur.


##### **Metin Hiperbağlantıları**
Bir çalışma sayfasına metin hiperbağlantısı eklemek için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Bir çalışsayı açın.
1. Bir hücreye bir hiperbağlantı ekleyin.
1. Hücrede gösterilecek metni ayarlayın.
1. Hiperbağlantının URL'sini ayarlayın.
1. Hiperbağlantının hedefini isteğe bağlı olarak ayarlayın.
1. İstenirse bir araç ipucu ayarlayın.

{{% alert color="primary" %}} 

NOT: Hiperbağlantı hedefi, web URL'lerini yeni, mevcut veya en üst pencerede açmak için sırasıyla _self, _top veya _parent olarak ayarlanabilir.

{{% /alert %}} 

Aşağıdaki örnek, bir çalışma sayfasına iki hiperbağlantı ekler. Biri hedefi olmaksızın, diğeri ise _parent olarak ayarlanmıştır.

**Çıktı: çalışma sayfasına eklenen metin bağlantıları** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **Resim Hiperbağlantıları**
Bir resim hiperbağlantısı eklemek için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Bir çalışsayı açın.
1. Bir hücreye bir bağlantı ekleyin.
1. Hiperbağlantı olarak görüntülenecek resmin URL'sini ayarlayın.
1. Hiperbağlantının URL'sini ayarlayın.
1. İstenirse bir araç ipucu ayarlayın.
1. İsteniyorsa hiperbağlantı metnini ayarlayın.

**Çıktı: çalışma sayfasına eklenen resim hiperbağlantıları** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

Setting the image hyperlink's AltText fills a similar function as setting an <ALT> tag in HTML. The text is displayed only if the hyperlinked image is not displayed. (For example, if the image isn't at the specified location.) If the image of the second hyperlink is not found, the output of the code snippet below would look as follows.

**Resim URL'si bulunamadı** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Hücre Komut Hiperbağlantıları**
Hücre komut hiperbağlantısı, bir web sayfası açmak yerine sunucu tarafında bir olayı tetikleyen özel bir hiperbağlantı türüdür. Geliştiriciler, hiperbağlantıya tıklandığında sunucu tarafı olayına kod ekleyebilir ve herhangi bir görevi gerçekleştirebilir. Bu özellik, geliştiricilere daha etkileşimli uygulamalar oluşturmalarını sağlar.

Hücre komutu bağlantısını eklemek için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Bir çalışsayı açın.
1. Bir hücreye bir bağlantı ekleyin.
1. Bağlantının Komutunu istenen herhangi bir değere ayarlayın.
   Değer, bağlantının olay işleyicisi tarafından tanınması için kullanılır.
1. İstenirse bir araç ipucu ayarlayın.
1. Bağlantı olarak görüntülenecek Görüntü için URL'yi ayarlayın.

**Çalışma sayfasına bir hücre komut bağlantısı eklenmiş.** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Hücre Komutu Bağlantılarının Olay İşlemesi**
Geliştiriciler, belirli bir hücre komutu bağlantısı tıklandığında belirli görevleri gerçekleştirmek için GridWeb denetiminin CellCommand etkinliği için bir olay işleyici oluşturmalıdırlar. CellCommand etkinliğinin olay işleyicisi, Argument özelliği sunan CellEventArgs türünde bir nesne sağlar. Bir belirli bağlantıyı tanımlamak için Argument özelliğini kullanın.

Aşağıdaki örnek, yukarıdaki kodda oluşturulan hücre komutu bağlantısı için bir olay işleyici oluşturur. Bağlantının CellCommand'u Tıkla olarak ayarlandı. Bu nedenle, olay işleyicisinde önce kontrol edin ve ardından A6 hücresinde bir ileti gösteren kod ekleyin.

Olay işleyicisi, bağlantı tıklandığında çağrılır.

**Çıktı: bağlantı tıklandığında A6 hücresine eklenen metin** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **Bağlantıları Erişme**
Mevcut bir bağlantıya erişmek için:

1. İçeren hücreye erişin.
1. Hücre başvurusunu alın.
1. Başvuruyu Hyperlinks koleksiyonunun GetHyperlink yöntemine iletmek için geçirin.
1. Bağlantının özelliklerini değiştirin.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **Bağlantıları Kaldırma**
Bir bağlantıyı kaldırmak için:

1. Etkin çalışma sayfasına erişin.
1. Hyperlinks koleksiyonunun Kaldır yöntemini kullanarak bir bağlantıyı kaldırın.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
