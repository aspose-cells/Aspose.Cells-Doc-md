---
title: Satır ve Sütunları Biçimlendir
linktitle: Satır ve Sütunlar
type: docs
weight: 100
url: /tr/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET, satır yüksekliğini veya sütun genişliğini değiştirmeyi, satırlara veya sütunlara biçimlendirme uygulamayı destekler.
keywords: Satır yüksekliği ve sütun genişliği ayarlı, satır yüksekliği ve sütun genişliği ayarlı, satır yüksekliğini veya sütun genişliğini değiştirme, satır ve sütunları biçimlendirme, satır yüksekliği ve sütun genişliği ayarlama hakkında bilgi.
---


{{% alert color="primary" %}}

Çalışma kitaplarıyla çalışırken ve verileri satırlara veya sütunlara eklerken, bazen satır yüksekliğinin veya sütun genişliğinin değişmesi gerekebilir. Bazen satırlara veya sütunlara biçimlendirme uygulamak, mevcut yüksekliğin veya genişliğin veriyi gösterebilmesi için değişmesini gerektirir. Normalde, kullanıcılar Microsoft Excel'i kullanarak WYSIWYG ortamında satır yüksekliklerini ve sütun genişliklerini ayarlar. Ancak, Aspose.Cells geliştiricileri bu işlemleri çalışma zamanında gerçekleştirebilir.

{{% /alert %}}

## **Satırlarla Çalışmak**

### **Satır Yüksekliğini Ayarlamak**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyon sağlar.

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonu, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda daha detaylı bir şekilde ele alınmıştır.

### **Bir Satırın Yüksekliğini Ayarlama**

Tek bir satırın yüksekliğini, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunun [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) yöntemini çağırarak ayarlamak mümkündür. [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) yöntemi aşağıdaki parametreleri alır:

- **Satır dizini**, yüksekliği değiştirdiğiniz satırın dizini.
- **Satır yüksekliği**, satıra uygulanan satır yüksekliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **Bir Çalışma Sayfasındaki Tüm Satırların Yüksekliğini Ayarlama**

Geliştiriciler, çalışma sayfasındaki tüm satırlara aynı yüksekliği ayarlamak istiyorlarsa, bunu [**StandardHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) koleksiyonunun [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) özelliğini kullanarak yapabilirler.

**Örnek:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **Sütunlarla Çalışmak**

### **Bir Sütunun Genişliğini Ayarlama**

Bir sütunun genişliğini, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunun [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) yöntemini çağırarak ayarlayabilirsiniz. [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) yöntemi aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliği değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, istenen sütun genişliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **Piksel cinsinden Sütun Genişliğini Ayarlama**

Bir sütunun genişliğini, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunun [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) yöntemini çağırarak ayarlayabilirsiniz. [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) yöntemi aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliği değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, pikseller cinsinden istenen sütun genişliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **Bir Çalışma Sayfasındaki Tüm Sütunların Genişliğini Ayarlama**

Çalışma sayfasındaki tüm sütunlara aynı genişliği ayarlamak için [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunun [**StandardWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth) özelliğini kullanın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **Gelişmiş Konular**
- [Satır ve Sütunları Otomatik Sığdır](/cells/tr/net/autofit-rows-and-columns/)
- [Aspose.Cells Kullanarak Metni Sütunlara Dönüştürme](/cells/tr/net/convert-text-to-columns-using-aspose-cells/)
- [Satırları ve Sütunları Kopyalama](/cells/tr/net/copying-rows-and-columns/)
- [Çalışma Sayfasındaki Boş Satırları ve Sütunları Silme](/cells/tr/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Satır ve Sütunları Gruplama ve Grubu Kaldırma](/cells/tr/net/grouping-and-ungrouping-rows-and-columns/)
- [Satır ve Sütunları Gizleme ve Gösterme](/cells/tr/net/hiding-and-showing-rows-and-columns/)
- [Excel Çalışma Sayfasına Satır Eklemek veya Silmek](/cells/tr/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Excel dosyasının Satır ve Sütunlarını Eklemek ve Silmek](/cells/tr/net/inserting-and-deleting-rows-and-columns/)
- [Çalışma Sayfasındaki Yinelemeli Satırları Kaldırma](/cells/tr/net/remove-duplicate-rows-in-a-worksheet/)
- [Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle](/cells/tr/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
