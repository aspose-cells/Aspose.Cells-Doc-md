---
title: Çalışma Sayfalarını Kaldırma
type: docs
weight: 30
url: /tr/net/aspose-cells-gridweb/remove-worksheets/
keywords: GridWeb, kaldır, GridWorksheet ı kaldır, çalışma sayfası kaldır
description: Bu makale, GridWeb de bir çalışma sayfasını (GridWorksheet) nasıl kaldıracağınızı tanıtır.
---

{{% alert color="primary" %}} 

Bu konu, Aspose.Cells.GridWeb API'sını kullanarak Microsoft Excel dosyalarından çalışma sayfalarını nasıl kaldıracağınız hakkında bilgi sağlar. Bir çalışma sayfasını, sayfa dizinini veya adını belirterek kaldırmak mümkündür.

{{% /alert %}} 
## **Bir Çalışma Sayfasını Kaldırmak**
### **Sayfa Dizinini Kullanarak Kullanma**
Aşağıdaki kod, GridWorksheetCollection'ın RemoveAt metodunda sayfa indeksini belirterek bir çalışma sayfasının nasıl kaldırılacağını gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingIndex.cs" >}}
### **Sayfa Adını Kullanma**
Aşağıdaki kod, GridWorksheetCollection'ın RemoveAt metodunda sayfa adını belirterek bir çalışma sayfasının nasıl kaldırılacağını gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

Ayrıca, bir çalışma sayfasını referans veya örneğini kullanarak kaldırmak da mümkündür. Bunun için GridWorksheetCollection'ın Remove metodunu kullanın. Bu yaklaşım genellikle kullanılır.

{{% /alert %}}
