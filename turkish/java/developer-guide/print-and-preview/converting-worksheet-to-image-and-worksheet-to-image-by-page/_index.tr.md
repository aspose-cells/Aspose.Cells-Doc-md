---
title: Çalışma Sayfasını Görüntüye Dönüştürme ve Sayfa Başına Çalışma Sayfasını Görüntüye Dönüştürme
type: docs
weight: 210
url: /tr/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Bu belge, geliştiricilere bir çalışma sayfasını bir görüntü dosyasına nasıl dönüştürecekleri ve bir çalışma sayfasının birden fazla sayfasının nasıl ayrı bir görüntü dosyasına dönüştürecekleri konusunda detaylı bir anlayış sağlamak üzere tasarlanmıştır.

Bazı durumlarda, çalışma sayfalarını örneğin, uygulamalarda veya web sayfalarında kullanmak için görüntü olarak sunmanız gerekebilir. Görüntüleri bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna yerleştirmeniz gerekebilir veya başka bir senaryoda kullanmanız gerekebilir. Basitçe, çalışma sayfasını bir resim olarak oluşturmak istersiniz. Aspose.Cells API'ları, Microsoft Excel dosyalarındaki çalışma sayfalarını görüntülere dönüştürmeyi destekler. Ayrıca, Aspose.Cells bir çalışma kitabını her sayfa için bir resim dosyasına dönüştürmeyi de destekler.

{{% /alert %}}

## **Aspose.Cells Kullanarak Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Bu makale, Aspose.Cells for Java API'sını kullanarak bir çalışma sayfasını resme dönüştürme yöntemini göstermektedir. API, [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) gibi birçok değerli sınıfı içerir. [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) sınıfı, çalışma sayfası için resimleri oluşturmak için kullanılır ve birçok aşırı yüklenmiş [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)) yöntemi, herhangi bir özellik veya seçenek ayarlanmaksızın bir çalışma sayfasını doğrudan resim dosyalarına dönüştürebilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **Sonuç**

Yukarıdaki kodu çalıştırdıktan sonra, Sheet1 adlı çalışma sayfası SheetImage.jpg adlı bir resim dosyasına dönüştürülür.

**Çıktı JPG**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Aspose.Cells Kullanarak Sayfa Sayfa Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Bu örnek, birkaç sayfası olan bir şablon çalışma kitabından bir çalışma sayfasını bir resim dosyasına dönüştürmek için Aspose.Cells'ı kullanmanın nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **Sonuç**

Yukarıdaki kodu çalıştırdıktan sonra, Sheet1 adlı çalışma sayfası iki resim dosyasına dönüştürülür (her biri için bir adet) Sheet 1 Page 1.Tiff ve Sheet 1 Page 2.Tiff.

**Oluşturulan resim dosyası (Sheet 1 Page 1.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**Oluşturulan resim dosyası (Sheet 1 Page 2.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

Bu makale, bir çalışma sayfasını bir resim dosyasına dönüştürme ve Aspose.Cells kullanarak birden fazla sayfası olan çalışma sayfalarını birden fazla resim dosyasına dönüştürme (her biri için bir adet) yöntemini göstermektedir. Aspose.Cells, diğer bileşenlere göre daha fazla esneklik sunar ve olağanüstü hız, verimlilik ve güvenilirlik sağlar. Sonuçlar, Aspose.Cells'ın yıllar süren araştırma, tasarım ve dikkatli ayarlardan yararlandığını göstermektedir.

{{% /alert %}}

## İlgili Makaleler

- [Farklı Resim Formatlarına Çalışsayısı Dönüştürme](/cells/tr/java/converting-worksheet-to-different-image-formats/)
- [Belirtilen Genişlik ve Yükseklikte Çalışsayısı veya Tabloyu Resme Dışa Aktarma](/cells/tr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
