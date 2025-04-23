---
title: Satır ve Sütunları Gizleme ve Gösterme
type: docs
weight: 60
url: /tr/net/hiding-and-showing-rows-and-columns/
---

{{% alert color="primary" %}}

Bazen bir çalışma sayfasında belirli satırları veya sütunları gizlemek ve daha sonra göstermek anlamlı olabilir. Microsoft Excel bu özelliği sağlar ve Aspose.Cells de aynısını sağlar.

{{% /alert %}}

## **Satır ve Sütunların Görünürlüğünü Kontrol Etme**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlamak için bir [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonu, bir çalışma sayfasındaki satırları veya sütunları yönetmek için birkaç metod sağlar. Bunlardan bazıları aşağıda tartışılmıştır.

### **Satır ve Sütunları Gizleme**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunun sırasıyla [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) ve [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) metodlarını çağırarak bir satır veya sütunu gizleyebilirler. Her iki metod da belirli satır veya sütunu gizlemek için satır veya sütun dizinini parametre olarak alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Bir satır veya sütunu sıfır genişliğine ayarlayarak bir satır veya sütunu gizlemek de mümkündür.

{{% /alert %}}

### **Satır ve Sütunları Gösterme**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunun sırasıyla [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) ve [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) metodlarını çağırarak gizlenen herhangi bir satır veya sütunu gösterebilirler. Her iki metod da iki parametre alır:

- **Satır veya sütun dizini** - belirli bir satır veya sütunun gösterilmesi için kullanılan dizin.
- **Satır yüksekliği veya sütun genişliği** - gizlendikten sonra atanan satır yüksekliği veya sütun genişliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Gizli bir sütunu görünür hale getirirken, onu önceden atanan genişliğe veya orijinal genişliğe geri yüklemeniz gerekiyorsa, sütunu negatif genişlikle gizlemelisiniz. Örneğin: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Birden Fazla Satır ve Sütunu Gizleme**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunun sırasıyla [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) ve [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) metodlarını çağırarak bir defada birden fazla satır veya sütunu gizleyebilirler. Her iki metod da gizlenmesi gereken başlangıç satırı veya sütunu dizini ve gizlenmesi gereken satır veya sütun sayısını parametre olarak alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Aynı şekilde birden fazla satır ve sütunu görünür hale getirmek için [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıfının [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) ve [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) metodları da kullanılabilir.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
