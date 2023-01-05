---
title: GridDesktop'ta Çalışma Sayfasında Yakınlaştırma veya Uzaklaştırma
type: docs
weight: 160
url: /tr/net/zooming-in-or-out-on-the-worksheet-in-griddesktop/
---
{{% alert color="primary" %}} 

Bazen verilerinizle çalışırken yazı tipi boyutunu gerçekten değiştirmeden ekrandaki içeriği büyütmek isteyebilirsiniz. Örneğin, metninizi küçük bir yazı tipi kullanacak şekilde biçimlendirmiş olabilirsiniz. (Bu genellikle tüm bilgilerinizi bir çıktıda almak için gereklidir.) Bununla birlikte, çalışma sayfasında çalışırken yazı tipi çok küçük olduğu için okunması zordur.

Microsoft Excel'de, belgeleri hızlı ve kolay bir şekilde yakınlaştırmak ve uzaklaştırmak için bir yakınlaştırma kaydırıcısı mevcuttur. Yakınlaştırma kaydırıcısı genellikle yazılım penceresinin sağ alt köşesindedir.

Aspose.Cells ayrıca geliştiricilerin çalışma sayfasının yakınlaştırma faktörünü ayarlamasına olanak tanır, böylece içerikler istediğiniz yüzde değerine göre görünmelidir.

{{% /alert %}} 
## **Aspose.Cells.GridDesktop Kullanarak Yakınlaştırma veya Uzaklaştırma**
Aspose.Cells, çalışma sayfalarını yönetmek için çok çeşitli özelliklere ve yöntemlere sahip Aspose.Cells.GridDesktop.Worksheet sınıfını sağlar. Bir çalışma sayfasının yakınlaştırma faktörünü ayarlamak için Worksheet sınıfının Yakınlaştırma özelliğini kullanın. Yakınlaştırma faktörü, Yakınlaştırma özelliğine sayısal (tamsayı) bir değer atanarak ayarlanır.

TrackBar (.NET) kontrolünü kullanarak yakınlaştırma kaydırıcısı benzeri bir MS Excel oluşturuyoruz. Bir WinForm projesinde, Toolbox'tan Aspose.Cells.GridDesktop kontrolünü forma yerleştirir ve adını, boyutunu veya diğer yönlerini buna göre ayarlamak için bazı özellikler belirtiriz. Şimdi TrackBar kontrolünü @ sağ alt köşeye GridDesktop kontrolünün altına yerleştiriyoruz, ayrıca TrackBar kontrolünün tutamacı aracılığıyla belirttiğiniz yüzde değerini gösterecek bir Etiket kontrolü koyuyoruz. TrackBar'ın Scroll olayına göreli kod satırları ekliyoruz, böylece Trackbar kontrolünü kaydırdığınızda, GridDesktop içindeki verileri/içeriği göstermek için yakınlaştırmalı veya uzaklaştırmalıdır.

Aşağıda, GridDesktop'un etkin çalışma sayfasının yakınlaştırma faktörünü ayarlamak için Yakınlaştırma özelliğinin nasıl kullanılacağını gösteren eksiksiz bir örnek verilmiştir. Öncelikle bir şablon Excel dosyasını GridDesktop'a aktarıyoruz.

Şablon Excel dosyasını GridDesktop'ta ve izleme çubuğu değerini ayarlamak için formun Load olayına aşağıdaki kodu yazın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


Şimdi track scroll olayının içindeki aşağıdaki kodu kopyalayın ve uygulamayı çalıştırın. Hareket eden izleme çubuğunun çalışma sayfasının yakınlaştırma özelliğini değiştireceğini fark edeceksiniz.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
