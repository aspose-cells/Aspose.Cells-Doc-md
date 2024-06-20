---
title: Tarayıcı penceresinde GridWeb i yeniden boyutlandırın
type: docs
weight: 40
url: /tr/net/aspose-cells-gridweb/resize-gridweb-in-the-browser-window/
keywords: GridWeb, boyutlandırma
description: Bu makale, GridWeb de nasıl yeniden boyutlandırılacağını tanıtır.
---

## **Olası Kullanım Senaryoları**
Bazen Aspose.Cells.GridWeb'in kendisini tarayıcı penceresine göre yeniden boyutlandırmasını istersiniz. GridWeb'in her zaman boyutunu (yükseklik, genişlik) ayarlamasını ve tarayıcı penceresinin boyutuna uygun olmasını isteyebilirsiniz. Aspose.Cells.GridWeb, bu amaca yönelik istemci tarafında *resize()* işlevi sağlar. Dahası, GridWeb kontrolünü tarayıcı penceresinde yeniden boyutlandırılabilir hale getirebilirsiniz. Örneğin, genişlik/yüksekliğini özelleştirmek için alt sağ kolu (fare aracılığıyla) kullanabilirsiniz. Ayrıca bu işlevin çalışması için projenizin sayfa kaynağında jquery JavaScript dosyalarını da belirtmeniz gerekebilir.
## **GridWeb'in resize yöntemini kullanma**
Aşağıdaki kod, her 100 milisaniyede bir boyutlandırma işlemi olup olmadığını kontrol eder. Daha fazla boyutlandırma işlemi olmadığında, o zaman boyutlandırma işleminin artık bittiğini düşünür. GridWeb'e içe aktarılan örnek bir şablon dosyası kullanıyoruz. GridWeb'in boyutunu tarayıcı penceresinde yeniden boyutlandırmak için istemci tarafı kodunu kullanıyoruz. Ekran görüntüsü, tarayıcı penceresini boyutlandırırken GridWeb'in kendisini buna göre boyutlandırdığını göstermektedir.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_1.png)
### **Örnek Kod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **GridWeb'i resizable yapmak için resizable jquery ui özelliğini kullanma**
Aşağıdaki kod, GridWeb kontrolünün tarayıcı penceresinde yeniden boyutlandırılmasını sağlar. Örneğin, GridWeb'in boyutunu özelleştirmek için alt sağ köşe kolu kullanabilirsiniz. İlk olarak GridWeb'e içeri aktarılan aynı şablon dosyasını kullanırız. GridWeb'i yeniden boyutlandırmak için jquery betiklerini kullanırız. Ekran görüntüsü, GridWeb'in tarayıcı penceresinde alt sağ köşe kolunu kullanarak boyutlandırıldığını göstermektedir.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_2.png)
### **Örnek Kod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
