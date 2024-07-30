---
title: Sayfa Görünümleri
type: docs
weight: 40
url: /tr/python-net/worksheet-views/
description: Bu makale, Aspose.Cells for Python via .NET API sini kullanarak bir Excel çalışma kitabının ve çalışma sayfalarının sayfa sonu önizlemesi ile nasıl etkileşime geçeceğinizi açıklayacaktır. Bölünmüş paneller, donmuş paneller ve yakınlaştırma faktörü ile çalışın. 
keywords: Python Excel Kütüphanesi, Python Sayfa Sonu Önizleme Nasıl Açılır, Python Normal Görünümü Etkinleştirme, Python Yakınlaştırma Faktörünü Ayarlama, Python Panoları Dondurma, Python Panoları Ayırma, Python Panoları Kaldırma.
---

## **Sayfa Kesme Önizleme**

Tüm çalışma sayfaları iki modda görüntülenebilir:

- Normal görünüm.
- Sayfa kesme önizlemesi.

Normal görünüm, bir çalışma sayfasının varsayılan görünümüdür. Sayfa aralığı önizlemesi, bir çalışma sayfasını yazdırılacağı gibi görüntüleyen bir düzenleme görünümüdür. Sayfa aralığı önizlemesi, her sayfada hangi verilerin yer alacağını gösterir, böylece yazdırma alanını ve sayfa aralıklarını ayarlayabilirsiniz. Aspose.Cells for Python via .NET geliştiricileri, normal görünümü veya sayfa aralığı önizleme modlarını etkinleştirebilir.

### **Görünüm Modlarını Kontrol Etme**

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişime izin veren bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Normal veya sayfa görünümü önizlemesi modlarını etkinleştirmek için [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) özelliğini kullanın. [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview), yalnızca bir **true** ya da **false** değerini depolayabilen bir Boolean özelliğidir.

#### **Normal Görünümü Etkinleştirme**

Normal görünüm için çalışma sayfasını, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) özelliğini **false** olarak ayarlayarak belirleyin.

#### **Sayfa Kesme Önizlemesini Etkinleştirme**

Herhangi bir çalışma sayfasını sayfa görünümü önizlemesi için [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) özelliğini **true** olarak ayarlayarak belirleyin. Bunu yapmak, çalışma sayfasını normal görünümden sayfa görünümü önizlemesine geçirir.

Aşağıda, bir Excel dosyasının ilk çalışma sayfası için sayfa görünümü önizleme modunu etkinleştirmek için [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) özelliğini nasıl kullanacağını gösteren tam bir örnek verilmiştir.

book1.xls dosyası, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının bir örneği oluşturularak açılır. İlk çalışma sayfası için görünüm, [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) özelliğinin **true** olarak ayarlanmasıyla sayfa görünümü önizlemesi olarak değiştirilir. Değiştirilmiş dosya, çıktı.xls olarak kaydedilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-PageBreakPreview-1.py" >}}

## **Yakınlaştırma Faktörü**

### **Microsoft Excel Kullanımı**

Microsoft Excel, kullanıcılara bir çalışma tablosunun yakınlaştırma veya ölçekleme faktörünü ayarlamalarına izin veren bir özellik sağlar. Bu özellik, kullanıcıların çalışma tablosu içeriğini daha küçük veya daha büyük görüntülemelerine yardımcı olur. Kullanıcılar yakınlaştırma faktörünü herhangi bir değere ayarlayabilirler.

### **Aspose.Cells ve Yakınlaştırma Faktörü**

Aspose.Cells, geliştiricilere çalışma sayfası yakınlaştırma faktörünü ayarlama olanağı tanır.
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıfı içeren bir özelliktir. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir çalışma sayfasının yakınlaştırma faktörünü ayarlamak için, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) özelliğini kullanın. Yakınlaştırma faktörü, [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) özelliğine sayısal (tamsayı) bir değer atayarak ayarlanır.

Aşağıdaki tam örnek, Excel dosyasının ilk çalışma sayfasının yakınlaştırma faktörünü ayarlamanın nasıl yapıldığını gösterir.

Book1.xls dosyası, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının bir örneğini oluşturarak açılır. İlk çalışma sayfasının yakınlaştırma faktörü 75 olarak ayarlanır ve değiştirilmiş dosya output.xls olarak kaydedilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ZoomFactor-1.py" >}}

