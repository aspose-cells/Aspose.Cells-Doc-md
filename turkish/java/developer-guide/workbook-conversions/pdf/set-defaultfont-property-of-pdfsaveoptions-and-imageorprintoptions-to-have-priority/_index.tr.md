---
title: PdfSaveOptions ve ImageOrPrintOptions'ın DefaultFont özelliğini önceliğe sahip olacak şekilde ayarlayın
type: docs
weight: 30
url: /tr/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **Olası Kullanım Senaryoları**

 ayarlarken**Varsayılan yazı tipi** mülkiyet[**PdfKaydetmeSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions) ve[**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) PDF veya görüntüye kaydetmenin bunu ayarlamasını bekleyebilirsiniz.**Varsayılan yazı tipi** çalışma kitabındaki yazı tipi eksik (yüklenmemiş) olan tüm metne.

 Genel olarak, PDF veya görüntüye kaydederken, Aspose.Cells önce Çalışma Kitabının varsayılan yazı tipini (örn.[**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) ). Çalışma kitabının varsayılan yazı tipi hala metni düzgün bir şekilde gösteremiyor/işleyemiyorsa, Aspose.Cells belirtilen yazı tipiyle oluşturmaya çalışacaktır.**Varsayılan yazı tipi** öznitelik[**PdfKaydetmeSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Beklentilerinizle başa çıkmak için, " adında bir Boolean özelliğimiz var.**CheckWorkbookDefaultFont** " içinde[**PdfKaydetmeSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) . Çalışma kitabının varsayılan yazı tipini denemeyi devre dışı bırakmak veya**Varsayılan yazı tipi** ayarlamak[**PdfKaydetmeSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) önceliğe sahip olmak.

## **PdfSaveOptions/ImageOrPrintOptions'ın DefaultFont özelliğini ayarlayın**

Aşağıdaki örnek kod bir Excel dosyasını açar. A1 hücresinde (ilk çalışma sayfasında) "Noel Saati Yazı Tipi metni" olarak ayarlanmış bir metin bulunur. Yazı tipi adı, makinede yüklü olmayan "Noel Zamanı Kişisel Kullanımı" şeklindedir. Ayarladık**Varsayılan yazı tipi**özniteliği[**PdfKaydetmeSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)"Times New Roman"a. biz de ayarladık**CheckWorkbookDefaultFont**Boole özelliği "**yanlış**A1 hücresinin metninin "Times New Roman" yazı tipiyle işlenmesini ve çalışma kitabının varsayılan yazı tipini (bu durumda "Calibri") kullanmamasını sağlar. Kod, ilk çalışma sayfasını PNG ve TIFF resim formatlarına dönüştürür. Sonunda PDF dosya biçimine dönüştürülür.

{{% alert color="primary" %}}

 varsayılan değeri***CheckWorkbookDefaultFont*** öznitelik**doğru**.

{{% /alert %}}

Bu, ekran görüntüsü[şablon dosyası](49446914.xlsx)örnek kodda kullanılmıştır.

![yapılacaklar:resim_alternatif_Metin](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Bu, ayarlandıktan sonra çıkan PNG görüntüsüdür.[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)"Times New Roman" özelliği.

![yapılacaklar:resim_alternatif_Metin](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

çıktıya bakın[TIFF](out1_imageTIFF.tiff)ayarladıktan sonra görüntü[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)"Times New Roman" özelliği.

çıktıya bakın[PDF](out1_pdf.pdf)ayarladıktan sonra dosya[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont)"Times New Roman" özelliği.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
