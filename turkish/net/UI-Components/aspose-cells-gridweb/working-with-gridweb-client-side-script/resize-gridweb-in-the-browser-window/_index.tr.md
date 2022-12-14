---
title: Tarayıcı penceresinde GridWeb'i yeniden boyutlandırma
type: docs
weight: 40
url: /tr/net/resize-gridweb-in-the-browser-window/
---
## **Olası Kullanım Senaryoları**
Bazen Aspose.Cells.GridWeb'in istediğiniz tarayıcı penceresine göre kendisini yeniden boyutlandırması gerekir. GridWeb'in her zaman boyutunu (yükseklik, genişlik) ayarlaması ve tarayıcı penceresinin boyutuyla uyumlu olması gerekebilir. Aspose.Cells.GridWeb istemci tarafı sağlar*yeniden boyutlandırma()* amaç için işlev görür. Ayrıca, tarayıcı penceresinde GridWeb kontrolünü yeniden boyutlandırılabilir hale getirebilirsiniz. Örneğin, pencerede genişliğini/yüksekliğini özelleştirmek için sağ alt tutamacı (fare aracılığıyla) kullanabilirsiniz. Projenizdeki sayfa kaynağında çalışmasını sağlamak için jquery Javascript dosyalarını da eklemeniz/belirtmeniz gerekir.
## **GridWeb'in yeniden boyutlandırma yöntemini kullanma**
Aşağıdaki kod, her 100 milisaniyede bir yeniden boyutlandırma eyleminin yapılıp yapılmadığını kontrol edecektir. Artık yeniden boyutlandırma eylemi kalmadığında, yeniden boyutlandırma işleminin artık bittiğini düşünür. GridWeb'e aktarılan örnek bir şablon dosyası kullanıyoruz. GridWeb'i yeniden boyutlandırmak için istemci tarafı kodunu kullanıyoruz. Ekran görüntüsü, tarayıcı penceresini yeniden boyutlandırırken GridWeb'in kendisini buna göre yeniden boyutlandırdığını gösteriyor.

![yapılacaklar:resim_alternatif_Metin](resize-gridweb-in-the-browser-window_1.png)
### **Basit kod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **Yeniden boyutlandırılabilir jquery ui özelliğini kullanarak GridWeb'i yeniden boyutlandırılabilir yapma**
Aşağıdaki kod, GridWeb kontrolünü tarayıcı penceresinde yeniden boyutlandırılabilir hale getirecektir. Örneğin, penceredeki GridWeb boyutunu özelleştirmek için sağ alt tutamacı kullanabilirsiniz. Önce GridWeb'e içe aktarılan aynı şablon dosyasını kullanıyoruz. GridWeb'i yeniden boyutlandırılabilir yapmak için jquery betikleri kullanıyoruz. Ekran görüntüsü, GridWeb'in tarayıcı penceresindeki sağ alt tutamaç kullanılarak yeniden boyutlandırıldığını gösteriyor.

![yapılacaklar:resim_alternatif_Metin](resize-gridweb-in-the-browser-window_2.png)
### **Basit kod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
