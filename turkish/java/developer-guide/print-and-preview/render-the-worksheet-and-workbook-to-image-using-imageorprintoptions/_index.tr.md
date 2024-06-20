---
title: Görüntü veya Yazdırma Seçenekleri Kullanarak Çalışsayı Yada Çalışma Kitabını Görüntüleme
type: docs
weight: 220
url: /tr/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---

{{% alert color="primary" %}}

Bu belge, bir çalışsayı yada çalışma kitabını bir resim dosyasına dönüştürme ve resim, TIFF sıkıştırması, resim formatı ve sayfa kalitesi gibi farklı resim ve yazdırma seçenekleri uygulama hakkında detaylı bir anlayış sağlamak için tasarlanmıştır.

{{% /alert %}}

## **Genel Bakış**

Bazen çalışsayılarınızı resimsel bir temsil olarak sunmanız gerekebilir. Çalışsayı resimlerini uygulamalarınıza veya web sayfalarınıza eklemeniz veya kullanmanız gerekebilir. Resimlerini bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna eklemeniz veya bunları başka bir senaryoda kullanmanız gerekebilir. Basitçe başka bir yerde kullanabilmek için çalışsayısının bir resim olarak görüntülenmesini istersiniz. Aspose.Cells, Excel dosyalarındaki çalışsayıları resme dönüştürmeyi destekler. Ayrıca, Aspose.Cells, resim formatı, çözünürlük (dikey ve yatay), resim kalitesi ve diğer resim ve yazdırma seçenekleri belirleme gibi farklı seçenekleri destekler.

API, örneğin [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) gibi birkaç değerli sınıf sağlar.

[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) sınıfı, çalışsayısı için resimleri oluşturma görevini üstlenirken [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) aynı görevi bir çalışma kitabı için yapar. Yukarıda bahsedilen her iki sınıfın da, bir çalışsayısını veya bir çalışma kitabını doğrudan dönüştürebilen *toImage* yönteminin farklı yüklenmiş sürümleri vardır ve bunlar tercih ettiğiniz özellikler veya seçeneklerle belirtilmiş resim dosyasına dönüştürebilir. Resim dosyasını diske/akışa kaydedebilirsiniz. BMP, PNG, GIFF, JPEG, TIFF, EMF ve benzeri birçok resim formatı desteklenmektedir.

### **Çalışsayısını Resme Dönüştür**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **Dönüşüm Seçenekleri**

Belirli sayfaları resme kaydetmek mümkündür. Aşağıdaki kod, bir çalışma kitabındaki ilk ve ikinci çalışsayılarını JPG resimlerine dönüştürür.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

Veya çalışma kitabı üzerinde döngü yaparak her çalışsayısını ayrı bir resime dönüştürebilirsiniz:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **Çalışma Kitabını Resme Dönüştür:**

Tüm çalışma kitabını resim formatına dönüştürmek için yukarıdaki yaklaşımı kullanabilir veya sadece [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) sınıfını ve aynı zamanda [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfının bir örneğini ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) nesnesini kabul eden basitçe kullanabilirsiniz.

Tüm çalışma kitabını tek bir TIFF resme çoklu çerçeve veya sayfa olarak kaydedebilirsiniz:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## İlgili Makaleler

- [Farklı Resim Formatlarına Çalışsayısı Dönüştürme](/cells/tr/java/converting-worksheet-to-different-image-formats/)
- [Görünüm Kutusu Özelliği ile Grafiksel Bir Ortama Tabloyu Dışa Aktarma](/cells/tr/java/export-chart-to-svg-with-viewbox-attribute/)
- [Belirtilen Genişlik ve Yükseklikte Çalışsayısı veya Tabloyu Resme Dışa Aktarma](/cells/tr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Çalışsayısı veya Sayfa Görseline ve Sayfa Sayfasına Çalışsayısı Dönüştürme](/cells/tr/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
