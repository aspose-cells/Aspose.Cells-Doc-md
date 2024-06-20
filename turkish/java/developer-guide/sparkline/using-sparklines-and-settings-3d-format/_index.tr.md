---
title: Sparklines ve 3D Format Ayarlarını Kullanma
type: docs
weight: 40
url: /tr/java/using-sparklines-and-settings-3d-format/
---

## **Sparklines Kullanma**
Microsoft Excel 2010, bilgileri daha önce hiç olmadığı kadar fazla şekilde analiz etmenizi sağlar. Kullanıcıların yeni veri analiz ve görselleştirme araçlarıyla önemli veri eğilimlerini takip etmesine ve vurgulamasına izin verir. Sparklines, veriyi ve tabloyu aynı anda görüntüleyebileceğiniz mini grafiklerdir. Sparklines uygun şekilde kullanıldığında, veri analizi daha hızlı ve daha anlaşılır olur. Ayrıca, aşırı kalabalık çalışma tablolarını çok fazla meşgul grafiklerle önler. Onlar, aynı tabloda veriyi görmek için basit bir görünüm sağlar. Ayrıca, Aspose.Cells, elektronik tablolardaki sparklines'ı manipüle etmek için bir API sağlar.

Aspose.Cells, elektronik tablolardaki sparklines'ları manipüle etmek için bir API sağlar.
### **Microsoft Excel'de Sparklines Kullanma**
Microsoft Excel 2010'da Sparklines eklemek için:

1. Sparklines'ların görünmesini istediğiniz hücreleri seçin. Onları görüntülemeyi kolaylaştırmak için, verinin yanındaki hücreleri seçin.
1. Menü şeridinde **Ekle**'yi tıklayın, ardından **Sparklines** grubunda **Sütun**'u seçin.
1. Kaynak verinin bulunduğu çalışma sayfasındaki hücre aralığını seçin veya girin. Grafikler görünecektir.

Sparklines, örneğin, bir bayan voleybol ligi için kazanma veya kaybetme kaydını görmek için size yardımcı olur. Sparklines, ligdeki her takımın tüm sezonlarının toplamını dahi verebilir.
### **Aspose.Cells, kullanıcıların verilen veri aralığı için özel grafikleri ekleyerek seçilen hücre alanlarına farklı tipte minik grafikler ekleyebilecekleri özgürlüğü sunar.**
Geliştiriciler, Aspose.Cells tarafından sağlanan API'yi kullanarak kıvılcımları (şablon dosyasında) oluşturabilir, silebilir veya okuyabilir. Kıvılcımları yöneten sınıflar, [Aspose.Cells.Charts](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) ad alanında bulunur, bu nedenle bu özellikleri kullanmadan önce bu ad alanını içe aktarmanız gerekir.

Belirli bir veri aralığı için özel grafikler ekleyerek, geliştiriciler seçili hücre alanlarına farklı türde küçük grafikler eklemek özgürlüğüne sahiptir.

Aşağıdaki örnek, Sparklines özelliğini sergiler. Örnek, şunları gösterir:

1. Basit bir şablon dosyasını açın.
1. Bir çalışma sayfası için sparklines bilgilerini okuyun.
1. Belirli bir veri aralığı için yeni sparklines ekleyin.
1. Excel dosyasını diske kaydedin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparkLine.java" >}}
## **3B Formatını Ayarlama**
Senaryonuz için sadece sonuçları alabilirsiniz, bu nedenle 3B grafik stillerine ihtiyacınız olabilir. Aspose.Cells, Microsoft Excel 2007 3B biçimlendirmesini uygulamak için ilgili API'yi sağlar.

Aşağıda, bir grafik oluşturmayı ve Microsoft Excel 2007 3B biçimlendirmesini uygulamayı sergilemek için tam bir örnek verilmiştir. Örnek kodu çalıştırdıktan sonra bir sütun grafiği (3B efektleri ile) çalışma sayfasına eklenecektir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat.java" >}}
