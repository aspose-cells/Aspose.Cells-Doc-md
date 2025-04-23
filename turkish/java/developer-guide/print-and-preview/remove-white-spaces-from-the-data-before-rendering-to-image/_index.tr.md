---
title: Görüntüye dönüştürmeden önce Veriden Boşlukları Kaldırma
type: docs
weight: 270
url: /tr/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---

{{% alert color="primary" %}}

Bazen, çalışma sayfalarını uygulamalarda veya web sayfalarında sunmanız gerekebilir. Örneğin, bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna veya başka bir belgeye resim eklemek isteyebilirsiniz. Temelde, bir çalışma sayfasını bir resim olarak görüntülemek istiyorsunuz, böylece diğer uygulamalara yapıştırılabilir. Aspose.Cells API'leri, Microsoft Excel çalışma sayfalarını resimlere dönüştürmenize olanak tanır.

{{% /alert %}}

[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) sınıfı, örneğin resim formatı, sayfalı sayfalar vb. gibi belirli özelliklere sahip bir çalışma sayfasını resim dosyasına dönüştürebilir. BMP, GIF, JPG, TIFF ve EMF dahil olmak üzere birkaç resim formatı desteklenmektedir.

Sayfa-ile-resim özelliğini kullandığınızda, çıktı resminin etrafında beyaz/boş alan, yani bir kenar, bulunur. Bunun kaldırabilirsiniz. Kaynak çalışma sayfasının üst, sol, alt ve sağ sayfa düzeni kenar boşluklarını 0 olarak ayarlayın ve buna göre [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) özelliklerini belirtin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
{{< app/cells/assistant language="java" >}}
