---
title: Çalışma Sayfasını Farklı Görüntü Formatlarına Dönüştürme
type: docs
weight: 30
url: /tr/java/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}}

Aspose.Cells, çalışma kitabından bir çalışma sayfasını dışa aktarmanıza ve farklı biçimlere dönüştürmenize olanak tanır. Bu makalede, bir çalışma sayfasının farklı biçimlere nasıl dönüştürüleceği açıklanmaktadır.

{{% /alert %}}

## **Çalışma Sayfasını Görüntüye Dönüştürme**

Bazen, bir çalışma sayfasının resmini kaydetmek yararlıdır. Görüntüler çevrimiçi olarak paylaşılabilir, diğer belgelere eklenebilir (örneğin, Microsoft Word'de yazılan raporlar veya PowerPoint sunumları).

Aspose.Cells üzerinden görüntü aktarımı sağlar**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)** sınıf. Bu sınıf, bir görüntüye dönüştürülecek çalışma sayfasını temsil eder. bu**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**sınıf sağlar**[toImage()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream))**çalışma sayfasını görüntü dosyasına dönüştürme yöntemi. BMP, PNG, JPEG, TIFF ve EMF biçimleri desteklenir.

{{% alert color="primary" %}}

Aspose.Cells for Java ayrıca TIFF biçimine dönüştürmeyi de destekler. Bir çalışma sayfasını TIFF görüntüsüne dönüştürmek için JAI kitaplığını sınıf yolunuza ekleyin.

{{% /alert %}} {{% alert color="primary" %}}

Şu anda, çalışma sayfasını API numaralı görüntüye dönüştürme, 3B kabarcık grafiklerini desteklemiyor.

{{% /alert %}}

Aşağıdaki kod, Microsoft Excel dosyasındaki bir çalışma sayfasının PNG dosyasına nasıl dönüştürüleceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Çalışma Sayfasını SVG'ye Dönüştürme**

 SVG'nin açılımı**ölçeklendirilebilir Vektör Grafiği**. SVG, iki boyutlu vektör grafikleri için XML standartlarına dayalı bir belirtimdir. World Wide Web Consortium (W3C) tarafından 1999'dan beri geliştirilmekte olan açık bir standarttır.

v7.1.0'ın piyasaya sürülmesinden bu yana,**Aspose.Cells for Java** çalışma sayfalarını SVG resimlerine dönüştürebilir.

Bu özelliği kullanmak için com.aspose.cells ad alanını programınıza veya projenize aktarmanız gerekir. Oluşturma ve yazdırma için çeşitli değerli sınıflara sahiptir, örneğin,**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**, **[WorkbookRender](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender)**, ve diğerleri.

bu**[com.aspose.cells.ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** class, çalışma sayfasının SVG formatında kaydedileceğini belirtir.

bu**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**sınıf nesnesini alır**[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** kaydetme biçimini SVG biçimine ayarlayan bir parametre olarak.

Aşağıdaki kod parçacığı, bir Excel dosyasındaki bir çalışma sayfasının bir SVG görüntü dosyasına nasıl dönüştürüleceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Aktif çalışma sayfasını bir çalışma kitabında işleyin**

Bir çalışma kitabındaki etkin çalışma sayfasını dönüştürmenin basit bir yolu, etkin sayfa dizinini ayarlamak ve ardından çalışma kitabını SVG olarak kaydetmektir. Aktif sayfayı SVG'ye dönüştürür. Aşağıdaki örnek kod bu özelliği gösterir:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## İlgili Makaleler

- [Grafiği viewBox özniteliğiyle SVG'ye aktar](/cells/tr/java/export-chart-to-svg-with-viewbox-attribute/)
- [Çalışma Sayfasını veya Grafiği İstenilen Genişlik ve Yükseklikte Görüntüye Aktarın](/cells/tr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Çalışma Sayfasını Görüntüye ve Çalışma Sayfasını Görüntüye Sayfa Sayfa Dönüştürme](/cells/tr/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
