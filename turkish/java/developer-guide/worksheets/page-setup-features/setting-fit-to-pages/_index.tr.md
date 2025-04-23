---
title: Excel i Geniş ve Yüksek olarak Yazdırma
type: docs
weight: 200
url: /tr/java/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Bu makale, Aspose.Cells kütüphanesi kullanarak FitToPagesWide ve FitToPagesTall ayarlarının nasıl yapılacağını açıklayan kodu göstermektedir.
keywords: Java da FitToPagesWide ve FitToPagesTall Nasıl Ayarlanır, Java da FitToPagesWide ve FitToPagesTall nasıl eklenir, Excel de FitToPagesWide ve FitToPagesTall ayarları nasıl yapılır, Excel de FitToPagesWide ve FitToPagesTall nasıl temizlenir, Excel de Sığdırmak İçin Sayfaları Geniş ve Yüksek Yazdırma, Bir Sayfaya Tüm Sayfaları Yazdırma, Tüm Sayfa Sütunlarını Tek Sayfada Yazdırma.
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

Belirli bir çalışma sayfasında FitToPagesWide ve FitToPagesTall ayarlarını yapmak için: Önce [örnek dosyayı](input.xlsx) yükleyin, ardından istenen çalışma sayfası için [**Worksheet.PageSetup.setFitToPagesTall(int value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/#setFitToPagesTall-int-) ve [**Worksheet.PageSetup.setFitToPagesWide(int value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/#setFitToPagesWide-int-) metodlarını [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/) nesnesinin çağırmanız gerekir. İşte Java örneği:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-set-FitToPagesWide-FitToPagesTall.java" >}}

Çıktı sonucu:
<br>
<img src="1.png" width=60% />

## **Çalışma Sayfasını Tek Sayfada Yazdırma Aspose.Cells ile nasıl yapılır**

Çalışma sayfasını tek sayfa olarak yazdırmak için: Önce [örnek dosyayı](sample.xlsx) yükleyin, ardından [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/) nesnesinin [**PdfSaveOptions.setOnePagePerSheet(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setOnePagePerSheet-boolean-) metodunu çağırmanız gerekir. İşte Java örneği:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-OnePagePerSheet.java" >}}

Çıktı sonucu:
<br>
<img src="3.png" width=60% />


## **Aspose.Cells kullanarak Çalışma Sayfasının Tüm Sütunlarını Tek Sayfada Yazdırma**

Çalışma sayfasındaki tüm sütunları tek sayfaya yazdırmak için: Önce [örnek dosyayı](sample.xlsx) yükleyin, ardından [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/) nesnesinin [**PdfSaveOptions.setAllColumnsInOnePagePerSheet(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setAllColumnsInOnePagePerSheet-boolean-) metodunu çağırmanız gerekir. İşte Java örneği:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-AllColumnsInOnePagePerSheet.java" >}}

Çıktı sonucu:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="java" >}}
