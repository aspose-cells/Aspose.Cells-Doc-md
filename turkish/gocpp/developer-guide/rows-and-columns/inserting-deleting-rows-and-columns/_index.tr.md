---
title: Satır ve Sütun Ekleme, Silme
type: docs
weight: 40
url: /tr/go-cpp/inserting-deleting-rows-and-columns/
---

## **Giriş**

Sıfırdan yeni bir çalışsayfa oluştururken veya mevcut bir çalışsayfada çalışırken, daha fazla veriyi yerleştirmek için ekstra satırlar veya sütunlar eklemeniz veya belirli konumlardan satır veya sütunları silmeniz gerekebilir. Bu gereksinimleri karşılamak için Aspose.Cells, aşağıda tartışılan çok basit bir sınıf ve yöntem seti sağlar.

### **Satır ve Sütun Yönetimi**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) adlı bir sınıf sağlar. [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, bir Excel dosyasındaki her sayfaya erişimi sağlayan bir [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) koleksiyonu içerir. Bir sayfa [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı, tüm hücreleri temsil eden bir [Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonu sağlar.

[Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonu, bir çalışma sayfasındaki satırları ve sütunları yöneten birkaç yöntem sağlar. Bunlardan bazıları aşağıda tartışılmaktadır.

{{% alert color="primary" %}}

Satırlar veya sütunlar eklenirse, çalışma sayfasındaki içerik aşağıya veya sağa kaydırılır ve satırlar veya sütunlar kaldırılırsa içerik yukarıya veya sola kaydırılır.

{{% /alert %}}

Çalışma sayfasına herhangi bir konumda yeni bir satır eklemek için, [Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonunun [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) yöntemini çağırın. [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) yöntemi, yeni satırın ekleneceği satırın dizinini alır.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertRow.go" >}}

#### **Birden Fazla Satır Ekleme**

Bir çalışma sayfasına birden fazla satır eklemek için, [Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonunun [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrows_int_int/) yöntemini çağırın. [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrowinsertrows_int_ints/) yöntemi iki parametre alır:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingMultipleRows.go" >}}

#### **Birden Fazla Satırı Silme**

Bir çalışma sayfasında birden çok satır silmek için, [Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonunun [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) yöntemini çağırın. [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) yöntemi iki parametre alır:

- Satır endeksi, satırların silineceği başlangıç satırının endeksi.
- satır sayısı, silinmesi gereken toplam satır sayısı

#### **Bir Sütun Eklemek**

Geliştiriciler, herhangi bir konumda çalışma sayfasına bir sütun eklemek için [Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonunun [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) yöntemini de çağırabilir. [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) yöntemi, yeni sütunun eklenacağı sütun dizinini alır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertColumn.go" >}}

Çalışma sayfasından herhangi bir konumda bir sütunu silmek için, [Cells](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonunun [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) yöntemini çağırın. [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) yöntemi, silinecek sütunun dizinini alır.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteColumn.go" >}}
