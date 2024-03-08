---
title: Image
type: docs
weight: 300
url: /tr/python-net/convert-excel-to-image/
description: Grafiği Aspose.Cells for Python via .NET API kullanarak Image'e dönüştürün.
keywords: Python Convert Chart to Image, Export Chart to Image in Python via NET, Python Save Chart to Image.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, çalışma kitabından bir çalışma sayfasını dışa aktarmanıza ve onu farklı formatlara dönüştürmenize olanak tanır. Bu makalede, bir çalışma sayfasının farklı biçimlere nasıl dönüştürüleceği açıklanmaktadır.

{{% /alert %}}

##  Çalışma Kitabını TIFF'e Dönüştürme

 Bir Excel dosyası birden çok sayfa içeren birden çok sayfa içerebilir.[Çalışma Kitabı Oluşturma](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) Excel'i birden fazla sayfalı TIFF'e dönüştürmenize olanak tanır. Ayrıca TIFF için birden fazla seçeneği kontrol edebilirsiniz.[Sıkıştırma](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [Renk derinliği](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/), Çözünürlük([Yatay çözünürlük](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [Dikey çözünürlük](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

 Aşağıdaki kod parçacığı, Excel'in birden çok sayfalı TIFF'e nasıl dönüştürüleceğini gösterir.[kaynak Excel dosyası](workbook-to-tiff-with-mulitiple-pages.xlsx) Ve[TIFF resmi oluşturuldu](workbook-to-tiff-with-mulitiple-pages.tiff) referansınız için eklenmiştir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

##  **Çalışma Sayfasını Image'e Dönüştürme**

Çalışma sayfaları analiz etmek istediğiniz verileri içerir. Örneğin bir çalışma sayfası parametreler, toplamlar, yüzdeler, istisnalar ve hesaplamalar içerebilir.

Bir geliştirici olarak çalışma sayfalarını resim olarak sunmanız gerekebilir. Örneğin, bir uygulamada veya web sayfasında bir çalışma sayfasının resmini kullanmanız gerekebilir. Microsoft Word belgesine, PDF dosyasına, PowerPoint sunumuna veya başka bir belge türüne resim eklemek isteyebilirsiniz. Basitçe söylemek gerekirse, başka bir yerde kullanabilmeniz için bir çalışma sayfasının resim olarak işlenmesini istiyorsunuz.

Aspose.Cells for Python via .NET, Excel çalışma sayfalarının resimlere dönüştürülmesini destekler. Bu özelliği kullanmak için içe aktarmanız gerekir.**[aspose.cells.rendering](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/)**programınızın veya projenizin ad alanı. Oluşturma ve yazdırma için çeşitli değerli sınıflara sahiptir, örneğin *[Sayfa İşleme](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**, *[Görüntü Veya Yazdırma Seçenekleri](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/)**, *[Çalışma Kitabı Oluşturma](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/)**, ve diğerleri.

**[SheetRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**sınıf, görüntü olarak işlenecek bir çalışma sayfasını temsil eder. Aşırı yüklenmiş bir yönteme sahiptir, *[Hayal etmek](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)**, bir çalışma sayfasını farklı niteliklere veya seçeneklere sahip görüntü dosyalarına dönüştürebilir. Bir System.Drawing.Bitmap nesnesi döndürür ve bir görüntü dosyasını diske veya akışa kaydedebilirsiniz. Çeşitli görüntü formatları desteklenir; örneğin BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Aşağıdaki kod parçacığı, Excel dosyasındaki bir çalışma sayfasının görüntü dosyasına nasıl dönüştürüleceğini gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

Şu anda, çalışma sayfalarını resimlere dönüştürmek için kullanılan API, 3B kabarcık grafiklerini desteklememektedir.

{{% /alert %}}

##  **Çalışma Sayfasını SVG'e Dönüştürme**

SVG, Ölçeklenebilir Vektör Grafikleri anlamına gelir. SVG, iki boyutlu vektör grafiklerine yönelik XML standartlarını temel alan bir spesifikasyondur. World Wide Web Konsorsiyumu (W3C) tarafından 1999 yılından bu yana geliştirilmekte olan açık bir standarttır.

Aspose.Cells for Python via .NET, 7.1.0 sürümünden bu yana çalışma sayfalarını SVG resmine dönüştürebiliyor. Aşağıdaki kod parçacığı, Excel dosyasındaki bir çalışma sayfasının SVG görüntü dosyasına nasıl dönüştürüleceğini gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

##  **İleri konular**
- [Excel Grafiğini Image'e dönüştürün](/cells/tr/python-net/convert-an-excel-chart-to-image/)
- [Grafiği SVG Formatında Image'e Dönüştürme](/cells/tr/python-net/converting-chart-to-image-in-svg-format/)
- [ViewBox özelliğiyle Grafiği SVG'e aktar](/cells/tr/python-net/export-chart-to-svg-with-viewbox-attribute/)
