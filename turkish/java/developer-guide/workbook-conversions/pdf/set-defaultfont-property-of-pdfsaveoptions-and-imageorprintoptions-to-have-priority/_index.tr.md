---
title: PdfSaveOptions ve ImageOrPrintOptions ın DefaultFont özelliğinin önceliği olması
type: docs
weight: 30
url: /tr/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Olası Kullanım Senaryoları**

[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) **DefaultFont** özelliğini ayarladığınızda, PDF veya görüntüye kaydetme, eksik (yüklü olmayan) bir yazı tipine sahip olan çalışma kitabındaki tüm metni **DefaultFont**'a ayarlayacağınızı beklersiniz.

Genellikle, PDF veya görüntüye kaydederken, Aspose.Cells önce çalışma kitabının varsayılan yazı tipini (yani, [**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font-)) ayarlamaya çalışır. Eğer çalışma kitabının varsayılan yazı tipi hâlâ metni düzgün gösteremiyorsa veya düzgün görüntüleyemiyorsa, Aspose.Cells [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) dosyasındaki **DefaultFont** özniteliğine karşılık gelen yazı tipiyle render etmeyi dener.

Beklentilerinizle başa çıkmak için, [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) içinde "**CheckWorkbookDefaultFont**" adlı bir Boolean özelliğimiz bulunmaktadır. Bu, çalışma kitabının varsayılan yazı tipini deneme işlevselliğini devre dışı bırakmak veya **DefaultFont** ayarlamasının [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) önceliğe sahip olmasını sağlamak için false değerine ayarlayabilirsiniz.

## **PdfSaveOptions/ImageOrPrintOptions'ın DefaultFont özelliğini ayarlayın**

Aşağıdaki örnek kod, bir Excel dosyasını açar. A1 hücresinde (ilk çalışma sayfasında) "Christmas Time Yazı Tipi metni" adlı bir metin ayarlanmıştır. Bu metnin yazı tipi "Christmas Time Personal Use" adındaki yüklü olmayan bir yazı tipidir. **DefaultFont** özelliğini **Times New Roman** olarak ayarlarız. Ayrıca **CheckWorkbookDefaultFont** Boolean özelliğini "**false**" olarak ayarlarız, bu da A1 hücresinin metnin çalışma kitabının varsayılan yazı tipini kullanmamasını sağlar (bu durumda "Calibri"). Kod, ilk çalışma sayfasını PNG ve TIFF görüntü biçimlerine dönüştürür. Son olarak PDF dosya biçimine dönüştürür.

{{% alert color="primary" %}}

***CheckWorkbookDefaultFont*** özelliğinin varsayılan değeri **true**'dur.

{{% /alert %}}

Bu, örnek kodda kullanılan [şablon dosyası](49446914.xlsx) ekran görüntüsüdür.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Bu, [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) özelliğini "Times New Roman"'a ayarladıktan sonraki çıktı PNG görüntüsüdür.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

"Times New Roman" yazı tipi [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) özelliği ayarlandıktan sonra çıktıyı [TIFF](out1_imageTIFF.tiff) görseline bakın.

"Times New Roman" yazı tipi [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont) özelliği ayarlandıktan sonra çıktıyı [PDF](out1_pdf.pdf) dosyasına bakın.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
{{< app/cells/assistant language="java" >}}
