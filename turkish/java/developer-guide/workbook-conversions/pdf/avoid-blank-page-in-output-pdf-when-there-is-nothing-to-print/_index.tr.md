---
title: Yazdırılacak Hiçbir Şey Olmadığında Çıktı PDF'sinde Boş Sayfadan Kaçının
type: docs
weight: 30
url: /tr/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Olası Kullanım Senaryoları**

Excel dosyası boş olduğunda ve kullanıcı bunu Aspose.Cells kullanarak PDF'ye kaydettiğinde, çıktı PDF'sinde boş bir sayfa oluşturur. Bazen, bu varsayılan davranış istenmeyen bir durumdur. Aspose.Cells sağlar[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) Bu sorunla başa çıkmak için mülk. olarak ayarlarsanız**yanlış**, sonra[**Hücre İstisnası**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)Çıktı PDF'sinde yazdırılacak hiçbir şey olmadığında ortaya çıkar.

## **Yazdırılacak Hiçbir Şey Olmadığında Çıktı PDF'sinde Boş Sayfadan Kaçının**

Aşağıdaki örnek kod, boş bir çalışma kitabı oluşturur ve ardından bunu ayarladıktan sonra çıktı PDF'si olarak kaydeder.[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) olarak mülkiyet**yanlış**. Çıktı PDF'sinde yazdırılacak bir şey olmadığından,[**Hücre İstisnası**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)aşağıda gösterildiği gibi gerçekleşir.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **İstisna**

{{< highlight "java" >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
