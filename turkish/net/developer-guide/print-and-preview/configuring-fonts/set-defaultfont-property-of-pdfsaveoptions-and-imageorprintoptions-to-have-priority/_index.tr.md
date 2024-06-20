---
title: PdfSaveOptions ve ImageOrPrintOptions ın DefaultFont özelliğinin önceliği olması
type: docs
weight: 30
url: /tr/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Olası Kullanım Senaryoları**

[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) **DefaultFont** özelliğini ayarlarken, PDF veya görüntüye kaydetmenin eksik (yüklü olmayan) bir yazı tipi karakterine sahip çalışma kitabındaki tüm metni ayarlayacağınızı bekleyebilirsiniz.

Genellikle, PDF veya görüntüye kaydederken, Aspose.Cells öncelikle Workbook'ün varsayılan yazı tipini deneyecektir (yani, Workbook.DefaultStyle.Font). Çalışma kitabının varsayılan yazı tipi hala metni düzgün gösteremiyorsa, Aspose.Cells, [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)'de belirtilen DefaultFont özelliğini kullanarak metni render etmeye çalışacaktır.

Beklentinize uyum sağlamak için, [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)'de "**CheckWorkbookDefaultFont**" adında bir Boolean özelliğimiz bulunmaktadır. Bu, çalışma kitabının varsayılan yazı tipini denemeyi devre dışı bırakmak için **false** olarak ayarlayabilir veya **CheckWorkbookDefaultFont** özelliğinin önceliği olmasını sağlamak için [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)'deki **DefaultFont** ayarına öncelik verebilirsiniz.

## **PdfSaveOptions/ImageOrPrintOptions'ın DefaultFont özelliğini ayarlayın**

Aşağıdaki örnek kod, bir Excel dosyası açar. A1 hücresinin (ilk çalışma sayfasında) "Yılbaşı Zamanı Yazı Tipi metni" olarak ayarlanmış bir metni vardır. Yazı tipi "Christmas Time Personal Use" isminde yüklü olmayan bir yazı tipidir. [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)'in ***DefaultFont*** özelliğini "Times New Roman" olarak ayarlarız. **CheckWorkbookDefaultFont** Boolean özelliğini de **"false"** olarak ayarlarız ki bu, A1 hücresinin metninin çalışma kitabının varsayılan yazı tipi olan "Calibri"yi kullanmamasını ve "Times New Roman" yazı tipiyle render edilmesini sağlar. Kod, ilk çalışma sayfasını PNG ve TIFF görüntü biçimlerine renderlar. Son olarak, bir PDF dosya biçimine renderlar.

{{% alert color="primary" %}}

***CheckWorkbookDefaultFont*** özelliğinin varsayılan değeri **true**'dur.

{{% /alert %}}

Bu, örnek kodda kullanılan [şablon dosyası](49446913.xlsx) ekran görüntüsüdür.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Bu, [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) özelliğini "Times New Roman"'a ayarladıktan sonraki çıktı PNG görüntüsüdür.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) özelliğini "Times New Roman"'a ayarladıktan sonraki çıktı [TIFF](48496672.tiff) görüntüsünü görün.

[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) özelliğini "Times New Roman"'a ayarladıktan sonraki çıktı [PDF](48496673.pdf) dosyasını görün.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
