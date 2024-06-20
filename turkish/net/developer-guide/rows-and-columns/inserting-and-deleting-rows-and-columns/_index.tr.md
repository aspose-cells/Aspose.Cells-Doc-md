---
title: Excel dosyasının Satırları ve Sütunları Eklemek ve Silmek
linktitle: Satırları ve Sütunları Eklemek ve Silmek
type: docs
weight: 70
url: /tr/net/inserting-and-deleting-rows-and-columns/
description: Bu makale, Aspose.Cells for .NET API si ile satırları ve sütunları nasıl ekleyip sileceğinizi gösterir.
keywords: Aspose.Cells C#, satırları ve sütunları yönetir, satırlar ve sütunlar ekler, satırlar ve sütunlar siler
---

## **Giriş**

Sıfırdan yeni bir çalışma sayfası oluştururken veya mevcut bir çalışma sayfası üzerinde çalışırken, daha fazla veri eklemek için ekstra satırlar veya sütunlar eklememiz gerekebilir. Tersine, çalışma sayfasının belirli pozisyonlarından satırları veya sütunları silebiliriz.
Bu gereksinimleri karşılamak için Aspose.Cells, aşağıda tartışılan çok basit bir sınıf ve yöntem seti sağlar.

### **Satırları ve Sütunları Yönetmek**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişimi sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) koleksiyonu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu sağlar.

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu, bir çalışma sayfasındaki satırları ve sütunları yönetmek için birkaç yöntem sağlar. Bunlardan bazıları aşağıda tartışılmıştır.

{{% alert color="primary" %}}

Satırlar veya sütunlar eklenirse, çalışma sayfasındaki içerik aşağıya veya sağa kaydırılır ve satırlar veya sütunlar kaldırılırsa içerik yukarıya veya sola kaydırılır.

{{% /alert %}}


## **Satırları ve Sütunları Eklemek**

### **Bir Satır Nasıl Eklenir**

Yeni bir satırı çalışma sayfasına herhangi bir konumda eklemek için [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) koleksiyonunun [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) yöntemini çağırarak yapılır. Yeni satırın ekleneceği satırın indeksini alan [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) yöntemi çağrılır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **Birkaç Satır Nasıl Eklenir**

Birden çok satırı çalışma sayfasına eklemek için [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) koleksiyonunun [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) yöntemini çağırın. [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) yöntemi iki parametre alır:

- Satır indeksi, yeni satırların ekleneceği satırın indeksi.
- Satır sayısı, eklenmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **Biçimlendirme Seçenekleriyle Bir Satır Nasıl Eklenir**

Biçimlendirme seçenekleriyle bir satır eklemek için, bir parametre olarak [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) kullanan [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) aşırı yüklemesini kullanın. [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) sınıfının [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) özelliğini [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Sıralama ile ayarlayın. [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Sıralama'nın aşağıda listelenen üç üyesi bulunmaktadır.

- SameAsAbove: Satırı üstteki satır ile aynı şekilde biçimlendirir.
- SameAsBelow: Satırı alttaki satır ile aynı şekilde biçimlendirir.
- Temizle: Biçimlendirmeyi temizler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **Bir Sütun Nasıl Eklenir**

Geliştiriciler, herhangi bir konumda çalışma sayfasına bir sütun ekleyebilirler, bunun için [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) koleksiyonunun [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) yöntemini çağırarak yapılır. [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) yöntemi çağrılır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **Satırları ve Sütunları Silmek**

### **Birden Fazla Satır Nasıl Silinir**

Çalışma sayfasından birden fazla satır silmek için, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonunun [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) yöntemini çağırın. [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) yöntemi iki parametre alır:

- Satır endeksi, satırların silineceği başlangıç satırının endeksi.
- satır sayısı, silinmesi gereken toplam satır sayısı

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **Bir Sütunu Nasıl Silebilirsiniz**

Herhangi bir konumda faaliyet sayfasından bir sütun silmek için, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonunun [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) yöntemini çağırın. [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) yöntemi silinecek sütunun endeksini alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
