---
title: Çalışma Sayfasını Farklı Görüntü Formatlarına Dönüştürme
type: docs
weight: 90
url: /tr/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

Aspose.Cells, bir çalışma kitabından bir çalışma sayfasını dışa aktarmanıza ve onu farklı görüntü formatlarına dönüştürmenize olanak tanır. Bu makalede, bir çalışma sayfasının farklı görüntü biçimlerine nasıl dönüştürüleceği açıklanmaktadır.

{{% /alert %}} 
##  **Çalışma Sayfasını Resme Dönüştürme**
Çalışma sayfaları analiz etmek istediğiniz verileri içerir. Örneğin bir çalışma sayfası parametreler, toplamlar, yüzdeler, istisnalar ve hesaplamalar içerebilir.

Bir geliştirici olarak çalışma sayfalarını resim olarak sunmanız gerekebilir. Örneğin, bir uygulamada veya web sayfasında bir çalışma sayfasının resmini kullanmanız gerekebilir. Microsoft Word belgesine, PDF dosyasına, PowerPoint sunumuna veya başka bir belge türüne resim eklemek isteyebilirsiniz. Basitçe söylemek gerekirse, başka bir yerde kullanabilmeniz için bir çalışma sayfasının resim olarak işlenmesini istiyorsunuz.

Aspose.Cells, Excel çalışma sayfalarının resimlere dönüştürülmesini destekler. Bu özelliği kullanmak için içe aktarmanız gerekir.[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)programınızın veya projenizin ad alanı. Oluşturma ve yazdırma için çeşitli değerli sınıflara sahiptir; örneğin,[Sayfa İşleme](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [Görüntü Veya Yazdırma Seçenekleri](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)ve diğerleri.

`Aspose.Cells.Rendering.ISheetRender` sınıfı, resim olarak işlenecek bir çalışma sayfasını temsil eder. Aşırı yüklenmiş bir yöntemi vardır,[Hayal etmek](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), bir çalışma sayfasını farklı niteliklere veya seçeneklere sahip görüntü dosyalarına dönüştürebilir. Çeşitli görüntü formatları desteklenir; örneğin, BMP, PNG, GIF, JPG, JPEG, EMF.

Aşağıdaki kod parçacığı, Excel dosyasındaki bir çalışma sayfasının görüntü dosyasına nasıl dönüştürüleceğini gösterir.
###  **PNG Biçimi**
 Lütfen aşağıdaki örnek koda bakın;[örnek Excel dosyası](67338402.xlsx) , ve[çıktı PNG Görüntüler](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}
<!--
### **TIFF Format**
Please see the following sample code, its [sample Excel file](67338402.xlsx), and the [output TIFF Image](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}
-->
##  **Çalışma Sayfasını SVG'e Dönüştürme**
SVG, Ölçeklenebilir Vektör Grafikleri anlamına gelir. SVG, iki boyutlu vektör grafiklerine yönelik XML standartlarını temel alan bir spesifikasyondur. World Wide Web Konsorsiyumu (W3C) tarafından 1999 yılından bu yana geliştirilmekte olan açık bir standarttır.

Aspose.Cells for C++, 18.5.0 sürümünden bu yana çalışma sayfalarını SVG resmine dönüştürebiliyor.

Bu özelliği kullanmak için `Aspose.Cells.Rendering` ad alanını programınıza veya projenize aktarın. Oluşturma ve yazdırma için birkaç değerli sınıfa sahiptir; örneğin `ISheetRender`, `IImageOrPrintOptions` ve diğerleri.

`Aspose.Cells.Rendering.IImageOrPrintOptions` sınıfı, çalışma sayfasının SVG formatında kaydedileceğini belirtir. Aşağıdaki kod parçacığı, Excel dosyasındaki bir çalışma sayfasının SVG görüntü dosyasına nasıl dönüştürüleceğini gösterir

 Lütfen aşağıdaki örnek koda bakın;[örnek Excel dosyası](67338402.xlsx) , ve[çıktı SVG Görüntüler](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}
