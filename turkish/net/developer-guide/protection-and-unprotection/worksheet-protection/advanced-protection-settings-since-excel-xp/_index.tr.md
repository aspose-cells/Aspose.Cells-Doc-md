---
title: Excel XP den beri Gelişmiş Koruma Ayarları
type: docs
weight: 30
url: /tr/net/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

2002 veya XP sürümüyle birlikte, Microsoft birçok gelişmiş koruma ayarı eklemiştir.

{{% /alert %}}

## **Giriş**

Bu koruma ayarları, kullanıcıların aşağıdakileri kısıtlamasına veya izin vermesini sağlar:

- Satırları veya sütunları sil.
- İçerik, nesneler veya senaryoları düzenle.
- Hücreleri, satırları veya sütunları biçimlendir.
- Satırları, sütunları veya hyperlinkleri ekle.
- Kilitli veya kilitsiz hücreleri seç.
- Özet tabloları ve çok daha fazlasını kullanın.

Aspose.Cells, Excel XP veya sonraki sürümlerinin sunduğu tüm gelişmiş koruma ayarlarını destekler.

### **Excel XP'de bulunan koruma ayarlarını görüntülemek için:**

**Araçlar** menüsünden **Koruma** ardından **Sayfayı Koru**'yu seçin.

1. **Araçlar** menüsünden **Koruma** ve ardından **Çalışma Sayfası Koru** seçin. Bir iletişim kutusu görüntülenecektir.

Excel 2016'da mevcut koruma ayarlarını görmek için

1. **Dosya** menüsünden **Çalışma Kitabını Koru** ve ardından **Mevcut Sayfayı Koru** seçin.
1. **İncele** menüsünde **Çalışma Sayfası Koru** seçin.

Yukarıda bahsedilen adımları takip etmek, çalışma sayfasına özelliklerin izin verilmesi veya kısıtlanması ya da çalışma sayfasına şifre uygulanması konusunda bir iletişim kutusu gösterecektir.

### **Aspose.Cells Kullanarak Gelişmiş Koruma Ayarları**

Aspose.Cells, tüm gelişmiş koruma ayarlarını destekler.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir.

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bu gelişmiş koruma ayarlarını uygulamak için kullanılan [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) özelliğini sağlar. Aslında, [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) özelliği, birkaç Boolean özelliği devre dışı bırakma veya etkinleştirme için kullanılan bir [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) sınıfı nesnesidir.

Aşağıda küçük bir örnek uygulama bulunmaktadır. Bir Excel dosyası açar ve Excel XP ve sonraki sürümler tarafından desteklenen gelişmiş koruma ayarlarının çoğunu kullanır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

Lütfen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) yöntemini kullanırken [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) özelliğini kullanmayın. Ayrıca, gelişmiş koruma ayarlarının sadece Excel XP ve sonraki sürümler tarafından desteklendiğinden, dosyayı Excel97To2003 veya Xlsx biçiminde kaydedin.

{{% /alert %}}

### **Hücre Kilitleme Sorunu**

Kullanıcıların hücreleri düzenlemesini kısıtlamak istiyorsanız, koruma ayarlarının uygulanmadan önce hücrelerin kilitli olması gerekir. Aksi takdirde, çalışma sayfası korunmuş olsa bile hücreler düzenlenebilir. Microsoft Excel XP'de, hücreler aşağıdaki iletişim kutusu aracılığıyla kilitleyebilir:

|**Excel XP'de Hücreleri Kilitlme İletişim Kutusu**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Aspose.Cells API'sı kullanarak da hücreleri kilitlemek mümkündür. Her hücre, bir Boole özelliği içeren [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) biçimlendirmesi alabilir. Hücreyi kilitlemek veya açmak için [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) özelliğini **true** veya **false** olarak ayarlayın.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
