---
title: Yazdırılacak Bir Şey Olmadığında PDF Çıkışında Boş Sayfadan Kaçının
type: docs
weight: 30
url: /tr/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Aspose.Cells for Python via .NET API ile Yazdırılacak Hiçbir Şey Olmadığında PDF Çıkışındaki Boş Sayfayı Nasıl Önleyeceğinizi öğrenin.
keywords: Python Avoid Blank Page in Output PDF when there is Nothing to Print
---
##  **Olası Kullanım Senaryoları**

Excel dosyası boş olduğunda ve kullanıcı bunu Aspose.Cells for Python via .NET kullanarak PDF'e kaydettiğinde, PDF çıktısında boş bir sayfa oluşturur. Bazen bu varsayılan davranış istenmeyen bir durumdur. Aspose.Cells for Python via .NET şunları sağlar[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)Bu sorunla başa çıkmak için mülk. *yanlış** olarak ayarlarsanız, o zaman[**Hücrelerİstisna**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)PDF çıktısında yazdırılacak hiçbir şey olmadığında meydana gelecektir.

##  **Yazdırılacak Bir Şey Olmadığında PDF Çıkışında Boş Sayfadan Kaçının**

Aşağıdaki örnek kod boş bir çalışma kitabı oluşturur ve bunu PDF olarak ayarladıktan sonra kaydeder.[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)özelliği *yanlış** olarak belirtin. PDF çıktısında yazdırılacak bir şey olmadığından,[**Hücrelerİstisna**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)aşağıda gösterildiği gibi gerçekleşir.

##  **Basit kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

##  **İstisna**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
