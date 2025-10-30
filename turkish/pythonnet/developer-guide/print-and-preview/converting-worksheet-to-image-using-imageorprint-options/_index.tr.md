---
title: Resim veya Yazdır Seçeneklerini Kullanarak Çalışma Sayfasını Resme Dönüştürme
type: docs
weight: 90
url: /tr/python-net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

Bu belge, bir çalışma sayfasını bir resim dosyasına dönüştürme ve resim için farklı resim ve yazdır seçeneklerini (çözünürlük, TIFF sıkıştırma, resim formatı ve sayfa kalitesi gibi) uygulama konusunda ayrıntılı bir anlayış sağlamak amacıyla tasarlanmıştır.

{{% /alert %}}

## **Çalışma Sayfalarını Resim Olarak Kaydetme - Farklı Yaklaşımlar**

Bazen, çalışma sayfalarınızı görsel temsil olarak göstermeniz gerekebilir. Bu durumda, uygulamalar veya web sayfalarında çalışma sayfası resimlerini gösterebilirsiniz. Resimleri Word, PDF veya PowerPoint'e veya başka bir senaryoya eklemek isteyebilirsiniz. Temelde, çalışma sayfasını başka yerlerde kullanmak için resim olarak render etmek istiyorsunuz. Aspose.Cells for Python via .NET, Excel dosyalarındaki çalışma sayfalarını resme dönüştürmeyi destekler. Ayrıca, farklı seçenekler, resim biçimi, çözünürlük (dikey ve yatay), resim kalitesi ve diğer resim ve yazdırma seçenekleri de ayarlanabilir.

Bu işlem için Office Otomasyonunu deneyebilirsiniz ancak Office otomasyonunun kendi dezavantajları vardır. Güvenlik, kararlılık, ölçeklenebilirlik ve hız, fiyat ve özellikler gibi çeşitli nedenler ve sorunlar bulunmaktadır. Kısacası, birçok neden bulunmakla birlikte en önemli neden, Microsoft'un Office otomasyonuna karşı kesinlikle tavsiye etmemesidir.

Bu makale, Visual Studio .NET'te nasıl konsol uygulaması oluşturulacağı, Aspose.Cells for Python via .NET API kullanılarak farklı resim ve yazdırma seçenekleriyle bir çalışma sayfasını resme dönüştürmenin en basit ve kısa yollarını anlatır.

Programınıza/projenize [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) ad alanını eklemeniz gerekecektir. [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) vb. gibi birçok değerli sınıfı bulunmaktadır.

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) sınıfı, çalışma sayfası için resimleri oluşturmak için temsil eder, istenen öznitelikler veya seçenekler belirtilmiş çalışma sayfasını doğrudan resim dosyasına dönüştürebilen aşırı yüklenmiş [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) yöntemine sahiptir. System.Drawing.Bitmap nesnesi döndürebilir ve bir resim dosyasını disk/akışa kaydedebilirsiniz. BMP, PNG, GIFF, JPG, JPEG, TIFF, EMF ve diğerleri gibi birçok resim formatı desteklenmektedir.

## **Aspose.Cells kullanarak Çalışma Sayfasını Resme Dönüştürme ve ImageOrPrint seçenekleriyle**

### **Microsoft Excel'de şablon çalışma kitabı oluşturma**

MS Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim. Şimdi, şablon dosyasının "Sheet1" adlı çalışma sayfasını "SheetImage.tiff" adlı bir görüntü dosyasına dönüştüreceğim ve yatay ve dikey çözünürlük, TiffCompression vb. gibi farklı görüntü seçenekleri uygulayacağım.

### **Çalışma Sayfasını Bir Görüntü Dosyasına Dönüştürme**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-WorksheetToAnImage-1.py" >}}


## **WorkbookRender kullanarak Görüntü dönüşümü**

Bir TIFF görüntüsü birden fazla çerçeve içerebilir. Tüm çalışma kitabını tek bir TIFF görüntüsüne çoğaltılmış çerçeveler veya sayfalarla kaydedebilirsiniz:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-UseWorkbookRenderForImageConversion-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
