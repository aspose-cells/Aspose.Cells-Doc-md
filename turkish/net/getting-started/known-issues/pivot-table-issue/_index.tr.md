---
title: Pivot Tablo Sorunu
type: docs
weight: 50
url: /tr/net/pivot-table-issue/
---
## **Belirti**
"Oluşturulan excel dosyasını IE'nin "Aç" butonundan açmaya çalıştım. Excel, bir excel şablonu okunarak oluşturulmuştur. Aç butonuna tıkladığımda açılıyor ve aynı anda bir pencere açılıyor. "Özet Tablo Kaynak dosyası açılamıyor..." diyen hata mesajı.

Ancak oluşturulan excel dosyasını "Kaydet" düğmesini kullanarak kaydettiğimde ve kaydedilen yoldan dosyadan açtığımda, düzgün ve hatasız açılıyor. "
### **Çözüm**
Aspose.Cells, pivot veri formatını ayarlar ve çalışma kitabı MS Excel'de açıldığında MS Excel'i veri kaynağına dayalı olarak pivot tablo raporu ve diğer hesaplama görevlerini oluşturmaya zorlar. Yani biri kullanmalı**SaveType.OpenInBrowser** kullanmak yerine**SaveType.OpenInExcel**Bunun birçok nedeninden biri, çıktı oluşturulan dosyayı indirme iletişim kutusunun "Aç" düğmesini kullanarak çalışma zamanında MS Excel'e kaydederken OpenInExcel seçeneğini kullandığınızda, MS Excel'in pivot tablo raporu oluşturmak için Çalışma Kitabı verilerini ayrıştıramamasıdır. Bu, dosya adı sorunundan kaynaklanır. Orijinal ada "dosyaAdı" + "[1]" + ".xls" yapmak için "[1]" gibi bir şey eklediğinden IE'nin rutinidir ve bu nedenle orijinal ada hiçbir şey eklemez. Aspose.Cells ile yapın. (yani... "fileName" + "[1]" + ".xls" yapmak için her zaman "[1]" ekler ve fileName.xls gibi değil). Kısacası, bir dosya pivot tablo içeriyorsa, OpenInExcel SaveType seçeneği kullanılarak açılamaz ve bu, dosyayı sıfırdan oluşturursanız veya pivot tablo raporu oluşturmak için kaynak veriler için herhangi bir şablon dosyası kullanıyorsanız, her ikisi için de geçerli olacaktır. Bu nedenle, pivot tablo raporu oluşturmak için dosyada pivot tablo verileri varsa OpenInBrowser SaveType seçeneğini kullanmalısınız.

Workbook.Save() yöntemini kullanıyorsanız, kodunuzu değiştirmeli ve SaveType.OpenInBrowser'a güncellemelisiniz.

Veya kodunuzda "ek" seçeneğini kullanıyorsanız, kodunuzu "satır içi" kullanmak için düzenleyin. yani



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
