---
title: Satır ve Sütunları Gizleme ve Gösterme
type: docs
weight: 60
url: /tr/python-net/hiding-and-showing-rows-and-columns/
description: Bu makale, Aspose.Cells for Python via .NET API siyle Satır ve Sütunları Gizleme ve Gösterme yi göstermektedir.
keywords: Python Excel Kütüphanesi, Aspose.Cells Python Satırları Gizle ve Göster, Python Sütunları Gizle ve Göster, Python Satır ve Sütunları Gizle, Python Satır ve Sütunları Göster.
---

{{% alert color="primary" %}}

Bazı durumlarda, bir çalışma sayfasında belirli satırları veya sütunları gizlemek ve daha sonra göstermek mantıklı olabilir. Microsoft Excel bu özelliği sağlar ve Aspose.Cells for Python via .NET de aynısını yapar.

{{% /alert %}}

## **Satır ve Sütunların Görünürlüğünü Kontrol Etme**

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlamak için bir [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) içerir. Çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonu sağlar. [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonu, çalışma sayfasındaki satırları veya sütunları yönetmek için birkaç metot sağlar. Bu metotlardan bazıları aşağıda tartışılmıştır.

## **Satır ve Sütunları Gizleme**

Geliştiriciler, [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonunun sırasıyla [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) ve [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) metodlarını çağırarak bir satır veya sütunu gizleyebilirler. Her iki metod da belirli satır veya sütunu gizlemek için satır veya sütun dizinini parametre olarak alır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Bir satır veya sütunu sıfır genişliğine ayarlayarak bir satır veya sütunu gizlemek de mümkündür.

{{% /alert %}}

## **Satır ve Sütunları Gösterme**

Geliştiriciler, [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonunun sırasıyla [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) ve [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) metodlarını çağırarak gizlenen herhangi bir satır veya sütunu gösterebilirler. Her iki metod da iki parametre alır:

- **Satır veya sütun dizini** - belirli bir satır veya sütunun gösterilmesi için kullanılan dizin.
- **Satır yüksekliği veya sütun genişliği** - gizlendikten sonra atanan satır yüksekliği veya sütun genişliği.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Gizli bir sütunu görünür hale getirirken, onu önceden atanan genişliğe veya orijinal genişliğe geri yüklemeniz gerekiyorsa, sütunu negatif genişlikle gizlemelisiniz. Örneğin: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

## **Birden Fazla Satır ve Sütunu Gizleme**

Geliştiriciler, [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonunun sırasıyla [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) ve [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns/) metodlarını çağırarak bir defada birden fazla satır veya sütunu gizleyebilirler. Her iki metod da gizlenmesi gereken başlangıç satırı veya sütunu dizini ve gizlenmesi gereken satır veya sütun sayısını parametre olarak alır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Aynı şekilde birden fazla satır ve sütunu görünür hale getirmek için [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) sınıfının [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows/) ve [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns/) metodları da kullanılabilir.

{{% /alert %}}
