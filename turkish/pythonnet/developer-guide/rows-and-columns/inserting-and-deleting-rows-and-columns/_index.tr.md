---
title: Excel dosyasının Satırları ve Sütunları Eklemek ve Silmek
linktitle: Satırları ve Sütunları Eklemek ve Silmek
type: docs
weight: 70
url: /tr/python-net/inserting-and-deleting-rows-and-columns/
description: Bu makale, Aspose.Cells for Python via .NET API tarafından satırları ve sütunları nasıl ekleyip sileceğinizi göstermektedir.
keywords: Python Excel Kütüphanesi, Aspose.Cells Python satırları ve sütunları yönetme, Python da satırlar ve sütunlar ekleme, Python da satırları ve sütunları silme, Python da satırları ve sütunları kaldırma.
---

## **Giriş**

Sıfırdan yeni bir çalışma sayfası oluştururken veya mevcut bir çalışma sayfası üzerinde çalışırken, daha fazla veri eklemek için ekstra satırlar veya sütunlar eklememiz gerekebilir. Tersine, çalışma sayfasının belirli pozisyonlarından satırları veya sütunları silebiliriz.
Bu gereksinimleri karşılamak için Aspose.Cells for Python via .NET, aşağıda tartışılan çok basit bir sınıf ve yöntem seti sağlar.

### **Satırları ve Sütunları Yönetmek**

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden bir sınıf [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonu sağlar.

[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonu, bir çalışma sayfasındaki satırları ve sütunları yönetmek için birkaç yöntem sağlar. Bunlardan bazıları aşağıda tartışılmıştır.

{{% alert color="primary" %}}

Satırlar veya sütunlar eklenirse, çalışma sayfasındaki içerik aşağıya veya sağa kaydırılır ve satırlar veya sütunlar kaldırılırsa içerik yukarıya veya sola kaydırılır.

{{% /alert %}}


## **Satırları ve Sütunları Eklemek**

### **Bir Satır Nasıl Eklenir**

Yeni bir satırı çalışma sayfasına herhangi bir konumda eklemek için [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) koleksiyonunun [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) yöntemini çağırarak yapılır. Yeni satırın ekleneceği satırın indeksini alan [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) yöntemi çağrılır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARow-1.py" >}}

### **Birkaç Satır Nasıl Eklenir**

Birden çok satırı çalışma sayfasına eklemek için [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) koleksiyonunun [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) yöntemini çağırın. [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) yöntemi iki parametre alır:

- Satır indeksi, yeni satırların ekleneceği satırın indeksi.
- Satır sayısı, eklenmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.py" >}}

### **Biçimlendirme Seçenekleriyle Bir Satır Nasıl Eklenir**

Biçimlendirme seçenekleriyle bir satır eklemek için, bir parametre olarak [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) kullanan [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int-aspose.cells.InsertOptions) aşırı yüklemesini kullanın. [**copy_format_type**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions/copy_format_type/) sınıfının [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) özelliğini [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/) Sıralama ile ayarlayın. [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/) Sıralama'nın aşağıda listelenen üç üyesi bulunmaktadır.

- SAME_AS_ABOVE: Üstteki satırın biçimini aynı şekilde biçimlendirir.
- SAME_AS_BELOW:  Altındaki satırın biçimini aynı şekilde biçimlendirir.
- TEMİZLE: Biçimlendirmeyi temizler.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.py" >}}

### **Bir Sütun Nasıl Eklenir**

Geliştiriciler, herhangi bir konumda çalışma sayfasına bir sütun ekleyebilirler, bunun için [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) koleksiyonunun [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) yöntemini çağırarak yapılır. [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) yöntemi çağrılır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingAColumn-1.py" >}}

## **Satırları ve Sütunları Silmek**

### **Birden Fazla Satır Nasıl Silinir**

Çalışma sayfasından birden fazla satır silmek için, [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonunun [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) yöntemini çağırın. [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) yöntemi iki parametre alır:

- Satır endeksi, satırların silineceği başlangıç satırının endeksi.
- satır sayısı, silinmesi gereken toplam satır sayısı

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.py" >}}


### **Bir Sütunu Nasıl Silebilirsiniz**

Herhangi bir konumda faaliyet sayfasından bir sütun silmek için, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonunun [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) yöntemini çağırın. [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) yöntemi silinecek sütunun endeksini alır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingAColumn-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
