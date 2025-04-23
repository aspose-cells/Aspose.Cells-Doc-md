---
title: Boş sayfa olmadığında Çıktı PDF de Boş Sayfa İşlemi
type: docs
weight: 30
url: /tr/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Olası Kullanım Senaryoları**

Excel dosyası boş olduğunda ve kullanıcı Aspose.Cells'i kullanarak PDF'ye kaydettiğinde, çıktı PDF'de boş bir sayfa oluşturur. Bu varsayılan davranış bazen istenmeyebilir. Aspose.Cells, bu sorunla başa çıkmak için [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) özelliğini sağlar. Eğer bu özelliği **false** olarak ayarlarsanız, çıktı PDF'de bir şey basılacak olmadığında [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) meydana gelecektir.

## **Çıktı PDF'inde Boş Sayfa Oluşmasını Engelle**

Aşağıdaki örnek kod, boş bir çalışma kitabı oluşturur ve ardından [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) özelliğini **false** olarak ayarladıktan sonra çıktı PDF olarak kaydeder. Çıktı PDF'de yazdırılacak hiçbir şey olmadığında, aşağıda gösterildiği gibi [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) meydana gelir.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **İstisna**

{{< highlight java >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
