---
title: Boş sayfa olmadığında Çıktı PDF de Boş Sayfa İşlemi
type: docs
weight: 30
url: /tr/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Aspose.Cells for Python via .NET API ile çıktı PDF sinde Boş Sayfa Bulunmaması konusunda nasıl bir adım atmanız gerektiğini öğrenin.
keywords: Python da Çıktı PDF sinde Boş Sayfa Bulunmaması
---

## **Olası Kullanım Senaryoları**

Excel dosyası boş olduğunda ve kullanıcı bu dosyayı Aspose.Cells for Python via .NET kullanarak PDF olarak kaydettiğinde, çıktı PDF'de boş bir sayfa gösterilir. Bu varsayılan davranış bazen istenmeyebilir. Aspose.Cells for Python via .NET bu sorunla başa çıkmak için [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) özelliğini sağlar. Bu özelliği **false** olarak ayarlarsanız, çıktı PDF'de hiçbir şey yazdırılacak bir şey olmadığında **[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)** olur.

## **Çıktı PDF'inde Boş Sayfa Oluşmasını Engelle**

Aşağıdaki örnek kod, boş bir çalışma kitabı oluşturur ve ardından **false** olarak ayarlanmış olan [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) özelliğini ayarladıktan sonra PDF olarak kaydeder. Çıktı PDF'de yazdırılacak bir şey olmadığı için aşağıdaki gibi **[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)** gösterilir.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

## **İstisna**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
