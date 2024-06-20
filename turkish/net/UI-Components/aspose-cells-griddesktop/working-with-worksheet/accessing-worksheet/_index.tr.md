---
title: Çalışma Sayfasına Erişme
type: docs
weight: 10
url: /tr/net/aspose-cells-griddesktop/access-worksheet/
keywords: GridDesktop,çalışma sayfası
description: Bu makale, GridDesktop ta çalışma sayfası ile nasıl çalışılacağını tanıtır.
---

{{% alert color="primary" %}} 

Bir çalışma sayfası, bir Excel dosyasının ayrılmaz bir parçasıdır. Aslında, bir Excel dosyası bir veya daha fazla çalışma sayfasından oluşur. Her bir çalışma sayfası yalnızca en fazla 65.536 satır ve 256 sütundan oluşabilir. Excel dosyasındaki verileri tutan çalışma sayfasıdır.

Aspose.Cells.GridDesktop, var olan ve yeni Excel dosyaları oluşturabilir ve manipüle edebilir, dolayısıyla Aspose.Cells.GridDesktop kullanarak çalışma sayfalarına erişmenin bir yolu elbette vardır. Bu konu, bunu tartışmaktadır.

{{% /alert %}} 
## **Çalışma Sayfası İndex'ini Kullanma**
Geliştiriciler, aşağıdaki örnekte gösterildiği gibi herhangi bir çalışma sayfasına erişmek için istenen çalışma sayfasının çalışma sayfası indeksi kullanarak bir çalışma sayfasının örneğine erişebilir. Bu yaklaşım, bir Excel dosyasındaki bir dizi çalışma sayfası üzerinden döngü yapmak için uygundur.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Çalışma Sayfası Adını Kullanma**
Eğer çalışma sayfasının adı biliniyorsa, aşağıdaki gibi adını kullanarak bir çalışma sayfasına erişmek mümkündür.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Etkin Bir Çalışma Sayfasına Erişme**
Bir Excel dosyasının birden fazla çalışma sayfası olması mümkündür. Kullanıcının üzerinde çalıştığı sayfa etkin çalışma sayfası olarak adlandırılır. Etkin bir sayfaya erişmek mümkündür.

Etkin bir çalışma sayfasına erişmek için Aspose.Cells.GridDesktop'un iki yaklaşımı vardır:
### **ActiveSheetIndex Özelliğini Kullanma**
Aspose.Cells.GridDesktop kontrolünü kullanarak etkin bir çalışma sayfasına erişmenin bir yolu, GridDesktop kontrolünün ActiveSheetIndex özelliğini kullanmaktır. Bu özellik kullanılarak, Aspose.Cells.GridDesktop kontrolündeki etkin çalışma sayfasının indeksi alınabilir. Ardından bu indeks, aşağıda gösterildiği gibi bir çalışma sayfasına erişmek için geleneksel bir şekilde kullanılabilir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **GetActiveWorksheet Yöntemini Kullanma**
Diğer yaklaşım, GridDesktop kontrolünün GetActiveWorksheet yöntemini çağırmaktır. Bu yöntem, Aspose.Cells.GridDesktop kontrolündeki şu anda etkin olan çalışma sayfasının bir referansını sağlar.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
