---
title: Stilleri GridWeb'e Uygula
type: docs
weight: 20
url: /tr/net/apply-styles-to-gridweb/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb'in kendi varsayılan görünümü ve hissi vardır ancak görünümünü değiştirmek mümkündür. Aspose.Cells.GridWeb, geliştiricilerin görünümünü tamamen kontrol etmesine izin veren çeşitli özellikler sağlar. Bu konu, bu özelliklerden bazılarını tartışmaktadır.

{{% /alert %}} 
## **Aspose.Cells.GridWeb'e Hazır Ayar veya Özel Stiller Uygulama**
### **Hazır Stiller**
Geliştiricilerin çabalarından tasarruf etmek için Aspose.Cells.GridWeb bazı hazır stiller sunar. Stili uygulamak için listeden bir stil seçmeniz yeterlidir.

|**stiller**|**Renk uyumu**|
|:- |:- |
|Standart|Gümüş|
|Renkli1|Gül|
|renkli2|Mavi|
|Profesyonel1|camgöbeği|
|Profesyonel2|tekrar camgöbeği|
|Geleneksel1|Karanlık|
|Geleneksel2|Gri|
|Gelenek|Özelleştirilmiş|
Belirli bir stil seçildiğinde, GridWeb kontrolünün tüm görünümünü değiştirir. Geliştiriciler, tasarım süresi boyunca Izgaraya uygulanacak bir Hazır Ayar Stili seçebilirler ancak bu görev, Aspose.Cells.GridWeb'in esnek API'i kullanılarak çalışma zamanında da gerçekleştirilebilir.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb denetimi, GridWeb sınıfı tarafından temsil edilir.

{{% /alert %}} 

Önceden ayarlanmış bir stil seçmek için:

1. Bir web formuna Aspose.Cells.GridWeb denetimi ekleyin.
1. Kontrole uygulanacak bir hazır ayar stili seçin.

GridWeb denetimi, geliştiricilerin istenen herhangi bir hazır ayar stilini atayabileceği PresetStyle özelliğini sağlar.

 Aşağıdaki kod parçacığının çıktısı aşağıda gösterilmiştir.

**Üzerine Colorful1 stili uygulanmış GridWeb denetimi** 

![yapılacaklar:resim_alternatif_Metin](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **Başlık Çubuğu Stili**
GridWeb kontrolüne bakarsanız, iki başlık çubuğu göreceksiniz. Biri sütunlar (yani A, B, C, D vb.) ve diğeri satırlar (yani 1, 2, 3, 4 vb.) içindir. Aspose.Cells.GridWeb, geliştiricilerin bu başlık çubuklarının görünümünü kontrol etmesine olanak tanır. Geliştiriciler, başlık çubuklarının stilini tasarım zamanında veya çalışma zamanında ayarlayabilir.

{{% alert color="primary" %}} 

GridWeb denetimi, denetimin her iki başlık çubuğuna da bir stil uygulayan HeaderBarStyle özelliğini sağlar.

{{% /alert %}} 

 Aşağıdaki örnek kodun çıktısı burada gösterilmektedir.

**Başlık Çubuğunun değiştirilmiş stili** 

![yapılacaklar:resim_alternatif_Metin](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **Sekme Çubuğu Stili**
 Sekme çubuğunun stilini ayarlamak mümkündür.

**Etkin ve etkin olmayan sekme çubuklarının değiştirilmiş stilleri** 

![yapılacaklar:resim_alternatif_Metin](apply-styles-to-gridweb_3.png)

Yukarıdaki şekilde, Sayfa4 etkin sekmedir, bu nedenle aşağıdaki örnek kodda tanımlandığı gibi görünümü diğer sekmelerden farklıdır.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **Yeniden Kullanılabilir Özelleştirilmiş Stil Dosyası**
Aspose.Cells.GridWeb, görünüm veya stil ayarlarını bir dosyada tutmayı da destekler. GridWeb kontrolünün tüm görünüm özelliklerini ayarladığınızda, bu özellikleri veya ayarları bir disk dosyasına kaydedebilirsiniz. Bu yaklaşım, geliştiricilerin kontrolün tüm stil (veya görünüm) özelliklerini tek tek ayarlamak yerine eski stil yapılandırmalarını bir stil dosyasından yeniden kullanarak zamandan ve emekten tasarruf etmeleri için çok yararlıdır.
### **Stil Dosyasını Kaydetme**
Stil özelliklerini ayarlamayı bitirdikten sonra, GridWeb denetiminin SaveCustomStyleFile yöntemini çağırarak stil yapılandırma ayarlarınızı bir XML dosyası biçiminde kaydedebilirsiniz (bunun nedeni, Stil dosyasının bir XML dosyası olarak saklanmasıdır).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

Kaydedilen stil dosyası XML formatındadır, dolayısıyla geliştiriciler bu dosyayı istenirse herhangi bir metin düzenleyiciyle de düzenleyebilir.

{{% /alert %}} 
### **Stil Dosyası Yükleniyor**
Varolan bir stil dosyasından GridWeb denetimine stil ayarları uygulamak için, geliştiriciler stil dosyasının yolunu kontrolün CustomStyleFileName özelliğine ayarlayabilir. Ancak, bunu yapmadan önce kontrolün PresetStyle özelliğini Özel olarak ayarlamak gerekir. Bunun nedeni, stil dosyasının bir geliştirici tarafından zaten tanımlanmış olan özel stil bilgilerini içermesidir.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb Designer kullanarak stil dosyası yüklemek veya kaydetmek de mümkündür.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

ÖNEMLİ: Stil dosyasının GridWeb kontrolüne yüklenmesi, kontrol hücrelerinin biçimlendirme ayarlarını etkilemez.

{{% /alert %}} 
### **XML Stil Şablonunun Standart Biçimi**
{{< highlight "java" >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}
