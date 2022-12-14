---
title: DataView'u GridWeb'e Aktarın
type: docs
weight: 60
url: /tr/net/import-dataview-to-gridweb/
---
{{% alert color="primary" %}} 

Microsoft .NET Framework'ün piyasaya sürülmesiyle, yeni bir veri depolama yöntemi tanıtıldı. Artık verileri çevrimdışı modda depolayan DataSet, DataTable ve DataView nesneleri. Bu nesneler, veri havuzları olarak çok kullanışlıdır. Aspose.Cells.GridWeb kullanarak DataTable veya DataView nesnelerinden çalışma sayfalarına veri aktarmak mümkündür. Aspose.Cells.GridWeb yalnızca bir DataView'dan veri almayı destekler. nesne ancak bir DataTable nesnesi de dolaylı olarak kullanılabilir. Bu özelliği ayrıntılı olarak tartışalım.

{{% /alert %}} 
## **DataView'dan Verileri İçe Aktarma**
GridWeb denetiminde GridWorsheetCollection'ın ImportDataView yöntemini kullanarak bir DataView nesnesinden verileri içe aktarın. Verileri içe aktarmak istediğiniz DataView nesnesini ImportDataView yöntemine iletin. İçe aktarma sırasında sütun başlığı ve veri stilleri belirtmek mümkündür.

{{% alert color="primary" %}} 

Veriler bir DataView nesnesinden içe aktarıldığında, içe aktarılan verileri tutmak için yeni bir çalışma sayfası oluşturulur. Çalışma sayfası, DataTable ile aynı şekilde adlandırılır.

{{% /alert %}} 

**Çıktı: DataView'dan yeni bir çalışma sayfasına aktarılan veriler** 

![yapılacaklar:resim_alternatif_Metin](import-dataview-to-gridweb_1.png)

 Sütunların genişlikleri, içerdikleri tüm verileri gösterecek şekilde ayarlanır. Veriler DataView'dan içe aktarıldığında, sütun genişlikleri otomatik olarak ayarlanmaz. Kullanıcıların bunları kendileri ayarlaması gerekir. Sütun genişliklerini programlı olarak ayarlamak için bkz.[Satırları ve Sütunları Yeniden Boyutlandırma](/cells/tr/net/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

ImportDataView yönteminin aşırı yüklenmiş bir sürümü, geliştiricilerin, içe aktarılan verileri tutan sayfanın adını ve DataView nesnesinden içe aktarılacak belirli sayıda satır ve sütunu belirtmesine olanak tanır.

{{% /alert %}}
