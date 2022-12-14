---
title: Çalışma Sayfasını Grafik Bağlamına Dönüştür
type: docs
weight: 300
url: /tr/net/render-worksheet-to-graphic-context/
---
{{% alert color="primary" %}}

Aspose.Cells artık çalışma sayfasını grafik bağlamına dönüştürebilir. Grafik bağlam, görüntü dosyası, ekran veya yazıcı gibi herhangi bir şey olabilir. Çalışma sayfasını grafik içeriğe dönüştürmek için lütfen aşağıdaki iki yöntemden birini kullanın.

- [**SheetRender.ToImage(int pageIndex, Graphics g, kayan nokta x, kayan nokta y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float genişliği, float yüksekliği)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

 Aşağıdaki kod, çalışma sayfasını grafik bağlamına dönüştürmek için Aspose.Cells'in nasıl kullanılacağını gösterir. Bir kod yürüttüğünüzde, tüm çalışma sayfasını yazdıracak ve kalan boş alanı grafik bağlamında mavi renkle dolduracak ve görüntüyü şu şekilde kaydedecektir:**OutputImage_out_.png** dosya. Bu kodu denemek için herhangi bir kaynak excel dosyasını kullanabilirsiniz. Daha iyi anlamak için lütfen kodun içindeki yorumları da okuyun.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}
