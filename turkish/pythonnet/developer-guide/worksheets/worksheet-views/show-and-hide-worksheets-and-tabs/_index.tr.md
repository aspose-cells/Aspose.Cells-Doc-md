---
title: Sayfaları ve Tabları Gösterme ve Gizleme
type: docs
weight: 10
url: /tr/python-net/show-and-hide-worksheets-and-tabs/
description: Bu makale, Aspose.Cells for Python via .NET API kullanarak Excel çalışma sayfasını programlı olarak gösterme ve gizleme için örnek kod sağlar. Ayrıca, Excel çalışma kitabı sekmelerini gösterip gizleme işlemleri de anlatılır.
keywords: Python Excel Kütüphanesi, Python da Çalışma Sayfasını Göster ve Gizle, Sekmeleri Göster ve Gizle, Sekme Çubuğu Genişliğini Kontrol Et.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, kullanıcıların çalışma kitabının öğelerini görüntüleyip gizlemesine olanak tanır, bunlar arasında çalışma sayfaları ve sekmeler bulunur.

{{% /alert %}}

## **Bir Çalışma Sayfasını Gösterme ve Gizleme**

Bir Excel dosyasında bir veya daha fazla çalışma sayfası olabilir. Her oluşturduğumuzda, çalışma kitabına çalışma sayfaları ekleriz ve onlarda çalışırız. Her çalışma sayfası, kendi verileri ve biçimlendirme ayarlarıyla bağımsızdır. Bazen, geliştiriciler kendi çıkarları doğrultusunda birkaç çalışma sayfasını gizli, diğerlerini görünür yapmak isteyebilir. Bu nedenle, **Aspose.Cells for Python via .NET** geliştirilmişlerin çalışma sayfalarının görünürlüğünü kontrol etmelerine olanak tanır.

Aspose.Cells for Python via .NET, Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, her çalışma sayfasına erişim sağlayan [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonunu içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir yelpazede özellik ve yöntem sağlar. Bir çalışma sayfasının görünürlüğünü kontrol etmek için [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) özelliğini kullanın. [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) bir Boolean özelliğidir, yani sadece **true** veya **false** değerini saklayabilir.

### **Bir Çalışma Sayfasını Görünür Yapma**

Bir çalışma sayfasını görünür yapmak için [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) özelliğini **true** olarak ayarlayın

### **Bir Çalışsayıyı Gizleme**

Bir çalışma sayfasını gizlemek için [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) özelliğini **false** olarak ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideUnhideWorksheet-1.py" >}}

## **Tabları Gösterme ve Gizleme**

Microsoft Excel dosyasının alt kısmına dikkatlice baktığınızda, bir dizi kontrolü göreceksiniz. Bunlar şunları içerir:

- Sayfa sekmeleri.
- Sekme kaydırma düğmeleri.

Sayfa sekmeleri, Excel dosyasındaki çalışma sayfalarını temsil eder. Herhangi bir sekmeye tıklayarak o çalışma sayfasına geçebilirsiniz. Çalışma kitabında daha fazla çalışma sayfası olduğunda, daha fazla sayfa sekmesi olacaktır. İyi bir sayıda çalışma sayfasının olduğu Excel dosyasında bunları dolaşmak için düğmeler kullanmanız gerekebilir. Bu nedenle, Microsoft Excel, sayfa sekmeleri ve sekmeler arasında kaydırmak için düğmeler sağlar.

Aspose.Cells for Python via .NET kullanarak, geliştiriciler çalışma sayfası sekmelerinin ve sekme kaydırma düğmelerinin görünürlüğünü kontrol edebilirler.

Aspose.Cells for Python via .NET, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) adlı bir sınıf sağlar; bu sınıf, bir Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, bir Excel dosyasını yönetmek için geniş özellik ve yöntemler sunar. Bir Excel dosyasındaki sekmelerin görünürlüğünü kontrol etmek için, geliştiriciler [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) özelliğini kullanabilirler. [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) boolean bir özelliktir ve yalnızca **doğru** veya **yanlış** değerleri depolayabilir.

### **Sekmeleri Görünür Yapma**

Sekmeleri [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) özelliği **true** olarak ayarlayarak görünür yapın.

### **Sekmeleri Gizleme**

Excel dosyasındaki sekmeleri [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) özelliğini false olarak ayarlayarak gizleyin.

Aşağıda, bir Excel dosyasını (book1.xls) açan, sekmelerini gizleyen ve değiştirilmiş dosyayı output.xls olarak kaydeden tam bir örnek bulunmaktadır. Kodun çalıştırılmasından sonra çalışma kitabının sekmelerinin gizlendiğini göreceksiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **Sekme Çubuğu Genişliğini Kontrol Etme**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
