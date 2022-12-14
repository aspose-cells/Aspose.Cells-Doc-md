---
title: GridWeb'i ve Başlık Çubuğunu Yeniden Boyutlandırın
type: docs
weight: 30
url: /tr/net/resize-gridweb-and-its-header-bar/
---
{{% alert color="primary" %}} 

[GridWeb'i Web Formuna Ekleme](/cells/tr/net/add-gridweb-to-web-form/), WYSIWYG kullanarak Aspose.Cells.GridWeb kontrolünün yeniden boyutlandırılması ele alındı. Bu makale aynı şeyi çalışma zamanında Aspose.Cells.GridWeb API kullanarak nasıl yapacağınızı açıklar. Ayrıca, verilerinin daha kolay okunmasını sağlamak için Aspose.Cells.GridWeb kontrolünün başlık çubuklarının nasıl yeniden boyutlandırılacağını açıklar.

{{% /alert %}} 
## **Aspose.Cells.GridWeb'in Genişlik ve Yüksekliğini Değiştirme**
Aspose.Cells.GridWeb kontrolünün genişliğini ve yüksekliğini değiştirmek basit ama önemli bir özelliktir. Aspose.Cells.GridWeb denetimi, API'deki GridWeb sınıfı tarafından temsil edilir. GridWeb denetiminin genişlik ve yüksekliğini yeniden boyutlandırmak için, genişlik ve yükseklik özelliklerini kullanmanız yeterlidir.

{{% alert color="primary" %}} 

Kontrolün genişliği ve yüksekliği piksel veya nokta olarak tanımlanabilir.

{{% /alert %}} 

Aşağıdaki kod parçacığının çıktısı aşağıda gösterilmiştir.

**GridWeb kontrolünün genişliği ve yüksekliği değiştirildi** 

![yapılacaklar:resim_alternatif_Metin](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **Başlık Çubuğunun Genişliğini ve Yüksekliğini Değiştirme**
Aspose.Cells.GridWeb denetimi aşağıdaki gibi iki başlık çubuğu içerir:

- Üst başlık çubuğu, bu başlık çubuğu A , B , C , D gibi sütunları temsil eder.
- Sol başlık çubuğu, bu başlık çubuğu satırları 1 , 2 , 3 , 4 vb. olarak temsil eder.

Bu başlık çubuklarının her ikisi de aşağıda gösterilmiştir.

**Başlık çubukları** 

![yapılacaklar:resim_alternatif_Metin](resize-gridweb-and-its-header-bar_2.png)

Sırasıyla GridWeb denetiminin HeaderBarHeight ve HeaderBarWidth özelliklerini kullanarak üst başlık çubuğunun yüksekliğini ve sol başlık çubuğunun genişliğini değiştirin. Aşağıdaki şekil, aşağıdaki kod örneğinin çıktısını göstermektedir.

**Başlık çubuğunun genişliği ve yüksekliği değiştirildi** 

![yapılacaklar:resim_alternatif_Metin](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
