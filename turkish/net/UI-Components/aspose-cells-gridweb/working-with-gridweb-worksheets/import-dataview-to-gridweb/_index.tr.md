---
title: GridWeb de DataView İçe Aktar
type: docs
weight: 60
url: /tr/net/aspose-cells-gridweb/import-dataview-to-gridweb/
keywords: GridWeb, içe aktar
description: Bu makale, GridWeb de veri içe aktarmanın nasıl yapıldığını tanıtıyor.
---

{{% alert color="primary" %}} 

Microsoft .NET Framework'ün piyasaya sürülmesiyle verileri depolamanın yeni bir yolu tanıtıldı. Şimdi, verileri çevrimdışı modda depolayan DataSet, DataTable ve DataView nesneleri mevcut. Bu nesneler veri depoları olarak çok kullanışlıdır. Aspose.Cells.GridWeb kullanarak, DataTable veya DataView nesnelerinden herhangi birini çalışma sayfalarına içe aktarmak mümkündür. Aspose.Cells.GridWeb yalnızca DataView nesnesinden veri içe aktarmayı destekler, ancak DataTable nesnesi dolaylı olarak da kullanılabilir. Bu özelliği detaylı olarak tartışalım.

{{% /alert %}} 
## **DataView'den Veri İçe Aktarma**
GridWeb kontrolünde GridWorsheetCollection'ın ImportDataView yöntemini kullanarak DataView nesnesinden veri içe aktarın. ImportDataView yöntemine veri içe aktarılacak DataView nesnesini iletebilirsiniz. İçe aktarma sırasında sütun başlığı ve veri stilleri belirtmek mümkündür.

{{% alert color="primary" %}} 

Bir DataView nesnesinden veri içe aktarıldığında, içe aktarılan veriyi tutmak için yeni bir çalışma sayfası oluşturulur. Çalışma sayfasının adı, DataTable ile aynıdır.

{{% /alert %}} 

**Çıktı: DataView'dan içe aktarılan veriler yeni bir çalışma sayfasına** 

![todo:image_alt_text](import-dataview-to-gridweb_1.png)

Sütun genişlikleri içerdikleri tüm verileri göstermek için ayarlanır. DataView'dan veri içe aktarıldığında, sütun genişlikleri otomatik olarak ayarlanmaz. Kullanıcıların bunu kendileri ayarlamaları gerekir. Sütun genişliklerini programatik olarak ayarlamak için, [Satırları ve Sütunları Yeniden Boyutlandır](/cells/tr/net/aspose-cells-gridweb/resize-rows-and-columns/) sayfasına bakınız.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

ImportDataView yönteminin aşırı yüklenmiş bir sürümü, geliştiricilere içe aktarılan verileri tutan çalışma sayfasının adını ve DataView nesnesinden kaç satır ve sütunun içe aktarılacağını belirtme olanağı sağlar.

{{% /alert %}}
