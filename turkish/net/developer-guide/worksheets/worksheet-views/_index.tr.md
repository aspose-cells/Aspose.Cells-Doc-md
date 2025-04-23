---
title: Sayfa Görünümleri
type: docs
weight: 40
url: /tr/net/worksheet-views/
description: Bu makale, bir Excel çalışma kitabının ve çalışma sayfalarının sayfa görünümü önizlemesiyle etkileşimde bulunmak için C# ve .NET API sını nasıl kullanılacağını açıklar. Bölünmüş panellerle, dondurulmuş panellerle ve yakınlaştırma faktörüyle çalışır. 
---

## **Sayfa Kesme Önizleme**

Tüm çalışma sayfaları iki modda görüntülenebilir:

- Normal görünüm.
- Sayfa kesme önizlemesi.

Normal görünüm, bir çalışma sayfasının varsayılan görünümüdür. Sayfa görünümü önizlemesi, bir çalışma sayfasını yazdırılacağı gibi gösteren bir düzenleme görünümüdür. Sayfa görünümü önizlemesi, her sayfanın hangi verilerin gideceğini gösterir, böylece yazdırma alanını ve sayfa kesmelerini ayarlayabilirsiniz. Aspose.Cells kullanarak geliştiriciler normal görünümü veya sayfa görünümü önizlemesi modlarını etkinleştirebilir.

### **Görünüm Modlarını Kontrol Etme**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı sunar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Normal veya sayfa görünümü önizlemesi modlarını etkinleştirmek için [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) özelliğini kullanın. [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview), yalnızca bir **true** ya da **false** değerini depolayabilen bir Boolean özelliğidir.

#### **Normal Görünümü Etkinleştirme**

Normal görünüm için çalışma sayfasını, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) özelliğini **false** olarak ayarlayarak belirleyin.

#### **Sayfa Kesme Önizlemesini Etkinleştirme**

Herhangi bir çalışma sayfasını sayfa görünümü önizlemesi için [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) özelliğini **true** olarak ayarlayarak belirleyin. Bunu yapmak, çalışma sayfasını normal görünümden sayfa görünümü önizlemesine geçirir.

Aşağıda, bir Excel dosyasının ilk çalışma sayfası için sayfa görünümü önizleme modunu etkinleştirmek için [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) özelliğini nasıl kullanacağını gösteren tam bir örnek verilmiştir.

book1.xls dosyası, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının bir örneği oluşturularak açılır. İlk çalışma sayfası için görünüm, [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) özelliğinin **true** olarak ayarlanmasıyla sayfa görünümü önizlemesi olarak değiştirilir. Değiştirilmiş dosya, çıktı.xls olarak kaydedilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **Yakınlaştırma Faktörü**

### **Microsoft Excel Kullanımı**

Microsoft Excel, kullanıcılara bir çalışma tablosunun yakınlaştırma veya ölçekleme faktörünü ayarlamalarına izin veren bir özellik sağlar. Bu özellik, kullanıcıların çalışma tablosu içeriğini daha küçük veya daha büyük görüntülemelerine yardımcı olur. Kullanıcılar yakınlaştırma faktörünü herhangi bir değere ayarlayabilirler.

### **Aspose.Cells ve Yakınlaştırma Faktörü**

Aspose.Cells, geliştiricilere çalışma sayfası yakınlaştırma faktörünü ayarlama olanağı tanır.
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıfı içeren bir özelliktir. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir çalışma sayfasının yakınlaştırma faktörünü ayarlamak için, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) özelliğini kullanın. Yakınlaştırma faktörü, [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) özelliğine sayısal (tamsayı) bir değer atayarak ayarlanır.

Aşağıdaki tam örnek, Excel dosyasının ilk çalışma sayfasının yakınlaştırma faktörünü ayarlamanın nasıl yapıldığını gösterir.

Book1.xls dosyası, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının bir örneğini oluşturarak açılır. İlk çalışma sayfasının yakınlaştırma faktörü 75 olarak ayarlanır ve değiştirilmiş dosya output.xls olarak kaydedilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **Pencereyi Dondurma**

