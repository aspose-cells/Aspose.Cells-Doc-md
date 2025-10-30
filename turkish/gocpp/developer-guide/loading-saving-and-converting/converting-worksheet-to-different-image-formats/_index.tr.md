---
title: Farklı Görüntü Biçimlerine Çalışsayı Dönüştürme
type: docs
weight: 90
url: /tr/go-cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells, bir çalışma kitabındaki bir çalışma sayfasını dışa aktarmanıza ve farklı görüntü biçimlerine dönüştürmenize olanak tanır. Bu makale, bir çalışma sayfasını farklı görüntü biçimlerine nasıl dönüştüreceğinizi açıklar.

{{% /alert %}}

## **Çalışsayıyı Görüntüye Dönüştürme**

Çalışma sayfaları analiz etmek istediğiniz verileri içerebilir. Örneğin, bir çalışma sayfası parametreleri, toplamları, yüzdeleri, istisnaları ve hesaplamaları içerebilir.

Bir geliştirici olarak, çalışma sayfalarının görüntüleri olarak gösterilmesi gerekebilir. Örneğin, bir uygulama veya web sayfasında çalışma sayfası görüntüsü kullanmanız gerekebilir. Bir Word belgesine, PDF dosyasına, PowerPoint sunumuna veya başka bir belge türüne resim eklemek isteyebilirsiniz. Kısaca, çalışma sayfasını bir görüntü olarak render edip başka yerde kullanmak istiyorsunuz.

Aspose.Cells, Excel çalışma sayfalarını görüntülere dönüştürmeyi destekler. Bu özelliği kullanmak için, programınıza veya projenize [Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) isim alanını içe aktarmanız gerekir. Bu alanda, render ve yazdırma için çeşitli kullanışlı sınıflar bulunur, örneğin, [SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) ve diğerleri.

`Aspose.Cells.Rendering.ISheetRender` sınıfı, görüntü olarak render edilecek bir çalışma sayfasını temsil eder. Bu sınıfın aşırı yüklenmiş metodu, [ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) ile, farklı özellikler veya seçeneklerle bir çalışma sayfasını resim dosyası veya dosyalarına dönüştürebilir. Birkaç görüntü formatı desteklenir, örneğin BMP, PNG, GIF, JPG, JPEG, TIFF ve EMF.

Aşağıdaki kod örneği, bir Excel dosyasındaki bir çalışma sayfasını bir görüntü dosyasına dönüştürmenin nasıl yapıldığını gösterir.

### **GoLang kullanarak Excel/Spreadsheet'i PNG'ye dönüştürün**

Lütfen, örnek kodunu, [örnek Excel dosyasını](67338402.xlsx) ve [çıktı PNG Görüntülerini](67338401.zip) inceleyin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Png.go" >}}

### **GoLang kullanarak Excel/Spreadsheet'i TIFF'e dönüştürün**

Lütfen, örnek kodunu, [örnek Excel dosyasını](67338402.xlsx) ve [çıktı TIFF Görüntüsünü](67338419.zip) inceleyin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Tiff.go" >}}

## **GoLang kullanarak Excel/Spreadsheet'i SVG'ye dönüştürün**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Svg.go" >}}

SVG, Ölçeklenebilir Vektör Grafikleri anlamına gelir. SVG, iki boyutlu vektör grafikleri için XML standartlarına dayanan bir spesifikasyondur. 1999'dan beri World Wide Web Consortium (W3C) tarafından geliştirilen açık bir standarttır.

Aspose.Cells for Go via C++, sürüm 24.12.0’den itibaren çalışma sayfalarını SVG görüntülerine dönüştürebildi.

Bu özelliği kullanabilmek için programınıza veya projenize `Aspose.Cells.Rendering` ad alanını içe aktarmanız gerekir. Render ve yazdırma için birkaç değerli sınıf içerir, örneğin `ISheetRender`, `IImageOrPrintOptions`, ve diğerleri.

`Aspose.Cells.Rendering.IImageOrPrintOptions` sınıfı, çalışma sayfasının SVG biçiminde kaydedileceğini belirtir. Aşağıdaki kod parçası, bir Excel dosyasındaki bir çalışma sayfasını SVG bir görüntü dosyasına dönüştürmeyi gösterir.

Lütfen, örnek kodunu, [örnek Excel dosyasını](67338402.xlsx) ve [çıktı SVG Görüntülerini](67338403.zip) inceleyin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_SVG.go" >}}
