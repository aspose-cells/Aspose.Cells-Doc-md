---
title: Çalışma Sayfasına Erişim
type: docs
weight: 10
url: /tr/net/accessing-worksheet/
---
{{% alert color="primary" %}} 

Çalışma sayfası, bir Excel dosyasının ayrılmaz bir parçasıdır. Aslında, bir Excel dosyası bir veya daha fazla çalışma sayfasından oluşur. Her çalışma sayfası yalnızca 65.536 satır ve 256 sütundan oluşabilir. Bir Excel dosyasındaki verileri tutan çalışma sayfasıdır.

Aspose.Cells.GridDesktop, mevcut ve yeni Excel dosyalarını oluşturabilir ve değiştirebilir, bu nedenle, elbette, Aspose.Cells.GridDesktop kullanarak çalışma sayfalarına erişmenin bir yolu vardır. Bu konu nasıl yapılacağını tartışıyor.

{{% /alert %}} 
## **Çalışma Sayfası Dizinini Kullanma**
Geliştiriciler, aşağıdaki örnekte gösterildiği gibi herhangi bir çalışma sayfasının çalışma sayfası dizinini kullanarak herhangi bir Çalışma Sayfası örneğine erişebilir. Bu yaklaşım, bir Excel dosyasındaki birkaç çalışma sayfasını yinelemek için iyidir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Çalışma Sayfası Adını Kullanma**
Çalışma sayfasının adı biliniyorsa, aşağıda gösterildiği gibi bir çalışma sayfasına adını kullanarak erişmek mümkündür.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Etkin Bir Çalışma Sayfasına Erişme**
Bir Excel dosyasının birden fazla çalışma sayfası olması mümkündür. Kullanıcının üzerinde çalıştığı tek htata aktif çalışma sayfası denir. Aktif sayfaya erişmek mümkündür.

Etkin bir çalışma sayfasına erişmek için Aspose.Cells.GridDesktop iki yaklaşım sunar:
### **AcriveSheetIndex Özelliğini Kullanma**
Aspose.Cells.GridDesktop denetimini kullanarak etkin bir çalışma sayfasına erişmenin bir yolu, GridDesktop denetiminin ActiveSheetIndex özelliğini kullanmaktır. Bu özellik kullanılarak Aspose.Cells.GridDesktop kontrolünde aktif olan çalışma sayfasının indeksini almak mümkündür. Daha sonra bu dizin, aşağıda gösterildiği gibi çalışma sayfasına geleneksel bir şekilde erişmek için kullanılabilir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **GetActiveWorksheet Yöntemini Kullanma**
Diğer yaklaşım, GridDesktop denetiminin GetActiveWorksheet yöntemini çağırmaktır. Bu yöntem, aşağıda gösterildiği gibi Aspose.Cells.GridDesktop kontrolünde şu anda etkin olan çalışma sayfasının bir referansını sağlar.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
