---
title: Aspose.Cells.GridDesktop'u WPF Uygulamasında Kullanma
type: docs
weight: 50
url: /tr/net/using-aspose-cells-griddesktop-in-wpf-application/
---
{{% alert color="primary" %}} 

 Bu makale, bir WPF uygulamasında Aspose.Cells.GridDesktop gibi bir Windows Forms denetimini barındırmak için Visual Studio için Windows Presentation Foundation (WPF) Tasarımcısının nasıl kullanılacağını gösterir.
Süreci göstermek için Visual Studio 2015 kullanacağız, ancak Visual Studio 2008 veya sonraki sürümleri de dahil olmak üzere herhangi bir sürümü kullanabilirsiniz.

{{% /alert %}} 

Bu öğretici, bir WPF uygulamasına Aspose.Cells.GridDesktop denetimi ekleme sürecinde size yol gösterecektir. Bunu kendi tarafınızda denemek için WPF geliştirmeyi destekleyen herhangi bir Visual Studio IDE sürümüne ihtiyacınız var.
## **Visual Studio'yu kullanarak bir WPF uygulaması oluşturun**
 Önce Visual Studio IDE kullanarak bir WPF uygulaması oluşturun. Tıklamak**Dosya** >> **Yeni** >> **Proje** menü ve seçin**WPF Uygulaması** Şablonlar'dan projeyi adlandırın ve tıklayın**Tamam**. Projenizi 2.0'dan daha yüksek herhangi bir .NET Çerçevesine hedefleyebilirsiniz, ancak müşteri profili .NET Çerçevelerini kullanamazsınız.
## **Gerekli ad alanlarına referanslar ekleyin**
References from Solution Explorer penceresine sağ tıklayarak ve Add Reference menüsünü seçerek aşağıdaki derlemelere referansları ekleyin.

- WindowsFormsIntegration derlemesi (WindowsFormsIntegration.dll).
- Windows Form derlemesi (System.Windows.Forms.dll).
- Aspose.Cells.GridDesktop derlemesi (Aspose.Cells.GridDesktop.dll).

Bu eylem, gerekli derlemeleri uygulamaya ekler, yani; derlemeleri uygulamanın Bin klasörüne kopyalar.
## **XAML'ye başvurular ekleyin**
Ardından, XAML dosyasına gidin ve aşağıdaki ad alanlarını ve derleme referanslarını Windows etiketi içine ekleyin.

{{< highlight "java" >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**Son Windows etiketi, aşağıda gösterilene benzer görünecektir.**

![yapılacaklar:resim_alternatif_metin](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **XAML'ye Aspose.Cells.GridDesktop denetimi ekleyin**
 XAML'deki Grid etiketinin içine aşağıdaki kodu eklemeniz yeterlidir. bu**WindowsFormsHost** etiketi, Windows Form kontrolünü barındırmak için kullanılır ve**gridDesktop:GridDesktop** etiketi, Aspose.Cells.GridDesktop denetimini temsil eder. Kodda kolayca başvurulabilmesi için denetimi de adlandırabilirsiniz.

{{< highlight "java" >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**Son XAML aşağıdaki gibi görünecektir.** 

![yapılacaklar:resim_alternatif_metin](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Aspose.Cells.GridDesktop'u kullanın**
Artık .cs dosyasındaki Aspose.Cells.GridDesktop kontrolüne diğer Windows Forms uygulamaları gibi erişebilir ve kullanabiliriz. Gösterimi basit tutmak için, Aspose.Cells.GridDesktop kontrolüne örnek bir elektronik tablo yüklüyoruz ve onu geri kaydediyoruz. Ayrıca, aşağıdaki ifadeleri tetiklemek için FrameworkElement_OnLoaded olayını kullandık.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Yap ve Çalıştır**
 Şimdi, kullanarak uygulamayı oluşturun ve çalıştırın.**F5** veya**Başlama** Visual Studio kullanıcı arabirimindeki düğme.
