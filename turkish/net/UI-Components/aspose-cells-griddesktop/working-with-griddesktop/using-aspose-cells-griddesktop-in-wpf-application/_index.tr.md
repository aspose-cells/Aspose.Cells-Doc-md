---
title: WPF Uygulamasında Aspose.Cells.GridDesktop Kullanma
type: docs
weight: 50
url: /tr/net/aspose-cells-griddesktop/use-aspose-cells-griddesktop-in-wpf-application/
keywords: GridDesktop,wpf
description: Bu makale, WPF uygulamasında GridDesktop ı nasıl kullanacağınızı tanıtıyor.
---

{{% alert color="primary" %}} 

Bu makale, Windows Presentation Foundation (WPF) Designer'ı Visual Studio'da bir Windows Forms denetimini (örneğin Aspose.Cells.GridDesktop) bir WPF uygulamasında barındırmak için nasıl kullanacağınızı göstermektedir. 
Bu süreci göstermek için Visual Studio 2015 kullanacağız, ancak Visual Studio 2008 veya sonraki herhangi bir sürümü kullanabilirsiniz.

{{% /alert %}} 

Bu öğretici, Aspose.Cells.GridDesktop kontrolünü bir WPF uygulamasına eklemenin sürecini adım adım anlatacaktır. Bu işlemi kendi tarafınızda denemek için WPF geliştirmeyi destekleyen herhangi bir Visual Studio IDE sürümüne ihtiyacınız olacaktır.
## **Visual Studio Kullanarak WPF Uygulaması Oluşturma**
İlk olarak, Visual Studio IDE kullanarak WPF uygulaması oluşturun. Şablonlardan **WPF Uygulaması**'nı seçmek için **Dosya** >> **Yeni** >> **Proje** menüsüne tıklayın, projeye bir isim verin ve **Tamam**'a tıklayın. Projeyi 2.0'dan daha yüksek herhangi bir .NET Framework'e hedefleyebilirsiniz, ancak istemci profili .NET Framework'leri kullanamazsınız.
## **Gerekli ad alanlarına referanslar ekleyin**
Çözüm Gezgini penceresinden Referanslar'a sağ tıklayarak ve Ekle > Referans menüsünü seçerek aşağıdaki derlemelere referans ekleyin.

- WindowsFormsIntegration derlemesi (WindowsFormsIntegration.dll).
- Windows Forms derlemesi (System.Windows.Forms.dll).
- Aspose.Cells.GridDesktop derlemesi (Aspose.Cells.GridDesktop.dll).

Bu işlem, gerekli derlemeleri uygulamaya ekler; yani derlemeleri uygulamanın Bin klasörüne kopyalar.
## **XAML'e referanslar ekleyin**
Daha sonra, XAML dosyasına gidin ve Windows etiketi içine aşağıdaki ad alanlarını ve derleme referanslarını ekleyin.

{{< highlight java >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**Son Windows etiketi aşağıdaki gibi görünecektir.**

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Aspose.Cells.GridDesktop kontrolünü XAML'e ekleyin**
Sadece aşağıdaki kodu XAML'deki Grid etiketi içine ekleyin. **WindowsFormsHost** etiketi Windows Forms denetimini barındırmak için kullanılır ve **gridDesktop:GridDesktop** etiketi Aspose.Cells.GridDesktop kontrolünü temsil eder. Ayrıca kontrolü adlandırabilirsiniz, böylece kod içinde kolayca referans alabilirsiniz.

{{< highlight java >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**Son XAML aşağıdaki gibi görünecektir.** 

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Aspose.Cells.GridDesktop Kullanma**
Artık Aspose.Cells.GridDesktop kontrolüne .cs dosyasında diğer Windows Forms uygulamaları gibi erişebilir ve kullanabiliriz. Gösterimi basit tutmak için Aspose.Cells.GridDesktop kontrolünde örnek bir elektronik tablo yüklüyoruz ve geri kaydediyoruz. Dahası, FrameworkElement_OnLoaded olayını aşağıdaki ifadeleri tetiklemek için kullanıyoruz.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Derle ve Çalıştır**
Şimdi, Visual Studio UI üzerinde **F5** veya **Başlat** düğmesini kullanarak uygulamayı derleyin ve çalıştırın.
