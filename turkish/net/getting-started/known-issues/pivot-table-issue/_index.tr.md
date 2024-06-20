---
title: Pivot Tablo Sorunu
type: docs
weight: 50
url: /tr/net/pivot-table-issue/
---

## **Belirti**
"Oluşturulan excel dosyasını IE'nin "Aç" düğmesinden açmayı denedim. Excel, bir excel şablonunu okuyarak oluşturuldu. Aç düğmesini tıklarken açılıyor ve aynı anda "Pivot Tablo Kaynak dosyası açılamıyor....." şeklinde bir hata mesajı çıkıyor.

Ancak "Kaydet" düğmesini kullanarak oluşturulan excel dosyasını kaydedip dosyanın kaydedilen yolundan açtığımda herhangi bir hata olmadan düzgünce açılıyor.
### **Çözüm**
Aspose.Cells, Workbook'ün MS Excel'e açıldığında veri kaynağına dayalı pivot tablo raporu oluşturmaya ve diğer hesaplama işlemlerini yapmaya zorlamak için pivot veri formatını ayarlar ve MS Excel'i zorlar. Bu nedenlerden biri, indirme iletişim kutusunun "Aç" düğmesiyle çalışma zamanında MS Excel'e çıktı oluştururken OpenInBrowser kullanılmadığında MS Excel, pivot tablo raporu oluşturmak için Workbook verisini ayrıştıramaz. Bu, dosya adı sorunundan kaynaklanır, IE'nin rutinine dosyaya "özgün dosya adı" + "[1]" + ".xls" şeklinde bir şey ekleyerek "fileName" + "[1]" + ".xls" haline getirir ve bu nedenle Aspose.Cells ile hiçbir ilgisi yoktur (yani .... her zaman "fileName" + "[1]" + ".xls" ekler ve dosya adı gibi değil). Kısacası, bir dosya pivot tablo içeriyorsa, OpenInExcel SaveType seçeneği kullanılarak açılamaz ve bu hem sıfırdan dosya oluşturursanız hem de pivot tablo raporu oluşturmak için herhangi bir şablon dosyası kullanıyorsanız geçerlidir. Bu nedenle, dosyada pivot tablo verisi varsa pivot tablo raporu oluşturmak için OpenInBrowser SaveType seçeneğini kullanmalısınız.

Kodunuzu değiştirin ve Workbook.Save() yöntemini kullanarak SaveType.OpenInBrowser'a güncelleyin.

Veya kodunuzu "attachment" seçeneğini kullanıyorsanız "inline" olarak düzenleyin. yani



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
