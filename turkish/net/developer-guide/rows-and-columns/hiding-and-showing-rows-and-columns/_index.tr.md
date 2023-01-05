---
title: Satırları ve Sütunları Gizleme ve Gösterme
type: docs
weight: 60
url: /tr/net/hiding-and-showing-rows-and-columns/
---
{{% alert color="primary" %}}

Bazen, bir çalışma sayfasındaki belirli satırları veya sütunları gizlemek ve daha sonra görüntülemek mantıklıdır. Microsoft Excel bu özelliği sağlar ve Aspose.Cells de sağlar.

{{% /alert %}}

## **Satırların ve Sütunların Görünürlüğünü Kontrol Etme**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine olanak tanır. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon. bu[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)koleksiyon, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan birkaçı aşağıda tartışılmaktadır.

### **Satırları ve Sütunları Gizleme**

 Geliştiriciler, çağırarak bir satırı veya sütunu gizleyebilirsiniz.[**Satırı Gizle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) ve[**Sütunu Gizle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) yöntemleri[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)sırasıyla koleksiyon. Her iki yöntem de belirli satır veya sütunu gizlemek için satır ve sütun dizinini parametre olarak alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Sırasıyla satır yüksekliğini veya sütun genişliğini 0 olarak ayarlayarak bir satırı veya sütunu gizlemek de mümkündür.

{{% /alert %}}

### **Satırları ve Sütunları Gösterme**

 Geliştiriciler, herhangi bir gizli satırı veya sütunu çağırarak gösterebilir.[**Satırı Göster**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) ve[**Sütunu Göster**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) yöntemleri[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)sırasıyla koleksiyon. Her iki yöntem de iki parametre alır:

- **Satır veya sütun dizini** - belirli bir satır veya sütunu göstermek için kullanılan bir satır veya sütun dizini.
- **Satır yüksekliği veya sütun genişliği** - gösterildikten sonra satıra veya sütuna atanan satır yüksekliği veya sütun genişliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Gizli bir sütunu görünür hale getirirken, daha önce atanmış genişliğe veya orijinal genişliğine geri döndürmeniz gerekirse, lütfen sütunu negatif genişlikle gösterin. Örneğin: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Birden Çok Satırı ve Sütunu Gizleme**

 Geliştiriciler, çağrı yaparak aynı anda birden çok satırı veya sütunu gizleyebilirsiniz.[**Satırları Gizle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) ve[**Sütunları Gizle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) yöntemleri[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)sırasıyla koleksiyon. Her iki yöntem de başlangıç satır veya sütun indeksini ve gizlenmesi gereken satır veya sütun sayısını parametre olarak alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

 kullanmak da mümkündür.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıf'[**Satırları Göster**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) ve[**Sütunları Göster**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)birden çok satırı ve sütunu görünür hale getirme yöntemleri.

{{% /alert %}}
