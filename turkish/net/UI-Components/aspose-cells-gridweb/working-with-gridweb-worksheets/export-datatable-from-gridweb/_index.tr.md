---
title: GridWeb den DataTable ı Dışa Aktar
type: docs
weight: 70
url: /tr/net/aspose-cells-gridweb/export-datatable-from-gridweb/
keywords: GridWeb,dışa aktar
description: Bu makale, GridWeb de datatable ın nasıl dışa aktarılacağını tanıtıyor.
---

{{% alert color="primary" %}} 

[GridWeb'e DataView İçe Aktar](/cells/tr/net/aspose-cells-gridweb/import-dataview-to-gridweb/) Aspose.Cells.GridWeb kontrolüne DataView içeriğini içe aktarmaktan bahsetti. Bu konu, Aspose.Cells.GridWeb kontrolünden verilerin DataTable'a aktarılmasını tartışmaktadır.

{{% /alert %}} 
## **Tablo Verisi Dışa Aktarma**
### **Belirli bir DataTable'a**
Çalışma sayfası verilerini belirli bir DataTable nesnesine dışa aktarmak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Belirli bir DataTable nesnesi oluşturun.
1. Seçilen hücrelerin verilerini belirtilen DataTable nesnesine dışa aktarın.

Aşağıdaki örnek, dört sütunu olan belirli bir DataTable nesnesi oluşturur. Çalışma sayfasındaki veriler, çalışma sayfasında görünen tüm satır ve sütunlardan başlayarak, zaten oluşturulmuş bir DataTable nesnesine dışa aktarılır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **Yeni bir DataTable'a**
Bazen bir DataTable nesnesi oluşturmak istemezsiniz, sadece çalışma sayfasındaki verileri yeni bir DataTable nesnesine dışa aktarmaya ihtiyacınız vardır.

Aşağıdaki örnek, Export yönteminin kullanımını farklı bir şekilde göstermeye çalışır. Etkin çalışma sayfasının referansını alır ve o çalışma sayfasının tüm verilerini yeni bir DataTable nesnesine dışa aktarır. DataTable nesnesi istediğiniz şekilde kullanılabilir. Örneğin, DataTable nesnesini verileri görüntülemek için bir GridView'e bağlamak mümkündür.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}
