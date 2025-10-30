---
title: Golang kullanarak C++ ile Excel i Resme dönüştürün.
linktitle: Excel i Resme Dönüştür
type: docs
weight: 300
url: /tr/go-cpp/convert-excel-to-image/
description: Excel çalışma sayfalarının TIFF ve SVG formatları dahil olmak üzere görüntülere nasıl dönüştürüleceğini öğrenin, Aspose.Cells for C++ kullanılarak.
---

{{% alert color="primary" %}}

Aspose.Cells, bir çalışma kitabından çalışsayı dışa aktarmanıza ve farklı biçimlere dönüştürmenize olanak tanır. Bu makale, bir çalışsayının farklı biçimlere nasıl dönüştürüleceğini açıklar.

{{% /alert %}}

## Çalışma Kitabını TIFF'e Dönüştürme

Bir Excel dosyası çok sayfa ve çok sayfa içerebilir. [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/) kullanarak Excel’i çok sayfalı TIFF formatına dönüştürebilirsiniz. Ayrıca, TIFF için [Sıkıştırma](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/), [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/), Çözünürlük ([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/), [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

Aşağıdaki kod örneği, birden çok sayfa içeren Excel dosyasını TIFF'e nasıl dönüştüreceğinizi gösterir. [Kaynak Excel dosyası](workbook-to-tiff-with-mulitiple-pages.xlsx) ve [oluşturulan TIFF görüntüsü](workbook-to-tiff-with-mulitiple-pages.tiff) referansınız için ekli.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image.go" >}}
## **Çalışsayıyı Görüntüye Dönüştürme**

Çalışma sayfaları analiz etmek istediğiniz verileri içerebilir. Örneğin, bir çalışma sayfası parametreleri, toplamları, yüzdeleri, istisnaları ve hesaplamaları içerebilir.

Bir geliştirici olarak, çalışma sayfalarını görüntü olarak sunmanız gerekebilir. Örneğin, bir çalışma sayfasının bir görüntüsünü bir uygulamada veya web sayfasında kullanmanız gerekebilir. Bir çalışma sayfasını bir Microsoft Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna veya başka bir belge türüne eklemek isteyebilirsiniz. Basitçe söylemek gerekirse, bir çalışma sayfasını bir görüntü olarak oluşturmak istiyorsunuz ki başka bir yerde kullanabilesiniz.

Aspose.Cells, Excel çalışma sayfalarını görüntüye dönüştürme desteği sağlar. Bu özelliği kullanmak için, programınıza veya projenize [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/go-cpp/) ad alanını içe aktarmanız gerekir. Bu, gösterim ve yazdırma için birkaç değerli sınıfa sahiptir, örneğin [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/) ve diğerleri.

[**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/) sınıfı, görüntüler olarak render edilecek bir çalışma sayfasını temsil eder. [**ToImage**](https://reference.aspose.com/cells/go-cpp/sheetrender/toimage/) adlı aşırı yüklenmiş bir yöntemi vardır; bu, bir çalışma sayfasını farklı özellikler veya seçeneklerle resim dosyasına dönüştürebilir. Bir `System.Drawing.Bitmap` nesnesi döndürür ve bir resim dosyasını disk veya akışa kaydedebilirsiniz. Birkaç resim formatı desteklenir, örneğin BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Aşağıdaki kod örneği, bir Excel dosyasındaki bir çalışma sayfasını bir görüntü dosyasına dönüştürmenin nasıl yapıldığını gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-1.go" >}}
{{% alert color="primary" %}}

Şu anda, çalışma sayfalarını görüntülere dönüştürmek için API, 3D kabarcık grafiklerini desteklememektedir.

{{% /alert %}}

## **Çalışma Sayfasını SVG'ye Dönüştürme**

SVG, Ölçeklenebilir Vektör Grafikleri anlamına gelir. SVG, iki boyutlu vektör grafikleri için XML standartlarına dayanan bir spesifikasyondur. 1999'dan beri World Wide Web Consortium (W3C) tarafından geliştirilen açık bir standarttır.

Aspose.Cells for C++, sürüm 7.1.0’den itibaren çalışma sayfalarını SVG görüntüsüne dönüştürmeyi başardı. Aşağıdaki kod parçası, bir Excel dosyasındaki çalışma sayfasını SVG dosyasına dönüştürmenin nasıl yapılacağını gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-2.go" >}}
## **Gelişmiş Konular**
- [Bir Excel Grafiğini Görüntüye Dönüştürme](/cells/tr/cpp/convert-an-excel-chart-to-image/)
- [SVG Biçiminde Grafikleri Görüntüye Dönüştürme](/cells/tr/cpp/converting-chart-to-image-in-svg-format/)
- [Görünüm Kutusu Özelliği ile Grafiksel Bir Ortama Tabloyu Dışa Aktarma](/cells/tr/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [Excel'den TIFF'e Dönüşüm İlerlemesini İzle](/cells/tr/cpp/track-conversion-progress-of-excel-to-tiff/)
