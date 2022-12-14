---
title: Çalışma Sayfası Ekleme veya Ekleme
type: docs
weight: 20
url: /tr/net/add-or-insert-a-worksheet/
---
{{% alert color="primary" %}} 

Bu konuda, Aspose.Cells.GridDesktop kullanarak bir Excel dosyasına çalışma sayfası ekleme veya ekleme tekniklerini tartışacağız. Çalışma sayfası ekleme ve çalışma sayfası ekleme arasındaki fark, ek olarak, bir çalışma sayfasının Excel dosyasının çalışma sayfaları koleksiyonunun sonuna eklenmesidir, ancak ekleme, çalışma sayfası koleksiyonundaki belirli bir konuma bir çalışma sayfası eklemek anlamına gelir.

{{% /alert %}} 
## **Çalışma Sayfası Ekleme**
Aspose.Cells.GridDesktop kullanarak bir çalışma sayfası eklemek için lütfen aşağıdaki adımları izleyin:

1. Bir forma Aspose.Cells.GridDesktop denetimi ekleyin.
1. GridDesktop denetiminde Worksheet koleksiyonunun Add yöntemini çağırın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


Add yönteminin birçok aşırı yüklenmiş sürümü mevcuttur. Örneğin, yukarıdaki aşırı yüklenmiş sürüm kullanılarak, Excel dosyasına varsayılan bir sayfa adıyla bir çalışma sayfası eklenir. Add yönteminin diğer aşırı yüklenmiş sürümlerini kullanarak, adı aşağıdaki örnekte gösterildiği gibi tanımlamak mümkündür.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **Çalışma Sayfası Ekleme**
Aspose.Cells.GridDesktop kullanarak bir çalışma sayfası eklemek için lütfen aşağıdaki adımları izleyin:

1. Aspose.Cells.GridDesktop denetimini bir forma ekleyin.
1. GridDesktop denetiminde Worksheets koleksiyonunun Insert yöntemini çağırın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

ÖNEMLİ: Microsoft Excel (97-2003 XLS), en fazla 65.536 satır ve 256 sütun içeren Excel sayfalarını destekler. Aspose.Cells.GridDesktop aynı standartları takip eder. Aspose.Cells.GridDesktop denetiminde, geliştiriciler standart sınırdan daha fazla satır ve sütun içeren çalışma sayfaları ekleyebilir veya ekleyebilir, ancak Grid verilerini bir Excel dosyasına kaydetmeye çalıştıklarında bir istisna atılır. Bu, yalnızca 65.536 satır ve 256 sütunda bulunan verilerin bir Excel XLS dosyasına Aspose.Cells.GridDesktop kullanılarak kaydedilebileceği anlamına gelir, XLSX (MS Excel 2007/2010) dosya biçimini kullanıyorsanız, ancak böyle bir sınırlama yoktur.

{{% /alert %}}
