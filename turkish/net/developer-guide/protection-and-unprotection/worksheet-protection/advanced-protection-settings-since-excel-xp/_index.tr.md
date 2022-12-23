---
title: Excel XP'den bu yana Gelişmiş Koruma Ayarları
type: docs
weight: 30
url: /tr/net/advanced-protection-settings-since-excel-xp/
---
{{% alert color="primary" %}}

Excel 2002 veya XP'nin piyasaya sürülmesinden bu yana Microsoft, birçok gelişmiş koruma ayarı ekledi.

{{% /alert %}}

## **Giriş**

Bu koruma ayarları, kullanıcıların şunları yapmasına izin verir veya kısıtlar:

- Satırları veya sütunları silin.
- İçeriği, nesneleri veya senaryoları düzenleyin.
- Hücreleri, satırları veya sütunları biçimlendirin.
- Satırları, sütunları veya köprüleri ekleyin.
- Kilitli veya kilidi açılmış hücreleri seçin.
- Pivot tabloları ve çok daha fazlasını kullanın.

Aspose.Cells, Excel XP veya sonraki sürümleri tarafından sunulan tüm gelişmiş koruma ayarlarını destekler.

### **Excel XP ve Sonraki Sürümleri Kullanan Gelişmiş Koruma Ayarları**

Excel XP'de bulunan koruma ayarlarını görüntülemek için:

1.  itibaren**Araçlar** menü, seç**Koruma** bunu takiben**Sayfayı Koruyun**. Bir diyalog görüntülenecektir.

Excel 2016'da bulunan koruma ayarlarını görüntülemek için

1.  itibaren**Dosya** menü, seç**Çalışma Kitabını Koru** bunu takiben**Geçerli Sayfayı Koru**.
1.  seçin**Sayfayı Koruyun** içinde**Gözden geçirmek** Menü.

Yukarıda belirtilen adımların ardından, çalışma sayfası özelliklerine izin verebileceğiniz veya kısıtlayabileceğiniz veya çalışma sayfasına bir parola uygulayabileceğiniz bir iletişim kutusu gösterilecektir.

### **Aspose.Cells Kullanarak Gelişmiş Koruma Ayarları**

Aspose.Cells, tüm gelişmiş koruma ayarlarını destekler.

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)sınıf.

 bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Koruma**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) Bu gelişmiş koruma ayarlarını uygulamak için kullanılan özellik. bu[**Koruma**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) mülkiyet aslında bir nesnedir[**Koruma**](https://reference.aspose.com/cells/net/aspose.cells/protection)kısıtlamaları devre dışı bırakmak veya etkinleştirmek için çeşitli Boolean özelliklerini kapsayan sınıf.

Aşağıda küçük bir örnek uygulama var. Bir Excel dosyasını açar ve Excel XP ve sonraki sürümleri tarafından desteklenen gelişmiş koruma ayarlarının çoğunu kullanır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

 lütfen aramayın[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf'[**Korumak**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) yöntemini kullanırken[**Koruma**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)Emlak. Ayrıca, gelişmiş koruma ayarları yalnızca Excel XP ve sonraki sürümler tarafından desteklendiğinden, dosyayı Excel97To2003 veya Xlsx biçiminde kaydedin.

{{% /alert %}}

### **Cell Kilitleme Sorunu**

Kullanıcıların hücreleri düzenlemesini kısıtlamak istiyorsanız, herhangi bir koruma ayarı uygulanmadan önce hücreler kilitlenmelidir. Aksi takdirde, çalışma sayfası korumalı olsa bile hücreler düzenlenebilir. Microsoft Excel XP'de hücreler aşağıdaki iletişim kutusu aracılığıyla kilitlenebilir:

|**Excel XP'de hücreleri kilitlemek için iletişim kutusu**|
|:- |
|![yapılacaklar:resim_alternatif_metin](advanced-protection-settings-since-excel-xp_1.png)|

Aspose.Cells API kullanarak da hücreleri kilitlemek mümkündür. Her hücre alabilir[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Boole özelliği içeren biçimlendirme,[**Kilitli**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Yı kur[**Kilitli**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) mülkiyet**doğru** veya**YANLIŞ** hücreyi kilitlemek veya kilidini açmak için

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
