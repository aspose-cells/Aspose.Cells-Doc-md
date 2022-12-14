---
title: Yazdırılacak Hiçbir Şey Olmadığında Çıktı PDF'sinde Boş Sayfadan Kaçının
type: docs
weight: 30
url: /tr/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Olası Kullanım Senaryoları**

Excel dosyası boş olduğunda ve kullanıcı bunu Aspose.Cells kullanarak PDF'ye kaydettiğinde, çıktı PDF'sinde boş bir sayfa oluşturur. Bazen, bu varsayılan davranış istenmeyen bir durumdur. Aspose.Cells sağlar[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) Bu sorunla başa çıkmak için mülk. olarak ayarlarsanız**yanlış**, sonra[**Hücre İstisnası**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)Çıktı PDF'sinde yazdırılacak hiçbir şey olmadığında ortaya çıkar.

## **Yazdırılacak Hiçbir Şey Olmadığında Çıktı PDF'sinde Boş Sayfadan Kaçının**

Aşağıdaki örnek kod, boş bir çalışma kitabı oluşturur ve ardından bunu ayarladıktan sonra PDF olarak kaydeder.[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) olarak mülkiyet**yanlış**. Çıktı PDF'sinde yazdırılacak bir şey olmadığından,[**Hücre İstisnası**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)aşağıda gösterildiği gibi gerçekleşir.

## **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **İstisna**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
