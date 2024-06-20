---
title: Bir Çalışma Sayfasını Kaldır
type: docs
weight: 30
url: /tr/net/aspose-cells-griddesktop/remove-a-worksheet/
keywords: GridDesktop, kaldır, çalışma sayfası
description: Bu makale, GridDesktop ta çalışma sayfasını nasıl kaldıracağını tanıtır.
---

{{% alert color="primary" %}} 

Bu konu, Aspose.Cells.GridDesktop kontrolünü kullanarak çalışma sayfalarını kaldırmayı tartışmaktadır. Bu temel görevi gerçekleştirmenin birkaç basit yaklaşımı vardır.

{{% /alert %}} 
## **Bir Çalışma Sayfasını Kaldırmak**
Aspose.Cells.GridDesktop kontrolünü kullanarak bir çalışma sayfasını kaldırmak için lütfen aşağıdaki adımları izleyin:

1. Aspose.Cells.GridDesktop kontrolünü forma ekleyin.
1. GridDesktop kontrolündeki Worksheets koleksiyonunun Remove yöntemini çağırın.
### **Çalışma Sayfası İndex'ini Kullanma**
Bu yaklaşımda, Grid'in çalışma sayfaları koleksiyonundaki çalışma sayfasının indeksini (sıradaki) kaldırılacak çalışma sayfasının indeksi olarak geçmek yeterlidir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **Çalışma Sayfası Adını Kullanma**
Eğer çalışma sayfasının adı biliniyorsa, belirli bir çalışma sayfasını adını belirterek kaldırmak mümkündür.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Kaldır, bir metodur. Çalışma sayfasını indeksine (koleksiyon içinde) göre kaldırmak için kullanın veya indeks/adsına göre çalışma sayfasını kaldırmak için RemoveAt metodunu kullanın.

{{% /alert %}}
