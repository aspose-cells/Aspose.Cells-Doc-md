---
title: Grafiksel Ortama Çalışsayısı Renderleme
type: docs
weight: 300
url: /tr/net/render-worksheet-to-graphic-context/
---

{{% alert color="primary" %}}

Aspose.Cells artık çalışma sayfasını grafik bağlamına çizebilir. Grafik bağlamı, görüntü dosyası, ekran veya yazıcı gibi her şey olabilir. Lütfen çalışma sayfasını grafik bağlamına çizmek için aşağıdaki iki yöntemden birini kullanın.

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

Aşağıdaki kod, Aspose.Cells'i çalışma sayfasını grafik bağlamına çizmek için nasıl kullanacağınızı göstermektedir. Kodu çalıştırdığınızda, kod tüm çalışma sayfasını yazdıracak ve grafik bağlamındaki kalan boş alanı mavi renkle dolduracak ve görüntüyü **OutputImage_out_.png** dosyası olarak kaydedecektir. Bu kodu denemek için herhangi bir kaynak Excel dosyasını kullanabilirsiniz. Daha iyi anlam için lütfen kod içindeki yorumları da okuyun.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}
{{< app/cells/assistant language="csharp" >}}
