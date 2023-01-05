---
title: DataTable'ı GridWeb'den dışa aktarın
type: docs
weight: 70
url: /tr/net/export-datatable-from-gridweb/
---
{{% alert color="primary" %}} 

[DataView'u GridWeb'e Aktarın](/cells/tr/net/import-dataview-to-gridweb/)bir DataView içeriğini Aspose.Cells.GridWeb kontrolüne aktarmaktan bahsetti. Bu konuda, Aspose.Cells.GridWeb denetimindeki verilerin bir DataTable'a aktarılması anlatılmaktadır.

{{% /alert %}} 
## **Çalışma Sayfası Verilerini Dışa Aktarma**
### **Belirli bir DataTable'a**
Çalışma sayfası verilerini belirli bir DataTable nesnesine vermek için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Belirli bir DataTable nesnesi oluşturun.
1. Seçilen hücrelerin verilerini belirtilen DataTable nesnesine aktarın.

Aşağıdaki örnek, dört sütunlu belirli bir DataTable nesnesi oluşturur. Çalışma sayfası verileri, çalışma sayfasında tüm satırların ve sütunların göründüğü ilk hücreden başlayarak önceden oluşturulmuş bir DataTable nesnesine aktarılır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **Yeni bir DataTable'a**
Bazen bir DataTable nesnesi oluşturmak istemezsiniz, sadece çalışma sayfası verilerini yeni bir DataTable nesnesine aktarmanız gerekir.

Aşağıdaki örnek, Export yönteminin kullanımını göstermek için farklı bir yol deniyor. Aktif çalışma sayfasının referansını alır ve bu çalışma sayfasının tüm verilerini yeni bir DataTable nesnesine verir. DataTable nesnesi artık istediğiniz şekilde kullanılabilir. Örneğin, verileri görüntülemek için DataTable nesnesini bir GridView'e bağlamak mümkündür.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}
