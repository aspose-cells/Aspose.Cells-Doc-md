---
title: Stil Nesnelerini Yeniden Kullanma
type: docs
weight: 3000
url: /tr/net/reusing-style-objects/
---
{{% alert color="primary" %}}

Stil nesnelerini yeniden kullanmak bellekten tasarruf sağlayabilir ve bir programı daha hızlı hale getirebilir.

{{% /alert %}}

Bir çalışma sayfasındaki geniş bir hücre aralığına biçimlendirme uygulamak için:

1. Bir stil nesnesi oluşturun.
1. Nitelikleri belirtin.
1. Stili aralıktaki hücrelere uygulayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

 Çünkü[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) yaklaşımı çok daha az bellek kullanır ve verimlidir, çok fazla gereksiz bellek tüketen eski Cell.Style özelliği Aspose.Cells 7.1.0 sürümüyle kaldırılmıştır.

{{% /alert %}}