### **Microsoft Excel Kullanımı**

Pencerelerin dondurulmasını sağlayan bir özellik, Microsoft Excel tarafından sağlanır. Pencereyi dondurma, bir çalışma tablosunda kaydırma yaparken görünmesini istediğiniz verileri seçmenize olanak tanır.

### **Aspose.Cells & Pencereleri Dondurma**

Aspose.Cells, çalışma sayfalarına çalışma zamanında sabit panolar uygulamak için geliştiricilere olanak tanır.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıfı içeren bir özelliktir. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Sabit panoları yapılandırmak için, Çalışma Sayfası sınıfının [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) yöntemini çağırın. [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) yöntemi aşağıdaki parametreleri alır:

- **Satır**, dondurulmanın başlayacağı hücrenin satır indeksi.
- **Sütun**, dondurulmanın başlayacağı hücrenin sütun indeksi.
- **Dondurulan satırlar**, üst bölmedeki görünür satır sayısı.
- **Dondurulan sütunlar**, sol bölmedeki görünür sütun sayısı

Book1.xls dosyası, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının yapılandırıcısını çağırarak açılır ve ilk çalışma sayfasında birkaç satır ve sütun sabitlenir. Değiştirilmiş dosya output.xls olarak kaydedilir.

Aşağıdaki tam örnek, bir Excel dosyasının ilk çalışma sayfasının (0 dizininden başlayarak 4. satır ve 3. sütunu temsil eden C4'ten başlayarak) satır ve sütunları sabitlemek için [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) yönteminin nasıl kullanılacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **Bölmeler**

Aynı çalışma tablosunda farklı görünümler elde etmek için ekranı bölmek istemeniz durumunda bölmeler. Microsoft Excel, çalışma sayfanızın kopyasını birden fazla görüntülemenize ve her bir pencerede bağımsız olarak kaydırmanıza izin veren çok kullanışlı bir özellik sunar: bölmeler.

Pencereler aynı anda çalışır. Birinde değişiklik yaparsanız, değişiklik diğerinde aynı anda görünür. Aspose.Cells, kullanıcılar için bölme bölmeleri özelliği sağlar.

### **Bölmelerin Uygulanması ve Kaldırılması**

#### **Bölmeleri Böleme**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıfı içeren bir özelliktir. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bölünmüş görünümleri uygulamak için, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split) özelliğini kullanın. Bölünmüş panoları kaldırmak için, [**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit) yöntemini kullanın.

Örnekte, basit bir şablon dosyası kullanılır, ardından ilk çalışma sayfasındaki bir hücreye bölme bölmeleri özelliği uygulanır. Güncellenmiş dosya kaydedilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

Yukarıdaki kodu çalıştırdıktan sonra, oluşturulan dosyanın bölünmüş bir görünüme sahip olacağı.

#### **Pencereleri Kaldırma**

Bölme panolarını [**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit) yöntemiyle kaldırın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **Gelişmiş Konular**
- [Çalışma Sayfasında Sıfır Değerlerinin Görüntüsünü Gizleme](/cells/tr/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Çalışma Sayfası Sekme Rengini Ayarlama](/cells/tr/net/set-worksheet-tab-color/)
- [Kılavuz Çizgilerini ve Satır Sütun Başlıklarını Gösterme ve Gizleme](/cells/tr/net/show-and-hide-gridlines-and-row-column-headers/)
- [Satır Sütun ve Kaydırma Çubuklarını Gösterme ve Gizleme](/cells/tr/net/show-and-hide-rows-columns-and-scroll-bars/)
- [Çalışma Sayfalarını ve Sekmeleri Gösterme ve Gizleme](/cells/tr/net/show-and-hide-worksheets-and-tabs/)
- [Çalışma Sayfasında Değerlerin Yerine Formülleri Gösterme](/cells/tr/net/show-formulas-instead-of-values-in-a-worksheet/)
- [Hata Kontrol Seçeneklerini Kullan](/cells/tr/net/use-error-checking-options/)

{{< app/cells/assistant language="csharp" >}}
