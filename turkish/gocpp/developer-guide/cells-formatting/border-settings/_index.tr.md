---
title: Golang ile Kenarlık Ayarları (Border Settings)
linktitle: Kenar Ayarları
description: Hücrelerin kenar stilini ve rengini ayarlamak için Aspose.Cells kütüphanesini nasıl kullanacağınızı gösterir. Kenarın genişliğini, stilini ve rengini ayarlayarak hücrelerin görünümünü ve görünüşünü kontrol edebilirsiniz.
keywords: Aspose.Cells, Hücre Kenarlık Ayarları, C++, Kenar Genişliği, Kenar Stili, Kenar Rengi
type: docs
weight: 40
url: /tr/go-cpp/cells-border-settings/
---

## **Hücrelere Kenarlık Eklemek**

Microsoft Excel, hücreleri kenarlıklar ekleyerek biçimlendirmeye izin verir. Kenarlık tipi, eklendiği konuma göre değişir. Örneğin, üst kenarlık, hücrenin üst konumuna eklenmiş bir kenarlıktır. Kullanıcılar ayrıca kenarlıkların çizgi stilini ve rengini değiştirebilir.

Aspose.Cells ile geliştiriciler, sınırlar ekleyebilir ve bunları Microsoft Excel'de olduğu gibi esnek bir şekilde özelleştirebilirler.

### **Hücrelere Kenarlık Eklemek**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, Excel dosyasındaki her sayfaya erişim sağlayan [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir sayfa, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunu sağlar. [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının bir nesnesini temsil eder.

Aspose.Cells, [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) metodunu [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfında sağlar. [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) yöntemi, hücre biçimlendirme stilini ayarlamak için kullanılır. [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) sınıfı, hücrelere kenarlık eklemek için özellikler sağlar.

#### **Bir Hücreye Sınır Ekleme**

Geliştiriciler, bir hücreye kenarlık eklemek için [**Style**](https://reference.aspose.com/cells/go-cpp/style/) nesnesinin [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) koleksiyonunu kullanabilir. Kenarlık türü, [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) koleksiyonuna indeks olarak geçirilir. Tüm kenarlık türleri önceden tanımlanmış [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/) enum'unda yer alır.

**Sınır numaralandırması**

| **Kenar Tipleri** | **Açıklama** |
|------------------|-----------------|
| AltKenarlık     | Alt kenar çizgisi |
| DiagonalAşağı      | Sol üstten sağ alt çapraz çizgi |
| DiagonalYukarı | Sol alttan sağ üst çapraz çizgi |
| SolKenarlık    | Sol kenar çizgisi |
| SağKenarlık   | Sağ kenar çizgisi |
| ÜstKenarlık     | Üst kenar çizgisi |

[**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) koleksiyonu tüm kenarlıkları depolar. [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) koleksiyonundaki her kenarlık, [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/) nesnesi tarafından temsil edilir ve bu nesne, sırasıyla [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/) ve [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/) özellikleri ile kenarlığın çizgi rengi ve stilini ayarlamayı sağlar.

Bir kenarlığın çizgi rengini ayarlamak için, Color enum'undan bir renk seçin ve bunu Kenarlık nesnesinin Color özelliğine atayın.

Kenarın çizgi stili, [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/) enum'undan bir çizgi stili seçilerek ayarlanır.

**HücreSınırTürü numaralandırması**

| **Çizgi Stilleri**       | **Açıklama**               |
|------------------------|-------------------------------|
| DashDot               | İnce kesik çizgi         |
| DashDotDot            | İnce kesik noktali çizgi     |
| Dashed                | Kesik çizgi                  |
| Dotted                | Noktalı çizgi                  |
| Double                | Çift çizgi                  |
| Hair                  | Saç çizgisi                     |
| MediumDashDot         | Orta kalınlıkta kesik çizgi       |
| MediumDashDotDot      | Orta kalınlıkta kesik noktali çizgi   |
| MediumDashed          | Orta kalınlıkta kesik çizgi            |
| None                  | Hiçbir çizgi                      |
| Medium                | Orta kalınlıkta çizgi                  |
| SlantedDashDot        | Eğik orta kalınlıkta kesik çizgi |
| Thick                 | Kalın çizgi                   |
| Thin                  | İnce çizgi                    |

Çizgi stillerinden birini seçin ve ardından onu [**Border**](https://reference.aspose.com/cells/go-cpp/border/) nesnesinin [**GetLineStyle()**](https://reference.aspose.com/cells/go-cpp/border/getlinestyle/) özelliğine atayın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings.go" >}}
{{% alert color="primary" %}}

Her iki çizgi stili ve rengi aynı anda ayarlamalısınız. İki çapraz kenar çizgisi aynı çizgi stiline ve renge sahip olmalıdır.

{{% /alert %}}

#### **Hücre Aralığına Sınırlar Ekleme**

Sadece bir hücre yerine hücre aralığına da sınırlar eklemek mümkündür. Bunu yapmak için önce, [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/) koleksiyonunun [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange/) yöntemini çağırarak bir hücre aralığı oluşturun. Aşağıdaki parametreleri alır:

- İlk Sütun, aralığın ilk sütunu.
- İlk Sütun, aralığın ilk sütunu.
- Satır Sayısı, aralıktaki satır sayısı.
- Sütun Sayısı, aralıktaki sütun sayısı.

[**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/) yöntemi, belirtilen hücre aralığını içeren bir [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) nesnesi döner. [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) nesnesi, aşağıdaki parametreleri alan bir [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/) yöntemi sağlar ve hücre aralığına sınır ekler:

- **Sınır Türü**, [**BorderType**](https://reference.aspose.com/cells/go-cpp/bordertype/) enumerasyonundan seçilen sınır tipi.
- **Çizgi Stili**, sınır çizgi stili, [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/) enumerasyonundan seçilir.
- **Renk**, Renk sıralamasından seçilen çizgi rengi.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings-1.go" >}}
