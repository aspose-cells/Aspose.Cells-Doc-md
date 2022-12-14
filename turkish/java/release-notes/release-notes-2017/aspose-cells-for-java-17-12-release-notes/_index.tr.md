---
title: Aspose.Cells for Java 17.12 Sürüm Notları
type: docs
weight: 10
url: /tr/java/aspose-cells-for-java-17-12-release-notes/
---
{{% alert color="primary" %}} 

Bu sayfa Aspose.Cells for Java 17.12 için sürüm notları içerir.

{{% /alert %}} 

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42479|İyileştirilmiş LoadDataFilterOptions numaralandırma ve belirsizlik kaldırıldı|Artırma|
|CELLSJAVA-42460|CSV Biçimi - D2 ve D6, IsString'dir ancak Aspose.Cells, bunları IsNumeric olarak kabul eder|Artırma|
|CELLSJAVA-42457|XLSX PDF'ye dönüştürüldüğünde, grafiklerdeki bazı satırlar farklı|Böcek|
|CELLSJAVA-42465|Bazı CSS sınıf bildirimleri çıktı HTML'sinde ön ekli değildir|Böcek|
|CELLSJAVA-42456|HTML çıktısı kaynakla tutarsız - Excel'den HTML'ye dönüştürme|Böcek|
|CELLSJAVA-42478|HSQL DB'den uzun değer almak bir istisna oluşturuyor|Böcek|
|CELLSJAVA-42466|Denklem, çıktı PDF'sinde iyi işlenmemiş|Böcek|
|CELLSJAVA-42475|Çıktı PDF'sinde grafik eksik|Böcek|
|CELLSJAVA-42459|Çıktı PDF'sinde/resminde grafiğin veri etiketleri eksik|Böcek|
|CELLSJAVA-42453|Grafik görüntüsü aynı değil Microsoft Excel|Böcek|
|CELLSJAVA-42447|Veri etiketleri, çıktı HTML dosyası biçiminde yanlış görüntüleniyor|Böcek|
|CELLSJAVA-42481|Açılan kutu adını ayarla, kaynak Excel dosyası için çalışmaz ancak Microsoft Excel tarafından yeniden kaydedilirse sorunsuz çalışır|Böcek|
|CELLSJAVA-42476|Microsoft Excel Makro Etkin Çalışma Sayfası (.xlsm), Aspose.Cells API'leri aracılığıyla açılıp kaydedildikten sonra bozuluyor|Böcek|
|CELLSJAVA-42470|Bir Onay Kutusu bağlantılı hücrenin ayarlanması, MS Excel'in çıktı dosyasını içine açarken bir hata mesajı istemesine neden olur|Böcek|
|CELLSJAVA-42462|XLSB dosyasını okumak, NullPointerException'ı atar|İstisna|
## **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**
Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for Java numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.
### **HtmlSaveOptions.TableCssId özelliğini ekler**
css adının tr,col,td gibi öneklerini alır ve ayarlar, bunlar belirli TableCssId özniteliğine sahip tablo öğesinde bulunur. Varsayılan değer "" şeklindedir.
### **Cell.FormulaLocal özelliğini ekler**
Ayırıcılar, yerleşik Adlar, işlev adları vb. için farklı yerel ayarlara göre değişebilen yerel biçimlendirilmiş formülü alır. Bu yerel ayarlar bağımlıdır.
### **GlobalizationSettings.GetLocalFunctionName(string standardName) yöntemini ekler**
Verilen standart işlev adına göre yerel bağımlı işlev adını alır.
### **GlobalizationSettings.GetLocalBuiltInName(string standardName) yöntemini ekler**
Verilen standart metne göre yerleşik Ad için yerel ayara bağlı metni alır.
### **GlobalizationSettings.ListSeparator özelliğini ekler**
Liste, işlev parametreleri, ...vb. için ayırıcıyı alır.
### **GlobalizationSettings.RowSeparatorOfFormulaArray özelliğini ekler**
Formüldeki dizi verilerindeki satırlar için ayırıcıyı alır.
### **GlobalizationSettings.ColumnSeparatorOfFormulaArray özelliğini ekler**
Dizinin formüldeki satır verilerindeki öğeler için ayırıcıyı alır.
### **HtmlSaveOptions.ExportWorksheetCSSSeparately özelliğini ekler**
Çalışma sayfası css'sinin ayrı ayrı dışa aktarılıp aktarılmadığını gösterir. Varsayılan değer yanlıştır.
### **LoadDataFilterOptions.None'un yerine LoadDataFilterOptions.Structure ekler**
LoadDataFilterOptions.None belirsiz yönergeler verdi ve kafa karışıklığına neden oldu. Çalışma sayfası verileri için hiçbir şey yüklemediğini belirtmek için tasarlanmıştır. Şimdi yenisini (üye) sağlıyoruz, yani onun yerini alacak Yapı.
### **DataLabelShapeType sıralamasını ekler**
Bir grafik için kullanılacak önceden ayarlanmış şekil geometrisini belirtir.
### **DataLabels.ShapeType özelliği ekler**
Veri etiketinin şekil türünü alır veya ayarlar.
### **Bazı eskimiş FileFormatType'ı siler**
Eski dosya biçimi türlerini siler.
### **WorksheetCollection.RevisionLogs özelliği, RevisionLogCollection sınıfı ve Revisions.RevisionLog sınıfı eklendi**
Revizyon günlüğü ayarını alır.
### **Enum MsoDrawingType.WebExtension ekler**
Web uzantısı şeklini temsil eder.


### **Kullanım Örnekleri**
Lütfen Aspose.Cells Wiki belgelerine eklenen yardım konularının listesini kontrol edin:

- [Veriler Çok Büyükse Akıllı İşaretleyici Verilerini Diğer Çalışma Sayfalarına Otomatik Olarak Doldur](/cells/tr/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Çalışma Sayfası CSS'sini Çıktı HTML'sinde Ayrı Olarak Dışa Aktarın](/cells/tr/java/export-worksheet-css-separately-in-output-html/)
- [Cell.FormulaLocal'ı Excel VBA Range.FormulaLocal'a benzer şekilde uygulayın](/cells/tr/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/)
- [Tablo Elemanları Stillerini HtmlSaveOptions.TableCssId özelliğine sahip Önek](/cells/tr/java/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Excel'i PDF'ye dönüştürürken Office Eklentilerini İşleyin](/cells/tr/java/render-office-add-ins-while-converting-excel-to-pdf/)
- [Grafiğin Veri Etiketlerinin Şekil Türünü Ayarlama](/cells/tr/java/set-the-shape-type-of-data-labels-of-chart/)
- [Paylaşılan Çalışma Kitabında Revizyon Günlüklerinin Geçmişini Koruyan Güncelleme Günleri](/cells/tr/java/update-days-preserving-history-of-revision-logs-in-shared-workbook/)
