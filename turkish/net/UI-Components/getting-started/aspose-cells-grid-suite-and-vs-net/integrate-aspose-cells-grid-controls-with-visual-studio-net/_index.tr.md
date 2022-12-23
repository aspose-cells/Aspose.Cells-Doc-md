---
title: Aspose.Cells Izgara Denetimlerini Visual Studio.NET ile entegre edin
type: docs
weight: 10
url: /tr/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
---
{{% alert color="primary" %}} 

 Visual Studio.NET geliştiricileri, denetimleri kolayca**araç kutusu** Windows veya Web formuna. Aspose.Cells Izgara paketi, bir MSI yükleyicisiyle veya bir dizi DLL paketi olarak indirilebilir. Bu makalede, yükleyici yerine DLL'ler kullanılarak yüklendiğinde Visual Studio.NET'de Aspose.Cells.Grid denetimlerinin kullanılabilmesini sağlamak için ne yapılması gerektiği açıklanmaktadır.

{{% /alert %}} 
## **Aspose.Cells Izgara Denetimlerini Visual Studio.NET ile entegre edin**
Aspose.Cells Kılavuz denetimlerini Visual Studio .NET ile entegre etmek için:

1. Araç Kutusu'nu açın.
1. Genel sekmesini (veya denetim eklemek istediğiniz başka bir sekmeyi) seçin.
1. Genel sekmesine sağ tıklayın.
1.  Visual Studio.NET 2003'te: Seçin**Öğe Ekle/Kaldır** menüden.
1. Visual Studio.NET 2005'te seçin**Öğeleri Seçin** menüden. Araç Kutusunu Özelleştir iletişim kutusu görünecektir (Bu işlem, daha yeni VS.NET IDE'ler (örn. VS.NET 2013/2015 veya sonrası) için aşağı yukarı aynıdır).
1.  Tıklamak**Araştır** ve Aspose.Cells.GridDesktop.dll ve Aspose.Cells.GridWeb.dll dosyalarını bulun.
1.  DLL'leri seçin ve ardından tıklayın.**Açık**. Araç Kutusunu Özelleştir iletişim kutusu artık Aspose.Cells Grid Suite'ten gelen kontrolleri içerecektir. Yeni eklenen kontroller iletişim kutusunda vurgulanacaktır.
1.  Tıklamak**Tamam** denetimleri Visual Studio.NET Araç Kutunuza eklemek için.

 Aspose.Cells Izgara Kontrolleri Araç Kutusuna eklenmiş olacak**Genel** sekme. Yalnızca GridWeb denetimi etkin değildir. Bunun nedeni, Windows Forms uygulaması üzerinde çalışmamızdır. GridWeb yalnızca Web Formları üzerinde çalışırken kullanılabilirken GridDesktop yalnızca Windows formlarıyla kullanılabilir.
