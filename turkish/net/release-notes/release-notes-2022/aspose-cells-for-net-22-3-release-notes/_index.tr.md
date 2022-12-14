---
title: Aspose.Cells for .NET 22.3 Sürüm Notları
type: docs
weight: 10
url: /tr/net/aspose-cells-for-net-22-3-release-notes/
---
{{% alert color="primary" %}}

 Bu sayfa için sürüm notları içerir[Aspose.Cells for .NET 22.3](https://www.nuget.org/packages/Aspose.Cells/22.3.0).

{{% /alert %}}

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSNET-50375|PivotField'ı seçilen satır/sütundaki değerler aracılığıyla sıralamayı destekler|
|CELLSNET-50559|Hücrenin yapraklarını yinelemeli olarak alma desteği|
|CELLSNET-50512|Tanımlanan ad değiştirildiğinde ve hesaplama zinciri etkinleştirildiğinde, tanımlanan ada başvuran hücreleri yeniden hesaplama desteği|
|CELLSNET-50403|SaveFormat.Ots ve SaveFormat.Xlt'yi ekleyin|
|CELLSNET-50422|Boders içinde destek ayarı|
|CELLSNET-50342|Pivot tablo yenileme sırasında sıralanmıyor|
|CELLSNET-50451|Çalışma sayfası silindiğinde Dilimleyiciler silinir|
|CELLSNET-50462|Regresyon: Hücre aralığını kopyaladıktan sonra formüller kayboluyor|
|CELLSNET-50545| Koşullu biçimlendirilmiş alanlar doğru renkte değil|
|CELLSNET-50565|Formüller doğru hesaplanmadı|
|CELLSNET-50309|Aralıktan PNG'ye: çıktı beklendiği gibi değil|
|CELLSNET-50334|Regresyon: XLS'den PDF'e: başlık doğru şekilde oluşturulmadı|
|CELLSNET-50367|.XLSX'i PDF'ye dönüştürmek uzun zaman alıyor ve fazladan sayfalar üretiyor|
|CELLSNET-50401|Satır öğeleri tarafından takip edilen sayısal değerler veya sayılar, elde edilen pdf'de görünmez|
|CELLSNET-50478|Workbook.ExportXml, Tablo verilerinin yalnızca ilk satırını döndürür|
|CELLSNET-50507|Xml Import, şablonda önceden gizlenmiş sütunları gösterir|
|CELLSNET-50554|İçerik, Excel'den PDF'e dönüştürmede düzgün şekilde oluşturulmuyor|
|CELLSNET-50316|Kaydırılmış Metinler, PDF oluşturulurken Grafiklerde çalışmaz|
|CELLSNET-50411|Grafiğin yatay eksen etiketleri çıktı PDF'sinde düzgün şekilde oluşturulmuyor|
|CELLSNET-50341|Daralt ve Genişlet çok düzeyli gruplarla ilgili sorun|
|CELLSNET-50368| ODS'den PDF'e dönüştürme yanlış|
|CELLSNET-50377|XLS dosyasında özel "Metin" biçimlendirmesi uygulanmaz|
|CELLSNET-50380| ImportTableOptions.IsHtmlString özelliği, bağlantıları doğru şekilde vermiyor|
|CELLSNET-50418|Çalışma kitabına HTML yükle çalışmıyor|
|CELLSNET-50494|Çıkış XLSX dosyasındaki koşullu olarak biçimlendirilmiş hücreler için renk sorunu|
|CELLSNET-50563|.NET 6.0 uygulamasında katıştırılmış lisansı Tek dosya oluştur olarak ayarlarken sorun|
|CELLSNET-50585|URL'li harici bağlantılar için eğik çizgi yok, ters eğik çizgi var|
|CELLSNET-50390| System.ArgumentException: JSON verilerini tablo olarak içe aktarırken satır numarası veya sütun numarası sıfır olamaz|
|CELLSNET-50555| Bir hücrenin formülünü almaya çalışırken ArgumentOutOfRangeException|

## **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**

Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for .NET numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.

### **HtmlSaveOptions.ExcludeUnusedStyles'ın varsayılan değerini değiştirir.**

Html dosyalarını kaydederken, eski sürümler için, bu özelliğin değeri ne olursa olsun, havuzda çok sayıda stil nesnesi olduğunda, kullanılmayan stilleri bazen otomatik olarak kaldırırız. Oluşturulan html dosyaları için, kullanılmayan stilleri hariç tutmak, görsel efektleri etkilemeden dosya boyutunu küçültebilir. Dolayısıyla, bu sürümden, kaydetme davranışıyla tutarlı olması için bu özelliğin varsayılan değerini true yapıyoruz. Kullanıcının oluşturulan html için çalışma kitabındaki tüm stilleri tutması gerekiyorsa (kullanıcının çalışma kitabını daha sonra oluşturulan html'den geri yüklemesi gereken senaryo gibi), lütfen html'yi kaydederken bu özelliği false olarak ayarlayın.

### **Cell.GetLeafs(bool recursive) yöntemini ekler.**

Bir hücrenin tüm yapraklarını yinelemeli olarak almak için kullanıcıyı destekleyin.

### **Range.SetInsideBorders(BorderType, CellBorderType, CellsColor) yöntemini ekler.**

Menzil için iç sınırlar belirleme desteği.

### **SaveFormat.Ots,SaveFormat.Xlt ve LoadFormat.Ots numaralandırmasını ekler.**

ots ve xlt dosyalarını yüklemek ve kaydetmek için geliştirme.

### **FormulaSettings sınıfını ekler.**

Formülle ilgili tüm ayarları WorkbookSettings'ten ayırın ve bunları FormulaSettings olarak gruplandırın.

### **WorkbookSettings.FormulaSettings özelliğini ekler.**

Formüller için gruplandırılmış ayarları alır.

### **PivotItem.IsHideDetail özelliğini ekler.**

Pivot öğesinin ayrıntıyı gizleyip gizlemediğini alır ve ayarlar.

### **Eski WorkbookSettings.ReCalculateOnOpen özelliği.**

Lütfen bunun yerine WorkbookSettings.FormulaSettings.CalculateOnOpen'ı kullanın.

### **Eski WorkbookSettings.RecalculateBeforeSave özelliği.**

Lütfen bunun yerine WorkbookSettings.FormulaSettings.CalculateOnSave'i kullanın.

### **Eski WorkbookSettings.ForceFullCalculate özelliği.**

Lütfen bunun yerine WorkbookSettings.FormulaSettings.ForceFullCalculation'ı kullanın.

### **Eski WorkbookSettings.PrecisionAsDisplayed özelliği.**

Lütfen bunun yerine WorkbookSettings.FormulaSettings.PrecisionAsDisplayed kullanın.

### **Eski WorkbookSettings.CalcMode özelliği.**

Lütfen bunun yerine WorkbookSettings.FormulaSettings.CalculationMode'u kullanın.

### **Eski WorkbookSettings.Iteration özelliği.**

Lütfen bunun yerine WorkbookSettings.FormulaSettings.EnableIterativeCalculation'ı kullanın.

### **Eski WorkbookSettings.MaxIteration özelliği.**

Lütfen bunun yerine WorkbookSettings.FormulaSettings.MaxIteration kullanın.

### **Eski WorkbookSettings.MaxChange özelliği.**

Lütfen bunun yerine WorkbookSettings.FormulaSettings.MaxChange'i kullanın.

### **Eski WorkbookSettings.CalculationId özelliği.**

Lütfen bunun yerine WorkbookSettings.FormulaSettings.CalculationId kullanın.

### **Eski WorkbookSettings.CreateCalcChain özelliği.**

Lütfen bunun yerine WorkbookSettings.FormulaSettings.EnableCalculationChain'i kullanın.

### **Eski WorkbookSettings.CalcStackSize özelliği.**

Lütfen formülleri hesaplarken bunun yerine belirtilen yığın boyutuyla CalculationOptions kullanın.
