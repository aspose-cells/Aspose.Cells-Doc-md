---
title: Çalışma Sayfasını Görüntüye ve Çalışma Sayfasını Görüntüye Sayfa Sayfa Dönüştürme
type: docs
weight: 210
url: /tr/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

Bu belge, geliştiricilere bir çalışma sayfasını bir görüntü dosyasına ve birden fazla sayfa içeren bir çalışma sayfasını sayfa başına bir görüntü dosyasına dönüştürme konusunda ayrıntılı bir anlayış sağlamak için tasarlanmıştır.

Bazen, örneğin uygulamalarda veya web sayfalarında kullanmak için çalışma sayfalarını resim olarak sunmanız gerekebilir. Görüntüleri bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna eklemeniz veya başka bir senaryoda kullanmanız gerekebilir. Basitçe, çalışma sayfasını bir görüntü olarak işlemek istiyorsunuz. Aspose.Cells API'ler, Microsoft Excel dosyalarındaki çalışma sayfalarının görüntülere dönüştürülmesini destekler. Ayrıca Aspose.Cells, bir çalışma kitabının her sayfada bir tane olmak üzere birden çok görüntü dosyasına dönüştürülmesini destekler.

{{% /alert %}}

## **Çalışma Sayfasını Görüntü Dosyasına Dönüştürmek için Aspose.Cells'i Kullanma**

Bu makale, bir çalışma sayfasını resme dönüştürmek için Aspose.Cells for Java API'in nasıl kullanılacağını gösterir. API, aşağıdakiler gibi birkaç değerli sınıf sağlar:[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**Çalışma KitabıRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) , ve bunun gibi. bu[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) class, çalışma sayfası için görüntüleri işlemek üzere bir çalışma sayfasını temsil eder ve aşırı yüklenmiş[**Hayal etmek**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)) bir çalışma sayfasını herhangi bir nitelik veya seçenek kümesiyle doğrudan görüntü dosyalarına dönüştürebilen yöntem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **Sonuç**

Yukarıdaki kodu çalıştırdıktan sonra, Sayfa1 adlı çalışma sayfası, SheetImage.jpg adlı bir resim dosyasına dönüştürülür.

**Çıktı JPG'si**

![yapılacaklar:resim_alternatif_metin](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Çalışma Sayfasını Sayfaya Göre Görüntü Dosyasına Dönüştürmek için Aspose.Cells'i Kullanma**

Bu örnek, birkaç sayfası olan bir şablon çalışma kitabından bir çalışma sayfasını sayfa başına bir görüntü dosyasına dönüştürmek için Aspose.Cells'in nasıl kullanılacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **Sonuç**

Yukarıdaki kodu çalıştırdıktan sonra, Sheet1 adlı çalışma sayfası, Sheet 1 Page 1.Tiff ve Sheet 1 Page 2.Tiff olmak üzere iki resim dosyasına (her sayfada 1 adet) dönüştürülür.

**Oluşturulan görüntü dosyası (Sayfa 1 Sayfa 1.Tiff)**

![yapılacaklar:resim_alternatif_metin](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**Oluşturulan görüntü dosyası (Sayfa 1 Sayfa 2.Tiff)**

![yapılacaklar:resim_alternatif_metin](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

Bu makalede, Aspose.Cells kullanılarak bir çalışma sayfasının bir görüntü dosyasına nasıl dönüştürüleceği ve birden çok sayfa içeren çalışma sayfalarının birden çok görüntü dosyasına (sayfa başına bir adet) nasıl dönüştürüleceği gösterilmektedir. Aspose.Cells, diğer bileşenlerden daha fazla esneklik sunar ve olağanüstü hız, verimlilik ve güvenilirlik sağlar. Sonuçlar, Aspose.Cells'in yıllarca süren araştırma, tasarım ve dikkatli ayarlamadan yararlandığını gösteriyor.

{{% /alert %}}

## İlgili Makaleler

- [Çalışma Sayfasını Farklı Görüntü Formatlarına Dönüştürme](/cells/tr/java/converting-worksheet-to-different-image-formats/)
- [Çalışma Sayfasını veya Grafiği İstenilen Genişlik ve Yükseklikte Görüntüye Aktarın](/cells/tr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
