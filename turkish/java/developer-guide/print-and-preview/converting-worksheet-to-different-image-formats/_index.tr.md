---
title: Farklı Görüntü Biçimlerine Çalışsayı Dönüştürme
type: docs
weight: 30
url: /tr/java/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells, bir çalışma kitabından çalışsayı dışa aktarmanıza ve farklı biçimlere dönüştürmenize olanak tanır. Bu makale, bir çalışsayının farklı biçimlere nasıl dönüştürüleceğini açıklar.

{{% /alert %}}

## **Çalışsayıyı Görüntüye Dönüştürme**

Bazen bir çalışma sayfasının resmini kaydetmek faydalı olabilir. Görseller çevrimiçi paylaşılabilir, diğer belgelere eklenebilir (örneğin, Microsoft Word’de yazılmış raporlar veya Powerpoint sunumları).

Aspose.Cells, çalışma sayfasının görüntüye dönüşümünü sağlayan [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) sınıfını sağlar. Bu sınıf, bir görüntü dosyasına dönüştürmek için [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) yöntemini sağlar. BMP, PNG, JPEG, TIFF ve EMF biçimlerini destekler.

{{% alert color="primary" %}}

Aspose.Cells for Java ayrıca TIFF biçimine dönüşümü destekler. Bir çalışma sayfasını bir TIFF görüntüye dönüştürmek için, JAI kütüphanesini sınıf yolunuza ekleyin.

{{% /alert %}} {{% alert color="primary" %}}

Şu an, çalışma sayfasını görüntüye dönüştürme API’si 3D-bubble grafiklerini desteklememektedir.

{{% /alert %}}

Aşağıdaki kod, bir Microsoft Excel dosyasındaki çalışma sayfasını bir PNG dosyasına dönüştürmesini göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Çalışma Sayfasını SVG'ye Dönüştürme**

SVG, **Ölçeklenebilir Vektör Grafikleri** anlamına gelir. SVG, iki boyutlu vektör grafikleri için XML standartlarına dayalı bir özellikdir. 1999 yılından bu yana W3C (World Wide Web Consortium) tarafından geliştirilen açık bir standarttır.

V7.1.0’ın yayınlanmasıyla birlikte, **Aspose.Cells for Java** çalışma sayfalarını SVG görüntülerine dönüştürebilir.

Bu özelliği kullanmak için, com.aspose.cells ad alanını programınıza veya projenize içe aktarmanız gerekmektedir. Örneğin, render ve yazdırma için [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender) ve diğer değerli sınıflar sağlar.

[**com.aspose.cells.ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) sınıfı, çalışma sayfasının SVG biçiminde kaydedileceğini belirtir.

[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) sınıfı, SVG biçimine kaydetme formatını ayarlayan [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) nesnesini parametre olarak alır.

Aşağıdaki kod parçası, bir Excel dosyasındaki çalışma sayfasını bir SVG görüntü dosyasına dönüştürmenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Bir çalışma kitabındaki etkin çalışma sayfasını render et**

Bir çalışma kitabındaki etkin çalışma sayfasını dönüştürmenin basit bir yolu etkin sayfa dizinini ayarlayıp ardından çalışma kitabını SVG olarak kaydetmektir. Bu, etkin sayfayı SVG'ye dönüştürecektir. Aşağıdaki örnek kod bu özelliği göstermektedir:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## İlgili Makaleler

- [Görünüm Kutusu Özelliği ile Grafiksel Bir Ortama Tabloyu Dışa Aktarma](/cells/tr/java/export-chart-to-svg-with-viewbox-attribute/)
- [Belirtilen Genişlik ve Yükseklikte Çalışsayısı veya Tabloyu Resme Dışa Aktarma](/cells/tr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Çalışsayısı veya Sayfa Görseline ve Sayfa Sayfasına Çalışsayısı Dönüştürme](/cells/tr/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
{{< app/cells/assistant language="java" >}}
