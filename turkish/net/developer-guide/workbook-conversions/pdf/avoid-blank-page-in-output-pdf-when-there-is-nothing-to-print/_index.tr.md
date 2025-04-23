---
title: Boş sayfa olmadığında Çıktı PDF de Boş Sayfa İşlemi
type: docs
weight: 30
url: /tr/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Olası Kullanım Senaryoları**

Excel dosyası boş olduğunda ve kullanıcı Aspose.Cells'i kullanarak PDF'ye kaydettiğinde, çıktı PDF'de boş bir sayfa oluşturur. Bu varsayılan davranış bazen istenmeyebilir. Aspose.Cells, bu sorunla başa çıkmak için [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) özelliğini sağlar. Eğer bu özelliği **false** olarak ayarlarsanız, çıktı PDF'de bir şey basılacak olmadığında [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) meydana gelecektir.

## **Çıktı PDF'inde Boş Sayfa Oluşmasını Engelle**

Aşağıdaki örnek kod, boş bir çalışma kitabı oluşturur ve ardından **false** olarak ayarlanmış olan [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) özelliğini ayarladıktan sonra PDF olarak kaydeder. Çıktı PDF'de yazdırılacak bir şey olmadığı için aşağıdaki gibi **[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)** gösterilir.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **İstisna**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
