---
title: XLSX Dosyasını PDF Formatına Dönüştür
type: docs
weight: 30
url: /tr/python-net/convert-xlsx-file-to-pdf-format/
description: XLSX Dosyasını Aspose.Cells for Python via .NET API ile PDF Formatına nasıl dönüştüreceğinizi öğrenin.
keywords: Python Convert XLSX File to PDF Format, Convert xlsx to pdf using Python, Python xlsx to pdf, Save xlsx to pdf in python, xlsx to pdf format in Python
---
{{% alert color="primary" %}}

PDF (Taşınabilir Belge Formatı), belgeleri oluşturmak için kullanılan yazılım, donanım ve işletim sisteminden bağımsız olarak belgeleri temsil eder. PDF dosyası, cihazdan bağımsız ve çözünürlükten bağımsız bir şekilde herhangi bir metin, grafik ve resim kombinasyonuna sahip belgeler olabilir. PDF dosyaları çoğunlukla sıkıştırıldığından orijinal dosyadan daha az yer kaplar.

 Bazen Microsoft Excel dosyasını PDF'e dönüştürmeniz gerekebilir. Bunun için PDF belgesini tüm dünyaya dağıtmanıza olanak tanıyan hızlı, güvenli, doğru ve güvenilir bir çözüme ihtiyacınız vardır. Bu görevi gerçekleştirebilecek çok sayıda dönüştürme aracı vardır. Ancak orijinal Excel belgesinin düzeninin PDF çıktı dosyasında korunduğundan emin olmalısınız. Resimler, grafikler, şekiller, veri formatı, yazı tipleri, nitelikler, renkler, sayfa düzeni ayarları, metin yönlendirmesi, kenarlıklar, grafikler vb. doğru ve tam olarak oluşturulmalıdır.[Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/) yüksek kalitede dönüşüm sağlar.

Bu belge, bir Microsoft Excel belgesinin (görüntüler, grafikler, biçimlendirme vb. içeren) PDF'e nasıl dönüştürülebileceğinin kapsamlı bir şekilde anlaşılmasını sağlamak üzere tasarlanmıştır. Bu amaçla, Visual Studio.Net'te dönüştüren basit bir konsol uygulamasının nasıl oluşturulacağını gösterir. Aspose.Cells for Python via .NET API'i kullanarak PDF'e bir Excel dosyası. Dönüştürme yüksek derecede hassasiyet ve doğrulukla gerçekleştirilir.

{{% /alert %}}

##  **Excel'i PDF'e dönüştürme**

Bu örnekte şablon olarak bir Excel dosyası (SampleInput.xlsx) kullanılır. Çalışma kitabı grafik ve resim içeren çalışma sayfaları içerir. Her çalışma sayfası yazı tiplerini, nitelikleri, renkleri, gölgeleme efektlerini ve kenarlıkları kullanan farklı format türleri içerir. İlk çalışma sayfasında bir sütun grafiği, son çalışma sayfasında ise bir resim var.

###  **Şablon Excel Dosyası**

Şablon dosyasında grafikler ve Medya olarak resim dahil olmak üzere üç çalışma sayfası bulunur. İlk çalışma sayfasında grafikler ve son çalışma sayfasında aşağıdaki ekran görüntülerinde gösterildiği gibi bir resim bulunmaktadır.

|![yapılacak şey:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![yapılacak şey:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
| İlk çalışma sayfası**(Satış tahmini)**| İkinci çalışma sayfası**(Satış raporu)**|
|![yapılacak şey:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![yapılacak şey:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| Üçüncü çalışma sayfası**(Veri girişi)**| Son çalışma sayfası**(Resim)**|

###  **Dönüştürme işlemi**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

 Elektronik tablo formüller içeriyorsa, aramak en iyisidir.[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) Bu yöntem, elektronik tabloyu PDF'e dönüştürmeden hemen önce kullanılır. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}

###  **Sonuç**

Yukarıdaki kod çalıştırıldığında uygulama dizininizdeki Dosyalar klasöründe PDF numaralı bir dosya oluşturulur.
Aşağıdaki ekran görüntüleri PDF sayfalarını göstermektedir. Üstbilgilerin ve altbilgilerin aynı zamanda PDF çıkış dosyasında da tutulduğunu unutmayın.

|![yapılacak şey:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![yapılacak şey:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
| İlk çalışma sayfası**(Satış tahmini)**| İkinci çalışma sayfası**(Satış raporu)**|
|![yapılacak şey:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![yapılacak şey:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
| Üçüncü çalışma sayfası**(Veri girişi)**| Son çalışma sayfası**(Resim)**|
