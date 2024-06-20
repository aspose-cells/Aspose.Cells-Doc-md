---
title: GridWeb e Stil Uygulama
type: docs
weight: 20
url: /tr/net/aspose-cells-gridweb/apply-styles-to-gridweb/
keywords: GridWeb, stil, stiller
description: Bu makale, GridWeb de stil uygulamanın nasıl yapıldığını tanıtır.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb'ın kendi varsayılan görünümü vardır, ancak görünümünü değiştirme imkanı vardır. Aspose.Cells.GridWeb, geliştiricilerin tam kontrolü sağlamak için çeşitli özellikler sunar. Bu konu, bu özelliklerden bazılarını tartışmaktadır.

{{% /alert %}} 
## **Aspose.Cells.GridWeb'de Hazır veya Özel Stil Uygulama**
### **Hazır Stiller**
Geliştiricilerin çabalarını kaydetmek için, Aspose.Cells.GridWeb bazı hazır stiller sunar. Basitçe bir stil seçin ve uygulamak için listeden bir stil seçin.

|**Stilller**|**Renk Düzeni**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
Belirli bir stil seçildiğinde, GridWeb kontrolünün tüm görünümü değişir. Geliştiriciler, bir Hazır Stil seçebilir ve bu görevi tasarım zamanında Grid üzerinde uygulanasalar da, Aspose.Cells.GridWeb'in esnek API'sini kullanarak çalışma zamanında da gerçekleştirebilirler.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb kontrolü, GridWeb sınıfı tarafından temsil edilir.

{{% /alert %}} 

Önceden belirlenmiş bir stil seçmek için:

1. Bir web formuna Aspose.Cells.GridWeb denetimini ekleyin.
1. Denetim üzerine uygulanacak önceden belirlenmiş bir stil seçin.

GridWeb denetimi geliştiricilerin istedikleri önceden belirlenmiş stili atayabileceği PresetStyle özelliğini sağlar.

Aşağıdaki kod parçasının çıktısı aşağıda gösterilmiştir. 

**Renkli1 stili uygulanmış GridWeb denetimi** 

![todo:image_alt_text](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **Başlık Çubuğu Stili**
GridWeb denetimine bakarsanız, iki başlık çubuğu fark edeceksiniz. Bir sütunlar için (yani A, B, C, D vs.) ve diğeri satırlar için (yani 1, 2, 3, 4 vs.). Aspose.Cells.GridWeb geliştiricilere bu başlık çubuklarının görünümünü kontrol etme imkanı sunar. Geliştiriciler başlık çubuklarının stilini tasarım zamanında veya çalışma zamanında ayarlayabilirler.

{{% alert color="primary" %}} 

GridWeb denetimi, kontrolün her iki başlık çubuğuna da bir stil uygulayan HeaderBarStyle özelliğini sağlar.

{{% /alert %}} 

Aşağıdaki örnek kodunun çıktısı burada gösterilmektedir. 

**Başlık Çubuğunun Değiştirilmiş Stili** 

![todo:image_alt_text](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **Sekme Çubuğu Stili**
Sekme çubuğunun stili belirlenebilir. 

**Etkin ve etkin olmayan sekme çubuklarının değiştirilmiş stilleri** 

![todo:image_alt_text](apply-styles-to-gridweb_3.png)

Yukarıdaki şekilde, Sheet4 etkin sekmeyse, görünümü diğer sekmelerden farklıdır, aşağıdaki örnek kod tarafından tanımlandığı gibi.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **Yeniden Kullanılabilir Özelleştirilmiş Stil Dosyası**
Aspose.Cells.GridWeb ayrıca görünüm veya stil ayarlarını bir dosyaya kaydetmeyi destekler. GridWeb denetiminin tüm görünüm özelliklerini ayarladıysanız, bu özellikleri veya ayarları bir disk dosyasına kaydedebilirsiniz. Bu yaklaşım, geliştiricilerin eski stil yapılandırmalarını tek tek ayarlamak yerine bir stil dosyasından tekrar kullanarak zaman ve çaba kazanmaları için çok kullanışlıdır.
### **Stil Dosyası Kaydetme**
Stil özelliklerini ayarladıktan sonra, GridWeb denetiminin SaveCustomStyleFile yöntemini çağırarak stil yapılandırma ayarlarını XML dosyası olarak kaydedebilirsiniz (bu, Stil dosyasının bir XML dosyası olarak saklandığı içindir).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

Kaydedilen stil dosyası XML formatındadır, bu nedenle geliştiriciler istenirse bu dosyayı herhangi bir metin düzenleyici ile düzenleyebilirler.

{{% /alert %}} 
### **Stil Dosyası Yükleme**
Mevcut bir stil dosyasından GridWeb denetimine stil ayarlarını uygulamak için geliştiriciler denetimin CustomStyleFileName özelliğine stil dosyasının yolunu ayarlayabilirler. Ancak bunu yapmadan önce kontrolün PresetStyle özelliğini Özel olarak ayarlamak zorunludur. Çünkü stil dosyası önceden bir geliştirici tarafından tanımlanmış özel stil bilgisi içerir.

{{% alert color="primary" %}} 

Ayrıca Aspose.Cells.GridWeb Tasarımcısı kullanarak stil dosyası yükleme veya kaydetme de mümkündür.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

ÖNEMLİ: Stil dosyasını GridWeb denetine yüklemek, denetimin hücrelerinin biçimlendirme ayarlarını etkilemez.

{{% /alert %}} 
### **XML Stil Şablonunun Standart Formatı**
{{< highlight java >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}
