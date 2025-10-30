---
title: Satır ve Sütunları Biçimlendir
linktitle: Satır ve Sütunlar
type: docs
weight: 100
url: /tr/python-net/adjusting-row-height-and-column-width/
description: Aspose.Cells for Python via .NET, satır yüksekliğini veya sütun genişliğini değiştirme ve aynı zamanda satırlara veya sütunlara biçimlendirme uygulama konusunda destek sağlayabilir.
keywords: Python Excel Kütüphanesi, Python Satır yüksekliği ve Sütun genişliği ayarı, Python Satır yüksekliğini ve Sütun genişliğini ayarlama, Python satır yüksekliğini veya sütun genişliğini değiştirme, Python satır ve sütunları biçimlendirme, Python satır yüksekliği ve sütun genişliği nasıl ayarlanır.
---


{{% alert color="primary" %}}

Çalışma tablolarıyla çalışırken veri eklerken, bazen satırların yüksekliğini veya sütunların genişliğini değiştirmeniz gerekebilir. Bazen satırlara veya sütunlara biçimlendirme uygulamak, mevcut yüksekliğin veya genişliğin veriyi göstermek için değişmesi anlamına gelir. Normalde, kullanıcılar Microsoft Excel'i kullanarak WYSIWYG ortamında satır yüksekliğini ve sütun genişliğini ayarlarlar. Ancak, Aspose.Cells for Python via .NET ile geliştiriciler bu işlemleri çalışma zamanında gerçekleştirebilirler.

{{% /alert %}}

## **Satırlarla Çalışmak**

### **Satır Yüksekliğini Ayarlamak**

Aspose.Cells for Python via .NET, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonu sağlar.

[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonu, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda daha detaylı bir şekilde ele alınmıştır.

### **Bir Satırın Yüksekliğini Ayarlama**

Tek bir satırın yüksekliğini, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonunun [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) yöntemini çağırarak ayarlamak mümkündür. [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) yöntemi aşağıdaki parametreleri alır:

- **satır**, yüksekliğini değiştirdiğiniz satırın dizini.
- **yükseklik**, satıra uygulanacak yükseklik.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightOfRow-1.py" >}}

### **Bir Çalışma Sayfasındaki Tüm Satırların Yüksekliğini Ayarlama**

Geliştiriciler, çalışma sayfasındaki tüm satırlara aynı yüksekliği ayarlamak istiyorlarsa, bunu [**standard_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_height) koleksiyonunun [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) özelliğini kullanarak yapabilirler.

**Örnek:**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightAllRows-1.py" >}}

## **Sütunlarla Çalışmak**

### **Bir Sütunun Genişliğini Ayarlama**

Bir sütunun genişliğini, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonunun [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) yöntemini çağırarak ayarlayabilirsiniz. [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) yöntemi aşağıdaki parametreleri alır:

- **sütun**, genişliğini değiştirdiğiniz sütunun dizini.
- **genişlik**, istenen sütun genişliği.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.py" >}}

### **Piksel cinsinden Sütun Genişliğini Ayarlama**

Bir sütunun genişliğini, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonunun [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) yöntemini çağırarak ayarlayabilirsiniz. [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) yöntemi aşağıdaki parametreleri alır:

- **sütun**, genişliğini değiştirdiğiniz sütunun dizini.
- **piksel**, istenen sütun genişliği piksel cinsinden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.py" >}}

### **Bir Çalışma Sayfasındaki Tüm Sütunların Genişliğini Ayarlama**

Çalışma sayfasındaki tüm sütunlara aynı genişliği ayarlamak için [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonunun [**standard_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_width) özelliğini kullanın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.py" >}}

## **Gelişmiş Konular**
- [Satır ve Sütunları Otomatik Sığdır](/cells/tr/python-net/autofit-rows-and-columns/)
- [Aspose.Cells Kullanarak Metni Sütunlara Dönüştürme](/cells/tr/python-net/convert-text-to-columns-using-aspose-cells/)
- [Satırları ve Sütunları Kopyalama](/cells/tr/python-net/copying-rows-and-columns/)
- [Çalışma Sayfasındaki Boş Satırları ve Sütunları Silme](/cells/tr/python-net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Satır ve Sütunları Gruplama ve Grubu Kaldırma](/cells/tr/python-net/grouping-and-ungrouping-rows-and-columns/)
- [Satır ve Sütunları Gizleme ve Gösterme](/cells/tr/python-net/hiding-and-showing-rows-and-columns/)
- [Excel Çalışma Sayfasına Satır Eklemek veya Silmek](/cells/tr/python-net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Excel dosyasının Satır ve Sütunlarını Eklemek ve Silmek](/cells/tr/python-net/inserting-and-deleting-rows-and-columns/)
- [Çalışma Sayfasındaki Yinelemeli Satırları Kaldırma](/cells/tr/python-net/remove-duplicate-rows-in-a-worksheet/)
- [Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle](/cells/tr/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
{{< app/cells/assistant language="python-net" >}}
