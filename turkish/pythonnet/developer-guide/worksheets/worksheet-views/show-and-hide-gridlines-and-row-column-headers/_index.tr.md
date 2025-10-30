---
title: Izgara Çizgileri ve Satır Sütun Başlıklarını Gösterme ve Gizleme
type: docs
weight: 30
url: /tr/python-net/show-and-hide-gridlines-and-row-column-headers/
description: Bu makale, Aspose.Cells for Python via .NET API sini kullanarak Excel çalışma sayfasının ızgaralarını, satır ve sütun başlıklarını programlı olarak gizleme veya gösterme için örnek kod sağlar.
keywords: Python Excel Kütüphanesi, Python da Izgaraları Göster ve Gizle, Satır ve Sütun Başlıklarını Nasıl Gösterir ve Gizlerim, Python da Izgaraları ve Satır Sütun Başlıklarını Nasıl Gösterir ve Gizlerim.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, varsayılan olarak görünür olan çalışma sayfasının ızgaralarını gizleme ve gösterme işlemini destekler. Ayrıca, çalışma sayfasının Satır ve Sütun Başlıklarının görünürlüğünü de kontrol eder.

{{% /alert %}}

## **Izgara Çizgilerini Gösterme ve Gizleme**

Tüm Excel çalışma taşraları varsayılan olarak izgara çizgilerine sahiptir. Onlar, belirli hücrelere veri girmeyi kolaylaştırdığı için hücreleri çevreler. Izgara çizgileri, bir çalışma taşrasını hücre koleksiyonu olarak görüntülememizi sağlar, burada her hücre kolayca tanımlanabilir.

### **Izgaraların Görünürlüğünü Kontrol Etme**

Aspose.Cells for Python via .NET, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) sınıfı, geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine olanak sağlayan [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) koleksiyonunu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) sınıfı, bir çalışma sayfasını yönetmek için geniş bir özellik ve yöntem yelpazesi sunar. Izgaraların görünürlüğünü kontrol etmek için [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) sınıfı [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) özelliğini kullanın. [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) Boolean bir özelliktir ve yalnızca **doğru** veya **yanlış** değeri depolayabilir.

#### **Izgaraları Görünür Yapma**

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) özelliğini **true** olarak ayarlayarak ızgara çizgilerini görünür yapın.

#### **Izgaraları Gizleme**

Sınıf [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) özelliğini **false** olarak ayarlayarak ızgaraları gizleyin.

Aşağıda verilen tam bir örnek, [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) özelliğinin kullanımını göstermektedir, bir excel dosyasını(book1.xls) açarak, ilk çalışma sayfasındaki ızgaraları gizleyerek değiştirilmiş dosyayı output.xls olarak kaydetme işlemini gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **Satır Sütun Başlıklarını Göster ve Gizle**

Bir Excel dosyasındaki tüm çalışma sayfaları, satırlar ve sütunlar halinde düzenlenmiş hücrelerden oluşur. Tüm satır ve sütunların kendine özgü değerleri vardır ve bunlar onları tanımlamak ve hücreleri ayırt etmek için kullanılır. Örneğin, satırlar 1, 2, 3, 4 vb. olarak numaralandırılmıştır ve sütunlar alfabetik sıralı – A, B, C, D vb. – şekilde sıralanmıştır. Satır ve sütun değerleri başlıklarda gösterilir. Aspose.Cells for Python via .NET kullanarak, geliştiriciler bu satır ve sütun başlıklarının görünürlüğünü kontrol edebilirler.

### **Çalışma sayfalarının görünürlüğünü kontrol etmek**

Aspose.Cells for Python via .NET, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) sınıfını sağlar; bu sınıf, bir Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) sınıfı, geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine olanak sağlayan [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) koleksiyonunu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden geniş bir [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) koleksiyonu sağlar. [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) koleksiyonu, çalışma sayfasındaki satır veya sütunların yönetimi için çeşitli yöntemler sunar.

#### **Satır/Sütun Başlıklarını Görünür Yapma**

Sınıf [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) özelliğini **true** olarak ayarlayarak satır ve sütun başlıklarını görünür yapın.

#### **Satır/Sütun Başlıklarını Gizleme**

Sınıf [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) özelliğini **false** olarak ayarlayarak satır ve sütun başlıklarını gizleyin.

Aşağıda verilen tam bir örnek, [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) özelliğinin kullanımını göstermektedir, bir excel dosyasını(book1.xls) açarak, ilk çalışma sayfasındaki satır ve sütun başlıklarını gizleyerek değiştirilmiş dosyayı output.xls olarak kaydetme işlemini gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

[**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) ve [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns) yöntemlerini kullanarak, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) sınıfının birden fazla satırı ve sütunu görünür yapmak mümkündür.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
