---
title: Satır ve Sütun Ekleme, Silme
type: docs
weight: 40
url: /tr/cpp/inserting-deleting-rows-and-columns/
---
## **giriiş**
Sıfırdan yeni bir çalışma sayfası oluştururken veya mevcut bir çalışma sayfası üzerinde çalışırken, daha fazla veriyi barındırmak için fazladan satır veya sütun eklememiz gerekebilir. Tersine, çalışma sayfasında belirtilen konumlardaki satırları veya sütunları da silmemiz gerekebilir. Bu gereklilikleri yerine getirmek için Aspose.Cells, aşağıda tartışılan çok basit bir sınıflar ve yöntemler seti sağlar.
### **Satırları ve Sütunları Yönetme**
 Aspose.Cells bir sınıf sağlar,[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf bir içerir[IÇalışma Sayfaları](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. bu[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf bir sağlar[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

 bu[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)koleksiyon, bir çalışma sayfasındaki satırları ve sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda tartışılmaktadır.

{{% alert color="primary" %}} 

Satır veya sütun eklendiğinde çalışma sayfasındaki içerik aşağı veya sağa kaydırılır ve satır veya sütunlar kaldırılırsa içerik yukarı veya sola kaydırılır.

{{% /alert %}} 
#### **Satır Ekle**
 çağırarak çalışma sayfasına herhangi bir konumda bir satır ekleyin.[Satır Ekle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7) yöntemi[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Toplamak. bu[Satır Ekle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7)method yeni satırın ekleneceği satırın indeksini alır.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow.cpp" >}}


#### **Birden Çok Satır Ekleme**
 Bir çalışma sayfasına birden çok satır eklemek için[Satır Ekle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0) yöntemi[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Toplamak. bu[Satır Ekle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0)yöntem iki parametre alır:

- Satır dizini, yeni satırların ekleneceği satırın dizini.
- Satır sayısı, eklenmesi gereken toplam satır sayısı.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows.cpp" >}}


#### **Birden Çok Satırı Silme**
Bir çalışma sayfasından birden çok satırı silmek için[Satırları Sil](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1) yöntemi[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Toplamak. bu[Satırları Sil](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1)yöntem iki parametre alır:

- Satır dizini, satırların silineceği satırın dizini.
- Satır sayısı, silinmesi gereken toplam satır sayısı.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows.cpp" >}}


#### **Sütun Ekle**
 Geliştiriciler ayrıca, çalışma sayfasına herhangi bir konumda şunu çağırarak bir sütun ekleyebilir:[Sütun Ekle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55) yöntemi[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Toplamak.[Sütun Ekle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55)method yeni kolonun ekleneceği kolonun indeksini alır.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn.cpp" >}}


#### **Bir Sütunu Sil**
 Herhangi bir konumdaki çalışma sayfasından bir sütunu silmek için[Sütunu Sil](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b) yöntemi[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Toplamak. bu[Sütunu Sil](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b)Yöntem, silinecek sütunun dizinini alır.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn.cpp" >}}
