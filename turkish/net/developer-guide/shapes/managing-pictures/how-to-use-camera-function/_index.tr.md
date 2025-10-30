---
title: Aralık için Kamera Ekleme Yöntemi
type: docs
weight: 10
url: /tr/net/how-to-add-camera-for-range/
description: Bu makale, Aspose.Cells for .NET API içerik aralığına kamera ekleme nasıl yapılacağını tanıtacaktır.
keywords: Kamera Fonksiyonunun Kullanımı, Aralık içeriğine Kamera nasıl eklenir, Kamera aracını kullanma, Excel de Kamera Fonksiyonu, Aspose.Cells for .NET de Kamera Fonksiyonunun Kullanımı
---

## **Olası Kullanım Senaryoları**
Excel'deki Kamera aracı, gizli ama güçlü bir özelliktir ve herhangi bir hücre aralığının canlı, bağlantılı bir anlık görüntüsünü oluşturmanızı sağlar. İşte neden ve ne zaman kullanabileceğiniz.

Kamera Aracı'nın ne yaptığı:
1. Seçilen hücre aralığının "resmini" çeker.
2. "Resim" canlı bir bağlantıdır — kaynak hücreler değişirse, görüntü otomatik olarak güncellenir.
3. Resmi herhangi bir yere taşıyabilir veya yeniden boyutlandırabilirsiniz; hatta başka bir sayfaya da taşıyabilirsiniz.


## **Excel'de Kamera Fonksiyonu Nasıl Kullanılır**
İşte Excel'de Kamera Aracı'nı kullanmak için adım adım bir rehber — hücre aralıklarının canlı, dinamik görüntülerini oluşturmanın güçlü bir yolu.

### Kamera Aracını Etkinleştir

Kamera aracı varsayılan olarak gizlidir. İşte nasıl eklenir:

1. Excel'in Üst Sol Köşesindeki Hızlı Erişim Çubuğu'ndaki aşağı ok düğmesine tıklayın.
2. Daha Fazla Komut.... seçeneğini seçin.
3. Diyalog kutusunda: “Komutları Seç” açılır menüsünden Komutları Şeritte Olmayanlar’ı seçin. Aşağı kaydırın ve Kamera'yı seçin. Ekle’ye tıklayarak araç çubuğuna ekleyin.
4. Tamam’a tıklayın. Artık araç çubuğunuzda küçük bir kamera simgesi göreceksiniz.

### Kamera Aracını Kullanma
1. Yakalamak istediğiniz hücre aralığını seçin (örneğin, A1:C5).
2. Hızlı Erişim Çubuğu'ndaki Kamera simgesine tıklayın.
3. İmleciniz çapraz çizgiye dönüşecektir.
4. Görüntüyü yerleştirmek istediğiniz sayfa bölümüne tıklayın. Seçilen aralığın canlı resmi eklenir.

### Dinamik Bağlantı
Görsel orijinal hücrelere bağlıdır. Kaynak aralıkta değerler veya biçimlendirme değiştiğinde, görsel otomatik olarak güncellenir.


## **Aspose.Cells for .NET'de Aralık için Kamera Ekleme Nasıl Yapılır**
Aspose.Cells, hücre veya aralık içeriğini bir resim şekli olarak görüntülemeyi destekler. Görüntüyü, görüntülemek istediğiniz verileri içeren hücre veya aralığa bağlayabilirsiniz. Hücre veya aralık grafik nesnesine bağlı olduğu için, bu hücrede veya aralıkta yaptığınız değişiklikler otomatik olarak grafik nesnesinde görünür. 

İşte Aspose.Cells for .NET'de [örnek dosya](camera.xlsx) kullanılarak Kamera Fonksiyonunun nasıl kullanılacağına dair temel bir örnek:

1. Örnek dosyayı [Çalışma kitabı](https://apireference.aspose.com/cells/net/aspose.cells/workbook) sınıfını kullanarak yükleyin.
1. Koleksiyonun [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) metodunu çağırarak çalışma sayfasına bir resim ekleyin ( [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nesnesinde kapsüllenmiş). 
1. [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) nesnesinin [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) özniteliğini kullanarak hücre aralığını belirtin.
1. Çalışma sayfasında seçilen şekillerin değerini güncelleyin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Shapes-how-to-use-camera-function.cs" >}}

## **Sonuç Çıktısı**
Aşağıdaki ekran görüntüsü, Aspose.Cells for .NET tarafından oluşturulan hücre aralığı (A1:E12) kamerayı içermektedir ve çıktı Excel dosyasında gösterilmektedir.
<br>
Veri eklemeden önce:
<br>
<img src="1.png" width=70% />
<br>
Veri eklendikten sonra:
<br>
<img src="2.png" width=70% />
{{< app/cells/assistant language="csharp" >}}
