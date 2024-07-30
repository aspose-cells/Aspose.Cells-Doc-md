---
title: Satırları Sütunları ve Kaydırma Çubuklarını Göster ve Gizle
type: docs
weight: 20
url: /tr/python-net/show-and-hide-rows-columns-and-scroll-bars/
description: Bu makale, Aspose.Cells for Python via .NET API sini kullanarak Excel çalışma sayfası satırlarını ve sütunlarını programlı olarak görüntülemeyi ve gizlemeyi göstermektedir. Kaydırma çubuklarının görünürlüğü ayarlanabilir ve birkaç satır ve sütun gizlenebilir.
keywords: Python Excel Kütüphanesi, Python da satır ve sütunları gösterme, Python da satır ve sütunları gizleme, Python da dikey kaydırma çubuğunu gösterme, Python da yatay kaydırma çubuğunu gösterme, Python da dikey kaydırma çubuğunu gizleme, Python da yatay kaydırma çubuğunu gizleme, Python da Satırları ve Sütunları Gösterme ve Gizleme.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, bir çalışma sayfasının Satırlar, Sütun ve Kaydırma Çubuklarının görünürlüğünü kontrol etme yolları sağlar.

{{% /alert %}}

## **Satır ve Sütunları Göster ve Gizle**

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonunu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonunu sağlar. [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonu, çalışma sayfasındaki satırları veya sütunları yönetmek için birçok yöntem sağlar. Bunlardan bazıları aşağıda tartışılmıştır.

### **Satır ve Sütunları Göster**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) koleksiyonunun sırasıyla [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) ve [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) metodlarını çağırarak gizlenen herhangi bir satır veya sütunu gösterebilirler. Her iki metod da iki parametre alır:

- **Satır veya sütun dizini** - belirli bir satır veya sütunun gösterilmesi için kullanılan dizin.
- **Satır yüksekliği veya sütun genişliği** - gizlendikten sonra atanan satır yüksekliği veya sütun genişliği.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Gizli bir sütunu görünür hale getirirken, onu önceden atanan genişliğe veya orijinal genişliğe geri yüklemeniz gerekiyorsa, sütunu negatif genişlikle gizlemelisiniz. Örneğin: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Satır ve Sütunları Gizle**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonunun sırasıyla [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) ve [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) metodlarını çağırarak bir satır veya sütunu gizleyebilirler. Her iki metod da belirli satır veya sütunu gizlemek için satır veya sütun dizinini parametre olarak alır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Bir satır veya sütunu sıfır genişliğine ayarlayarak bir satır veya sütunu gizlemek de mümkündür.

{{% /alert %}}

### **Birden Fazla Satır ve Sütunu Gizleme**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonunun sırasıyla [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) ve [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns) metodlarını çağırarak bir defada birden fazla satır veya sütunu gizleyebilirler. Her iki metod da gizlenmesi gereken başlangıç satırı veya sütunu dizini ve gizlenmesi gereken satır veya sütun sayısını parametre olarak alır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

## **Kaydırma Çubuklarını Göster ve Gizle**

Kaydırma çubukları, herhangi bir dosyanın içeriğini gezinmek için kullanılır. Genellikle iki tür kaydırma çubuğu bulunur:

- Dikey kaydırma çubukları
- Yatay kaydırma çubukları

Microsoft Excel ayrıca kullanıcıların çalışma sayfası içeriğinde kaydırma yapmalarını sağlamak için yatay ve dikey kaydırma çubukları sağlar. Aspose.Cells for Python via .NET kullanarak geliştiriciler, Excel dosyalarında hem yatay hem de dikey kaydırma çubuklarının görünürlüğünü kontrol edebilirler.

### **Kaydırma Çubuklarının Görünürlüğünü Kontrol Etmek**

Aspose.Cells for Python via .NET, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, bir Excel dosyasını yönetmek için geniş bir özellik ve metod yelpazesi sağlar. Kaydırma çubuklarının görünürlüğünü kontrol etmek için [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) ve [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) özelliklerini kullanın. [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) ve [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible), yalnızca **true** veya **false** değerlerini depolayabilen Boolean özelliklerdir.

#### **Kaydırma Çubuklarını Görünür Yapma**

Kaydırma çubuklarını görünür yapmak için [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) veya [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) özelliğini **true** olarak ayarlayın.

#### **Kaydırma çubuklarını gizleme**

Kaydırma çubuklarını gizlemek için [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) veya [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) özelliğini **false** olarak ayarlayın.

**Örnek Kod**

Aşağıda, bir Excel dosyasını, book1.xls'yi açan, her iki kaydırma çubuğunu gizleyen ve ardından değiştirilmiş dosyayı output.xls olarak kaydeden tam bir kod bulunmaktadır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Worksheets-Display-DisplayHideScrollBars-1.py" >}}
