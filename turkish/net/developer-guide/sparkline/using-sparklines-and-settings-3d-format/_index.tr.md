---
title: Mini Grafikleri ve Ayarları 3B Formatını Kullanma
type: docs
weight: 40
url: /tr/net/using-sparklines-and-settings-3d-format/
---
## **Mini Grafikleri Kullanma**
Microsoft Excel 2010, bilgileri her zamankinden daha fazla yöntemle analiz edebilir. Kullanıcıların, yeni veri analizi ve görselleştirme araçlarıyla önemli veri trendlerini izlemesine ve vurgulamasına olanak tanır. Mini grafikler, verileri ve grafiği aynı tabloda görüntüleyebilmeniz için hücrelerin içine yerleştirebileceğiniz mini grafiklerdir. Küçük grafikler düzgün kullanıldığında, veri analizi daha hızlı ve isabetlidir. Ayrıca, birçok meşgul çizelge içeren aşırı kalabalık çalışma sayfalarından kaçınarak basit bir bilgi görünümü sağlarlar.

Aspose.Cells, elektronik tablolardaki mini grafikleri işlemek için bir API sağlar.
### **Microsoft Excel'deki Mini Grafikler**
Microsoft Excel 2010'da minik grafikler eklemek için:

1. Mini grafiklerin görünmesini istediğiniz hücreleri seçin. Görüntülenmelerini kolaylaştırmak için verilerin yan tarafındaki hücreleri seçin.
1.  Tıklamak**Sokmak** şeritte ve ardından seçin**kolon** içinde**mini grafikler** grup.
1. Çalışma sayfasında kaynak verileri içeren hücre aralığını seçin veya girin. Grafikler görünecektir.

Mini grafikler, trendleri görmenize yardımcı olur, örneğin bir softbol liginin galibiyet veya mağlubiyet rekoru. Mini grafikler, ligdeki her takımın tüm sezonunu bile özetleyebilir.
### **Aspose.Cells kullanan mini grafikler**
 Geliştiriciler, Aspose.Cells tarafından sağlanan API'i kullanarak mini grafikler oluşturabilir, silebilir veya okuyabilir (şablon dosyasında). Mini grafikleri yöneten sınıflar,[Aspose.Cells.Charts](https://reference.aspose.com/cells/net/aspose.cells.charts)bu nedenle, bu özellikleri kullanmadan önce bu ad alanını içe aktarmanız gerekir.

Geliştiriciler, belirli bir veri aralığı için özel grafikler ekleyerek, seçilen hücre alanlarına farklı türde küçük grafikler ekleme özgürlüğüne sahip olur.

Aşağıdaki örnek Mini Grafikler özelliğini göstermektedir. Örnek, aşağıdakilerin nasıl yapılacağını gösterir:

1. Basit bir şablon dosyası açın.
1. Bir çalışma sayfası için mini grafik bilgilerini okuyun.
1. Belirli bir veri aralığı için bir hücre alanına yeni mini grafikler ekleyin.
1. Excel dosyasını diske kaydedin.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-UsingSparklines-1.cs" >}}
## **3D Formatını Ayarlama**
Yalnızca senaryonuz için sonuçları alabilmek için 3B grafik stillerine ihtiyacınız olabilir. Aspose.Cells, Microsoft Excel 2007 3B biçimlendirmesini uygulamak için ilgili API'i sağlar.

Bir grafiğin nasıl oluşturulacağını ve Microsoft Excel 2007 3B biçimlendirmesinin nasıl uygulanacağını gösteren eksiksiz bir örnek aşağıda verilmiştir. Örnek kodu çalıştırdıktan sonra, çalışma sayfasına bir sütun grafiği (3B efektli) eklenecektir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-Applying3DFormat-1.cs" >}}
