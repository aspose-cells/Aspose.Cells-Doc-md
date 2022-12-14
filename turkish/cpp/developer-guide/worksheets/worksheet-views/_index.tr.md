---
title: Çalışma Sayfası Görünümleri
type: docs
weight: 40
url: /tr/cpp/worksheet-views/
---
## **Sayfa Sonu Önizlemesi**
Tüm çalışma sayfaları iki modda görüntülenebilir:

- Normal görünüm.
- Sayfa sonu önizlemesi.

Normal görünüm, çalışma sayfasının varsayılan görünümüdür. Sayfa sonu önizlemesi, bir çalışma sayfasını yazdırılacağı şekilde görüntüleyen bir düzenleme görünümüdür. Sayfa sonu önizlemesi, yazdırma alanını ve sayfa sonlarını ayarlayabilmeniz için her sayfada hangi verilerin olacağını gösterir. Aspose.Cells'i kullanan geliştiriciler, normal görünüm veya sayfa sonu önizleme modlarını etkinleştirebilir.
### **Görünüm Modlarını Kontrol Etme**
 Aspose.Cells bir sınıf sağlar[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf bir içerir[çalışma sayfaları](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)sınıf. bu[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class, çalışma sayfalarını yönetmek için çok çeşitli yöntemler sağlar. Normal veya sayfa sonu önizleme modlarını etkinleştirmek için[IsPageBreakÖnizleme](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) yöntemi[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf.[IsPageBreakÖnizleme](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) bir bool değeri döndürür; bu, yalnızca bir**doğru** veya**yanlış** değer.
#### **Normal Görünümü Etkinleştirme**
ayarlayarak bir çalışma sayfasını normal görünüme ayarlayın.[IsPageBreakÖnizleme](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)yöntemi[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf**yanlış**.
#### **Sayfa Sonu Önizlemesini Etkinleştirme**
ayarlayarak herhangi bir çalışma sayfasını sayfa sonu önizlemesine ayarlayın.[IsPageBreakÖnizleme](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)yöntemi[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf**doğru**Bunu yapmak, çalışma sayfasını normal görünümden sayfa sonu önizlemesine geçirir.

 nasıl kullanılacağını gösteren eksiksiz bir örnek aşağıda verilmiştir.[IsPageBreakÖnizleme](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)bir Excel dosyasının ilk çalışma sayfası için sayfa sonu önizleme modunu etkinleştirme yöntemi.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview.cpp" >}}
## **Yakınlaştırma Faktörü**
### **Microsoft Excel'i kullanma**
Microsoft Excel, kullanıcıların bir çalışma sayfasının yakınlaştırma veya ölçekleme faktörünü ayarlamasına olanak tanıyan bir özellik sağlar. Bu özellik, kullanıcıların çalışma sayfası içeriğini daha küçük veya daha büyük görünümlerde görmelerine yardımcı olur. Kullanıcılar yakınlaştırma faktörünü herhangi bir değere ayarlayabilir.
### **Aspose.Cells & Yakınlaştırma Faktörü**
 Aspose.Cells, geliştiricilerin çalışma sayfası yakınlaştırma faktörünü ayarlamasına da olanak tanır. Aspose.Cells bir sınıf sağlar[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf bir içerir[çalışma sayfaları](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. bu[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)class, çalışma sayfalarını yönetmek için çok çeşitli yöntemler sağlar. Bir çalışma sayfasının yakınlaştırma faktörünü ayarlamak için[yakınlaştır](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec) yöntemi[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıfa bir sayısal (tamsayı) değer atayarak yakınlaştırma faktörü ayarlanır.[yakınlaştır](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)yöntem.

 nasıl kullanılacağını gösteren eksiksiz bir örnek aşağıda verilmiştir.[yakınlaştır](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)Excel dosyasının ilk çalışma sayfasının yakınlaştırma faktörünü ayarlama yöntemi.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor.cpp" >}}
## **Donma bölmeleri**
### **Microsoft Excel'i kullanma**
Bölmeleri dondur, Microsoft Excel tarafından sağlanan bir özelliktir. Bölmeleri dondurmak, bir çalışma sayfasında kaydırırken görünür kalacak verileri seçmenize olanak tanır.
### **Aspose.Cells & Bölmeleri Dondur**
 Aspose.Cells, geliştiricilerin çalışma zamanında çalışma sayfalarına bölmeleri dondurma uygulamasına da izin verir. Aspose.Cells bir sınıf sağlar[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf bir içerir[çalışma sayfaları](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. bu[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)class, çalışma sayfalarını yönetmek için çok çeşitli yöntemler sağlar. Bölmeleri dondurmak için,[Donma bölmeleri](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)yöntemi[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. bu[Donma bölmeleri](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)yöntem aşağıdaki parametreleri alır:

- **Sıra**, dondurmanın başlayacağı hücrenin satır dizini.
- **Kolon**, dondurmanın başlayacağı hücrenin sütun dizini.
- **Donmuş satırlar**, üst bölmedeki görünür satırların sayısı.
- **Dondurulmuş sütunlar**, sol bölmedeki görünür sütunların sayısı

 nasıl kullanılacağını gösteren eksiksiz bir örnek aşağıda verilmiştir.[Donma bölmeleri](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)Excel dosyasının ilk çalışma sayfasının satırlarını ve sütunlarını (4. satır ve 3. sütunla temsil edilen, satır ve sütunların 0 dizininden başladığı C4'ten başlayarak) dondurma yöntemi.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes.cpp" >}}
## **Bölme Bölmeleri**
Aynı çalışma sayfasında iki farklı görünüm elde etmek için ekranı bölmeniz gerekiyorsa bölmeleri ayırın. Microsoft Excel, çalışma sayfanızın birden fazla kopyasını görüntülemenize ve çalışma sayfanızın her bölmesinde bağımsız olarak kaydırmanıza izin veren çok kullanışlı bir özellik sunar: bölünmüş bölmeler.

Bölmeler aynı anda çalışır. Birinde değişiklik yaparsanız, değişiklik aynı anda diğerinde de görünür. Aspose.Cells, kullanıcılar için bölünmüş bölmeler özelliği sağlar.
### **Bölünmüş Bölmeleri Uygulama ve Kaldırma**
#### **bölme bölmeleri**
 Aspose.Cells bir sınıf sağlar[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)class, bir Excel dosyasını yönetmek için çok çeşitli yöntemler sağlar. Bölünmüş görünümler uygulamak için[Bölmek](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a0e581a3a9528a767c57008521ee02b6f) yöntemi[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. Bölünmüş bölmeleri kaldırmak için,[Bölmeyi Kaldır](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)yöntem.

Örnekte, yüklenen basit bir şablon dosyası kullanıyoruz, ardından ilk çalışma sayfasındaki bir hücreye bölünmüş bölmeleri ayarla özelliği uygulandı. Güncellenen dosya kaydedilir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes.cpp" >}}
#### **Bölmeleri Kaldırma**
 kullanarak bölünmüş bölmeleri kaldırın.[Bölmeyi Kaldır](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)yöntem.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes.cpp" >}}
