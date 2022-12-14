---
title: Çalışma Sayfası Kaldırma
type: docs
weight: 30
url: /tr/net/remove-a-worksheet/
---
{{% alert color="primary" %}} 

Bu konuda, Aspose.Cells.GridDesktop denetimi kullanılarak çalışma sayfalarının kaldırılması anlatılmaktadır. Bu temel görevi gerçekleştirmek için birkaç basit yaklaşım vardır.

{{% /alert %}} 
## **Bir Çalışma Sayfasını Kaldırma**
Aspose.Cells.GridDesktop kontrolünü kullanarak bir çalışma sayfasını kaldırmak için lütfen aşağıdaki adımları izleyin:

1. Aspose.Cells.GridDesktop denetimini bir forma ekleyin.
1. Worksheets koleksiyonunun GridDesktop denetimindeki Remove yöntemini çağırın.
### **Çalışma Sayfası Dizinini Kullanma**
Bu yaklaşımda, kaldırılacak çalışma sayfasının çalışma sayfası dizinini (kılavuzun çalışma sayfaları koleksiyonunda) geçirmeniz yeterlidir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **Çalışma Sayfası Adını Kullanma**
Çalışma sayfasının adı biliniyorsa, adını belirterek belirli bir çalışma sayfasını kaldırmak mümkündür.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Kaldır bir yöntemdir. Dizini kullanarak (çalışma sayfaları koleksiyonunda) bir çalışma sayfasını kaldırmak için kullanın veya dizini/adını kullanarak çalışma sayfasını kaldırmak için RemoveAt yöntemini kullanın.

{{% /alert %}}
