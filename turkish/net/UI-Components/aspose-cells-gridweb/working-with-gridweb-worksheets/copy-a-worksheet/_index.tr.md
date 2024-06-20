---
title: Bir Çalışma Sayfası Kopyalamak
type: docs
weight: 50
url: /tr/net/aspose-cells-gridweb/copy-a-worksheet/
keywords: GridWeb, kopya, GridWorksheet
description: Bu makale, GridWeb de bir çalışma sayfasını (GridWorksheet) kopyalamanın nasıl yapıldığını tanıtır.
---

{{% alert color="primary" %}} 

[Çalışma Sayfaları Eklemek](/cells/tr/net/aspose-cells-gridweb/add-worksheets/) Aspose.Cells.GridWeb'e yeni çalışma sayfaları eklemenin nasıl yapıldığını açıklar. Ayrıca Aspose.Cells.GridWeb den başka bir çalışma sayfasının kopyasını (veya replikasını) eklemek de mümkündür. Bu özellik, aynı veya benzer verilerin bir çalışma sayfasından başka bir çalışma sayfasına da ihtiyaç duyulduğunda kullanışlı olabilir. Bu durumda, mevcut bir çalışma sayfasını kopyalamak ve Aspose.Cells.GridWeb'e yeni bir çalışma sayfası olarak eklemek, sıfırdan oluşturmaktan daha kolaydır.

{{% /alert %}} 
## **Çalışsayfalarını Kopyalama**
### **Sayfa indeksi Kullanma**
Aşağıdaki örnek kod, GridWorksheetCollection'ın AddCopy yönteminde çalışma sayfasının dizinini belirterek GridWeb kontrolüne bir çalışma sayfasının kopyasını nasıl ekleyeceğini gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **Sayfa Adını Kullanma**
Aşağıda yer alan örnek kod, çalışma sayfasının adını belirterek GridWorksheetCollection'ın AddCopy yöntemini kullanarak GridWeb kontrolüne bir çalışma sayfasının kopyasını nasıl ekleyeceğini gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

AddCopy metodu, yeni eklenen çalışma sayfasının dizinini döndürür ve bu, çalışma sayfası örneğine erişmek için kullanılabilir. Çalışma sayfalarına nasıl erişileceğine ilişkin daha fazla bilgi için [Çalışma Sayfalarına Erişim](/cells/tr/net/aspose-cells-gridweb/access-worksheets/) bölümünü okuyun.

{{% /alert %}}
