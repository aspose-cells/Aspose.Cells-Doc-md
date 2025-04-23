---
title: Belirtilen Çalışma Sayfalarını PDF Olarak Kaydet
type: docs
weight: 140
url: /tr/net/save-specified-worksheets-to-pdf/
---

Varsayılan olarak, Aspose.Cells tüm **görünür** çalışma sayfalarını bir çalışma kitabında PDF dosyasına kaydeder. [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) seçeneği ile belirtilen çalışma sayfalarını PDF dosyasına kaydedebilirsiniz. Örneğin, etkin çalışma sayfasını PDF olarak kaydedebilir, tüm çalışma sayfalarını (hem görünür hem gizli çalışma sayfalarını) PDF olarak kaydedebilir, özel birden fazla çalışma sayfasını PDF olarak kaydedebilirsiniz.

## **Etkin Çalışma Sayfasını PDF Olarak Kaydet**

Sadece etkin çalışma sayfasını PDF'ye dışa aktarmak istiyorsanız, bunu [**SheetSet.Active**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/) seçeneğine [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) seçeneği ile geçerek başarabilirsiniz.

Sheet2 sayfası kaynak dosyanın [sheetset-example.xlsx](sheetset-example.xlsx) dosyasında etkin sayfadır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

## **Tüm Çalışma Sayfalarını PDF Olarak Kaydet**

[**SheetSet.Visible**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/), çalışma kitabındaki görünür sayfaları gösterir ve [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) görünür sayfaları ve gizli/görünmez sayfaları içeren tüm sayfaları gösterir. Tüm sayfaları PDF olarak dışa aktarmak istiyorsanız, sadece [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) seçeneğini [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) seçeneğine geçebilirsiniz.

Kaynak dosya [sheetset-example.xlsx](sheetset-example.xlsx) gizli Sheet3 sayfası dahil olmak üzere dört sayfayı içerir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

## **Belirtilen Çalışsayfalarını PDF olarak kaydet**
İstenen/özel birden fazla çalışma sayfasını PDF olarak dışa aktarmak istiyorsanız, [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) seçeneğine birden fazla sayfa indeksini geçerek bunu başarabilirsiniz.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

## ** Çalışma Sayfalarını PDF'ye Yeniden Sırala**

Kaynak dosyayı değiştirmeden, sayfaları (örneğin ters sırada) PDF'ye yeniden sıralamak istiyorsanız, [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) seçeneğine yeniden sıralanmış sayfa indekslerini geçirerek bunu başarabilirsiniz.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ReorderSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
