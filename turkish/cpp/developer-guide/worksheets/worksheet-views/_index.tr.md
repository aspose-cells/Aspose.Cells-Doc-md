---
title: Sayfa Görünümleri
type: docs
weight: 40
url: /tr/cpp/worksheet-views/
---

## **Sayfa Kesme Önizleme**
Tüm çalışma sayfaları iki modda görüntülenebilir:

- Normal görünüm.
- Sayfa kesme önizlemesi.

 Normal görünüm bir çalışma sayfasının varsayılan görünümüdür. Sayfa kesme önizlemesi, bir çalışma sayfasının yazdırılacağı şekilde gösterilen bir düzen görünümüdür. Sayfa kesme önizlemesi, her sayfaya hangi verinin gideceğini gösterir, böylece baskı alanını ve sayfa kesmelerini ayarlayabilirsiniz. Aspose.Cells kullanarak geliştiriciler normal görünümü veya sayfa kesme önizlemesi modlarını etkinleştirebilir.
### **Görünüm Modlarını Kontrol Etme**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişimi sağlayan bir [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir.

Çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışma sayfasını yönetmek için geniş bir yöntem yelpazesi sağlar. Normal veya sayfa kesme önizlemesi modlarını etkinleştirmek için [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) yöntemini kullanın. [IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) bir bool değeri döndürür, bu da sadece **true** veya **false** değerini depolayabilir.
#### **Normal Görünümü Etkinleştirme**
Çalışma sayfasını normal görüne ayarlayarak [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) metodunu **false** olarak ayarlayın.
#### **Sayfa Kesme Önizlemesini Etkinleştirme**
Herhangi bir çalışma sayfasını [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) metodunu **true** olarak ayarlayarak sayfa kesme önizlemesine ayarlayın. Bunu yapmak, çalışma sayfasını normal görüşten sayfa kesme önizlemesine geçirir.

Aşağıda, [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) metodunu kullanarak bir Excel dosyasının ilk çalışma sayfası için sayfa kesme önizleme modunu etkinleştirmeyi gösteren tam bir örnek verilmiştir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
## **Yakınlaştırma Faktörü**
### **Microsoft Excel Kullanımı**
Microsoft Excel, kullanıcılara bir çalışma tablosunun yakınlaştırma veya ölçekleme faktörünü ayarlamalarına izin veren bir özellik sağlar. Bu özellik, kullanıcıların çalışma tablosu içeriğini daha küçük veya daha büyük görüntülemelerine yardımcı olur. Kullanıcılar yakınlaştırma faktörünü herhangi bir değere ayarlayabilirler.
### **Aspose.Cells ve Yakınlaştırma Faktörü**
Aspose.Cells, geliştiricilere de çalışma tablosunun yakınlaştırma faktörünü ayarlama imkanı sunar. Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) adlı bir sınıf sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişime izin veren bir [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonu içerir.

Bir çalışma sayfası [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışma sayfalarını yönetmek için geniş bir yöntem yelpazesi sağlar. Bir çalışma sayfasının yakınlaştırma faktörünü ayarlamak için, [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) yöntemini kullanın. Yakınlaştırma faktörü, [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) yöntemine bir sayısal (tamsayı) değer atayarak ayarlanır.

Aşağıdaki tam örnek, bir Excel dosyasının ilk çalışma sayfasının yakınlaştırma faktörünü ayarlamak için [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) yöntemini nasıl kullanacağını göstermektedir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
## **Pencereyi Dondurma**
### **Microsoft Excel Kullanımı**
Pencerelerin dondurulmasını sağlayan bir özellik, Microsoft Excel tarafından sağlanır. Pencereyi dondurma, bir çalışma tablosunda kaydırma yaparken görünmesini istediğiniz verileri seçmenize olanak tanır.
### **Aspose.Cells & Pencereleri Dondurma**
Aspose.Cells, geliştiricilere çalışma tablolarına çalışma zamanında pencerelerin dondurulmasını uygulama imkanı sunar. Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) adlı bir sınıf sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişime izin veren bir [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonu içerir.

Bir çalışma sayfası [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışma sayfalarını yönetmek için geniş bir yöntem yelpazesi sağlar. Pencereleri dondurmak için, [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) yöntemini çağırın. [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) yöntemi, aşağıdaki parametreleri alır:

- **Satır**, dondurulmanın başlayacağı hücrenin satır indeksi.
- **Sütun**, dondurulmanın başlayacağı hücrenin sütun indeksi.
- **Dondurulan satırlar**, üst bölmedeki görünür satır sayısı.
- **Dondurulan sütunlar**, sol bölmedeki görünür sütun sayısı

Aşağıdaki tam örnek, bir Excel dosyasının ilk çalışma sayfasının (satırların ve sütunların 0 dizininden başladığı C4 temsil edilen) satırları ve sütunları dondurmak için [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) yönteminin nasıl kullanılacağını göstermektedir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
## **Bölmeler**
Aynı çalışma tablosunda farklı görünümler elde etmek için ekranı bölmek istemeniz durumunda bölmeler. Microsoft Excel, çalışma sayfanızın kopyasını birden fazla görüntülemenize ve her bir pencerede bağımsız olarak kaydırmanıza izin veren çok kullanışlı bir özellik sunar: bölmeler.

Pencereler aynı anda çalışır. Birinde değişiklik yaparsanız, değişiklik diğerinde aynı anda görünür. Aspose.Cells, kullanıcılar için bölme bölmeleri özelliği sağlar.
### **Bölmelerin Uygulanması ve Kaldırılması**
#### **Bölmeleri Böleme**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) adlı bir sınıf sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, bir Excel dosyasını yönetmek için geniş bir yöntem yelpazesi sağlar. Bölme görünümlerini uygulamak için, [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının [Split](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) yöntemini kullanın. Bölmeleri kaldırmak için, [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) yöntemini kullanın.

Örnekte, basit bir şablon dosyası kullanılır, ardından ilk çalışma sayfasındaki bir hücreye bölme bölmeleri özelliği uygulanır. Güncellenmiş dosya kaydedilir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
#### **Pencereleri Kaldırma**
[RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) yöntemini kullanarak bölme bölmeleri kaldırın.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
