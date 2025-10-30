---
title: Satır Yüksekliğini ve Sütun Genişliğini Ayarlama
type: docs
weight: 10
url: /tr/cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

Yayınlanan veri tabloları üzerinde çalışırken, satırlara veya sütunlara veri eklerken, bazen satırların yüksekliğini veya sütunların genişliğini değiştirmeniz gerekebilir. Bazen satırlara veya sütunlara biçimlendirme uygulamak, mevcut yükseklik veya genişliğin veriyi gösterebilecek şekilde değişmesi gerektiği anlamına gelir. Genellikle, kullanıcılar satır yüksekliklerini ve sütun genişliklerini Microsoft Excel kullanarak WYSIWYG ortamında ayarlar. Ancak, Aspose.Cells geliştiricileri bu işlemleri çalışma zamanında gerçekleştirebilirler.

{{% /alert %}} 
## **Satırlarla Çalışmak**
### **Satır Yüksekliğini Ayarlamak**
Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunu sağlar. [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu, çalışma sayfasındaki satırları veya sütunları yönetmek için birkaç yöntem sağlar. Bunlardan bazıları aşağıda daha detaylı olarak tartışılmaktadır.
#### **Bir Satırın Yüksekliğini Ayarlama**
Bir satırın yüksekliğini [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) yöntemini çağırarak ayarlamak mümkündür. [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) yöntemi aşağıdaki parametreleri alır:

- **Satır dizini**, yüksekliği değiştirdiğiniz satırın dizini.
- **Satır yüksekliği**, satıra uygulanan satır yüksekliği.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


#### **Bir Çalışma Sayfasındaki Tüm Satırların Yüksekliğini Ayarlama**
Geliştiriciler, çalışma sayfasındaki tüm satırlar için aynı satır yüksekliğini ayarlamak istediklerinde, bunu [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun [SetStandardHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) yöntemini kullanarak yapabilirler.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
## **Sütunlarla Çalışmak**
### **Bir Sütunun Genişliğini Ayarlamak**
Sütunun genişliğini, [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) yöntemini çağırarak ayarlayabilirsiniz. [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) yöntemi aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliği değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, istenen sütun genişliği.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
### **Bir Çalışma Sayfasındaki Tüm Sütunların Genişliğini Ayarlama**
Çalışma sayfasındaki tüm sütunlar için aynı sütun genişliğini ayarlamak için [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun [SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/) metodu kullanılır.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
