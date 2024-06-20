---
title: Bir Çalışma Sayfası Eklemek veya Eklemek
type: docs
weight: 20
url: /tr/net/aspose-cells-griddesktop/add-or-insert-a-worksheet/
keywords: GridDesktop,ekleme,çalışma sayfası,çalışma sayfası ekleme
description: Bu makale, GridDesktop ta çalışma sayfası eklemenin veya eklemenin nasıl yapılacağını tanıtır.
---

{{% alert color="primary" %}} 

Bu konuda, Aspose.Cells.GridDesktop kullanarak bir Excel dosyasına çalışma sayfaları eklemek veya eklemek için teknikleri tartışacağız. Ekleme ve eklemek arasındaki fark, eklemenin sadece bir çalışma sayfasının Excel dosyasının çalışma sayfaları koleksiyonunun sonuna eklenmesi anlamına gelir ancak eklemenin, çalışma sayfaları koleksiyonunda belirli bir konuma bir çalışma sayfası eklemek anlamına gelir.

{{% /alert %}} 
## **Çalışma Sayfası Ekleme**
Aspose.Cells.GridDesktop kullanarak çalışma sayfası eklemek için lütfen aşağıdaki adımları izleyin:

1. İçe aktarılacak veriyi içeren bir DataTable nesnesi oluşturun.
1. GridDesktop kontrolünde Çalışma Sayfaları koleksiyonunun Ekle yöntemini çağırın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


Ekle yönteminin birçok aşırı yüklenmiş sürümü mevcuttur. Yukarıdaki aşırı yüklenmiş sürümü kullanarak örneğin, bir çalışma sayfası varsayılan bir sayfa adıyla Excel dosyasına eklenir. Ekle yönteminin diğer aşırı yüklenmiş sürümleri kullanılarak, aşağıdaki örnekte gösterildiği gibi adı tanımlamak mümkündür.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **Çalışma Sayfası Ekleme**
Aspose.Cells.GridDesktop kullanarak çalışma sayfası eklemek için lütfen aşağıdaki adımları izleyin:

1. Aspose.Cells.GridDesktop kontrolünü forma ekleyin.
1. GridDesktop kontrolünde Çalışma Sayfaları koleksiyonunun Ekle yöntemini çağırın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

ÖNEMLİ: Microsoft Excel (97-2003 XLS), en fazla 65.536 satır ve 256 sütun içeren Excel çalışma sayfalarını destekler. Aspose.Cells.GridDesktop aynı standartları takip eder. Aspose.Cells.GridDesktop kontrolünde geliştiriciler, standart limitin üzerindeki satır ve sütunları kullanabilirler ancak Grid verilerini bir Excel dosyasına kaydetmeye çalıştıklarında bir istisna oluşur. Bu, yalnızca 65.536 satır ve 256 sütun içeren verilerin bir Excel XLS dosyasına Aspose.Cells.GridDesktop kullanılarak kaydedilebileceği anlamına gelir; XLSX (MS Excel 2007/2010) dosya biçemi kullanıldığında böyle bir sınırlama yoktur.

{{% /alert %}}