## **Pencereyi Dondurma**

### **Microsoft Excel Kullanımı**

Pencerelerin dondurulmasını sağlayan bir özellik, Microsoft Excel tarafından sağlanır. Pencereyi dondurma, bir çalışma tablosunda kaydırma yaparken görünmesini istediğiniz verileri seçmenize olanak tanır.

### **Aspose.Cells & Pencereleri Dondurma**

Aspose.Cells, çalışma sayfalarına çalışma zamanında sabit panolar uygulamak için geliştiricilere olanak tanır.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıfı içeren bir özelliktir. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Sabit panoları yapılandırmak için, Çalışma Sayfası sınıfının [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) yöntemini çağırın. [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) yöntemi aşağıdaki parametreleri alır:

- **satır**, dondurmanın başlayacağı hücrenin satır dizini.
- **sütun**, dondurmanın başlayacağı hücrenin sütun dizini.
- **dondurulan_satırlar**, üst penceredeki görünür satır sayısı.
- **dondurulan_sütunlar**, sol penceredeki görünür sütun sayısı.

Book1.xls dosyası, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının yapılandırıcısını çağırarak açılır ve ilk çalışma sayfasında birkaç satır ve sütun sabitlenir. Değiştirilmiş dosya output.xls olarak kaydedilir.

Aşağıdaki tam örnek, bir Excel dosyasının ilk çalışma sayfasının (0 dizininden başlayarak 4. satır ve 3. sütunu temsil eden C4'ten başlayarak) satır ve sütunları sabitlemek için [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) yönteminin nasıl kullanılacağını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-FreezePanes-1.py" >}}

## **Bölmeler**

Aynı çalışma tablosunda farklı görünümler elde etmek için ekranı bölmek istemeniz durumunda bölmeler. Microsoft Excel, çalışma sayfanızın kopyasını birden fazla görüntülemenize ve her bir pencerede bağımsız olarak kaydırmanıza izin veren çok kullanışlı bir özellik sunar: bölmeler.

Pencereler aynı anda çalışır. Birinde değişiklik yaparsanız, değişiklik diğerinde aynı anda görünür. Aspose.Cells, kullanıcılar için bölme bölmeleri özelliği sağlar.

### **Bölmelerin Uygulanması ve Kaldırılması**

#### **Bölmeleri Böleme**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıfı içeren bir özelliktir. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, bir Excel dosyasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bölünmüş görünümleri uygulamak için, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split) özelliğini kullanın. Bölünmüş panoları kaldırmak için, [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split) yöntemini kullanın.

Örnekte, basit bir şablon dosyası kullanılır, ardından ilk çalışma sayfasındaki bir hücreye bölme bölmeleri özelliği uygulanır. Güncellenmiş dosya kaydedilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-SplitPanes-1.py" >}}

Yukarıdaki kodu çalıştırdıktan sonra, oluşturulan dosyanın bölünmüş bir görünüme sahip olacağı.

#### **Pencereleri Kaldırma**

Bölme panolarını [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split) yöntemiyle kaldırın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-RemovePanes-1.py" >}}

## **Gelişmiş Konular**
- [Çalışma Sayfasında Sıfır Değerlerinin Görüntüsünü Gizleme](/cells/tr/python-net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Çalışma Sayfası Sekme Rengini Ayarlama](/cells/tr/python-net/set-worksheet-tab-color/)
- [Kılavuz Çizgilerini ve Satır Sütun Başlıklarını Gösterme ve Gizleme](/cells/tr/python-net/show-and-hide-gridlines-and-row-column-headers/)
- [Satır Sütun ve Kaydırma Çubuklarını Gösterme ve Gizleme](/cells/tr/python-net/show-and-hide-rows-columns-and-scroll-bars/)
- [Çalışma Sayfalarını ve Sekmeleri Gösterme ve Gizleme](/cells/tr/python-net/show-and-hide-worksheets-and-tabs/)
- [Çalışma Sayfasında Değerlerin Yerine Formülleri Gösterme](/cells/tr/python-net/show-formulas-instead-of-values-in-a-worksheet/)
- [Hata Kontrol Seçeneklerini Kullan](/cells/tr/python-net/use-error-checking-options/)

