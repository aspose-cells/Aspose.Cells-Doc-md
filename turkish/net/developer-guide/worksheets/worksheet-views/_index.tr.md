---
title: Çalışma Sayfası Görünümleri
type: docs
weight: 40
url: /tr/net/worksheet-views/
---
## **Sayfa Sonu Önizlemesi**

Tüm çalışma sayfaları iki modda görüntülenebilir:

- Normal görünüm.
- Sayfa sonu önizlemesi.

Normal görünüm, çalışma sayfasının varsayılan görünümüdür. Sayfa sonu önizlemesi, bir çalışma sayfasını yazdırılacağı şekilde görüntüleyen bir düzenleme görünümüdür. Sayfa sonu önizlemesi, yazdırma alanını ve sayfa sonlarını ayarlayabilmeniz için her sayfada hangi verilerin olacağını gösterir. Aspose.Cells'i kullanan geliştiriciler, normal görünüm veya sayfa sonu önizleme modlarını etkinleştirebilir.

### **Görünüm Modlarını Kontrol Etme**

Aspose.Cells bir sağlar[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel dosyasını temsil eden sınıf. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Normal veya sayfa sonu önizleme modlarını etkinleştirmek için[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf[**IsPageBreakÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) Emlak.[**IsPageBreakÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) bir Boolean özelliğidir, yani yalnızca bir**doğru** veya bir**yanlış** değer.

#### **Normal Görünümü Etkinleştirme**

 ayarlayarak bir çalışma sayfasını normal görünüme ayarlayın.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf[**IsPageBreakÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) mülkiyet**yanlış**.

#### **Sayfa Sonu Önizlemesini Etkinleştirme**

 ayarlayarak herhangi bir çalışma sayfasını sayfa sonu önizlemesine ayarlayın.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf[**IsPageBreakÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) mülkiyet**doğru**Bunu yapmak, çalışma sayfasını normal görünümden sayfa sonu önizlemesine geçirir.

 nasıl kullanılacağını gösteren eksiksiz bir örnek aşağıda verilmiştir.[**IsPageBreakÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)özelliği, bir Excel dosyasının ilk çalışma sayfası için sayfa sonu önizleme modunu etkinleştirir.

book1.xls dosyası, örneğinin bir örneği oluşturularak açılır.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf. Görünüm, ayarlanarak ilk çalışma sayfası için sayfa sonu önizlemesine geçirilir.[**IsPageBreakÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)mülkiyet**doğru**. Değiştirilen dosya output.xls olarak kaydedilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **Yakınlaştırma Faktörü**

### **Microsoft Excel'i kullanma**

Microsoft Excel, kullanıcıların bir çalışma sayfasının yakınlaştırma veya ölçekleme faktörünü ayarlamasına olanak tanıyan bir özellik sağlar. Bu özellik, kullanıcıların çalışma sayfası içeriğini daha küçük veya daha büyük görünümlerde görmelerine yardımcı olur. Kullanıcılar yakınlaştırma faktörünü herhangi bir değere ayarlayabilir.

### **Aspose.Cells & Yakınlaştırma Faktörü**

Aspose.Cells, geliştiricilerin çalışma sayfası yakınlaştırma faktörünü ayarlamasına olanak tanır.
Aspose.Cells bir sağlar[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel dosyasını temsil eden sınıf. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Bir çalışma sayfasının yakınlaştırma faktörünü ayarlamak için[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf'[**yakınlaştır**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)Emlak. Yakınlaştırma faktörü, ekrana bir sayısal (tamsayı) değer atayarak ayarlanır.[**yakınlaştır**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) Emlak.

nasıl kullanılacağını gösteren eksiksiz bir örnek aşağıda verilmiştir.[**yakınlaştır**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) Excel dosyasının ilk çalışma sayfasının yakınlaştırma faktörünü ayarlama özelliği.

book1.xls dosyası, örneğinin bir örneği oluşturularak açılır.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf. İlk çalışma sayfasının yakınlaştırma faktörü 75 olarak ayarlanır ve değiştirilen dosya output.xls olarak kaydedilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **Donma bölmeleri**

### **Microsoft Excel'i kullanma**

Bölmeleri dondur, Microsoft Excel tarafından sağlanan bir özelliktir. Bölmeleri dondurmak, bir çalışma sayfasında kaydırırken görünür kalacak verileri seçmenize olanak tanır.

### **Aspose.Cells & Bölmeleri Dondur**

Aspose.Cells, geliştiricilerin çalışma zamanında çalışma sayfalarına bölmeleri dondurma uygulamasına olanak tanır.

Aspose.Cells bir sağlar[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel dosyasını temsil eden sınıf. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Dondurma bölmelerini yapılandırmak için Worksheet sınıfını çağırın'[**Donma bölmeleri**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)yöntem. bu[**Donma bölmeleri**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)yöntem aşağıdaki parametreleri alır:

- **Sıra**, dondurmanın başlayacağı hücrenin satır dizini.
- **Kolon**, dondurmanın başlayacağı hücrenin sütun dizini.
- **Donmuş satırlar**, üst bölmedeki görünür satırların sayısı.
- **Dondurulmuş sütunlar**, sol bölmedeki görünür sütunların sayısı

book1.xls dosyası çağrılarak açılır.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıfın yapıcısı onu başlatırken ve birkaç satır ve sütun ilk çalışma sayfasında dondurulur. Değiştirilen dosya output.xls olarak kaydedilir.

 nasıl kullanılacağını gösteren eksiksiz bir örnek aşağıda verilmiştir.[**Donma bölmeleri**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)Excel dosyasının ilk çalışma sayfasının satırlarını ve sütunlarını dondurma yöntemi (C4'ten başlayarak, 4. satır ve 3. sütunla temsil edilir, burada satırlar ve sütunlar 0 dizininden başlar).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **Bölme Bölmeleri**

Aynı çalışma sayfasında iki farklı görünüm elde etmek için ekranı bölmeniz gerekiyorsa bölmeleri ayırın. Microsoft Excel, çalışma sayfanızın birden fazla kopyasını görüntülemenize ve çalışma sayfanızın her bölmesinde bağımsız olarak kaydırmanıza izin veren çok kullanışlı bir özellik sunar: bölünmüş bölmeler.

Bölmeler aynı anda çalışır. Birinde değişiklik yaparsanız, değişiklik aynı anda diğerinde de görünür. Aspose.Cells, kullanıcılar için bölünmüş bölmeler özelliği sağlar.

### **Bölünmüş Bölmeleri Uygulama ve Kaldırma**

#### **bölme bölmeleri**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class, bir Excel dosyasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Bölünmüş görünümler uygulamak için[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf'[**Bölmek**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split) . Bölünmüş bölmeleri kaldırmak için,[**Bölmeyi Kaldır**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)yöntem.

Örnekte, yüklenen basit bir şablon dosyası kullanıyoruz, ardından ilk çalışma sayfasındaki bir hücreye bölünmüş bölmeleri ayarla özelliği uygulandı. Güncellenen dosya kaydedilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

Yukarıdaki kodu çalıştırdıktan sonra, oluşturulan dosya bölünmüş bir görünüme sahip olacaktır.

#### **Bölmeleri Kaldırma**

 kullanarak bölünmüş bölmeleri kaldırın.[**Bölmeyi Kaldır**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **ileri konular**
- [Çalışma Sayfasında Sıfır Değerlerinin Görüntülenmesini Gizleme](/cells/tr/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Çalışma Sayfası Sekme Rengini Ayarla](/cells/tr/net/set-worksheet-tab-color/)
- [Kılavuz Çizgilerini ve Satır Sütun Başlıklarını Gösterme ve Gizleme](/cells/tr/net/show-and-hide-gridlines-and-row-column-headers/)
- [Satırları, Sütunları ve Kaydırma Çubuklarını Gösterme ve Gizleme](/cells/tr/net/show-and-hide-rows-columns-and-scroll-bars/)
- [Çalışma Sayfalarını ve Sekmeleri Göster ve Gizle](/cells/tr/net/show-and-hide-worksheets-and-tabs/)
- [Çalışma Sayfasında Değerler Yerine Formülleri Gösterme](/cells/tr/net/show-formulas-instead-of-values-in-a-worksheet/)
- [Hata Denetimi Seçeneklerini Kullanın](/cells/tr/net/use-error-checking-options/)

