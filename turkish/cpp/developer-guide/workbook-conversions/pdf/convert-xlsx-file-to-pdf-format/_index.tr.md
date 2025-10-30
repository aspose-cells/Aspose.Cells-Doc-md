---
title: C++ kullanarak XLSX Dosyasını PDF Formatına Dönüştürün
linktitle: XLSX Dosyasını PDF Biçimine Dönüştür
type: docs
weight: 30
url: /tr/cpp/convert-xlsx-file-to-pdf-format/
description: Aspose.Cells for C++ ile Excel dosyalarını yüksek hassasiyet ve doğrulukla PDF formatına nasıl dönüştüreceğinizi öğrenin.
---

{{% alert color="primary" %}}

PDF (Taşınabilir Belge Formatı), belgeleri belgeyi oluşturan yazılım, donanım ve işletim sisteminden bağımsız hale getirir. Bir PDF dosyası, metin, grafik ve görüntüleri cihazdan bağımsız ve çözünürlükten bağımsız olarak içerebilir. PDF'ler genellikle sıkıştırılır, bu da onları orijinal dosyadan daha az yer kaplar.

Bazen bir Microsoft Excel dosyasını PDF'ye dönüştürmeniz gerekir. Bunun için hızlı, güvenli, doğru ve güvenilir bir çözüme ihtiyacınız vardır ki dünya genelinde PDF belgeleri dağıtabilin. Bu işi yapabilen birçok dönüşüm aracı vardır. Ama önemli olan, orijinal Excel belgesinin düzeninin çıktı PDF dosyasında korunmasıdır. Resimler, grafikler, şekiller, veri biçimlendirme, yazı tipleri, öznitelikler, renkler, sayfa ayarları, metin yönü, kenarlıklar, grafikler vb. doğru ve hassas şekilde gösterilmelidir. [Aspose.Cells](https://products.aspose.com/cells/cpp/) yüksek doğrulukta dönüşüm sağlar.

Bu belge, bir Microsoft Excel belgesinin (resimler, grafikler, biçimlendirme vb. içeren) PDF'ye nasıl dönüştürüleceğine dair kapsamlı bir anlayış sağlamayı amaçlamaktadır. Bunun için, Aspose.Cells API kullanarak Excel dosyasını PDF'ye dönüştüren basit bir C++ konsol uygulaması nasıl oluşturulacağını gösterir. Dönüştürme, yüksek hassasiyet ve doğrulukla gerçekleştirilir.

{{% /alert %}}

## **Excel'i PDF'ye Dönüştürme**

Bu örnekte, şablon olarak bir Excel dosyası (SampleInput.xlsx) kullanılmıştır. Çalışma kitabında grafikler ve resimler bulunan çalışma sayfaları bulunmaktadır. Her çalışma sayfası, fontlar, özellikler, renkler, gölgeleme efektleri ve kenarlıklar kullanılarak farklı biçimlendirme türleri içermektedir. İlk çalışma sayfasında bir sütun grafiği ve son sayfada bir resim bulunmaktadır.

### **Şablon Excel Dosyası**

Şablon dosyası üç çalışma sayfası içermektedir; bunlar Medya olarak grafikler ve resimler içerir. İlk çalışma sayfasında grafikler, son çalışma sayfasında ise bir resim bulunmaktadır; aşağıdaki ekran görüntülerinde gösterildiği gibi.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|İlk çalışma sayfası **(Satış Tahmini)**|İkinci çalışma sayfası **(Satış Raporu)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Üçüncü çalışma sayfası **(Veri Girişi)**|Son çalışma sayfası **(Resim)**|

### **Dönüşüm Süreci**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    try
    {
        // Get the template excel file path
        U16String designerFile = srcDir + u"SampleInput.xlsx";

        // Specify the pdf file path
        U16String pdfFile = outDir + u"Output.out.pdf";

        // Open the template excel file
        Workbook wb(designerFile);

        // Save the pdf file
        wb.Save(pdfFile, SaveFormat::Pdf);

        std::cout << "PDF file saved successfully!" << std::endl;
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Eğer elektronik tablo formüller içeriyorsa, PDF'ye dönüştürmeden hemen önce [Workbook.CalculateFormula](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) yöntemini çağırmak en iyisidir. Bu, formüle bağlı değerlerin yeniden hesaplanmasını sağlar ve PDF'de doğru değerlerin gösterilmesini sağlar.

{{% /alert %}}

### **Sonuç**

Yukarıdaki kod çalıştırıldığında, bir PDF dosyası uygulama dizinindeki Dosyalar klasöründe oluşturulur.
Aşağıdaki ekran görüntüleri, PDF sayfalarını göstermektedir. Başlık ve altbilgilerin çıktı PDF dosyasında da korunduğuna dikkat edin.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|İlk çalışma sayfası **(Satış Tahmini)**|İkinci çalışma sayfası **(Satış Raporu)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Üçüncü çalışma sayfası **(Veri Girişi)**|Son çalışma sayfası **(Resim)**|
{{< app/cells/assistant language="cpp" >}}
