---
title: Çalışma Sayfasındaki Köprüleri Yönetin
type: docs
weight: 100
url: /tr/net/manage-hyperlinks-in-worksheet/
---
{{% alert color="primary" %}} 

Bu konuda, Aspose.Cells.GridWeb'de ne tür köprülerin desteklendiği ve bunların programlı olarak nasıl yönetileceği anlatılmaktadır. Köprüler, web URL'lerine bağlantılar oluşturmak veya bir sunucuya geri gönderme gerçekleştirmek için kullanılabilir.

{{% /alert %}} 
## **Köprülerle Çalışmak**
### **Köprü Türleri**
Genel olarak, aşağıdaki köprüler Aspose.Cells.GridWeb tarafından desteklenir:

- [URL köprüleri](/cells/tr/net/manage-hyperlinks-in-worksheet/), web URL'lerine bağlanabilen köprüler.
- [Metin köprüleri](/cells/tr/net/manage-hyperlinks-in-worksheet/), metne uygulanan URL köprüleri.
- [Görüntü köprüleri](/cells/tr/net/manage-hyperlinks-in-worksheet/), Resimlere uygulanan URL köprüleri.
- [Cell komut köprüleri](/cells/tr/net/manage-hyperlinks-in-worksheet/), verileri bir sunucuya gönderen köprüler. Bu tür köprüler, tıklandığında sunucu tarafı olayını tetikleyen bir düğme gibi davranır.

Aşağıdaki bölümlerde, her tür köprünün kullanımı ayrıntılı olarak açıklanmaktadır. Ayrıca bağlantılara nasıl erişileceğini veya kaldırılacağını da tartışır.
### **Köprü Ekleme**

#### **URL Köprüleri**
URL köprüleri, normalde web sitelerinde gördüğünüz basit köprülere benzer. URL köprüsü, hücredeki bir bağlantı gibi çalışır. Tıklandığında, bir web sayfasına gider veya yeni bir tarayıcı penceresi açar.

Farklı türde URL köprüleri vardır:

- Metin köprüleri.
- Görüntü köprüleri.

Geliştiriciler, köprü için bir görüntü belirtebilir. Bir görüntü belirtilmezse, bir metin köprüsü oluşturulur; aksi takdirde bir görüntü köprüsü oluşturulur.


##### **Metin Köprüleri**
Bir çalışma sayfasına metin köprüsü eklemek için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Bir çalışma sayfasına erişin.
1. Çalışma sayfasındaki bir hücreye köprü ekleyin.
1. Hücrede gösterilecek metni ayarlayın.
1. Köprünün URL'sini ayarlayın.
1. İsterseniz köprünün hedefini ayarlayın.
1. İstenirse bir araç ucu ayarlayın.

{{% alert color="primary" %}} 

 NOT: Köprü hedefi şu şekilde ayarlanabilir:_ öz,_top veya _parent, web URL'lerini sırasıyla yeni, geçerli veya üst pencerede açmak için.

{{% /alert %}} 

Aşağıdaki örnek, bir çalışma sayfasına iki köprü ekler. Birinin hedefi yok, diğeri ise _parent olarak ayarlı.

**Çıktı: çalışma sayfasına eklenen metin köprüleri** 

![yapılacaklar:resim_alternatif_Metin](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **Görüntü Köprüleri**
Bir resim köprüsü eklemek için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Bir çalışma sayfasına erişin.
1. Bir hücreye köprü ekleyin.
1. Köprü olarak görüntülenecek görüntünün URL'sini ayarlayın.
1. Köprü URL'sini ayarlayın.
1. İstenirse bir araç ucu ayarlayın.
1. İsterseniz köprü metnini ayarlayın.

**Çıktı: çalışma sayfasına eklenen görüntü köprüleri** 

![yapılacaklar:resim_alternatif_Metin](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

 Görüntü köprüsünün AltText'ini ayarlamak, bir<ALT> HTML'de etiketleyin. Metin, yalnızca köprü bağlantılı görüntü görüntülenmiyorsa görüntülenir. (Örneğin, resim belirtilen konumda değilse.) İkinci köprünün resmi bulunmazsa, aşağıdaki kod parçacığının çıktısı aşağıdaki gibi görünecektir.

**Resim URL'si için resim bulunamadı** 

![yapılacaklar:resim_alternatif_Metin](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Cell Komut Köprüleri**
Hücre komut köprüsü, bir web sayfası açmak yerine sunucu tarafı olayını tetikleyen özel bir köprü türüdür. Geliştiriciler, sunucu tarafı olayına kod ekleyebilir ve köprü tıklandığında herhangi bir görevi gerçekleştirebilir. Bu özellik, geliştiricilerin daha etkileşimli uygulamalar oluşturmasını sağlar.

Bir hücre komutu köprüsü eklemek için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Bir çalışma sayfasına erişin.
1. Bir hücreye köprü ekleyin.
1. Köprünün Komutunu istediğiniz herhangi bir değere ayarlayın.
 Değer, köprünün olay işleyicisi tarafından onu tanımak için kullanılır.
1. İstenirse bir araç ucu ayarlayın.
1. Köprü olarak görüntülenecek Görüntü için URL'yi ayarlayın.

**Çalışma sayfasına bir hücre komut köprüsü eklendi** 

![yapılacaklar:resim_alternatif_Metin](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Cell Komut Köprülerinin Olay İşleme**
Geliştiricilerin, belirli bir hücre komut köprüsü tıklandığında belirli görevleri gerçekleştirmek üzere GridWeb denetiminin CellCommand olayı için bir olay işleyicisi oluşturması gerekir. CellCommand olayının olay işleyicisi, Argument özelliğini sunan CellEventArgs türünde bir nesne sağlar. CellCommand değerini karşılaştırarak belirli bir köprüyü tanımlamak için Argument özelliğini kullanın.

Aşağıdaki örnek, yukarıdaki kodda oluşturulan hücre komut köprüsü için bir olay işleyici oluşturur. Köprünün CellCommand'ı Click olarak ayarlandı. Bu nedenle, olay işleyicide önce kontrol edin ve ardından A6 hücresinde bir mesaj görüntüleyen kodu ekleyin.

Olay işleyicisi, köprü tıklandığında çağrılır.

**Çıktı: köprü tıklandığında A6 hücresine eklenen metin** 

![yapılacaklar:resim_alternatif_Metin](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **Köprülere Erişim**
Mevcut bir köprüye erişmek için:

1. Onu içeren hücreye erişin.
1. Hücre referansını alın.
1. Köprüye erişmek için başvuruyu Köprüler koleksiyonunun GetHyperlink yöntemine iletin.
1. Köprünün özelliklerini değiştirin.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **Köprüleri Kaldırma**
Bir köprüyü kaldırmak için:

1. Etkin çalışma sayfasına erişin.
1. Köprüler koleksiyonunun Kaldır yöntemini kullanarak bir köprüyü kaldırın.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
