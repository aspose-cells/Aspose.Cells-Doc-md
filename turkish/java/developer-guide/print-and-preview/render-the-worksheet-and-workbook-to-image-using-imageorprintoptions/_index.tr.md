---
title: ImageOrPrintOptions kullanarak Çalışma Sayfasını ve Çalışma Kitabını Görüntüye Dönüştürün
type: docs
weight: 220
url: /tr/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---
{{% alert color="primary" %}}

Bu belge, bir çalışma sayfasının veya çalışma kitabının bir görüntü dosyasına nasıl dönüştürüleceğinin ve görüntü için farklı görüntü ve yazdırma seçeneklerinin, çözünürlük, TIFF sıkıştırma, görüntü formatı ve sayfa kalitesi gibi seçeneklerin nasıl uygulanacağının ayrıntılı olarak anlaşılmasını sağlamak için tasarlanmıştır.

{{% /alert %}}

##  **genel bakış**

Bazen, çalışma sayfalarınızı resimli bir sunum olarak sunmanız gerekebilir. Çalışma sayfası görüntülerini uygulamalarınıza veya web sayfalarınıza sunmanız gerekir. Görüntüleri bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna eklemeniz veya başka bir senaryoda kullanmanız gerekebilir. Basitçe, başka bir yerde kullanabilmeniz için bir çalışma sayfasının görüntü olarak işlenmesini istiyorsunuz. Aspose.Cells, Excel dosyalarındaki çalışma sayfalarının görüntülere dönüştürülmesini destekler. Ayrıca Aspose.Cells, görüntü formatı, çözünürlük (dikey ve yatay), görüntü kalitesi ve diğer görüntü ve baskı seçenekleri gibi farklı seçeneklerin ayarlanmasını destekler.

API, birkaç değerli sınıf sağlar, örneğin,[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**Çalışma KitabıRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), vesaire.

 bu[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) class, çalışma sayfası için görüntüleri işleme görevini üstlenirken,[**Çalışma KitabıRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)bir çalışma kitabı için aynısını yapar. Yukarıda bahsedilen sınıfların her ikisi de, birkaç aşırı yüklenmiş sürüme sahiptir.*Hayal etmek*bir çalışma sayfasını veya çalışma kitabını, istediğiniz nitelikler veya seçeneklerle belirtilen görüntü dosya(lar)ına doğrudan dönüştürebilen yöntem. Görüntü dosyasını diske/akışa kaydedebilirsiniz. BMP, PNG, GIFF, JPEG, TIFF, EMF gibi desteklenen birkaç görüntü formatı vardır.

###  **Çalışma Sayfasını Resme Dönüştür**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

##  **Dönüşüm Seçenekleri**

Görüntüye belirli sayfaları kaydetmek mümkündür. Aşağıdaki kod, bir çalışma kitabındaki birinci ve ikinci çalışma sayfalarını JPG resimlerine dönüştürür.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

Veya çalışma kitabında dolaşabilir ve içindeki her çalışma sayfasını ayrı bir görüntüye dönüştürebilirsiniz:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

##  **Çalışma Kitabını Görüntüye Dönüştür:**

 Tüm çalışma kitabını görüntü formatına dönüştürmek için yukarıdaki yaklaşımı kullanabilir veya basitçe[**Çalışma KitabıRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) örneğini kabul eden sınıf[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) nesnesinin yanı sıra[**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Tüm çalışma kitabını birden fazla çerçeve veya sayfa içeren tek bir TIFF görüntüsüne kaydedebilirsiniz:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

##  İlgili Makaleler

- [Çalışma Sayfasını Farklı Görüntü Formatlarına Dönüştürme](/cells/tr/java/converting-worksheet-to-different-image-formats/)
- [Grafiği viewBox özniteliğiyle SVG'e aktarın](/cells/tr/java/export-chart-to-svg-with-viewbox-attribute/)
- [Çalışma Sayfasını veya Grafiği İstenilen Genişlik ve Yükseklikte Görüntüye Aktarın](/cells/tr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Çalışma Sayfasını Görüntüye ve Çalışma Sayfasını Görüntüye Sayfa Sayfa Dönüştürme](/cells/tr/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
