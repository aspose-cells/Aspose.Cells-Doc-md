---
title: Excel Dosyasının Satır ve Sütunlarını Ekleme ve Silme
linktitle: Satır ve Sütun Ekleme ve Silme
type: docs
weight: 70
url: /tr/net/inserting-and-deleting-rows-and-columns/
description: Bu makalede, Aspose.Cells for .NET API numaralı telefona göre satır ve sütunların nasıl ekleneceği ve silineceği gösterilmektedir.
keywords: Aspose.Cells C# manage rows and columns, insert rows and columns, delete rows and columns
---
##  **giriiş**

İster sıfırdan yeni bir çalışma sayfası oluşturun ister mevcut bir çalışma sayfası üzerinde çalışın, daha fazla veriyi barındırmak için fazladan satır veya sütun eklememiz gerekebilir. Bunun tersine, çalışma sayfasında belirtilen konumlardaki satırları veya sütunları da silmemiz gerekebilir.
Bu gereksinimleri karşılamak için Aspose.Cells, aşağıda tartışılan çok basit bir sınıf ve yöntem seti sağlar.

###  **Satırları ve Sütunları Yönet**

Aspose.Cells bir sınıf sağlıyor[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Bir Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)koleksiyon, bir çalışma sayfasındaki satırları ve sütunları yönetmeye yönelik çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda tartışılmaktadır.

{{% alert color="primary" %}}

Satır veya sütunlar eklendiğinde çalışma sayfasındaki içerik aşağı veya sağa kaydırılır; satırlar veya sütunlar kaldırıldığında içerik yukarı veya sola kaydırılır.

{{% /alert %}}


##  **Satır ve Sütun Ekle**

###  **Satır Nasıl Eklenir**

 Çağırarak çalışma sayfasının herhangi bir yerine bir satır ekleyin.[**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak.[**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)metodu yeni satırın ekleneceği satırın indeksini alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

###  **Birden Çok Satır Nasıl Eklenir**

 Bir çalışma sayfasına birden çok satır eklemek için[**Satırları Ekle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak.[**Satırları Ekle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)yöntem iki parametre alır:

- Satır dizini, yeni satırların ekleneceği satırın dizini.
- Satır sayısı, eklenmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

###  **Biçimlendirmeyle Satır Nasıl Eklenir**

Biçimlendirme seçeneklerini içeren bir satır eklemek için[**Satırları Ekle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)süren aşırı yük[**EkleSeçenekler**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) parametre olarak. Yı kur[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) mülkiyet[**EkleSeçenekler**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) ile sınıf[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Numaralandırma.[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)Numaralandırmanın aşağıda listelendiği gibi üç üyesi vardır.

- SameAsAbove: Satırı yukarıdaki satırla aynı şekilde biçimlendirir.
- SameAsBelow: Satırı aşağıdaki satırla aynı şekilde biçimlendirir.
- Temizle: Biçimlendirmeyi temizler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

###  **Sütun Nasıl Eklenir**

 Geliştiriciler ayrıca çalışma sayfasının herhangi bir yerindeki sütunu çağırarak da sütun ekleyebilirler.[**Sütun Ekle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Toplamak.[**Sütun Ekle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)yöntem, yeni sütunun ekleneceği sütunun dizinini alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

##  **Satırları ve Sütunları Sil**

###  **Birden Çok Satır Nasıl Silinir?**

 Bir çalışma sayfasından birden çok satırı silmek için,[**Satırları Sil**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak.[**Satırları Sil**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)yöntem iki parametre alır:

- Satır dizini, satırların silineceği satırın dizini.
- Satır sayısı, silinmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


###  **Sütun Nasıl Silinir?**

 Çalışma sayfasında herhangi bir yerden bir sütunu silmek için[**Sütunu Sil**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak.[**Sütunu Sil**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)yöntem silinecek sütunun dizinini alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
