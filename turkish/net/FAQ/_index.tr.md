---
title: SSS
type: docs
weight: 100
url: /tr/net/faq/
---

## **Workbook.CalculateFormula'da System.StackOverFlowException Nasıl Düzeltilir?**
Bazı durumlarda, kullanıcılar Workbook.CalculateFormula yönteminde System.StackOverFlowException ile karşılaşabilir. Bu hata genellikle IIS'in varsayılan yığın boyutunun çok küçük olmasından kaynaklanır (yalnızca 265k). Bu hatayı düzeltebilirsiniz, yığınlama boyutu artırılmış başka bir iş parçacığı oluşturarak ve ardından Workbook.CalculateFormula ile ilgili kodu içine taşıyarak.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **Excel'i PDF'ye dönüştürürken çizgilerin kalınlığı ile ilgili sorun**
Bazı durumlarda, Excel dosyası PDF'ye dönüştürüldüğünde, çizgilerin kalınlığı çıktı PDF'inde farklı olabilir. Bu sorun, Aspose.Cells tarafından değil, ayarları 'Düz hat sanatını yumuşat' ve 'İnce çizgileri geliştir' olan **Adobe Reader** tarafından kaynaklanmaktadır. Bu seçeneklerin işaretli olmaması durumunda PDF düzgün görüntülenir.

Eğer '**Düz hat sanatını yumuşat**' ve '**İnce çizgileri geliştir**' seçeneğini kontrol ederseniz, çizgilerin kalınlığı farklı olacaktır. Aşağıdaki adımları nasıl yapılacağını görün:

- **Düzenle**'ye gidin
- **Tercihler**'i seçin
- **Sayfa Gösterimi** Kategorisinde **'Düz hat sanatını yumuşat'** ve **'İnce çizgileri geliştir'**'ı işaretleyin

**'Düz hat sanatını yumuşat'** ve **'İnce çizgileri geliştir'** seçeneğini işaretlemeyin, çizgilerin kalınlığı aynı olacaktır. Bu amaçla aşağıdaki adımları takip edin:

- **Düzenle**'ye gidin
- **Tercihler**'i seçin
- **Sayfa Gösterimi** Kategorisinde **'Düz hat sanatını yumuşat'** ve **'İnce çizgileri geliştir'**'ı işaretlemediğinizden emin olun
## **Büyük Elektronik Tabloları Yükleme Sırasında System.OutOfMemoryException Nasıl Düzeltilir?**
Büyük elektronik tabloları yüklerken Workbook oluşturucunun System.OutOfMemoryException fırlatabileceği olasılığı vardır. Bu hata, mevcut belleğin elektronik tabloyu tamamen yüklemek için yetersiz olduğunu gösterir. Bu nedenle, elektronik tabloların verimli bir şekilde yüklenmesine yardımcı olabilecek [Bellek Tercihleri](/cells/tr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/) etkinleştirilerek yüklenmelidir.

Aspose.Cells API'ları, elektronik tabloların yüklenmesi ve işlenmesi sırasında bellek tüketimini optimize etmek için Bellek Tercihleri sağlar. Bu seçenekler ayrıca, Workbook nesnesindeki dev veri setlerine sahip büyük elektronik tabloların etkili bir şekilde yüklenmesine yardımcı olur.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **Belirli bir Workbook için hangi yığın boyutunun gerektiğini belirleme**
Her ne kadar Aspose.Cells formül hesaplama motorunu geliştirmiş olsak da, çoğu durumda verilen bir şablon dosyası için tüm formüllerin başarıyla hesaplandığını belirtmek sizin için daha küçük yığın boyutunu belirtmeden. Ancak yine de bazen Workbook.CalculateFormula yönteminde StackOverFlowException kaçınılmaz olabilir. Kullanıcılar tarafından formül hesaplamalarını izlemek için yeni API'lar sağlarız. 'AbstractCalculationMonitor' adında bir sınıf ekledik ve bu sorunla başa çıkmak/izlemek için *CalculationOptions.CalculationMonitor* adında bir özellik sağladık.

Kullanıcılar, API'leri kullanarak yığın boyutunu kendileri denetleyebilirler. Lütfen unutmayın, her hücre için yığını kontrol etmek performansı büyük ölçüde düşürecektir. Referansınız için aşağıdaki örnek kod bölümüne bakın:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "CalculationMonitor-CustomStackTrace.cs" >}}

{{% alert color="primary" %}} 

Çalışma zamanında kullanılan yığın boyutunu almanın daha iyi bir yolu yoktur. Yukarıdaki verdiğimiz kod sadece bir örnektir. Performans kesinlikle önemli ölçüde düşecektir. Bu nedenle, kodun rekursif hücre sayısı belirli bir sayıya ulaşınca yığını kontrol etmeyi, bir rekursif hücre için yığının ortalama artış oranını toplamayı ve yığını kontrol etmek için frekansı belirlemeyi içeren kullanıcılar tarafından (gerçekten kullanmak isteyenler için) farklı senaryo ve gereksinimlerine göre optimize edilebileceğini düşünüyoruz.

{{% /alert %}}

