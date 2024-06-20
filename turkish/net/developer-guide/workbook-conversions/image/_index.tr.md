---
title: Görüntü
type: docs
weight: 300
url: /tr/net/convert-excel-to-image/
---


{{% alert color="primary" %}}

Aspose.Cells, bir çalışma kitabından çalışsayı dışa aktarmanıza ve farklı biçimlere dönüştürmenize olanak tanır. Bu makale, bir çalışsayının farklı biçimlere nasıl dönüştürüleceğini açıklar.

{{% /alert %}}

## Çalışma Kitabını TIFF'e Dönüştürme

Bir Excel dosyası çoklu sayfalı çoklu çalışma sayfalarını içerebilir. [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), Excel'i çoklu sayfalı TIFF'e dönüştürmenizi sağlar. Ayrıca, TIFF için [Sıkıştırma](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [Renk derinliği](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth), Çözünürlük([Yatay çözünürlük](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [Dikey çözünürlük](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)) gibi birden çok seçeneği kontrol edebilirsiniz.

Aşağıdaki kod örneği, birden çok sayfa içeren Excel dosyasını TIFF'e nasıl dönüştüreceğinizi gösterir. [Kaynak Excel dosyası](workbook-to-tiff-with-mulitiple-pages.xlsx) ve [oluşturulan TIFF görüntüsü](workbook-to-tiff-with-mulitiple-pages.tiff) referansınız için ekli.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **Çalışsayıyı Görüntüye Dönüştürme**

Çalışma sayfaları analiz etmek istediğiniz verileri içerebilir. Örneğin, bir çalışma sayfası parametreleri, toplamları, yüzdeleri, istisnaları ve hesaplamaları içerebilir.

Bir geliştirici olarak, çalışma sayfalarını görüntü olarak sunmanız gerekebilir. Örneğin, bir çalışma sayfasının bir görüntüsünü bir uygulamada veya web sayfasında kullanmanız gerekebilir. Bir çalışma sayfasını bir Microsoft Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna veya başka bir belge türüne eklemek isteyebilirsiniz. Basitçe söylemek gerekirse, bir çalışma sayfasını bir görüntü olarak oluşturmak istiyorsunuz ki başka bir yerde kullanabilesiniz.

Aspose.Cells, Excel çalışma sayfalarını görüntülere dönüştürmeyi destekler. Bu özelliği kullanabilmek için programınıza veya projenize [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) ad alanını almalısınız. Rendere etme ve yazdırma için birçok değerli sınıfı içerir, örneğin [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) ve diğerlerini.

[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) sınıfı, bir görüntüye dönüştürülecek bir çalışma sayfasını temsil eder. Farklı özelliklere veya seçeneklere sahip bir çalışma sayfasını görüntü dosyasına(dosyalarına) dönüştürebilen aşırı yüklenmiş bir [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) yöntemi vardır. Bir System.Drawing.Bitmap nesnesi döndürür ve bir görüntü dosyasını diske veya akışa kaydedebilirsiniz. BMP, PNG, GIF, JPG, JPEG, TIFF, EMF gibi birçok görüntü formatı desteklenir.

Aşağıdaki kod örneği, bir Excel dosyasındaki bir çalışma sayfasını bir görüntü dosyasına dönüştürmenin nasıl yapıldığını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

Şu anda, çalışma sayfalarını görüntülere dönüştürmek için API, 3D kabarcık grafiklerini desteklememektedir.

{{% /alert %}}

## **Çalışma Sayfasını SVG'ye Dönüştürme**

SVG, Ölçeklenebilir Vektör Grafikleri anlamına gelir. SVG, iki boyutlu vektör grafikleri için XML standartlarına dayanan bir spesifikasyondur. 1999'dan beri World Wide Web Consortium (W3C) tarafından geliştirilen açık bir standarttır.

Aspose.Cells for .NET, 7.1.0 sürümünden beri çalışma sayfalarını SVG görüntüsüne dönüştürebilmektedir. Aşağıdaki kod parçası, bir Excel dosyasındaki çalışma sayfasını SVG görüntü dosyasına dönüştürmenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **Gelişmiş Konular**
- [Bir Excel Grafiğini Görüntüye Dönüştürme](/cells/tr/net/convert-an-excel-chart-to-image/)
- [SVG Biçiminde Grafikleri Görüntüye Dönüştürme](/cells/tr/net/converting-chart-to-image-in-svg-format/)
- [Görünüm Kutusu Özelliği ile Grafiksel Bir Ortama Tabloyu Dışa Aktarma](/cells/tr/net/export-chart-to-svg-with-viewbox-attribute/)
- [Excel'den TIFF'e Dönüşüm İlerlemesini İzle](/cells/tr/net/track-conversion-progress-of-excel-to-tiff/)
