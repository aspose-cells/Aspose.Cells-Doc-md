---
title: PdfSaveOptions ve ImageOrPrintOptions ın DefaultFont özelliğinin önceliği olması
type: docs
weight: 30
url: /tr/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Olası Kullanım Senaryoları**

[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) **DefaultFont** özelliğini ayarlarken, PDF veya görüntüye kaydetmenin eksik (yüklü olmayan) bir yazı tipi karakterine sahip çalışma kitabındaki tüm metni ayarlayacağınızı bekleyebilirsiniz.

Genellikle, PDF veya görsel olarak kaydederken, Aspose.Cells for Python via .NET ilk olarak Çalışma Kitabının varsayılan yazı tipini (yani, Workbook.DefaultStyle.Font) ayarlamaya çalışır. Eğer çalışma kitabının varsayılan yazı tipi düzgün görüntüleme/yazma yapamıyorsa, Aspose.Cells for Python via .NET [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) içindeki DefaultFont özniteliğine karşılık gelen yazı tipi ile görüntülemeye çalışır.

Beklentilerinizi karşılamak için [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) içinde "**check_workbook_default_font**" adında bir Boolean özelliğimiz var. Bu özelliği **false** yaparak çalışma kitabının varsayılan fontunu kullanmayı devre dışı bırakabilir veya [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) içindeki **default_font** ayarına öncelik verebilirsiniz.

## **PdfSaveOptions/ImageOrPrintOptions'ın DefaultFont özelliğini ayarlayın**

Aşağıdaki örnek kod, bir Excel dosyasını açar. Birinci çalışma sayfasındaki A1 hücresine "Christmas Time Font text" adlı metin belirlenmiştir. Yazı tipi adı "Christmas Time Personal Use" olup, makinede yüklü değildir. [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) içindeki ***default_font*** özniteliği "Times New Roman" olarak ayarlanmıştır. Ayrıca, **check_workbook_default_font** Boole değeri **"false"** olarak ayarlanmıştır, bu da A1 hücresinin metninin "Times New Roman" yazı tipiyle görüntülendiğini ve çalışma kitabının varsayılan yazı tipinin ("Calibri") kullanılmaması gerektiğini garanti eder. Kod, ilk çalışma sayfasını PNG ve TIFF formatında render eder ve sonunda PDF dosyasına dönüştürür.

{{% alert color="primary" %}}

***CheckWorkbookDefaultFont*** özelliğinin varsayılan değeri **true**'dur.

{{% /alert %}}

Bu, örnek kodda kullanılan [şablon dosyası](49446913.xlsx) ekran görüntüsüdür.

![todo:image_alt_text](1.png)

Bu, [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) özelliğini "Times New Roman"'a ayarladıktan sonraki çıktı PNG görüntüsüdür.

![todo:image_alt_text](2.png)

[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) özelliğini "Times New Roman"'a ayarladıktan sonraki çıktı [TIFF](48496672.tiff) görüntüsünü görün.

[**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) özelliğini "Times New Roman"'a ayarladıktan sonraki çıktı [PDF](48496673.pdf) dosyasını görün.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.py" >}}

{{< app/cells/assistant language="python-net" >}}
