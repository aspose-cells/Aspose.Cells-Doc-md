---
title: Çalışma Sayfalarını ve Sekmeleri Göster ve Gizle
type: docs
weight: 10
url: /tr/net/show-and-hide-worksheets-and-tabs/
---
{{% alert color="primary" %}}

Aspose.Cells, kullanıcının çalışma sayfaları ve sekmeler dahil olmak üzere bir çalışma kitabının öğelerini göstermesini ve gizlemesini sağlar.

{{% /alert %}}

## **Bir Çalışma Sayfasını Göster ve Gizle**

 Bir Excel dosyasında bir veya daha fazla çalışma sayfası olabilir. Ne zaman bir Excel dosyası oluştursak, içinde çalıştığımız Excel dosyasına çalışma sayfaları ekleriz. Bir Excel dosyasındaki her çalışma sayfası, kendi verileri ve biçimlendirme ayarları vb. ile diğer çalışma sayfasından bağımsızdır. Bazen, geliştiriciler kendi ilgileri için Excel dosyasında birkaç çalışma sayfasını gizli ve diğerlerini görünür yapmak isteyebilirler. Yani,**Aspose.Cells** geliştiricilerin Excel dosyalarındaki çalışma sayfalarının görünürlüğünü kontrol etmelerini sağlar.

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)class, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Bir çalışma sayfasının görünürlüğünü kontrol etmek için[**Görünür**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) mülkiyeti[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Görünür**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) bir Boolean özelliğidir, yani yalnızca bir**doğru** veya**yanlış** değer.

### **Bir Çalışma Sayfasını Görünür Hale Getirme**

 ayarlayarak bir çalışma sayfasını görünür yapın.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf'[**Görünür**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) mülkiyet**doğru**

### **Bir Çalışma Sayfasını Gizleme**

 ayarlayarak bir çalışma sayfasını gizleyin.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf'[**Görünür**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) mülkiyet**yanlış**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **Sekmeleri Göster ve Gizle**

Microsoft Excel dosyasının en altına yakından bakarsanız, bir dizi kontrol görürsünüz. Bunlar şunları içerir:

- Sayfa sekmeleri.
- Sekme kaydırma düğmeleri.

Sayfa sekmeleri, Excel dosyasındaki çalışma sayfalarını temsil eder. Söz konusu çalışma sayfasına geçmek için herhangi bir sekmeye tıklayın. Çalışma kitabında ne kadar çok çalışma sayfası varsa, o kadar çok sayfa sekmesi vardır. Excel dosyasında çok sayıda çalışma sayfası varsa, bunlar arasında gezinmek için düğmelere ihtiyacınız vardır. Bu nedenle, Microsoft Excel, sayfa sekmeleri arasında gezinmek için sekme kaydırma düğmeleri sağlar.

Geliştiriciler, Aspose.Cells'i kullanarak Excel dosyalarındaki sayfa sekmelerinin ve sekme kaydırma düğmelerinin görünürlüğünü kontrol edebilir.

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class, bir Excel dosyasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Geliştiriciler, bir Excel dosyasındaki sekmelerin görünürlüğünü kontrol etmek için[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) Emlak.[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) bir Boolean özelliğidir, yani yalnızca bir**doğru** veya**yanlış** değer.

### **Sekmeleri Görünür Hale Getirmek**

 ile sekmeleri görünür yapın[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) mülkiyet**doğru**.

### **Sekmeleri Gizleme**

 ayarlayarak bir Excel dosyasındaki sekmeleri gizleyin.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)false özelliği.

Aşağıda, bir Excel dosyasını (book1.xls) açan, sekmelerini gizleyen ve değiştirilen dosyayı output.xls olarak kaydeden tam bir örnek bulunmaktadır. Kod yürütme işleminden sonra, çalışma kitabının sekmelerinin gizlendiğini göreceksiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **Sekme Çubuğu Genişliğini Kontrol Etme**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
