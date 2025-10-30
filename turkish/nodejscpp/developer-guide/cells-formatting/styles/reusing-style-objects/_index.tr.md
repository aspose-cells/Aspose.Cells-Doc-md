---  
title: Stil Nesnelerini Yeniden Kullanma
linktitle: Stil Nesnelerini Yeniden Kullanma  
description: Aspose.Cells for Node.js via C++ te, yeniden kullanılabilir stil nesneleri oluşturarak stil yönetimini basitleştirebilir ve kod verimliliğini artırabilirsiniz. Kılavuzumuz, yeniden kullanılabilir stil nesnelerinin avantajlarından nasıl yararlanacağınızı ve bunları uygulamanıza nasıl entegre edeceğinizi gösterecektir.  
keywords: Aspose.Cells for Node.js via C++, Stil Nesnelerini Yeniden Kullanma, Stil Yönetimi, Kod Verimliliği, Yeniden Kullanılabilir Stiller, Uygulama Geliştirme, API Referansı, Örnek Kod, İndirin, Destek.  
type: docs  
weight: 3000  
url: /tr/nodejs-cpp/reusing-style-objects/  
---  

{{% alert color="primary" %}}  
Stil nesnelerini yeniden kullanmak, belleği boşaltabilir ve programı daha hızlı hale getirebilir.  
{{% /alert %}}  

Bir çalışsayfadaki geniş bir hücre aralığına bazı biçimlendirme uygulamak için:

1. Bir stil nesnesi oluşturun.
1. Öznitelikleri belirtin.
1. Stili aralıktaki hücrelere uygulayın.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-ReusingStyleObjects.js" >}}


{{% alert color="primary" %}}  
Çünkü [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) / [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) yaklaşımı daha az bellek kullanır ve daha verimlidir, eski Cell.style özelliği gereksiz yere çok bellek kullanması nedeniyle Aspose.Cells 7.1.0 sürümüyle kaldırılmıştır.  
{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
