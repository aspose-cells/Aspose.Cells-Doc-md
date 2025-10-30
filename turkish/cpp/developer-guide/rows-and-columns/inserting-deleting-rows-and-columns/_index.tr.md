---
title: Satır ve Sütun Ekleme, Silme
type: docs
weight: 40
url: /tr/cpp/inserting-deleting-rows-and-columns/
---

## **Giriş**
Sıfırdan yeni bir çalışsayfa oluştururken veya mevcut bir çalışsayfada çalışırken, daha fazla veriyi yerleştirmek için ekstra satırlar veya sütunlar eklemeniz veya belirli konumlardan satır veya sütunları silmeniz gerekebilir. Bu gereksinimleri karşılamak için Aspose.Cells, aşağıda tartışılan çok basit bir sınıf ve yöntem seti sağlar.
### **Satır ve Sütun Yönetimi**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) adında bir sınıf sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her sayfaya erişime izin veren bir [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonu içerir. Bir çalışsayfa [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışsayfadaki tüm hücreleri temsil eden bir [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu sağlar.

[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu, çalışsayfadaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar, bunlardan bazıları aşağıda daha detaylı olarak tartışılmaktadır.

{{% alert color="primary" %}} 

Satırlar veya sütunlar eklenirse, çalışma sayfasındaki içerik aşağıya veya sağa kaydırılır ve satırlar veya sütunlar kaldırılırsa içerik yukarıya veya sola kaydırılır.

{{% /alert %}} 
#### **Bir Satır Ekle**
Worksheeta satır eklemek için [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) methodunu [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun çağrılmasıyla herhangi bir konumda çalıştırın. [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) methodu ile yeni satırın ekleneceği satırın dizinini alır.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


#### **Birden Fazla Satır Ekleme**
Çalışsayadh birden çok satır eklemek için [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) methodunu çağırın. [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) methodu iki parametre alır:

- Satır indeksi, yeni satırların ekleneceği satırın indeksi.
- Satır sayısı, eklenmesi gereken toplam satır sayısı.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


#### **Birden Fazla Satırı Silme**
Çalışma sayfasından birden çok satır silmek için [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun [DeleteRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) methodunu çağırın. [DeleteRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) methodu iki parametre alır:

- Satır endeksi, satırların silineceği başlangıç satırının endeksi.
- satır sayısı, silinmesi gereken toplam satır sayısı



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


#### **Bir Sütun Eklemek**
Geliştiriciler [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) methodunu çağırarak çalışsaydh herhangi bir konuma bir sütun da ekleyebilirler. [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) methodu ile yeni sütunun ekleneceği sütunun dizinini alır.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


#### **Bir Sütunu Sil**
Herhangi bir konumdan çalışma sayfasından bir sütun silmek için [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) methodunu çağırın. [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) methodu silinecek sütunun dizinini alır.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
