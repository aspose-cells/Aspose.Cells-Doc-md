---
title: Çalışma Sayfası Görünümleri
type: docs
weight: 40
url: /tr/cpp/worksheet-views/
---
##  **Sayfa Sonu Önizlemesi**
Tüm çalışma sayfaları iki modda görüntülenebilir:

- Normal görünüm.
- Sayfa sonu önizlemesi.

Normal görünüm, çalışma sayfasının varsayılan görünümüdür. Sayfa sonu önizlemesi, bir çalışma sayfasını yazdırılacağı gibi görüntüleyen bir düzenleme görünümüdür. Sayfa sonu önizlemesi her sayfada hangi verilerin yer alacağını gösterir, böylece yazdırma alanını ve sayfa sonlarını ayarlayabilirsiniz. Geliştiriciler Aspose.Cells'i kullanarak normal görünüm veya sayfa sonu önizleme modlarını etkinleştirebilir.
###  **Görünüm Modlarını Kontrol Etme**
 Aspose.Cells bir sınıf sağlıyor[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bu bir Microsoft Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf bir içerir[Çalışma sayfaları](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Bir Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon.

Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class, çalışma sayfalarını yönetmek için çok çeşitli yöntemler sağlar. Normal veya sayfa sonu önizleme modlarını etkinleştirmek için[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) yöntemi[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf.[IsPageBreakÖnizleme](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) bir bool değeri döndürür; bu, yalnızca bir değeri saklayabileceği anlamına gelir.**doğru** veya**YANLIŞ** değer.
####  **Normal Görünümü Etkinleştirme**
Ayarlayarak bir çalışma sayfasını normal görünüme ayarlayın.[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)yöntemi[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)sınıfı *false** olarak değiştirin.
####  **Sayfa Sonu Önizlemesini Etkinleştirme**
Ayarlayarak herhangi bir çalışma sayfasını sayfa sonu önizlemesine ayarlayın.[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)yöntemi[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)sınıfı *true** olarak değiştirin. Bunu yapmak, çalışma sayfasını normal görünümden sayfa sonu önizlemesine geçirir.

Aşağıda, nasıl kullanılacağını gösteren eksiksiz bir örnek verilmiştir.[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)Bir Excel dosyasının ilk çalışma sayfası için sayfa sonu önizleme modunu etkinleştirme yöntemi.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
##  **Yakınlaştırma Faktörü**
###  **Microsoft Excel'i kullanma**
Microsoft Excel, kullanıcıların çalışma sayfasının yakınlaştırma veya ölçeklendirme faktörünü ayarlamasına olanak tanıyan bir özellik sağlar. Bu özellik, kullanıcıların çalışma sayfası içeriğini daha küçük veya daha büyük görünümlerde görmesine yardımcı olur. Kullanıcılar yakınlaştırma faktörünü herhangi bir değere ayarlayabilir.
###  **Aspose.Cells & Yakınlaştırma Faktörü**
 Aspose.Cells ayrıca geliştiricilerin çalışma sayfası yakınlaştırma faktörünü ayarlamasına da olanak tanır. Aspose.Cells bir sınıf sağlıyor[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bu bir Microsoft Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf bir içerir[Çalışma sayfaları](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Bir Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon.

Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)class, çalışma sayfalarını yönetmek için çok çeşitli yöntemler sağlar. Bir çalışma sayfasının yakınlaştırma faktörünü ayarlamak için[Yakınlaştırmayı Ayarla](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) yöntemi[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf. Yakınlaştırma faktörü, sayısal (tamsayı) bir değer atanarak ayarlanır.[Yakınlaştırmayı Ayarla](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)yöntem.

Aşağıda, nasıl kullanılacağını gösteren eksiksiz bir örnek verilmiştir.[Yakınlaştırmayı Ayarla](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)Excel dosyasının ilk çalışma sayfasının yakınlaştırma faktörünü ayarlama yöntemi.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
##  **Donma bölmeleri**
###  **Microsoft Excel'i kullanma**
Bölmeleri dondurma, Microsoft Excel tarafından sağlanan bir özelliktir. Bölmeleri dondurmak, bir çalışma sayfasında kaydırma yaparken verilerin görünür kalmasını seçmenize olanak tanır.
###  **Aspose.Cells & Bölmeleri Dondur**
 Aspose.Cells ayrıca geliştiricilerin çalışma zamanında çalışma sayfalarına dondurma bölmeleri uygulamasına da olanak tanır. Aspose.Cells bir sınıf sağlıyor[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bu bir Microsoft Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf bir içerir[Çalışma sayfaları](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Bir Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon.

Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)class, çalışma sayfalarını yönetmek için çok çeşitli yöntemler sağlar. Bölmeleri dondurmayı yapılandırmak için[Donma bölmeleri](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)yöntemi[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf.[Donma bölmeleri](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)yöntem aşağıdaki parametreleri alır:

- *Satır**, dondurmanın başlayacağı hücrenin satır dizini.
- *Sütun**, dondurmanın başlayacağı hücrenin sütun dizini.
- *Dondurulmuş satırlar**, üst bölmedeki görünür satırların sayısı.
- *Dondurulmuş sütunlar**, sol bölmedeki görünür sütunların sayısı

 Aşağıda, nasıl kullanılacağını gösteren eksiksiz bir örnek verilmiştir.[Donma bölmeleri](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)Excel dosyasının ilk çalışma sayfasının satırlarını ve sütunlarını (C4'ten başlayarak, 4. satır ve 3. sütunla temsil edilen, satır ve sütunların 0 dizininden başladığı) dondurma yöntemi.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
##  **Bölünmüş Bölmeler**
Aynı çalışma sayfasında iki farklı görünüm elde etmek için ekranı bölmeniz gerekiyorsa bölmeleri ayırın. Microsoft Excel, çalışma sayfanızın birden fazla kopyasını görüntülemenize ve çalışma sayfanızın her bölmesinde bağımsız olarak gezinebilmenize olanak tanıyan çok kullanışlı bir özellik sunar: bölünmüş bölmeler.

Bölmeler aynı anda çalışır. Birinde değişiklik yaptığınızda değişiklik aynı anda diğerinde de görünür. Aspose.Cells kullanıcılara bölmeleri bölme özelliğini sunuyor.
###  **Bölünmüş Bölmeleri Uygulama ve Kaldırma**
####  **Bölme Bölmeleri**
 Aspose.Cells bir sınıf sağlıyor[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bu bir Microsoft Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)class, bir Excel dosyasını yönetmek için çok çeşitli yöntemler sağlar. Bölünmüş görünümleri uygulamak için şunu kullanın:[Bölmek](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) yöntemi[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf. Bölünmüş bölmeleri kaldırmak için şunu kullanın:[Bölmeyi Kaldır](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)yöntem.

Örnekte, yüklenen basit bir şablon dosyası kullanıyoruz, ardından ilk çalışma sayfasındaki bir hücreye bölünmüş bölmeleri ayarlama özelliği uygulanıyor. Güncellenen dosya kaydedilir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
####  **Bölmeleri Çıkarma**
 kullanarak bölünmüş bölmeleri kaldırın.[Bölmeyi Kaldır](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)yöntem.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
