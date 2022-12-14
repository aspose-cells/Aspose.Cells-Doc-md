---
title: resim
type: docs
weight: 300
url: /tr/net/convert-excel-to-image/
---
{{% alert color="primary" %}}

Aspose.Cells, çalışma kitabından bir çalışma sayfasını dışa aktarmanıza ve farklı biçimlere dönüştürmenize olanak tanır. Bu makalede, bir çalışma sayfasının farklı biçimlere nasıl dönüştürüleceği açıklanmaktadır.

{{% /alert %}}

## Çalışma Kitabını TIFF'e Dönüştürme

 Bir Excel dosyası, birden çok sayfa içeren birden çok sayfa içerebilir.[Çalışma KitabıRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) Excel'i birden çok sayfayla TIFF'e dönüştürmenize olanak tanır. Ayrıca, TIFF için birden fazla seçeneği kontrol edebilirsiniz, örneğin[Sıkıştırma](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [Renk derinliği](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth), Çözünürlük([yatay çözünürlük](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [Dikey çözünürlük](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

 Aşağıdaki kod parçacığı, Excel'in birden çok sayfayla TIFF'e nasıl dönüştürüleceğini gösterir. bu[kaynak Excel dosyası](workbook-to-tiff-with-mulitiple-pages.xlsx) ve[oluşturulan TIFF görüntüsü](workbook-to-tiff-with-mulitiple-pages.tiff) referansınız için eklenmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **Çalışma Sayfasını Görüntüye Dönüştürme**

Çalışma sayfaları, çözümlemek istediğiniz verileri içerir. Örneğin, bir çalışma sayfası parametreler, toplamlar, yüzdeler, istisnalar ve hesaplamalar içerebilir.

Bir geliştirici olarak, çalışma sayfalarını resim olarak sunmanız gerekebilir. Örneğin, bir uygulamada veya web sayfasında bir çalışma sayfasının görüntüsünü kullanmanız gerekebilir. Microsoft Word belgesine, PDF dosyasına, PowerPoint sunumuna veya başka bir belge türüne resim eklemek isteyebilirsiniz. Basitçe söylemek gerekirse, başka bir yerde kullanabilmeniz için bir çalışma sayfasının görüntü olarak işlenmesini istiyorsunuz.

Aspose.Cells, Excel çalışma sayfalarının resimlere dönüştürülmesini destekler. Bu özelliği kullanmak için içe aktarmanız gerekir.**[Aspose.Cells.Rendering](https://reference.aspose.com/cells/net/aspose.cells.rendering)** Programınıza veya projenize ad alanı. Oluşturma ve yazdırma için çeşitli değerli sınıflara sahiptir, örneğin**[SheetRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, **[WorkbookRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)**, ve diğerleri.

 bu**[SheetRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)** class, görüntü olarak işlenecek bir çalışma sayfasını temsil eder. Aşırı yüklenmiş bir yöntemi vardır,**[ToImage](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)**, bir çalışma sayfasını farklı özniteliklere veya seçeneklere sahip görüntü dosyalarına dönüştürebilir. Bir System.Drawing.Bitmap nesnesi döndürür ve bir görüntü dosyasını diske veya akışa kaydedebilirsiniz. BMP, PNG, GIF, JPG, JPEG, TIFF, EMF gibi çeşitli görüntü formatları desteklenir.

Aşağıdaki kod parçacığı, bir Excel dosyasındaki bir çalışma sayfasının bir görüntü dosyasına nasıl dönüştürüleceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

Şu anda, çalışma sayfalarını görüntülere dönüştürmek için kullanılan API, 3B balon grafiklerini desteklemiyor.

{{% /alert %}}

## **Çalışma Sayfasını SVG'ye Dönüştürme**

SVG, Ölçeklenebilir Vektör Grafikleri anlamına gelir. SVG, iki boyutlu vektör grafikleri için XML standartlarına dayalı bir belirtimdir. World Wide Web Consortium (W3C) tarafından 1999'dan beri geliştirilmekte olan açık bir standarttır.

Aspose.Cells for .NET, 7.1.0 sürümünden beri çalışma sayfalarını SVG görüntüsüne dönüştürebiliyor. Aşağıdaki kod parçacığı, bir Excel dosyasındaki bir çalışma sayfasının bir SVG görüntü dosyasına nasıl dönüştürüleceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **ileri konular**
- [Bir Excel Grafiğini Görüntüye Dönüştür](/cells/tr/net/convert-an-excel-chart-to-image/)
- [Grafiği SVG Formatında Görüntüye Dönüştürme](/cells/tr/net/converting-chart-to-image-in-svg-format/)
- [Grafiği viewBox özniteliğiyle SVG'ye aktar](/cells/tr/net/export-chart-to-svg-with-viewbox-attribute/)
- [Excel'in TIFF'e Dönüştürme İlerlemesini İzleyin](/cells/tr/net/track-conversion-progress-of-excel-to-tiff/)
