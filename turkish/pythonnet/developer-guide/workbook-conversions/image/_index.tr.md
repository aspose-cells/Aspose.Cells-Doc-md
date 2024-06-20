---
title: Görüntü
type: docs
weight: 300
url: /tr/python-net/convert-excel-to-image/
description: Aspose.Cells for Python via .NET API sını kullanarak Grafikleri Görüntüye Dönüştürmek.
keywords: Python Grafikleri Görüntüye Dönüştür, Python da Grafikleri Dışa Aktar via NET, Python Grafikleri Görüntüye Kaydet.
---


{{% alert color="primary" %}}

Aspose.Cells for Python via .NET size bir çalışma kitabından bir çalışma sayfasını dışa aktarma ve farklı biçimlere dönüştürme imkanı sağlar. Bu makale, bir çalışma sayfasını farklı biçimlere dönüştürmenin nasıl yapıldığını açıklar.

{{% /alert %}}

## Çalışma Kitabını TIFF'e Dönüştürme

Bir Excel dosyası çoklu sayfa içeren çoklu sayfaları içerebilir. [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender), çoklu sayfalı olarak Excel'i TIFF'e dönüştürmenizi sağlar. Ayrıca, TIFF için [Sıkıştırma](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [Renk derinliği](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/), Çözünürlük ([Yatay çözünürlük](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [Dikey çözünürlük](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)) gibi birden çok seçeneği kontrol edebilirsiniz.

Aşağıdaki kod örneği, birden çok sayfa içeren Excel dosyasını TIFF'e nasıl dönüştüreceğinizi gösterir. [Kaynak Excel dosyası](workbook-to-tiff-with-mulitiple-pages.xlsx) ve [oluşturulan TIFF görüntüsü](workbook-to-tiff-with-mulitiple-pages.tiff) referansınız için ekli.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

## **Çalışsayıyı Görüntüye Dönüştürme**

Çalışma sayfaları analiz etmek istediğiniz verileri içerebilir. Örneğin, bir çalışma sayfası parametreleri, toplamları, yüzdeleri, istisnaları ve hesaplamaları içerebilir.

Bir geliştirici olarak, çalışma sayfalarını görüntü olarak sunmanız gerekebilir. Örneğin, bir çalışma sayfasının bir görüntüsünü bir uygulamada veya web sayfasında kullanmanız gerekebilir. Bir çalışma sayfasını bir Microsoft Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna veya başka bir belge türüne eklemek isteyebilirsiniz. Basitçe söylemek gerekirse, bir çalışma sayfasını bir görüntü olarak oluşturmak istiyorsunuz ki başka bir yerde kullanabilesiniz.

Aspose.Cells for Python via .NET, Excel çalışma sayfalarını görüntülere dönüştürmeyi destekler. Bu özelliği kullanmak için programınıza veya projenize [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/) ad alanını içe aktarmanız gerekir. Rendere etme ve yazdırma için birkaç değerli sınıfa sahiptir, örneğin [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/) vb.

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) sınıfı, bir görüntüye dönüştürülecek bir çalışma sayfasını temsil eder. Farklı özelliklere veya seçeneklere sahip bir çalışma sayfasını görüntü dosyasına(dosyalarına) dönüştürebilen aşırı yüklenmiş bir [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) yöntemi vardır. Bir System.Drawing.Bitmap nesnesi döndürür ve bir görüntü dosyasını diske veya akışa kaydedebilirsiniz. BMP, PNG, GIF, JPG, JPEG, TIFF, EMF gibi birçok görüntü formatı desteklenir.

Aşağıdaki kod örneği, bir Excel dosyasındaki bir çalışma sayfasını bir görüntü dosyasına dönüştürmenin nasıl yapıldığını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

Şu anda, çalışma sayfalarını görüntülere dönüştürmek için API, 3D kabarcık grafiklerini desteklememektedir.

{{% /alert %}}

## **Çalışma Sayfasını SVG'ye Dönüştürme**

SVG, Ölçeklenebilir Vektör Grafikleri anlamına gelir. SVG, iki boyutlu vektör grafikleri için XML standartlarına dayanan bir spesifikasyondur. 1999'dan beri World Wide Web Consortium (W3C) tarafından geliştirilen açık bir standarttır.

Aspose.Cells for Python via .NET, 7.1.0 sürümünden itibaren çalışma sayfalarını SVG görüntüsüne dönüştürebilme yeteneğine sahiptir. Aşağıdaki kod örneği, bir Excel dosyasındaki bir çalışma sayfasını bir SVG görüntü dosyasına dönüştürmenin nasıl yapıldığını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

## **Gelişmiş Konular**
- [Bir Excel Grafiğini Görüntüye Dönüştürme](/cells/tr/python-net/convert-an-excel-chart-to-image/)
- [SVG Biçiminde Grafikleri Görüntüye Dönüştürme](/cells/tr/python-net/converting-chart-to-image-in-svg-format/)
- [Görünüm Kutusu Özelliği ile Grafiksel Bir Ortama Tabloyu Dışa Aktarma](/cells/tr/python-net/export-chart-to-svg-with-viewbox-attribute/)
