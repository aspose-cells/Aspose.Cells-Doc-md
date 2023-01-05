---
title: Stil Nesnelerini Yeniden Kullanma
type: docs
weight: 60
url: /tr/java/reusing-style-objects/
---
{{% alert color="primary" %}}

Stil nesnelerini yeniden kullanmak bellekten tasarruf sağlayabilir ve programın daha hızlı çalışmasını sağlayabilir.

{{% /alert %}}

Bir çalışma sayfasındaki geniş bir hücre aralığına biçimlendirme uygulamak için:

1. Bir stil nesnesi oluşturun.
1. Nitelikleri belirtin.
1. Stili aralıktaki hücrelere uygulayın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

Yukarıda tartışılanla aynı süreç aşağıdaki gibi de gerçekleştirilebilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

 Çünkü[**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle() ) ve[**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle(com.aspose.cells.Style) ) yöntemler çok daha az bellek kullanır ve verimlidir, eski*Cell.getStyle()* Çok fazla gereksiz bellek tüketen özellik, piyasaya sürülmesiyle kaldırıldı.*Aspose.Cells 7.1.0*.

{{% /alert %}}
