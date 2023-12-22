---
title: Gelişmiş Koşullu Biçimlendirmeyi Uygula
description: Gelişmiş koşullu biçimlendirmeyi uygulamak için C#'deki Aspose.Cells kitaplığı nasıl kullanılır? Bu kriterleri ayarlayarak hücrelerin nasıl görüneceği ve görüneceği üzerinde daha fazla kontrole sahip olursunuz.
keywords: Aspose.Cells, Advanced Conditional Formatting, C#, Conditional, Formatting
type: docs
weight: 70
url: /tr/net/apply-advanced-conditional-formatting/
---
{{% alert color="primary" %}} 

Microsoft Excel 2007 ve sonraki sürümleri (2010/2013/2016), koşullu biçimlendirme için bazı gelişmiş özellikler sağlar. Örneğin, oldukça karmaşık hale gelen hücre gölgelendirmesi, kenarlıklar, renkli simgeler, oklar, bayraklar ve yazı tipi formatlaması vb. uygulamanıza olanak tanır.

{{% /alert %}} 
##  **Microsoft Excel Dosyalarına Gelişmiş Koşullu Biçimlendirme Uygula**
Koşullu biçimlendirme şunları yapabilir:

- Hücrelere basit bir çubuk grafik yerleştirerek temel sayıları grafiksel olarak geliştirmek için gölgeli veri çubukları ekleyin.
- Aralıktaki diğer hücrelerdeki değerlerle ilişkilerine göre hücreleri renk ölçekleriyle otomatik olarak gölgeleyin. Varsayılan ayarlar en düşük değeri kırmızı renkte gölgelendirerek en yüksek değere kadar yeşil renkte gölgelendirir.
- Simge kümelerini renk ölçeklerine benzer şekilde kullanın; ancak hücreleri gölgelemek yerine hücrelere oklar ve trafik ışıkları gibi küçük simgeler ekler.

Aspose.Cells, çalışma zamanında hücrelerde Microsoft Excel 2007 ve XLSX biçimindeki sonraki sürümler tarafından sağlanan koşullu biçimlendirmeyi tamamen destekler. Bu örnekte IconSet'ler, DataBar'lar, Renk Ölçekleri, TimePeriods, Top/Bottom ve farklı öznitelik kümelerine sahip diğer kurallar da dahil olmak üzere gelişmiş koşullu biçimlendirme türlerine yönelik bir alıştırma gösterilmektedir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormatting-1.cs" >}}
###  **ColorScale Koşullu Biçimlendirme için Microsoft Excel Tarafından Seçilen Rengi Hesaplayın**
Aspose.Cells, bir şablon dosyasında ColorScale koşullu biçimlendirme kullanıldığında Microsoft Excel tarafından seçilen rengi hesaplamanıza olanak tanır. Microsoft Excel tarafından seçilen rengin nasıl hesaplanacağını öğrenmek için aşağıdaki örnek koda bakın.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ComputeColorChoosenByMSExcel-1.cs" >}}
