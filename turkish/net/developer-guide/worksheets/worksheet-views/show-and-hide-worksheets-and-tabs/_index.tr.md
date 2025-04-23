---
title: Sayfaları ve Tabları Gösterme ve Gizleme
type: docs
weight: 10
url: /tr/net/show-and-hide-worksheets-and-tabs/
description: Bu makale, C# API sı veya .NET Kütüphanesi ni kullanarak programatik olarak bir Excel çalışma sayfasını gösterme ve gizleme için örnek kod sağlar. Ayrıca, Excel çalışma kitabı sekmelerini gösterme ve gizleme konusunda bilgi sağlar.
---

{{% alert color="primary" %}}

Aspose.Cells kullanıcının çalışma sayfalarını ve sekmelerini gösterebilmesine ve gizleyebilmesine olanak tanır.

{{% /alert %}}

## **Bir Çalışma Sayfasını Gösterme ve Gizleme**

Bir Excel dosyasında bir veya birden fazla çalışma sayfası olabilir. Excel dosyası oluşturduğumuzda, içinde çalıştığımız Excel dosyasına çalışma sayfaları ekleriz. Bir Excel dosyasındaki her çalışma sayfası kendi veri ve biçimlendirme ayarları gibi diğer çalışma sayfalarından bağımsızdır. Bazı durumlarda, geliştiriciler kendi ilgileri için Excel dosyalarındaki birkaç çalışma sayfasını gizlemek ve diğerlerini göstermek isteyebilirler. **Aspose.Cells** bu nedenle geliştiricilere Excel dosyalarında çalışma sayfalarının görünürlüğünü kontrol etme imkanı sunar.

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonu içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir yelpazede özellik ve yöntem sağlar. Bir çalışma sayfasının görünürlüğünü kontrol etmek için [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) özelliğini kullanın. [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) bir Boolean özelliğidir, yani sadece **true** veya **false** değerini saklayabilir.

### **Bir Çalışma Sayfasını Görünür Yapma**

Bir çalışma sayfasını görünür yapmak için [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) özelliğini **true** olarak ayarlayın

### **Bir Çalışsayıyı Gizleme**

Bir çalışma sayfasını gizlemek için [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) özelliğini **false** olarak ayarlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **Tabları Gösterme ve Gizleme**

Microsoft Excel dosyasının alt kısmına dikkatlice baktığınızda, bir dizi kontrolü göreceksiniz. Bunlar şunları içerir:

- Sayfa sekmeleri.
- Sekme kaydırma düğmeleri.

Sayfa sekmeleri, Excel dosyasındaki çalışma sayfalarını temsil eder. Herhangi bir sekmeye tıklayarak o çalışma sayfasına geçebilirsiniz. Çalışma kitabında daha fazla çalışma sayfası olduğunda, daha fazla sayfa sekmesi olacaktır. İyi bir sayıda çalışma sayfasının olduğu Excel dosyasında bunları dolaşmak için düğmeler kullanmanız gerekebilir. Bu nedenle, Microsoft Excel, sayfa sekmeleri ve sekmeler arasında kaydırmak için düğmeler sağlar.

Aspose.Cells kullanarak geliştiriciler Excel dosyalarında sayfa sekmelerinin ve sekmelerin kaydırma düğmelerinin görünürlüğünü kontrol edebilirler.

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasını yönetmek için geniş bir yelpazede özellik ve yöntem sağlar. Bir Excel dosyasındaki sekmelerin görünürlüğünü kontrol etmek için geliştiriciler, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) özelliğini kullanabilir. [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) bir Boolean özelliğidir, yani sadece **true** veya **false** değerini saklayabilen.

### **Sekmeleri Görünür Yapma**

Sekmeleri [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) özelliği **true** olarak ayarlayarak görünür yapın.

### **Sekmeleri Gizleme**

Excel dosyasındaki sekmeleri [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) özelliğini false olarak ayarlayarak gizleyin.

Aşağıda, bir Excel dosyasını (book1.xls) açan, sekmelerini gizleyen ve değiştirilmiş dosyayı output.xls olarak kaydeden tam bir örnek bulunmaktadır. Kodun çalıştırılmasından sonra çalışma kitabının sekmelerinin gizlendiğini göreceksiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **Sekme Çubuğu Genişliğini Kontrol Etme**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
