---
title: DataTable dan Grid e Veri İçe Aktarma
type: docs
weight: 50
url: /tr/net/aspose-cells-griddesktop/import-data-from-a-datatable-to-grid/
keywords: GridDesktop, içe aktar, veri, datatable
description: Bu makale, GridDesktop ta veri içe aktarmanın nasıl yapıldığını tanıtıyor.
---

{{% alert color="primary" %}} 

.NET Framework'ün yayımlanmasından bu yana, Microsoft, bir DataTable nesnesi şeklinde çevrimdışı modda veri depolamanın mükemmel bir yolunu sunmuştur. Geliştiricilerin ihtiyaçlarını anlayarak, Aspose.Cells.GridDesktop da bir veri tablosundan veri içe aktarma işlemini destekler. Bu konu, bunun nasıl yapılacağını tartışmaktadır.

{{% /alert %}} 
## **Örnek**
Aspose.Cells.GridDesktop kontrolünü kullanarak bir veri tablosunun içeriğini içe aktarmak için: Bir form üzerine Aspose.Cells.GridDesktop kontrolünü ekleyin.

1. İçe aktarılacak veriyi içeren bir DataTable nesnesi oluşturun.
2. İstenen çalışsayfanın referansını alın.
1. İstenen çalışma sayfasının referansını alın.
4. Çalışsayfanın sütun başlıklarını veri tablosunun sütun adlarına göre ayarlayın.
5. İstenirse sütunların genişliğini ayarlayın.
1. İstenirse sütunların genişliğini ayarlayın.
1. Çalışma sayfasını görüntüleyin.

Aşağıdaki örnekte, DataTable nesnesi oluşturduk ve Products adlı bir veritabanı tablosundan alınan bazı verilerle doldurduk. Son olarak, o DataTable nesnesinden Aspose.Cells.GridDesktop kullanarak istenilen bir çalışma sayfasına veri aktardık.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
