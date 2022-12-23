---
title: Satır Yüksekliğini ve Sütun Genişliğini Ayarlama
type: docs
weight: 10
url: /tr/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Elektronik tablolarla çalışırken ve satırlara veya sütunlara veri eklerken, satırların yüksekliğini veya sütunların genişliğini değiştirmeniz gerekebilir. Bazen, satırlara veya sütunlara biçimlendirme uygulamak, verileri göstermek için geçerli yükseklik veya genişliğin değişmesi gerektiği anlamına gelir. Normalde, kullanıcılar bir WYSIWYG ortamında Microsoft Excel kullanarak satır yüksekliklerini ve sütun genişliklerini ayarlar. Ancak, Aspose.Cells ile geliştiriciler bu işlemleri çalışma zamanında gerçekleştirebilir.

{{% /alert %}} 
## **Satırlarla Çalışmak**
### **Satır Yüksekliğini Ayarlama**
 Aspose.Cells bir sınıf sağlar,[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf bir içerir[IÇalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[IÇalışma Sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. bu[IÇalışma Sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf bir sağlar[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon. bu[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)koleksiyon, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda daha ayrıntılı olarak tartışılmaktadır.
#### **Bir Satırın Yüksekliğini Ayarlama**
 çağırarak tek bir satırın yüksekliğini ayarlamak mümkündür.[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) koleksiyonun[Satır Yüksekliğini Ayarla](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f) yöntem. bu[Satır Yüksekliğini Ayarla](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f)method aşağıdaki gibi parametreleri alır:

- **Satır dizini**, yüksekliğini değiştirdiğiniz satırın dizini.
- **Satır yüksekliği**, satıra uygulanacak satır yüksekliği.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow.cpp" >}}


#### **Çalışma Sayfasındaki Tüm Satırların Yüksekliğini Ayarlama**
 Geliştiricilerin çalışma sayfasındaki tüm satırlar için aynı satır yüksekliğini ayarlamaları gerekirse, bunu[Standart Yüksekliği Ayarla](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a0b79a3163e2b601aa1b6a6a1e3f1467f) yöntemi[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Toplamak.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet.cpp" >}}
## **Sütunlarla Çalışmak**
### **Bir Sütunun Genişliğini Ayarlama**
 öğesini çağırarak bir sütunun genişliğini ayarlayın.[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) koleksiyonun[Sütun Genişliğini Ayarla](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987) yöntem. bu[Sütun Genişliğini Ayarla](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987)yöntem aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliğini değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, istenen sütun genişliği.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn.cpp" >}}
### **Çalışma Sayfasındaki Tüm Sütunların Genişliğini Ayarlama**
 Çalışma sayfasındaki tüm sütunlar için aynı sütun genişliğini ayarlamak üzere[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) koleksiyonun[Standart Genişliği Ayarla](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a48f5dbccc3bf4bb9e6e882094b500bd7)yöntem.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet.cpp" >}}
