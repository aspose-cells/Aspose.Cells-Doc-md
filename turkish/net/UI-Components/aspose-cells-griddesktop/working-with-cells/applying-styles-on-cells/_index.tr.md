---
title: Hücreye Stil Uygula
type: docs
weight: 50
url: /tr/net/aspose-cells-griddesktop/apply-style-on-cell/
keywords: GridDesktop, biçim, stil, sayı biçimleri, sayı biçimi, NumberFormat
description: Bu makale, GridDesktop teki Çalışsayfadaki hücrede stil biçimini nasıl alınacağını veya ayarlanacağını tanıtır.
---

{{% alert color="primary" %}} 

Bu konu, bir hücreye stil biçimi uygulama ile ilgilenir; hücreye stil uygulamak için kullanılabilecek neredeyse tüm ilgili özellikleri kapsayacağız. Bazı temel biçimlendirme ayarlarının yanı sıra, detaylı olarak hücreye sınırlar çizme ve sayı biçimini ayarlama konusunu da tartışacağız.

{{% /alert %}} 
## **Bir Hücreye Özel Stil Uygulama - Bir Örnek**
Aspose.Cells.GridDesktop kullanarak bir hücrenin fontunu ve rengini değiştirmek için lütfen aşağıdaki adımları izleyin:

- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- Bir **Stil** uygulamak istediğimiz bir **Hücre**'ye erişin
- **Hücre**'nin **Stil**'ini alın
- Özel ihtiyaçlarınıza göre **Stil** özelliklerini ayarlayın
- Son olarak, **Stil**'i güncellenmiş olanla **Hücre**'ye ayarlayın

Geliştiriciler tarafından kullanılabilecek **Stil** nesnesi tarafından sunulan birçok faydalı özellik ve yöntem vardır. Aşağıdaki kodda, hücreye özel stil nasıl uygulanacağı gösterilmektedir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **Hücrelerin Sınırlarını Çizme**
**Stil** nesnesini kullanarak, bir hücrenin sınırlarını çok kolay bir şekilde çizebiliriz. Sınırlar herhangi bir renkte çizilebilir. Ayrıca, geliştiricilerin hücre etrafında sınırlar çizmek için kullanacakları belirli bir çizgi tipini seçme esnekliği de bulunmaktadır. Geliştiriciler, sırasıyla **Stil** nesnesinin **SetBorderLine** ve **SetBorderColor** metodlarını kullanarak herhangi bir türde ve renkte sınırları çizmek için kullanabilirler. Benzer şekilde, herhangi bir hücrenin sınır bilgilerini almak için geliştiriciler ayrıca **Stil** nesnesinin **GetBorderLine** ve **GetBorderColor** metodlarını da kullanabilirler.
### **Sınır Türleri**
Aşağıdaki gibi Aspose.Cells.GridDesktop tarafından desteklenen altı sınırdan altısı aşağıdaki gibidir:

- **Sol** , sol sınırı temsil eder
- **Sağ** , sağ sınırı temsil eder
- **Üst** , üst sınırı temsil eder
- **Alt** , alt sınırı temsil eder
- **DiagonalDown** , çapraz aşağı sınırı temsil eder
- **DiagonalUp** , çapraz yukarı sınırı temsil eder
### **Sınır Çizgi Türleri**
Bir sınır bir çizgiden oluşur. Çizgi tipini değiştirmek, bir sınırın görünümünü değiştirir. Aspose.Cells.GridDesktop tarafından desteklenen birçok sınır çizgi türü aşağıda listelenmiştir:

- **Hiçbiri** , hiçbir sınırı temsil eder
- **İnce** , düz çizgili sınırı temsil eder
- **Orta** , çizgi genişliği eşit olan düz çizgili sınırı temsil eder 2f
- **Tireli** , tireli çizgili sınırı temsil eder
- **Noktalı** , noktalı çizgili sınırı temsil eder
- **Kalın** , çizgi genişliği 3f olan katı çizgi sınırını temsil eder
- **Orta Kesikli** , çizgi genişliği 2f olan kesikli çizgi sınırını temsil eder
- **İnce Kesikli Noktalı** , kesikli noktalı çizgi sınırını temsil eder
- **Orta Kesikli Noktalı** , çizgi genişliği 2f olan kesikli noktalı çizgi sınırını temsil eder
- **İnce Kesikli Nokta Noktalı** , kesikli nokta noktalı çizgi sınırını temsil eder
- **Orta Kesikli Nokta Noktalı** , çizgi genişliği 2f olan kesikli nokta noktalı çizgi sınırını temsil eder
## **Hepsi Bir Arada Toplama - Örnek**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **Sayı Biçimlerini Ayarlama**
Aspose.Cells.GridDesktop ayrıca sayı biçimlerini ayarlama sağlar. Aspose.Cells.GridDesktop tarafından sunulan 58 dahili sayı biçimi bulunmaktadır. Desteklenen tüm sayı biçimlerinin tam listesini görmek için lütfen [Desteklenen Sayı Biçimleri.](/cells/tr/net/list-of-supported-number-formats/) bağlantısına bakınız

Tüm dahili sayı biçimlerine bir **Dizin** numarası atanmıştır. **Örneğin** **0.00E+00** sayı biçiminin **Dizin** numarası **11**'dir. Geliştiriciler, herhangi bir hücrede dahili bir sayı biçimini kullanmak için **Stil** nesnesinin NumberFormat özelliğini belirli sayı biçiminin **Dizin** numarasına ayarlayabilir. Bununla birlikte, geliştiriciler kendi özel sayı biçimlerine ihtiyaç duyuyorlarsa, **Stil** nesnesinin Custom özelliğini de kullanabilirler.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
