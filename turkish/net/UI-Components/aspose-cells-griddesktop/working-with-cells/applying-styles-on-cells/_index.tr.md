---
title: Cells'de Stilleri Uygulamak
type: docs
weight: 50
url: /tr/net/applying-styles-on-cells/
---
{{% alert color="primary" %}} 

Bu konu, hücrelere stil uygulamakla ilgilidir, bu nedenle, bir hücreye stil uygulamak için kullanılabilecek hemen hemen her şeyi ele almaya çalışacağız. Bazı temel biçimlendirme ayarlarının yanı sıra, sınır çizme ve hücrelerin sayı biçimini ayarlama hakkında da ayrıntılı olarak konuşacağız.

{{% /alert %}} 
## **Cell'de Özel Stil Uygulama - Bir Örnek**
Aspose.Cells.GridDesktop kullanarak bir hücrenin yazı tipini ve rengini değiştirmek için lütfen aşağıdaki adımları izleyin:

-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Erişim**Cell** uygulamak istediğimiz**stil**
-  Elde etmek**stil** arasında**Cell**
-  Ayarlamak**stil** özel ihtiyaçlarınıza göre özellikler
-  Son olarak ayarla**stil** arasında**Cell** güncellenen ile

 tarafından sunulan birçok yararlı özellik ve yöntem vardır.**stil** geliştiriciler tarafından stili gereksinimlerine göre özelleştirmek için kullanılabilen nesne. Aşağıdaki kodda, özel stilin hücreye nasıl uygulanacağı gösterilmiştir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **Cells'in Kenarlıklarını Çizme**
 kullanma**stil**nesne, bir hücrenin sınırlarını çok kolay çizebiliriz. Kenarlıklar herhangi bir renkte çizilebilir. Ayrıca geliştiriciler, hücrenin çevresine sınır çizmek için kullanılacak belirli bir çizgi türünü seçme esnekliğine de sahiptir. Geliştiriciler kullanabilir**Sınır Çizgisini Ayarla** ve**Kenarlık Rengini Ayarla** Yöntemleri**stil** herhangi bir tür ve renkte kenarlık çizmek için nesne. Benzer şekilde, geliştiriciler herhangi bir hücrenin sınır bilgilerini almak için**GetSınır Çizgisi** ve**Sınır Rengini Al** Yöntemleri**stil** nesne.
### **Kenarlık Türleri**
Aspose.Cells.GridDesktop tarafından aşağıdaki gibi desteklenen altı tür kenarlık vardır:

- **Sol** , sol kenarlığı temsil eder
- **Doğru** , sağ kenarlığı temsil eder
- **Tepe** , Üst sınırı temsil eder
- **Alt kısım** , alt sınırı temsil eder
- **Çapraz Aşağı** , diyagonal aşağı sınırı temsil eder
- **çapraz Yukarı** , çapraz yukarı sınırı temsil eder
### **Sınır Çizgisi Türleri**
Kenarlık bir çizgiden oluşur. Çizgi türünün değiştirilmesi, kenarlığın görünümünü değiştirir. Aspose.Cells.GridDesktop tarafından desteklenen ve aşağıda listelenen birçok sınır çizgisi türü vardır:

- **Hiçbiri** , kenarlık olmadığını temsil eder
- **İnce** , düz çizgi kenarlığını temsil eder
- **Orta** , çizgi genişliği 2f'ye eşit olan düz çizgi sınırını temsil eder
- **kesikli** , kesikli çizgi kenarlığını temsil eder
- **Noktalı** , noktalı çizgi kenarlığını temsil eder
- **Kalın** , çizgi genişliği 3f'ye eşit olan düz çizgi sınırını temsil eder
- **Orta Kesikli** , çizgi genişliği 2f'ye eşit olan kesikli çizgi sınırını temsil eder
- **İnce Çizgi Noktalı** , kısa çizgi noktalı çizgi kenarlığını temsil eder
- **Orta ÇizgiNoktalı** , çizgi genişliği 2f'ye eşit olan kısa çizgi noktalı çizgi kenarlığını temsil eder
- **İnce Çizgi Noktalı** , kısa çizgi noktalı çizgi kenarlığını temsil eder
- **Orta ÇizgiNoktalı** , çizgi genişliği 2f'ye eşit olan kısa çizgi noktalı çizgi kenarlığını temsil eder
## **Hepsini Bir Arada Özetlemek - Örnek**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **Sayı Biçimlerini Ayarlama**
Aspose.Cells.GridDesktop ayrıca hücrelere girilen değerler için sayı formatlarını belirleme konusunda güçlü bir özellik sunar. Aspose.Cells.GridDesktop tarafından sunulan 58 yerleşik sayı biçimi vardır. Desteklenen tüm sayı biçimlerinin tam listesini görmek için lütfen bkz.[Desteklenen Sayı Biçimleri.](/cells/tr/net/list-of-supported-number-formats/)

 Tüm yerleşik sayı biçimlerine bir**dizin** sayı.**Örneğin** the**dizin** sayısı**0.00E+00** sayı biçimi**11** . Geliştiriciler, herhangi bir hücrede yerleşik bir sayı biçimi kullanmak için NumberFormat özelliğini ayarlayabilir.**stil** itiraz etmek**dizin** belirli bir sayı biçiminin numarası. Bununla birlikte, geliştiricilerin kendi özel sayı biçimine sahip olmaları gerekiyorsa, Özel özelliğini de kullanabilirler.**stil** nesne.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
