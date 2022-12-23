---
title: Satırları, Sütunları ve Kaydırma Çubuklarını Gösterme ve Gizleme
type: docs
weight: 20
url: /tr/net/show-and-hide-rows-columns-and-scroll-bars/
description: Bu makale, C# dilini ve .NET API veya Kitaplığı kullanarak Excel çalışma sayfası satırlarını ve sütunlarını programlı olarak nasıl görüntüleyeceğinizi ve gizleyeceğinizi gösterir. Kaydırma çubuklarının görünürlüğü ayarlanabilir ve birkaç satır ve sütun gizlenebilir.
---
{{% alert color="primary" %}}

Aspose.Cells, bir çalışma sayfasının Satırlar, Sütunlar ve Kaydırma Çubuklarının görünürlüğünü kontrol etmenin yollarını sağlar.

{{% /alert %}}

## **Satırları ve Sütunları Göster ve Gizle**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine izin veren koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon. bu[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)koleksiyon, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan birkaçı aşağıda tartışılmaktadır.

### **Satırları ve Sütunları Göster**

 Geliştiriciler, herhangi bir gizli satırı veya sütunu çağırarak gösterebilir.[**Satırı Göster**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) ve[**Sütunu Göster**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) yöntemleri[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)sırasıyla koleksiyon. Her iki yöntem de iki parametre alır:

- **Satır veya sütun dizini** - belirli bir satır veya sütunu göstermek için kullanılan bir satır veya sütun dizini.
- **Satır yüksekliği veya sütun genişliği** - gösterildikten sonra satıra veya sütuna atanan satır yüksekliği veya sütun genişliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Gizli bir sütunu görünür hale getirirken, daha önce atanmış genişliğe veya orijinal genişliğine geri döndürmeniz gerekirse, lütfen sütunu negatif genişlikle gösterin. Örneğin: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Satırları ve Sütunları Gizle**

 Geliştiriciler, çağırarak bir satırı veya sütunu gizleyebilirsiniz.[**Satırı Gizle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) ve[**Sütunu Gizle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) yöntemleri[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)sırasıyla koleksiyon. Her iki yöntem de belirli satır veya sütunu gizlemek için satır ve sütun dizinini parametre olarak alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Sırasıyla satır yüksekliğini veya sütun genişliğini 0 olarak ayarlayarak bir satırı veya sütunu gizlemek de mümkündür.

{{% /alert %}}

### **Birden Çok Satırı ve Sütunu Gizle**

 Geliştiriciler, çağrı yaparak aynı anda birden çok satırı veya sütunu gizleyebilirsiniz.[**Satırları Gizle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) ve[**Sütunları Gizle**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) yöntemleri[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)sırasıyla koleksiyon. Her iki yöntem de başlangıç satır veya sütun indeksini ve gizlenmesi gereken satır veya sütun sayısını parametre olarak alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Kaydırma Çubuklarını Göster ve Gizle**

Kaydırma çubukları, herhangi bir dosyanın içeriğinde gezinmek için kullanılır. Normalde iki tür kaydırma çubuğu vardır:

- Dikey kaydırma çubukları
- Yatay kaydırma çubukları

Microsoft Excel, kullanıcıların çalışma sayfası içeriklerinde gezinebilmeleri için yatay ve dikey kaydırma çubukları da sağlar. Geliştiriciler, Aspose.Cells'i kullanarak Excel dosyalarındaki her iki kaydırma çubuğunun da görünürlüğünü kontrol edebilir.

### **Kaydırma Çubuklarının Görünürlüğünü Kontrol Etme**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Bu bir Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class, bir Excel dosyasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Kaydırma çubuklarının görünürlüğünü kontrol etmek için,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) ve[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) özellikler.[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) ve[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) Boole özellikleridir; bu, bu özelliklerin yalnızca depolayabileceği anlamına gelir.**doğru** veya**YANLIŞ** değerler.

#### **Kaydırma Çubuklarını Görünür Hale Getirmek**

 ayarlayarak kaydırma çubuklarını görünür yapın.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) veya[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) mülkiyet**doğru**.

#### **Kaydırma Çubuklarını Gizleme**

 ayarlayarak kaydırma çubuklarını gizleyin.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) veya[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) mülkiyet**YANLIŞ**.

**Basit kod**

Aşağıda, kitap1.xls adlı bir Excel dosyasını açan, her iki kaydırma çubuğunu da gizleyen ve ardından değiştirilen dosyayı output.xls olarak kaydeden eksiksiz bir kod bulunmaktadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
