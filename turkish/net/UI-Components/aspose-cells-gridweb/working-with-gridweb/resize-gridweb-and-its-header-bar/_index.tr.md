---
title: GridWeb Eklemek için Web Formuna Ekle, WYSIWYG kullanarak Aspose.Cells.GridWeb kontrolü boyutlandırıldı. Bu makale, aynı şeyi ama Aspose.Cells.GridWeb API sini çalışma zamanında kullanarak nasıl yapılacağını açıklar. Ayrıca Aspose.Cells.GridWeb kontrolünün başlık çubuklarını okunabilirliği artırmak için boyutlandırmanın nasıl yapılacağını da açıklar.
type: docs
weight: 30
url: /tr/net/aspose-cells-gridweb/resize-gridweb-and-its-header-bar/
keywords: GridWeb, boyutlandırma
description: Bu makale, GridWeb de nasıl yeniden boyutlandırılacağını tanıtır.
---

{{% alert color="primary" %}} 

[Web Form'a GridWeb Ekle](/cells/tr/net/aspose-cells-gridweb/add-gridweb-to-web-form/) , Aspose.Cells.GridWeb kontrolünü WYSIWYG kullanarak yeniden boyutlandırmayı tartışır. Bu makale, aynı şeyi ancak Aspose.Cells.GridWeb API'sini kullanarak çalışma zamanında nasıl yapılacağını açıklamaktadır. Ayrıca, Aspose.Cells.GridWeb kontrolünün başlık çubuklarını yeniden boyutlandırmayı, verilerini okuma işini daha kolay hale getirmek için nasıl yapılabileceğini açıklar.

{{% /alert %}} 
## **Aspose.Cells.GridWeb'in Genişliği ve Yüksekliği Değiştirme**
Aspose.Cells.GridWeb kontrolünün genişliğini ve yüksekliğini değiştirmek basit ancak önemli bir özelliktir. Aspose.Cells.GridWeb kontrolü, API'de GridWeb sınıfı tarafından temsil edilir. GridWeb kontrolünün genişliğini ve yüksekliğini yeniden boyutlandırmak için sadece genişlik ve yükseklik özelliklerini kullanın.

{{% alert color="primary" %}} 

Denetimin genişliği ve yüksekliği piksel veya noktalarda tanımlanabilir.

{{% /alert %}} 

Aşağıdaki kod parçasının çıktısı aşağıda gösterilmiştir.

**GridWeb kontrolünün genişliği ve yüksekliği değiştirildi** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **Başlık Çubuğunun Genişliği ve Yüksekliğini Değiştirme**
Aspose.Cells.GridWeb kontrolü şu şekilde iki başlık çubuğu içerir:

- Üst başlık çubuğu, bu başlık çubuğu sütunları A, B, C, D gibi temsil eder.
- Sol başlık çubuğu, bu başlık çubuğu satırları 1, 2, 3, 4 gibi temsil eder.

Bu başlık çubukları aşağıda gösterilmiştir.

**Başlık çubukları** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_2.png)

GridWeb kontrolünün HeaderBarHeight ve HeaderBarWidth özelliklerini kullanarak üst başlık çubuğunun yüksekliğini ve sol başlık çubuğunun genişliğini değiştirin. Aşağıdaki şekil, aşağıdaki kod örneğinin çıktısını göstermektedir.

**Değiştirilmiş başlık çubuğu genişliği ve yüksekliği** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
