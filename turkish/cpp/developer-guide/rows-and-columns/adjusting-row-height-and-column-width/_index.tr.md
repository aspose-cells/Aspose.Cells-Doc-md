---
title: Satır Yüksekliğini ve Sütun Genişliğini Ayarlama
type: docs
weight: 10
url: /tr/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Elektronik tablolarla çalışırken ve satırlara veya sütunlara veri eklerken satırların yüksekliğini veya sütunların genişliğini değiştirmeniz gerekebilir. Bazen satırlara veya sütunlara format uygulamak, verileri göstermek için geçerli yüksekliğin veya genişliğin değişmesi gerektiği anlamına gelir. Normalde kullanıcılar, Microsoft Excel'i kullanarak WYSIWYG ortamında satır yüksekliklerini ve sütun genişliklerini ayarlar. Ancak geliştiriciler Aspose.Cells ile bu işlemleri çalışma zamanında gerçekleştirebilirler.

{{% /alert %}} 
##  **Satırlar ile Çalışmak**
###  **Satır Yüksekliğini Ayarlama**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bu bir Microsoft Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Bu, Excel dosyasındaki her çalışma sayfasına erişime izin verir. Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf sağlar[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)koleksiyon, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda daha ayrıntılı olarak tartışılmaktadır.
####  **Satırın Yüksekliğini Ayarlama**
 Tek bir satırın yüksekliğini çağırarak ayarlamak mümkündür.[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Koleksiyonun[Satır Yüksekliğini Ayarla](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) yöntem.[Satır Yüksekliğini Ayarla](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)yöntem aşağıdaki parametreleri aşağıdaki gibi alır:

- *Satır dizini**, yüksekliğini değiştirdiğiniz satırın dizini.
- *Satır yüksekliği**, satıra uygulanacak satır yüksekliği.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


####  **Çalışma Sayfasındaki Tüm Satırların Yüksekliğini Ayarlama**
 Geliştiricilerin çalışma sayfasındaki tüm satırlar için aynı satır yüksekliğini ayarlaması gerekiyorsa bunu şunu kullanarak yapabilirler:[Standart Yüksekliği Ayarla](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) yöntemi[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Toplamak.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
##  **Sütunlarla Çalışmak**
###  **Sütunun Genişliğini Ayarlama**
 çağırarak bir sütunun genişliğini ayarlayın.[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Koleksiyonun[Sütun Genişliğini Ayarla](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) yöntem.[Sütun Genişliğini Ayarla](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/)yöntem aşağıdaki parametreleri alır:

- *Sütun dizini**, genişliğini değiştirdiğiniz sütunun dizini.
- *Sütun genişliği**, istenen sütun genişliği.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
###  **Çalışma Sayfasındaki Tüm Sütunların Genişliğini Ayarlama**
 Çalışma sayfasındaki tüm sütunlar için aynı sütun genişliğini ayarlamak için[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Koleksiyonun[Standart Genişliği Ayarla](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/)yöntem.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
