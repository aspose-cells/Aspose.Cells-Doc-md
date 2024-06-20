---
title: Satırları Sütunları ve Kaydırma Çubuklarını Göster ve Gizle
type: docs
weight: 20
url: /tr/net/show-and-hide-rows-columns-and-scroll-bars/
description: Bu makale, C# dilini ve .NET API veya Kütüphanesini kullanarak Excel çalışma sayfası satırlarını ve sütunlarını programlı olarak gösterme ve gizleme işlemini göstermektedir. Kaydırma çubuklarının görünürlüğü ayarlanabilmekte ve birkaç satır ve sütun gizlenebilmektedir.
---

{{% alert color="primary" %}}

Aspose.Cells, bir çalışma sayfasının Satırların, Sütunların ve Kaydırma Çubuklarının görünürlüğünü kontrol etmenin yollarını sağlar.

{{% /alert %}}

## **Satır ve Sütunları Göster ve Gizle**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilmektedir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu, çalışma sayfasında satırları veya sütunları yönetmek için birkaç yöntem sağlar. Bunlardan bazıları aşağıda tartışılmıştır.

### **Satır ve Sütunları Göster**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonunun sırasıyla [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) ve [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) metodlarını çağırarak gizlenen herhangi bir satır veya sütunu gösterebilirler. Her iki metod da iki parametre alır:

- **Satır veya sütun dizini** - belirli bir satır veya sütunun gösterilmesi için kullanılan dizin.
- **Satır yüksekliği veya sütun genişliği** - gizlendikten sonra atanan satır yüksekliği veya sütun genişliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Gizli bir sütunu görünür hale getirirken, onu önceden atanan genişliğe veya orijinal genişliğe geri yüklemeniz gerekiyorsa, sütunu negatif genişlikle gizlemelisiniz. Örneğin: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Satır ve Sütunları Gizle**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonunun sırasıyla [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) ve [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) metodlarını çağırarak bir satır veya sütunu gizleyebilirler. Her iki metod da belirli satır veya sütunu gizlemek için satır veya sütun dizinini parametre olarak alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Bir satır veya sütunu sıfır genişliğine ayarlayarak bir satır veya sütunu gizlemek de mümkündür.

{{% /alert %}}

### **Birden Fazla Satır ve Sütunu Gizleme**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonunun sırasıyla [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) ve [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) metodlarını çağırarak bir defada birden fazla satır veya sütunu gizleyebilirler. Her iki metod da gizlenmesi gereken başlangıç satırı veya sütunu dizini ve gizlenmesi gereken satır veya sütun sayısını parametre olarak alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Kaydırma Çubuklarını Göster ve Gizle**

Kaydırma çubukları, herhangi bir dosyanın içeriğini gezinmek için kullanılır. Genellikle iki tür kaydırma çubuğu bulunur:

- Dikey kaydırma çubukları
- Yatay kaydırma çubukları

Microsoft Excel ayrıca yatay ve dikey kaydırma çubukları sağlar böylece kullanıcılar çalışma sayfası içeriğinde kaydırma yapabilirler. Aspose.Cells kullanarak geliştiriciler Excel dosyalarında her iki türde de kaydırma çubuklarının görünürlüğünü kontrol edebilirler.

### **Kaydırma Çubuklarının Görünürlüğünü Kontrol Etmek**

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı bir Excel dosyasını yönetmek için geniş bir yelpazede özellik ve metot sağlar. Kaydırma çubuklarının görünürlüğünü kontrol etmek için [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) ve [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) özelliklerini kullanın. [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) ve [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) Boolean özellikleridir, bu da bu özelliklerin yalnızca **true** veya **false** değerlerini saklayabileceği anlamına gelir.

#### **Kaydırma Çubuklarını Görünür Yapma**

Kaydırma çubuklarını görünür yapmak için [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) veya [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) özelliğini **true** olarak ayarlayın.

#### **Kaydırma çubuklarını gizleme**

Kaydırma çubuklarını gizlemek için [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) veya [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) özelliğini **false** olarak ayarlayın.

**Örnek Kod**

Aşağıda, bir Excel dosyasını, book1.xls'yi açan, her iki kaydırma çubuğunu gizleyen ve ardından değiştirilmiş dosyayı output.xls olarak kaydeden tam bir kod bulunmaktadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
