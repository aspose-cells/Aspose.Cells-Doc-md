---
title: SSS
type: docs
weight: 100
url: /tr/net/faq/
---
## **Workbook.CalculateFormula'da System.StackOverFlowException Nasıl Düzeltilir?**
Bazen kullanıcılar, Workbook.CalculateFormula yönteminde System.StackOverFlowException ile karşılaşır. Bu istisna genellikle, IIS'nin varsayılan yığın boyutunun çok küçük olması nedeniyle oluşur (yalnızca 265k). Yığın boyutu artırılmış başka bir iş parçacığı oluşturarak ve ardından Workbook.CalculateFormula ile ilgili kodu bunun içine taşıyarak bu hatayı düzeltebilirsiniz.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **Excel'i PDF'ye dönüştürürken çizgilerin kalınlığı sorunu**
Bazen, Excel dosyası PDF'ye dönüştürüldüğünde, çıktı PDF'sinde çizgilerin kalınlığı farklıdır. Bu sorun Aspose.Cells'den kaynaklanmaz.**Adobe okuyucu** ayarları ne zaman**"Pürüzsüz çizgi sanatı"** ve**"İnce çizgileri geliştirin"** kontrol edilir. Bu seçeneklerin işaretini kaldırmak, PDF'yi iyi görüntüler.

 eğer kontrol**"Pürüzsüz çizgi sanatı"** ve**"İnce çizgileri geliştirin"**, çizgilerin kalınlığı farklıdır. Nasıl yapıldığını aşağıdaki adımlara bakın:

-  git**Düzenlemek**
-  Seçme**Tercihler**
-  İçinde**Sayfa Görünümü** Kategori Kontrol et**"Pürüzsüz çizgi sanatı"** ve**"İnce çizgileri geliştirin"**

 İşareti kaldırırsanız**"Pürüzsüz çizgi sanatı"** ve**"İnce çizgileri geliştirin"**, çizgilerin kalınlığı aynıdır. Bunu başarmak için aşağıdaki adımları uygulamanız yeterlidir:

-  git**Düzenlemek**
-  Seçme**Tercihler**
-  İçinde**Sayfa Görünümü** Kategori İşaretini kaldırın**"Pürüzsüz çizgi sanatı"** ve**"İnce çizgileri geliştirin"**
## **Büyük Elektronik Tabloları Yüklerken System.OutOfMemoryException Nasıl Düzeltilir?**
Çalışma Kitabı oluşturucusunun büyük elektronik tabloları yüklerken System.OutOfMemoryException oluşturma olasılığı oldukça yüksektir. Bu istisna, kullanılabilir belleğin elektronik tabloyu belleğe tamamen yüklemek için yetersiz olduğunu, bu nedenle elektronik tablonun etkinleştirilirken yüklenmesi gerektiğini gösterir.[Bellek Tercihleri](/cells/tr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

Aspose.Cells API'ler, elektronik tabloları yüklerken ve işlerken bellek tüketimini optimize etmek için Bellek Tercihleri sağlar. Bu seçenekler, aşağıda gösterildiği gibi, Workbook nesnesinde büyük veri kümeleri içeren büyük elektronik tabloların verimli bir şekilde yüklenmesine de yardımcı olur.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **Belirli bir Çalışma Kitabı için hangi yığın boyutunun gerekli olduğunu belirleme**
Aspose.Cells formül hesaplama motorunu geliştirmemize rağmen, çoğu durumda, daha küçük yığın boyutu belirtmeden belirli bir şablon dosyası için tüm formülleri başarıyla hesaplayabilmeniz gerekir. Ancak yine de bazen Workbook.CalculateFormula yöntemindeki StackOverFlowException kaçınılmaz olabilir. Kullanıcıların formül hesaplamalarını takip etmeleri için yeni API'ler sağlıyoruz. "AbstractCalculationMonitor" adlı bir sınıf ekledik ve bir özellik sağladık, örn.*CalculationOptions.CalculationMonitor*Sorunla başa çıkmak/izlemek için.

Kullanıcılar, API'leri kullanarak yığın boyutunu kendileri takip edebilir. Lütfen her hücre için yığının kontrol edilmesinin performansı kesinlikle daha büyük ölçüde düşüreceğini unutmayın. Referansınız için örnek kod segmentine bakın:

`     `genel sınıf MyCalculationMonitor : AbstractCalculationMonitor
`     `{  ` `genel geçersiz kılma geçersiz BeforeCalculate(int sheetIndex, int rowIndex, int colIndex)  ` `{  ` `if(new StackTrace(false).FrameCount > 2000)  ` `{ _x000d `" İstisna StackOverflowException riski nedeniyle formül hesaplamasını durdurun");  ` `}  ` `}  ` `} 



{{% alert color="primary" %}} 

Çalışma zamanında kullanılan yığın boyutunu almanın daha iyi bir yolu yoktur. Sağladığımız yukarıdaki kod sadece örnektir. Performans kesinlikle önemli ölçüde düşecektir. Bu nedenle, kodun (onu gerçekten kullanmak isteyen) kullanıcılar tarafından farklı senaryolarına ve gereksinimlerine göre optimize edilebileceğini düşünüyoruz. Özyinelemeli hücre sayısı belirli bir sayıya ulaştığında yığının kontrol edilmesi, bir özyinelemeli hücre için yığının ortalama artış hızının toplanması ve yığının kontrol edilme sıklığının belirlenmesi vb.

{{% /alert %}}

