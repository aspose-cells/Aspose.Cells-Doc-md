---
title: Çalışma Sayfasını Görüntüye Dönüştür - Verilerin etrafındaki boşlukları kaldırın
type: docs
weight: 40
url: /tr/net/convert-worksheet-to-image-remove-whitespace-around-data/
---
{{% alert color="primary" %}}

Bazen uygulamalarda veya web sayfalarında çalışma sayfası görüntüleri sunmanız gerekir. Örneğin, bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna veya başka bir belgeye resim eklemeniz gerekebilir. Temel olarak, başka uygulamalara yapıştırılabilmesi için bir çalışma sayfasını görüntü olarak işlemek istiyorsunuz. Aspose.Cells, Microsoft Excel çalışma sayfalarını resimlere dönüştürmenizi sağlar.

{{% /alert %}}

## **Verilerin etrafındaki Boşlukları Kaldır**

 bu[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)API, bir çalışma sayfasını, örneğin görüntü formatı, sayfalandırılmış sayfalar vb. belirtilen özniteliklere sahip bir görüntü dosyasına dönüştürür. BMP, GIF, JPG, TIFF ve EMF dahil olmak üzere çeşitli görüntü biçimleri desteklenir.

 Sayfadan görüntüye özelliğini kullandığınızda, çıktı görüntüsünün çevresinde varsayılan olarak bir boşluk, yani bir kenarlık bulunur. Kaynak çalışma sayfası için üst, alt, sol ve sağ sayfa kurulum kenar boşluklarını 0'a ayarlayarak bunu kaldırabilirsiniz.[**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)nitelikleri buna göre.

Aşağıdaki kod parçacığı, çıktı görüntüsündeki verilerin etrafındaki boşlukları kaldırır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

