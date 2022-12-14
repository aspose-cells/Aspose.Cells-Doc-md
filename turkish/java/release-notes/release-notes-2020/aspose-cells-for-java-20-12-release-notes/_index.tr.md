---
title: Aspose.Cells for Java 20.12 Sürüm Notları
type: docs
weight: 1
url: /tr/java/aspose-cells-for-java-20-12-release-notes/
---
{{% alert color="primary" %}}

 Bu sayfa için sürüm notları içerir[Aspose.Cells for Java 20.12](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.12/).

{{% /alert %}}

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43367|ISFORMULA işlevinin hesaplanmasını destekler|
|CELLSJAVA-43338|Excel dosyasını PDF'ye dönüştürürken çıktı farkı|
|CELLSJAVA-43346|Pivot tablo sayfa filtrelerine 12'den fazla alan eklenirken çıktı dosyası bozuk|
|CELLSJAVA-43351|Başlık tablosunun arka plan rengi pdf'ye dönüştürülürken doğru değil|
|CELLSJAVA-43358|HTML'den Excel'e dönüştürme sırasında metin eksik|
|CELLSJAVA-43341|LightCellsDataProvider ile CSV'yi dışa aktarırken fazladan boş sütunlar|
|CELLSJAVA-43352|PDF'ye dönüştürülen Excel dosyası çok sayıda sorun oluşturuyor|
|CELLSJAVA-43339|Kaynak dosya pdf'ye dönüştürülürken görüntü yanlış yerleştirilmiş|
|CELLSJAVA-43340|XLS'den PDF'e dönüştürmede eksik içerikler|
|CELLSJAVA-43336| Grafik açıklama girişleri çok sola işleniyor|
|CELLSJAVA-43356|Grafikteki boş değerler/boşluklar, 2 değer arasındayken dikkate alınmaz|
|CELLSJAVA-43344|Geçerli Kullanıcı adı, son yorumun yazarı olarak gösterilir|
|CELLSJAVA-43349|Gizli satırlar, XML'den XLS/XLSX'e dönüştürmede korunmaz|
|CELLSJAVA-43361|xls'den xlsx'e dönüştürmede yanlış hücre rengi|
|CELLSJAVA-43366|SetAsTotal özelliği güncellenmiyor|
|CELLSJAVA-43348|XLSB'den PDF'e dönüştürme: CellsException: -2147483648|
|CELLSJAVA-43343| Şekil için seçili bir öğeye sahip olmayan bir dosyayı PDF'ye dışa aktarırken istisna|

## **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**

Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for Java numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.

### **Cell.SetDynamicArrayFormula(string arrayFormula, FormulaParseOptions seçenekleri, bool hesapla) yöntemini ekler.**

Dinamik dizi formülünü ayarlamayı ve mümkünse komşu hücrelere yaymayı destekler.

### **Workbook.RefreshDynamicArrayFormulas(bool hesapla) yöntemini ekler.**

Dinamik dizi formüllerini yenilemeyi ve mevcut verilere göre komşu hücrelere yayılmayı destekler.

### **Cell.Comment özelliği ekler.**

Hücrenin yorumunu alır.

### **HtmlSaveOptions.ExportExtraHeadings özelliğini ekler**

Metin uzunluğu maksimum görüntüleme sütunundan daha uzun olduğunda fazladan başlıkların dışa aktarılıp aktarılmayacağını gösterir.
Varsayılan değer yanlıştır. Html dosyasını excel'e aktarmak istiyorsanız, lütfen varsayılan değeri koruyun.

### **HtmlSaveOptions.ExportFormula özelliği ekler**

Dosyayı html'ye kaydederken formülün dışa aktarılıp aktarılmadığını gösterir. Varsayılan değer doğrudur.
Çıktı html'sini excel'e aktarmak istiyorsanız, lütfen varsayılan değeri koruyun.

### **HtmlSaveOptions.MergeEmptyTdForcely özelliğini ekler**

Dosyayı html'ye dışa aktarırken boş TD öğesinin zorla birleştirilip birleştirilmediğini gösterir.
Değer true olarak ayarlandıktan sonra html dosyasının boyutu önemli ölçüde azaltılacaktır. Varsayılan değer yanlıştır.
Html dosyasını excel'e aktarmak veya dosyayı html'ye kaydederken mükemmel ızgara çizgilerini dışa aktarmak istiyorsanız,
lütfen varsayılan değeri koruyun.

### **LoadOptions.AutoFilter özelliğini ekler**

Dosyaları yüklerken verilerin otomatik olarak filtrelenip filtrelenmediğini gösterir.
Bazen otomatik filtreleme ayarlanmış olmasına rağmen, ilgili satırlar dosyada gizlenmez. Artık yalnızca SpreadSheetML dosyası için çalışır.

### **WorkbookSettings.Author özelliğini ekler**

Çalışma kitabının yazarını alır ve ayarlar.

### **MultipleFilterCollection.Add() yöntemini ekler.**

Otomatik filtrenin filtre dizesini ekler.
