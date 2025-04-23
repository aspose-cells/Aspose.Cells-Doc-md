---
title: Excel i Geniş ve Yüksek olarak Yazdırma
type: docs
weight: 200
url: /tr/net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Bu makale, Aspose.Cells kütüphanesi kullanarak FitToPagesWide ve FitToPagesTall ayarlarının nasıl yapılacağını açıklayan kodu göstermektedir.
keywords: C# nasıl FitToPagesWide ve FitToPagesTall ayarlanır, C# a FitToPagesWide ve FitToPagesTall nasıl eklenir, Excel de FitToPagesWide ve FitToPagesTall nasıl ayarlanır, Excel de FitToPagesWide ve FitToPagesTall Nasıl Temizlenir, Excel i Sığdırılmış Sayfa Genişliği ve Yüksekliği ile Yazdırma, Çalışma Sayfasını Tek Sayfa olarak Yazdırma, Çalışma Sayfasındaki Tüm Sütunları Tek Sayfada Yazdırma.
---

## **Giriş**

FitToPagesWide ve FitToPagesTall ayarları, e-print uygulamalarında (Microsoft Excel gibi) baskı sırasında bir e-tablonun nasıl ölçekleneceğini kontrol etmek için kullanılır. Bu ayarlar, baskı alınan çıktının yatay ve dikey olarak belirli bir sayfa sayısı içinde kalmasını sağlar. İşte her ayarın detayları:

1. FitToPagesWide: Bu ayar, baskı sonucunun kaç sayfa genişliğinde olacağını belirtir. Örneğin, FitToPagesWide 1 olarak ayarlandığında, içeriğin tek bir sayfa genişliğine sığacak şekilde ölçeklendiği anlamına gelir, sayfanın genişliği ne olursa olsun.
1. FitToPagesTall: Bu ayar, baskı sonucunun kaç sayfa yüksekliğinde olacağını belirtir. Örneğin, FitToPagesTall 1 olarak ayarlandığında, içeriğin tek bir sayfa yüksekliğine sığacak şekilde ölçeklendiği anlamına gelir, satır sayısı ne olursa olsun.

## **Neden FitToPagesWide ve FitToPagesTall Kullanılır**
İşte FitToPagesWide ve FitToPagesTall ayarlarını kullanmanın bazı nedenleri:
1. Yazdırılan Düzen Üzerinde Kontrol: Genişlik ve yükseklik olarak sayfa sayısını belirleyerek, yazdırılan belgenin okunabilir ve iyi organize edilmiş olmasını sağlayabilirsiniz, hiçbir sütun veya satır sayfalar arasında garip şekilde bölünmez.
1. Tutarlılık: Birden fazla sayfa veya rapor yazdırıyorsanız, bu ayarları kullanmak tutarlı bir format sağlar, böylece yazdırılan belgeleri karşılaştırmak ve analiz etmek daha kolay olur.
1. Profesyonel Sunum: İçeriği uygun şekilde ölçeklendirmek ve belirli sayfa sayısına sığdırmak, verilerinizin daha profesyonel ve göze hoş gelen bir sunumunu sağlar.

## **Excel'de Dosyayı Geniş ve Yüksek olarak Yazdırmak için nasıl yapılır**

Microsoft Excel'de FitToPagesWide ve FitToPagesTall ayarlarını yapmak için aşağıdaki adımları izleyin:

1. Excel çalışma kitabınızı açın ve yazdırmak istediğiniz sayfaya gidin.
1. Şerit üzerindeki Sayfa Düzeni sekmesine gidin.
1. Sayfa Yapılandırması grubunda, sağ alt köşedeki küçük oka tıklayarak Sayfa Yapılandırma iletişim kutusunu açın.
1. Sayfa Yapılandırma iletişim kutusunda, Sayfa sekmesine gidin.
1. Ölçeklendirme altında, "Sığdır" seçeneğini seçin ve ardından istediğiniz genişlik ve yükseklik sayfa sayısını belirtin: İlk kutuya kaç sayfa genişliğinde olmasını istediğinizi girin (Sığdır x sayfa genişliği). İkinci kutuya ise kaç sayfa yüksekliğinde olmasını istediğinizi girin (Sığdır y sayfa yüksekliği).
<br>
<img src="2.png" width=60% />

1. Ayarları uygulamak için Tamam'a tıklayın.


## **Aspose.Cells kullanarak Excel'i Uyumlu Sayfalar Geniş ve Yüksek olarak Yazdırma Yöntemi**

Belirli bir çalışma sayfasında FitToPagesWide ve FitToPagesTall ayarlarını yapmak için: İlk olarak, [örnek dosyayı](input.xlsx) yükleyin, ardından istediğiniz çalışma sayfası için [**Worksheet.PageSetup.FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/fittopagestall/) ve [**Worksheet.PageSetup.FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/fittopageswide/) özelliklerini [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/) nesnesinde değiştirmeniz gerekir. İşte C# örneği:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-set-FitToPagesWide-FitToPagesTall.cs" >}}

Çıktı sonucu:
<br>
<img src="1.png" width=60% />


## **Çalışma Sayfasını Tek Sayfada Yazdırma Aspose.Cells ile nasıl yapılır**

Çalışma sayfasını tek sayfa olarak yazdırmak için: İlk olarak, [örnek dosyayı](sample.xlsx) yükleyin, ardından [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/) nesnesinin [**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/onepagepersheet/) özelliğini ayarlayın. İşte C# örneği:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-OnePagePerSheet.cs" >}}

Çıktı sonucu:
<br>
<img src="3.png" width=60% />


## **Aspose.Cells kullanarak Çalışma Sayfasının Tüm Sütunlarını Tek Sayfada Yazdırma**

Çalışma sayfasının tüm sütunlarını tek sayfada yazdırmak için: Öncelikle, [örnek dosyayı](sample.xlsx) yükleyin ve ardından [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/) nesnesinin [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/allcolumnsinonepagepersheet/) özelliğini ayarlamanız gerekir. İşte C# dilinde bir örnek:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-AllColumnsInOnePagePerSheet.cs" >}}

Çıktı sonucu:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
