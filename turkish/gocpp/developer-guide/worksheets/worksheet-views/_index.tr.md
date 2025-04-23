---
title: Sayfa Görünümleri
type: docs
weight: 40
url: /tr/go-cpp/worksheet-views/
---

## **Sayfa Kesme Önizleme**

Tüm çalışma sayfaları iki modda görüntülenebilir:

- Normal görünüm.
- Sayfa kesme önizlemesi.

 Normal görünüm bir çalışma sayfasının varsayılan görünümüdür. Sayfa kesme önizlemesi, bir çalışma sayfasının yazdırılacağı şekilde gösterilen bir düzen görünümüdür. Sayfa kesme önizlemesi, her sayfaya hangi verinin gideceğini gösterir, böylece baskı alanını ve sayfa kesmelerini ayarlayabilirsiniz. Aspose.Cells kullanarak geliştiriciler normal görünümü veya sayfa kesme önizlemesi modlarını etkinleştirebilir.

### **Görünüm Modlarını Kontrol Etme**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı sağlar. Bu [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, Excel dosyasındaki her sayfa öğesine erişim sağlayan [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) koleksiyonunu içerir.

Bir sayfa öğesi [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı, sayfaları yönetmek için çok çeşitli yöntemler sağlar. Normal veya sayfa kırık kaplamalarını önizleme modlarını etkinleştirmek için [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) yöntemini kullanın. [IsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/ispagebreakpreview/) bir boole değeri döndürür, bu şu anlama gelir ki sadece **doğru** veya **yanlış** değeri saklayabilir.

#### **Normal Görünümü Etkinleştirme**

[SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) yönteminin **yanlış** olarak ayarlanmasıyla sayfa önizleme modunu normal görünüme getirin.

#### **Sayfa Kesme Önizlemesini Etkinleştirme**

Herhangi bir sayfa öğesini sayfa kırıntısı önizleme moduna ayarlamak için [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) yöntemini [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfında **true** olarak ayarlayın. Bu, sayfa öğesini normal görünümden sayfa kırıntısı önizleme moduna geçirir.

Aşağıda, ilk sayfa öğesi için sayfa kırıntısı önizleme modunu etkinleştirmek amacıyla [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) yönteminin nasıl kullanılacağını gösteren tam bir örnek bulunmaktadır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnablingPageBreakPreview.go" >}}

## **Yakınlaştırma Faktörü**

### **Microsoft Excel Kullanımı**

Microsoft Excel, kullanıcılara bir çalışma tablosunun yakınlaştırma veya ölçekleme faktörünü ayarlamalarına izin veren bir özellik sağlar. Bu özellik, kullanıcıların çalışma tablosu içeriğini daha küçük veya daha büyük görüntülemelerine yardımcı olur. Kullanıcılar yakınlaştırma faktörünü herhangi bir değere ayarlayabilirler.

### **Aspose.Cells ve Yakınlaştırma Faktörü**

Aspose.Cells ayrıca geliştiricilerin çalışma sayfalarına yakınlaştırma faktörü ayarlamalarına izin verir. Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfını sağlar. Bu sınıf, Excel dosyasındaki her sayfa öğesine erişim sağlayan [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) koleksiyonunu içerir.

Bir çalışma sayfası [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı ile temsil edilir. Bu sınıf, sayfa yönetimi için çok çeşitli yöntemler sağlar. Sayfa yakınlaştırma oranını ayarlamak için [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) yöntemini kullanın. Yakınlaştırma oranı, sayfa yakınlaştırma faktörünü belirtmek için sayısal (tam sayı) bir değer atayarak belirlenir.

Aşağıda, Excel dosyasının ilk sayfasının yakınlaştırma oranını ayarlamak için [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) yönteminin nasıl kullanılacağını gösteren tamamlayıcı bir örnek bulunmaktadır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ZoomFactor.go" >}}

## **Pencereyi Dondurma**

### **Microsoft Excel Kullanımı**

Pencerelerin dondurulmasını sağlayan bir özellik, Microsoft Excel tarafından sağlanır. Pencereyi dondurma, bir çalışma tablosunda kaydırma yaparken görünmesini istediğiniz verileri seçmenize olanak tanır.

### **Aspose.Cells & Pencereleri Dondurma**

Aspose.Cells ayrıca gelişticilerin çalışma sayfalarına sabitleme panoları uygulamalarına izin verir. Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfını sağlar. Bu sınıf, Excel dosyasındaki her sayfa öğesine erişim sağlayan [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) koleksiyonunu içerir.

Bir çalışma sayfası [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı ile temsil edilir. Bu sınıf, sayfaları yönetmek için çok çeşitli yöntemler sağlar. Sabit panoları yapılandırmak için [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) yöntemini çağırın. Bu yöntem aşağıdaki parametreleri alır:

- **Satır**, dondurulmanın başlayacağı hücrenin satır indeksi.
- **Sütun**, dondurulmanın başlayacağı hücrenin sütun indeksi.
- **Dondurulan satırlar**, üst bölmedeki görünür satır sayısı.
- **Dondurulan sütunlar**, sol bölmedeki görünür sütun sayısı

Aşağıda, ilk sayfa için satırları ve sütunları (başlangıç olarak C4, 4. satır ve 3. sütunu gösterir, satır ve sütunlar 0 indeksinden başlar) dondurmak için [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) yönteminin nasıl kullanılacağını gösteren tam bir örnek bulunmaktadır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FreezePanes.go" >}}

## **Bölmeler**

Aynı çalışma tablosunda farklı görünümler elde etmek için ekranı bölmek istemeniz durumunda bölmeler. Microsoft Excel, çalışma sayfanızın kopyasını birden fazla görüntülemenize ve her bir pencerede bağımsız olarak kaydırmanıza izin veren çok kullanışlı bir özellik sunar: bölmeler.

Pencereler aynı anda çalışır. Birinde değişiklik yaparsanız, değişiklik diğerinde aynı anda görünür. Aspose.Cells, kullanıcılar için bölme bölmeleri özelliği sağlar.

### **Bölmelerin Uygulanması ve Kaldırılması**

#### **Bölmeleri Böleme**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfını sağlar. Bu sınıf, bir Excel dosyasını yönetmek için çok çeşitli yöntemler sunar. Bölme görünümünü uygulamak için [Split](https://reference.aspose.com/cells/go-cpp/worksheet/split/) yöntemini kullanın. Bölme panellerini kaldırmak için ise [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/) yöntemini kullanın.

Örnekte, basit bir şablon dosyası kullanılır, ardından ilk çalışma sayfasındaki bir hücreye bölme bölmeleri özelliği uygulanır. Güncellenmiş dosya kaydedilir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SplitPanes.go" >}}

#### **Pencereleri Kaldırma**

Bölme panellerini kaldırmak için [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/) yöntemini kullanın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingPanes.go" >}}
