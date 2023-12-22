---
title: Satır ve Sütun Ekleme, Silme
type: docs
weight: 40
url: /tr/cpp/inserting-deleting-rows-and-columns/
---
##  **giriiş**
İster sıfırdan yeni bir çalışma sayfası oluşturun ister mevcut bir çalışma sayfası üzerinde çalışın, daha fazla veriyi barındırmak için fazladan satır veya sütun eklememiz gerekebilir. Bunun tersine, çalışma sayfasında belirtilen konumlardaki satırları veya sütunları da silmemiz gerekebilir. Bu gereksinimleri karşılamak için Aspose.Cells, aşağıda tartışılan çok basit bir sınıf ve yöntem seti sağlar.
###  **Satırları ve Sütunları Yönetme**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Microsoft Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf bir içerir[Çalışma sayfaları](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Bir Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf sağlar[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)koleksiyon, bir çalışma sayfasındaki satırları ve sütunları yönetmeye yönelik çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda tartışılmaktadır.

{{% alert color="primary" %}} 

Satır veya sütunlar eklendiğinde çalışma sayfasındaki içerik aşağı veya sağa kaydırılır; satırlar veya sütunlar kaldırıldığında içerik yukarı veya sola kaydırılır.

{{% /alert %}} 
####  **Satır Ekle**
 Çağırarak çalışma sayfasının herhangi bir yerine bir satır ekleyin.[InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) yöntemi[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Toplamak.[InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)metodu yeni satırın ekleneceği satırın indeksini alır.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


####  **Birden Çok Satır Ekleme**
 Bir çalışma sayfasına birden çok satır eklemek için[Satırları Ekle](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) yöntemi[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Toplamak.[Satırları Ekle](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)yöntem iki parametre alır:

- Satır dizini, yeni satırların ekleneceği satırın dizini.
- Satır sayısı, eklenmesi gereken toplam satır sayısı.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


####  **Birden Çok Satırı Silme**
 Bir çalışma sayfasından birden çok satırı silmek için,[Satırları Sil](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) yöntemi[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Toplamak.[Satırları Sil](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)yöntem iki parametre alır:

- Satır dizini, satırların silineceği satırın dizini.
- Satır sayısı, silinmesi gereken toplam satır sayısı.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


####  **Sütun Ekle**
 Geliştiriciler ayrıca çalışma sayfasının herhangi bir yerindeki sütunu çağırarak da sütun ekleyebilirler.[Sütun Ekle](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) yöntemi[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Toplamak.[Sütun Ekle](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)yöntem, yeni sütunun ekleneceği sütunun dizinini alır.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


####  **Bir Sütunu Sil**
 Çalışma sayfasında herhangi bir yerden bir sütunu silmek için[Sütunu Sil](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) yöntemi[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Toplamak.[Sütunu Sil](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)yöntem silinecek sütunun dizinini alır.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
