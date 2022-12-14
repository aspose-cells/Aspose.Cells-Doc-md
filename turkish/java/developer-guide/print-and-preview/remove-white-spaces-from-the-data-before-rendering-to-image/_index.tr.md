---
title: Görüntüye İşlemeden Önce Verilerdeki Beyaz Boşlukları Kaldırın
type: docs
weight: 270
url: /tr/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---
{{% alert color="primary" %}}

Bazen uygulamalarda veya web sayfalarında çalışma sayfası görüntüleri sunmanız gerekir. Örneğin, bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna veya başka bir belgeye resim eklemeniz gerekebilir. Temel olarak, başka uygulamalara yapıştırılabilmesi için bir çalışma sayfasını görüntü olarak işlemek istiyorsunuz. Aspose.Cells API'leri, Microsoft Excel çalışma sayfalarını görüntülere dönüştürmenizi sağlar.

{{% /alert %}}

 bu[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)class, bir çalışma sayfasını, örneğin görüntü formatı, sayfalandırılmış sayfalar vb. belirtilen herhangi bir özniteliğe sahip bir görüntü dosyasına dönüştürebilir. BMP, GIF, JPG, TIFF ve EMF dahil olmak üzere çeşitli görüntü biçimleri desteklenir.

 Sayfadan görüntüye özelliğini kullandığınızda, çıktı görüntüsünün çevresinde varsayılan olarak beyaz/boş alan, yani bir kenarlık bulunur. Bunu kaldırabilirsiniz. Kaynak çalışma sayfası için üst, sol, alt ve sağ sayfa kurulum kenar boşluklarını 0 olarak ayarlayın ve[**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)nitelikleri buna göre.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
