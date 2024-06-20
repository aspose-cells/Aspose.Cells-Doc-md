---
title: GridDesktop ta Çalışma Sayfasında Yakınlaşma veya Uzaklaşma
type: docs
weight: 160
url: /tr/net/aspose-cells-griddesktop/zoom-in-or-out-on-the-worksheet-in-griddesktop/
keywords: GridDesktop, yakınlaştırma, yakınlaştırma, uzaklaştırma
description: Bu makale, GridDesktop da yakınlaştırma veya uzaklaştırma nasıl yapılır konusunu ele almaktadır.
---

{{% alert color="primary" %}} 

Verilerinizle çalışırken bazen gerçekten yazı tipi boyutunu değiştirmeden ekran üzerindeki içeriği genişletmek isteyebilirsiniz. Örneğin, metnin tüm bilgilerinizi bir çıktıda almak için küçük bir yazı tipi kullanması gerekebilir. Ancak, çalışma sayfasında yazı tipi çok küçük olduğu için okuması zor olabilir.

Microsoft Excel'de belgelerin hızlı ve kolay bir şekilde yakınlaştırılmasını ve uzaklaştırılmasını sağlayan bir yakınlaştırma kaydırıcısı bulunmaktadır. Yakınlaştırma kaydırıcısı genellikle yazılım penceresinin sağ alt köşesinde bulunur.

Aspose.Cells ayrıca geliştiricilere çalışma sayfasının yakınlaştırma faktörünü belirlemelerine izin verir, böylece içerikler istediğiniz yüzde değerine göre görüntülenir.

{{% /alert %}} 
## **Aspose.Cells.GridDesktop Kullanarak Yakınlaştırma veya Uzaklaştırma**
Aspose.Cells, ASP.NET web formlarına diğer Microsoft .NET Framework tarafından sağlanan web denetimleri gibi GridWeb'i gömülebilen bir GUI tabanlı web denetimi olan Aspose.Cells.GridWeb'i sağlar. Bir web denetimi hakkındaki en önemli şey, çapraz tarayıcı desteği sağlamaktır. Aspose.Cells.GridWeb çapraz tarayıcı desteği sağlar.

Biz, TrackBar (.NET) kontrolünü kullanarak bir MS Excel benzeri yakınlaştırma kaydı oluşturuyoruz. Bir WinForm projesinde, Toolbox'tan Aspose.Cells.GridDesktop kontrolünü forma yerleştirir ve adını, boyutunu veya diğer yönlerini ayarlamak için bazı özellikler belirleriz. Şimdi, GridDesktop kontrolünün alt sağ köşesine TrackBar kontrolünü yerleştiriyoruz ve alttaki Label kontrolünü de TrackBar kontrolünün sapı aracılığıyla belirttiğiniz yüzde değerini gösterecek şekilde koyuyoruz. TrackBar'ın Scroll etkinliğine ilgili kod satırlarını ekleriz, böylece TrackBar kontrolünü kaydırdığınızda, GridDesktop'ın verilerini/ içeriklerini gösterecek şekilde yakınlaştırabilir veya uzaklaştırabilirsiniz.

Etkinleştirme tablosunun zoom özelliğini kullanarak GridDesktop'ın etkin çalışma sayfasının yakınlaştırma faktörünü ayarlamayı gösteren aşağıdaki tam örnek verilmiştir. İlk olarak, bir şablon Excel dosyasını GridDesktop'a içe aktarıyoruz.

Formun Yükleme etkinliğine aşağıdaki kodu yazın ve şablon Excel dosyasını GridDesktop'a ayarlayın ve izli çubuk değerini belirleyin.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


Şimdi, aşağıdaki kodu izle kaydırma etkinliği içine kopyalayın ve uygulamayı çalıştırın. İzli çubuğu hareket ettirdiğinizde, çalışma sayfasının zoom özelliğinin değiştiğini fark edeceksiniz.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
