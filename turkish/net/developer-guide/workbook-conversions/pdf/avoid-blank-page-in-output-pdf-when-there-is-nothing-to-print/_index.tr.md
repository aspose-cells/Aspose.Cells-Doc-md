---
title: Yazdırılacak Hiçbir Şey Olmadığında Çıktı PDF'de Boş Sayfadan Kaçının
type: docs
weight: 30
url: /tr/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Olası Kullanım Senaryoları**

Excel dosyası boş olduğunda ve kullanıcı Aspose.Cells'i kullanarak PDF'e kaydettiğinde, PDF çıktısında boş bir sayfa oluşturur. Bazen, bu varsayılan davranış istenmeyen bir durumdur. Aspose.Cells sağlar[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) Bu sorunla başa çıkmak için mülk. olarak ayarlarsanız**YANLIŞ**, o zamanlar[**Hücre İstisnası**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)PDF çıktısında yazdırılacak hiçbir şey olmadığında gerçekleşir.

## **Yazdırılacak Hiçbir Şey Olmadığında Çıktı PDF'de Boş Sayfadan Kaçının**

Aşağıdaki örnek kod, boş bir çalışma kitabı oluşturur ve ardından bunu ayarladıktan sonra PDF olarak kaydeder.[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) olarak mülkiyet**YANLIŞ**. PDF çıktısında yazdırılacak bir şey olmadığından,[**Hücre İstisnası**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)aşağıda gösterildiği gibi gerçekleşir.

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
