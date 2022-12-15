---
title: Çalışma Sayfasını Farklı Görüntü Formatlarına Dönüştürme
type: docs
weight: 90
url: /tr/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

Aspose.Cells, çalışma kitabından bir çalışma sayfasını dışa aktarmanıza ve farklı görüntü biçimlerine dönüştürmenize olanak tanır. Bu makalede, bir çalışma sayfasının farklı görüntü biçimlerine nasıl dönüştürüleceği açıklanmaktadır.

{{% /alert %}} 
## **Çalışma Sayfasını Görüntüye Dönüştürme**
Çalışma sayfaları, çözümlemek istediğiniz verileri içerir. Örneğin, bir çalışma sayfası parametreler, toplamlar, yüzdeler, istisnalar ve hesaplamalar içerebilir.

Bir geliştirici olarak, çalışma sayfalarını resim olarak sunmanız gerekebilir. Örneğin, bir uygulamada veya web sayfasında bir çalışma sayfasının görüntüsünü kullanmanız gerekebilir. Microsoft Word belgesine, PDF dosyasına, PowerPoint sunumuna veya başka bir belge türüne resim eklemek isteyebilirsiniz. Basitçe söylemek gerekirse, başka bir yerde kullanabilmeniz için bir çalışma sayfasının görüntü olarak işlenmesini istiyorsunuz.

Aspose.Cells, Excel çalışma sayfalarının resimlere dönüştürülmesini destekler. Bu özelliği kullanmak için içe aktarmanız gerekir.[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.rendering)Programınıza veya projenize ad alanı. Oluşturma ve yazdırma için çeşitli değerli sınıflara sahiptir, örneğin,[ISheetRender](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_sheet_render), [IImageOrPrintOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_image_or_print_options)ve diğerleri.

`Aspose.Cells.Rendering.ISheetRender` sınıfı, görüntü olarak işlenecek bir çalışma sayfasını temsil eder. Aşırı yüklenmiş bir yöntemi vardır,[Hayal etmek](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_sheet_render#ae508827a76d0c353ab0890024ec363c5), bir çalışma sayfasını farklı özniteliklere veya seçeneklere sahip görüntü dosyalarına dönüştürebilir. BMP, PNG, GIF, JPG, JPEG, TIFF, EMF gibi çeşitli görüntü formatları desteklenir.

Aşağıdaki kod parçacığı, bir Excel dosyasındaki bir çalışma sayfasının bir görüntü dosyasına nasıl dönüştürüleceğini gösterir.
### **PNG Formatı**
 Lütfen aşağıdaki örnek koda bakın,[örnek excel dosyası](67338402.xlsx) , ve[çıktı PNG Görselleri](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG.cpp" >}}
### **TIFF Biçimi**
 Lütfen aşağıdaki örnek koda bakın,[örnek excel dosyası](67338402.xlsx) , ve[çıkış TIFF Görüntüsü](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF.cpp" >}}
## **Çalışma Sayfasını SVG'ye Dönüştürme**
SVG, Ölçeklenebilir Vektör Grafikleri anlamına gelir. SVG, iki boyutlu vektör grafikleri için XML standartlarına dayalı bir belirtimdir. World Wide Web Consortium (W3C) tarafından 1999'dan beri geliştirilmekte olan açık bir standarttır.

Aspose.Cells for C++, 18.5.0 sürümünden beri çalışma sayfalarını SVG görüntüsüne dönüştürebiliyor.

Bu özelliği kullanmak için `Aspose.Cells.Rendering` ad alanını programınıza veya projenize aktarın. Oluşturma ve yazdırma için birkaç değerli sınıfı vardır, örneğin `ISheetRender`, `IImageOrPrintOptions` ve diğerleri.

`Aspose.Cells.Rendering.IImageOrPrintOptions` sınıfı, çalışma sayfasının SVG formatında kaydedileceğini belirtir. Aşağıdaki kod parçacığı, bir Excel dosyasındaki bir çalışma sayfasının bir SVG görüntü dosyasına nasıl dönüştürüleceğini gösterir.

 Lütfen aşağıdaki örnek koda bakın,[örnek excel dosyası](67338402.xlsx) , ve[çıktı SVG Görüntüleri](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG.cpp" >}}
