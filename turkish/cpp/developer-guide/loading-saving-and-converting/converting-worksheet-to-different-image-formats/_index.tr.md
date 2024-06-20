---
title: Farklı Görüntü Biçimlerine Çalışsayı Dönüştürme
type: docs
weight: 90
url: /tr/cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}} 

Aspose.Cells, bir çalışma kitabındaki bir çalışma sayfasını dışa aktarmanıza ve farklı görüntü biçimlerine dönüştürmenize olanak tanır. Bu makale, bir çalışma sayfasını farklı görüntü biçimlerine nasıl dönüştüreceğinizi açıklar.

{{% /alert %}} 
## **Çalışsayıyı Görüntüye Dönüştürme**
Çalışma sayfaları analiz etmek istediğiniz verileri içerebilir. Örneğin, bir çalışma sayfası parametreleri, toplamları, yüzdeleri, istisnaları ve hesaplamaları içerebilir.

Bir geliştirici olarak, çalışma sayfalarını görüntü olarak sunmanız gerekebilir. Örneğin, bir çalışma sayfasının bir görüntüsünü bir uygulamada veya web sayfasında kullanmanız gerekebilir. Bir çalışma sayfasını bir Microsoft Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna veya başka bir belge türüne eklemek isteyebilirsiniz. Basitçe söylemek gerekirse, bir çalışma sayfasını bir görüntü olarak oluşturmak istiyorsunuz ki başka bir yerde kullanabilesiniz.

Aspose.Cells, Excel çalışma sayfalarını görüntülere dönüştürmeyi destekler. Bu özelliği kullanabilmek için programınıza veya projenize [Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) ad alanını içe aktarmanız gerekir. Render ve yazdırma için birkaç değerli sınıf içerir, örneğin [SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) ve diğerleri.

`Aspose.Cells.Rendering.ISheetRender` sınıfı, bir çalışma sayfasını görüntü olarak oluşturacak. Değişik özelliklere veya seçeneklere sahip bir çalışma sayfasını farklı görüntü dosyalarına dönüştürebilen bir [ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) metoduna sahiptir. Çeşitli görüntü biçimleri desteklenir, örneğin BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Aşağıdaki kod örneği, bir Excel dosyasındaki bir çalışma sayfasını bir görüntü dosyasına dönüştürmenin nasıl yapıldığını gösterir.
### **PNG Biçimi**
Lütfen, örnek kodunu, [örnek Excel dosyasını](67338402.xlsx) ve [çıktı PNG Görüntülerini](67338401.zip) inceleyin.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}

### **TIFF Biçimi**
Lütfen, örnek kodunu, [örnek Excel dosyasını](67338402.xlsx) ve [çıktı TIFF Görüntüsünü](67338419.zip) inceleyin.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}

## **Çalışma Sayfasını SVG'ye Dönüştürme**
SVG, Ölçeklenebilir Vektör Grafikleri anlamına gelir. SVG, iki boyutlu vektör grafikleri için XML standartlarına dayanan bir spesifikasyondur. 1999'dan beri World Wide Web Consortium (W3C) tarafından geliştirilen açık bir standarttır.

Aspose.Cells for C++ sürümünden itibaren, çalışma sayfalarını SVG görüntüye dönüştürebilmektedir.

Bu özelliği kullanabilmek için programınıza veya projenize `Aspose.Cells.Rendering` ad alanını içe aktarmanız gerekir. Render ve yazdırma için birkaç değerli sınıf içerir, örneğin `ISheetRender`, `IImageOrPrintOptions`, ve diğerleri.

`Aspose.Cells.Rendering.IImageOrPrintOptions` sınıfı, çalışma sayfasının SVG biçiminde kaydedileceğini belirtir. Aşağıdaki kod parçası, bir Excel dosyasındaki bir çalışma sayfasını SVG bir görüntü dosyasına dönüştürmeyi gösterir.

Lütfen, örnek kodunu, [örnek Excel dosyasını](67338402.xlsx) ve [çıktı SVG Görüntülerini](67338403.zip) inceleyin.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}
