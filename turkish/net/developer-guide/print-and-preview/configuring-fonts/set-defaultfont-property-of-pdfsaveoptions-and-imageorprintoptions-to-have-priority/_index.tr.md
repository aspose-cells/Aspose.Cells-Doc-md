---
title: PdfSaveOptions ve ImageOrPrintOptions'ın DefaultFont özelliğini önceliğe sahip olacak şekilde ayarlayın
type: docs
weight: 30
url: /tr/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **Olası Kullanım Senaryoları**

 ayarlarken**Varsayılan yazı tipi** mülkiyet**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** ve**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, PDF'ye veya resme kaydetmenin, bu DefaultFont'u çalışma kitabındaki eksik (yüklü olmayan) bir fontu olan tüm metne ayarlamasını bekleyebilirsiniz.

 Genel olarak, PDF veya görüntüye kaydederken, Aspose.Cells önce Workbook'un varsayılan yazı tipini (örn. Workbook.DefaultStyle.Font) ayarlamaya çalışır. Çalışma kitabının varsayılan yazı tipi hala metni düzgün bir şekilde gösteremiyor/işleyemiyorsa, Aspose.Cells, içinde DefaultFont özniteliğine karşı belirtilen yazı tipiyle oluşturmaya çalışacaktır.**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**.

Beklentilerinizle başa çıkmak için, " adında bir Boolean özelliğimiz var.**CheckWorkbookDefaultFont** " içinde**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** . ayarlayabilirsiniz**yanlış**çalışma kitabının varsayılan yazı tipini denemeyi devre dışı bırakmak veya**Varsayılan yazı tipi** ayarlamak**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** önceliğe sahip olmak.

## **PdfSaveOptions/ImageOrPrintOptions'ın DefaultFont özelliğini ayarlayın**

 Aşağıdaki örnek kod bir Excel dosyasını açar. A1 hücresinde (ilk çalışma sayfasında) "Noel Saati Yazı Tipi metni" olarak ayarlanmış bir metin bulunur. Yazı tipi adı, makinede yüklü olmayan "Noel Zamanı Kişisel Kullanımı" şeklindedir. Ayarladık***Varsayılan yazı tipi*** özniteliği**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** "Times New Roman"a. biz de ayarladık**CheckWorkbookDefaultFont** Boole özelliği**"yanlış"** bu, A1 hücresinin metninin "Times New Roman" yazı tipiyle oluşturulmasını ve çalışma kitabının varsayılan yazı tipini (bu durumda "Calibri") kullanmamasını sağlar. Kod, ilk çalışma sayfasını PNG ve TIFF görüntü biçimlerine dönüştürür. Sonunda bir PDF dosya formatına dönüştürülür.

{{% alert color="primary" %}}

 varsayılan değeri***CheckWorkbookDefaultFont*** öznitelik**doğru**.

{{% /alert %}}

 Bu, ekran görüntüsü[şablon dosyası](49446913.xlsx) örnek kodda kullanılmıştır.

![yapılacaklar:resim_alternatif_Metin](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Bu, ayarlandıktan sonra çıkan PNG görüntüsüdür.**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**"Times New Roman" özelliği.

![yapılacaklar:resim_alternatif_Metin](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

 çıktıya bakın[TIFF](48496672.tiff) ayarladıktan sonra görüntü**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**"Times New Roman" özelliği.

çıktıya bakın[PDF](48496673.pdf)ayarladıktan sonra dosya**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**"Times New Roman" özelliği.

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
