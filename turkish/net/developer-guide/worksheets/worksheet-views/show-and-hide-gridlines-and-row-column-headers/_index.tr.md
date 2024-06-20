---
title: Izgara Çizgileri ve Satır Sütun Başlıklarını Gösterme ve Gizleme
type: docs
weight: 30
url: /tr/net/show-and-hide-gridlines-and-row-column-headers/
description: Bu makale, C# API sı veya .NET Kütüphanesi kullanarak Excel çalışma taşrasının izgara çizgilerini, satır ve sütun başlıklarını programlı olarak gösterme veya gizleme için örnek kodları sağlar.
---

{{% alert color="primary" %}}

Aspose.Cells, varsayılan olarak görünür olan çalışma taşraflarının izgara çizgilerini gizleme ve göstermeyi destekler. Aynı zamanda çalışma taşraflarının Satır Sütun Başlıklarının görünürlüğünü kontrol etmeyi sağlar.

{{% /alert %}}

## **Izgara Çizgilerini Gösterme ve Gizleme**

Tüm Excel çalışma taşraları varsayılan olarak izgara çizgilerine sahiptir. Onlar, belirli hücrelere veri girmeyi kolaylaştırdığı için hücreleri çevreler. Izgara çizgileri, bir çalışma taşrasını hücre koleksiyonu olarak görüntülememizi sağlar, burada her hücre kolayca tanımlanabilir.

### **Izgaraların Görünürlüğünü Kontrol Etme**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfında Excel dosyasındaki her çalışma taşrasına erişmek için bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonu bulunur. Bir çalışma taşrası [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir çalışma taşrasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Izgara çizgilerinin görünürlüğünü kontrol etmek için [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) özelliğini kullanın. [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible), yalnızca **true** veya **false** değerini saklayabilen bir Boolean özelliğidir.

#### **Izgaraları Görünür Yapma**

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) özelliğini **true** olarak ayarlayarak ızgara çizgilerini görünür yapın.

#### **Izgaraları Gizleme**

Sınıf [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) özelliğini **false** olarak ayarlayarak ızgaraları gizleyin.

Aşağıda verilen tam bir örnek, [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) özelliğinin kullanımını göstermektedir, bir excel dosyasını(book1.xls) açarak, ilk çalışma sayfasındaki ızgaraları gizleyerek değiştirilmiş dosyayı output.xls olarak kaydetme işlemini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **Satır Sütun Başlıklarını Göster ve Gizle**

Bir Excel dosyasındaki tüm çalışma sayfaları, satırlar ve sütunlarda düzenlenmiş hücrelerden oluşur. Tüm satırlar ve sütunlar benzersiz değerlere sahiptir ve bunları tanımlamak ve bireysel hücreleri tanımlamak için kullanılır. Örneğin, satırlar numaralandırılır - 1, 2, 3, 4, vb. - ve sütunlar alfabetik sıraya göre düzenlenir - A, B, C, D, vb. Satır ve sütun değerleri başlıklarda görüntülenir. Aspose.Cells kullanılarak, geliştiriciler bu satır ve sütun başlıklarının görünürlüğünü kontrol edebilir.

### **Çalışma sayfalarının görünürlüğünü kontrol etmek**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş bir yelpazede özellik ve yöntem sağlar. Satır ve sütun başlıklarının görünürlüğünü kontrol etmek için, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) özelliğini kullanın. [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible), yalnızca **true** veya **false** değerlerini depolayabilen bir Boolean özelliğidir.

#### **Satır/Sütun Başlıklarını Görünür Yapma**

Sınıf [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) özelliğini **true** olarak ayarlayarak satır ve sütun başlıklarını görünür yapın.

#### **Satır/Sütun Başlıklarını Gizleme**

Sınıf [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) özelliğini **false** olarak ayarlayarak satır ve sütun başlıklarını gizleyin.

Aşağıda verilen tam bir örnek, [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) özelliğinin kullanımını göstermektedir, bir excel dosyasını(book1.xls) açarak, ilk çalışma sayfasındaki satır ve sütun başlıklarını gizleyerek değiştirilmiş dosyayı output.xls olarak kaydetme işlemini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

[**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) ve [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) yöntemlerini kullanarak, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıfının birden fazla satırı ve sütunu görünür yapmak mümkündür.

{{% /alert %}}
