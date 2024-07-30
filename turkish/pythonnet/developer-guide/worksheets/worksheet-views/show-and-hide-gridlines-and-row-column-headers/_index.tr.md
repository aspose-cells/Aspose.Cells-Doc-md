---
title: Izgara Çizgileri ve Satır Sütun Başlıklarını Gösterme ve Gizleme
type: docs
weight: 30
url: /tr/python-net/show-and-hide-gridlines-and-row-column-headers/
description: Bu makale, Excel çalışma sayfasının ızgaralarını, satır ve sütun başlıklarını programlı olarak gizlemek veya göstermek için Aspose.Cells for Python via .NET API sini kullanma örnek kodlarını sağlamaktadır.
keywords: Python Excel Kütüphanesi, Python da İzgaraları Gösterme ve Gizleme, Python da Satır ve Sütun Başlıklarını Nasıl Gösterip Gizlersiniz, Python da İzgaraları ve Satır Sütun Başlıklarını Nasıl Gösterip Gizlersiniz.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, varsayılan olarak görünen çalışma sayfasının İzgaralarını gizlemeye ve göstermeye olanak sağlar. Aynı zamanda, çalışma sayfasının satır ve sütun başlıklarının görünürlüğünü kontrol etme imkanı sağlar.

{{% /alert %}}

## **Izgara Çizgilerini Gösterme ve Gizleme**

Tüm Excel çalışma taşraları varsayılan olarak izgara çizgilerine sahiptir. Onlar, belirli hücrelere veri girmeyi kolaylaştırdığı için hücreleri çevreler. Izgara çizgileri, bir çalışma taşrasını hücre koleksiyonu olarak görüntülememizi sağlar, burada her hücre kolayca tanımlanabilir.

### **Izgaraların Görünürlüğünü Kontrol Etme**

Aspose.Cells for Python via .NET bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) sınıfı, Excel dosyasında her çalışma sayfasına erişime izin veren bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) koleksiyonunu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/python-et/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) sınıfı, bir çalışma sayfasını yönetmek için geniş bir özellik ve metod yelpazesi sağlar. Izgaraların görünürlüğünü kontrol etmek için [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) sınıfının [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) özelliğini kullanın. [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/), yalnızca **true** veya **false** bir değer tutabilen bir Boolean özelliğidir.

#### **Izgaraları Görünür Yapma**

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) özelliğini **true** olarak ayarlayarak ızgara çizgilerini görünür yapın.

#### **Izgaraları Gizleme**

Sınıf [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) özelliğini **false** olarak ayarlayarak ızgaraları gizleyin.

Aşağıda verilen tam bir örnek, [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) özelliğinin kullanımını göstermektedir, bir excel dosyasını(book1.xls) açarak, ilk çalışma sayfasındaki ızgaraları gizleyerek değiştirilmiş dosyayı output.xls olarak kaydetme işlemini gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **Satır Sütun Başlıklarını Göster ve Gizle**

Bir Excel dosyasındaki tüm çalışma sayfaları, satırlarda ve sütunlarda düzenlenmiş hücrelerden oluşur. Tüm satırlar ve sütunlar benzersiz değerlere sahiptir ve bunları tanımlamak ve bireysel hücreleri tanımlamak için kullanılır. Örneğin, satırlar numaralandırılır - 1, 2, 3, 4, vb. - ve sütunlar alfabetik olarak sıralanır - A, B, C, D, vb. Satır ve sütun değerleri başlıklarda gösterilir. Aspose.Cells for Python via .NET kullanarak bu satır ve sütun başlıklarının görünürlüğünü kontrol edebilirler.

### **Çalışma sayfalarının görünürlüğünü kontrol etmek**

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/pytho-net/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) koleksiyonunu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) sınıfı, bir çalışma sayfasını yönetmek için geniş bir özellik ve metod yelpazesi sağlar. Satır ve sütun başlıklarının görünürlüğünü kontrol etmek için [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) sınıfının [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) özelliğini kullanın. [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/), yalnızca **true** veya **false** bir değer alabilen bir Boolean özelliğidir.

#### **Satır/Sütun Başlıklarını Görünür Yapma**

Sınıf [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) özelliğini **true** olarak ayarlayarak satır ve sütun başlıklarını görünür yapın.

#### **Satır/Sütun Başlıklarını Gizleme**

Sınıf [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) özelliğini **false** olarak ayarlayarak satır ve sütun başlıklarını gizleyin.

Aşağıda verilen tam bir örnek, [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) özelliğinin kullanımını göstermektedir, bir excel dosyasını(book1.xls) açarak, ilk çalışma sayfasındaki satır ve sütun başlıklarını gizleyerek değiştirilmiş dosyayı output.xls olarak kaydetme işlemini gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

[**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) ve [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns) yöntemlerini kullanarak, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) sınıfının birden fazla satırı ve sütunu görünür yapmak mümkündür.

{{% /alert %}}
