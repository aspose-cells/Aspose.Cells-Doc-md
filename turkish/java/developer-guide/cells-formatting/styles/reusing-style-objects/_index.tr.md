---
title: Stil Nesnelerini Yeniden Kullanma
type: docs
weight: 60
url: /tr/java/reusing-style-objects/
---

{{% alert color="primary" %}}

Stil nesnelerini yeniden kullanmak belleği tasarruf ettirebilir ve programın daha hızlı çalışmasını sağlayabilir.

{{% /alert %}}

Bir çalışsayfadaki geniş bir hücre aralığına bazı biçimlendirme uygulamak için:

1. Bir stil nesnesi oluşturun.
1. Öznitelikleri belirtin.
1. Stili aralıktaki hücrelere uygulayın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

Yukarıda tartışılan aynı süreç aşağıdaki gibi de başarılabilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

[**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle--) ve [**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell/#setStyle-com.aspose.cells.Style-) yöntemleri çok daha az bellek kullanır ve verimlidir, bu nedenle gereksiz yere çok fazla bellek tüketen eski *Cell.getStyle()* özelliği *Aspose.Cells 7.1.0* sürümü ile kaldırıldı.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
