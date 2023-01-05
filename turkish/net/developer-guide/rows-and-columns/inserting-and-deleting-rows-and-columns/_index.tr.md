---
title: Excel dosyasına Satır ve Sütun Ekleme ve Silme
linktitle: Satır ve Sütun Ekleme ve Silme
type: docs
weight: 70
url: /tr/net/inserting-and-deleting-rows-and-columns/
---
## **Giriş**

Sıfırdan yeni bir çalışma sayfası oluştururken veya mevcut bir çalışma sayfası üzerinde çalışırken, daha fazla veriyi barındırmak için fazladan satır veya sütun eklememiz gerekebilir. Tersine, çalışma sayfasında belirtilen konumlardaki satırları veya sütunları da silmemiz gerekebilir.
Bu gereklilikleri yerine getirmek için Aspose.Cells, aşağıda tartışılan çok basit bir sınıflar ve yöntemler seti sağlar.

### **Satırları ve Sütunları Yönet**

Aspose.Cells bir sınıf sağlar[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

 bu[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)koleksiyon, bir çalışma sayfasındaki satırları ve sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda tartışılmaktadır.

{{% alert color="primary" %}}

Satır veya sütun eklendiğinde çalışma sayfasındaki içerik aşağı veya sağa kaydırılır ve satır veya sütunlar kaldırılırsa içerik yukarı veya sola kaydırılır.

{{% /alert %}}


## **Satır ve Sütun Ekleme**

### **Satır Ekle**

 çağırarak çalışma sayfasına herhangi bir konumda bir satır ekleyin.[**Satır Ekle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. bu[**Satır Ekle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)method yeni satırın ekleneceği satırın indeksini alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **Birden Fazla Satır Ekle**

 Bir çalışma sayfasına birden çok satır eklemek için[**Satır Ekle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. bu[**Satır Ekle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)yöntem iki parametre alır:

- Satır dizini, yeni satırların ekleneceği satırın dizini.
- Satır sayısı, eklenmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **Biçimlendirmeyle Satır Ekleme**

Biçimlendirme seçenekleriyle bir satır eklemek için[**Satır Ekle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)aşırı yüklenme[**Ekleme Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) parametre olarak. Yı kur[**Kopya BiçimiTürü**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) mülkiyet[**Ekleme Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) ile sınıf[**Kopya BiçimiTürü**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Numaralandırma. bu[**Kopya BiçimiTürü**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)Numaralandırmanın aşağıda listelendiği gibi üç üyesi vardır.

- SameAsAbove: Satırı yukarıdaki satırla aynı şekilde biçimlendirir.
- SameAsBelow: Satırı aşağıdaki satırla aynı şekilde biçimlendirir.
- Temizle: Biçimlendirmeyi temizler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **Sütun Ekle**

 Geliştiriciler ayrıca, çalışma sayfasına herhangi bir konumda şunu çağırarak bir sütun ekleyebilir:[**Sütun Ekle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Toplamak. bu[**Sütun Ekle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)method yeni kolonun ekleneceği kolonun indeksini alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **Satırları ve Sütunları Sil**

### **Birden Çok Satırı Sil**

Bir çalışma sayfasından birden çok satırı silmek için[**Satırları Sil**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. bu[**Satırları Sil**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)yöntem iki parametre alır:

- Satır dizini, satırların silineceği satırın dizini.
- Satır sayısı, silinmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **Bir Sütunu Sil**

 Herhangi bir konumdaki çalışma sayfasından bir sütunu silmek için[**Sütunu Sil**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. bu[**Sütunu Sil**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)Yöntem, silinecek sütunun dizinini alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
