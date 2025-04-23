---
title: Excel XP den beri Gelişmiş Koruma Ayarları
type: docs
weight: 30
url: /tr/python-net/advanced-protection-settings-since-excel-xp/
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

Aspose.Cells for Python via .NET, Excel XP veya sonraki sürümler tarafından sunulan tüm gelişmiş koruma ayarlarını destekler.

### **Excel XP'de bulunan koruma ayarlarını görüntülemek için:**

**Araçlar** menüsünden **Koruma** ardından **Sayfayı Koru**'yu seçin.

1. **Araçlar** menüsünden **Koruma** ve ardından **Çalışma Sayfası Koru** seçin. Bir iletişim kutusu görüntülenecektir.

Excel 2016'da mevcut koruma ayarlarını görmek için

1. **Dosya** menüsünden **Çalışma Kitabını Koru** ve ardından **Mevcut Sayfayı Koru** seçin.
1. **İncele** menüsünde **Çalışma Sayfası Koru** seçin.

Yukarıda bahsedilen adımları takip etmek, çalışma sayfasına özelliklerin izin verilmesi veya kısıtlanması ya da çalışma sayfasına şifre uygulanması konusunda bir iletişim kutusu gösterecektir.

### **Gelişmiş Koruma Ayarları Aspose.Cells for Python via .NET Kullanılarak**

Aspose.Cells for Python via .NET, tüm gelişmiş koruma ayarlarını destekler.

Aspose.Cells for Python via .NET, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her sayfaya erişim sağlayan [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ile temsil edilir.

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, bu gelişmiş koruma ayarlarını uygulamak için kullanılan [**protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection) özelliğini sağlar. Aslında, [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection) özelliği, birkaç Boolean özelliği devre dışı bırakma veya etkinleştirme için kullanılan bir [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection) sınıfı nesnesidir.

Aşağıda küçük bir örnek uygulama bulunmaktadır. Bir Excel dosyası açar ve Excel XP ve sonraki sürümler tarafından desteklenen gelişmiş koruma ayarlarının çoğunu kullanır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AdvancedProtectionSettings-1.py" >}}

{{% alert color="primary" %}}

Lütfen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**protect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect) yöntemini kullanırken [**protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection) özelliğini kullanmayın. Ayrıca, gelişmiş koruma ayarlarının sadece Excel XP ve sonraki sürümler tarafından desteklendiğinden, dosyayı Excel97To2003 veya Xlsx biçiminde kaydedin.

{{% /alert %}}

### **Hücre Kilitleme Sorunu**

Kullanıcıların hücreleri düzenlemesini kısıtlamak istiyorsanız, koruma ayarlarının uygulanmadan önce hücrelerin kilitli olması gerekir. Aksi takdirde, çalışma sayfası korunmuş olsa bile hücreler düzenlenebilir. Microsoft Excel XP'de, hücreler aşağıdaki iletişim kutusu aracılığıyla kilitleyebilir:

|**Excel XP'de Hücreleri Kilitlme İletişim Kutusu**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Python için Aspose.Cells via .NET API'sini kullanarak hücreleri kilitlemek mümkündür. Her hücre, [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) formatlamasıyla birlikte gelen Boolean özellik [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked)'i içerebilir. Hücreyi kilitlemek veya kilidini açmak için [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked) özelliğini **doğru** veya **yanlış** olarak ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-LockCell-1.py" >}}

