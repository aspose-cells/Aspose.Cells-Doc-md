---
title: Elektronik tabloyu Görüntüye Dönüştür  Veri Etrafındaki Boşlukları Kaldırma
type: docs
weight: 40
url: /tr/net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

Bazen, çalışma sayfalarını uygulamalarda veya web sayfalarında sunmanız gerekebilir. Örneğin, çalışma sayfalarını bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna veya başka bir belgeye yerleştirmeniz gerekebilir. Temelde, bir çalışma sayfasını bir görüntü olarak oluşturmak ve başka uygulamalara yapıştırmak istersiniz. Aspose.Cells, Microsoft Excel çalışma sayfalarını görüntülere dönüştürmenizi sağlar.

{{% /alert %}}

## **Veri Etrafındaki Boşlukları Kaldır**

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) API'si, örneğin görüntü biçimi, sayfa sayfalama çalışma sayfaları vb. gibi belirli özelliklere sahip bir çalışma sayfasını bir görüntü dosyasına dönüştürür. BMP, GIF, JPG, TIFF ve EMF gibi birçok görüntü formatı desteklenir.

Sayfa görüntüleme özelliğini kullandığınızda, çıktı görüntüsü varsayılan olarak etrafında boşluk bulunur. Bu, kaynak çalışma sayfası için üst, alt, sol ve sağ sayfa düzeni kenarlarını 0 olarak ayarlayarak ve buna uygun [**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) özniteliklerini belirleyerek kaldırabilirsiniz.

Aşağıdaki kod parçası, çıktı görüntüsündeki veri etrafındaki boşluğu kaldırır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
