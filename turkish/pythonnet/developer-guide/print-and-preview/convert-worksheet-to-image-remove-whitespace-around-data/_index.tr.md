---
title: Elektronik tabloyu Görüntüye Dönüştür  Veri Etrafındaki Boşlukları Kaldırma
type: docs
weight: 40
url: /tr/python-net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

Bazen, çalışma sayfası görüntülerini uygulamalarda veya web sayfalarında göstermeniz gerekebilir. Örneğin, bir Word, PDF veya PowerPoint dosyasına resim eklemek isteyebilirsiniz. Çalışma sayfasını, diğer uygulamalara yapıştırılabilecek şekilde, görüntü olarak göstermek istersiniz. Aspose.Cells for Python via .NET, Microsoft Excel çalışma sayfalarını görüntüye dönüştürmenize olanak sağlar.

{{% /alert %}}

## **Veri Etrafındaki Boşlukları Kaldır**

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) API'si, örneğin görüntü biçimi, sayfa sayfalama çalışma sayfaları vb. gibi belirli özelliklere sahip bir çalışma sayfasını bir görüntü dosyasına dönüştürür. BMP, GIF, JPG, TIFF ve EMF gibi birçok görüntü formatı desteklenir.

Sayfa görüntüleme özelliğini kullandığınızda, çıktı görüntüsü varsayılan olarak etrafında boşluk bulunur. Bu, kaynak çalışma sayfası için üst, alt, sol ve sağ sayfa düzeni kenarlarını 0 olarak ayarlayarak ve buna uygun [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) özniteliklerini belirleyerek kaldırabilirsiniz.

Aşağıdaki kod parçası, çıktı görüntüsündeki veri etrafındaki boşluğu kaldırır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RemoveWhitespaceAroundData-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
