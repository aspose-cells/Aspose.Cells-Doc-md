---
title: Belirtilen Çalışma Sayfalarını PDF Olarak Kaydet
type: docs
weight: 51
url: /tr/java/save-specified-worksheets-to-pdf/
---

Varsayılan olarak, Aspose.Cells tüm **görünür** çalışma sayfalarını bir çalışma kitabında PDF dosyasına kaydeder. [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) seçeneği ile belirtilen çalışma sayfalarını PDF dosyasına kaydedebilirsiniz. Örneğin, etkin çalışma sayfasını PDF olarak kaydedebilir, tüm çalışma sayfalarını (hem görünür hem gizli çalışma sayfalarını) PDF olarak kaydedebilir, özel birden fazla çalışma sayfasını PDF olarak kaydedebilirsiniz.

## **Etkin Çalışma Sayfasını PDF Olarak Kaydet**

Sadece etkin çalışma sayfasını PDF'ye dışa aktarmak istiyorsanız, bunu [**SheetSet.Active**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--) seçeneğine [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) seçeneği ile geçerek başarabilirsiniz.

Sheet2 sayfası kaynak dosyanın [sheetset-example.xlsx](sheetset-example.xlsx) dosyasında etkin sayfadır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

## **Tüm Çalışma Sayfalarını PDF Olarak Kaydet**

[**SheetSet.Visible**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--), çalışma kitabındaki görünür sayfaları gösterir ve [**SheetSet.All**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--) görünür sayfaları ve gizli/görünmez sayfaları içeren tüm sayfaları gösterir. Tüm sayfaları PDF olarak dışa aktarmak istiyorsanız, sadece [**SheetSet.All**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--) seçeneğini [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) seçeneğine geçebilirsiniz.

Kaynak dosya [sheetset-example.xlsx](sheetset-example.xlsx) gizli Sheet3 sayfası dahil olmak üzere dört sayfayı içerir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

## **Belirtilen Çalışsayfalarını PDF olarak kaydet**
İstenen/özel birden fazla çalışma sayfasını PDF olarak dışa aktarmak istiyorsanız, [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) seçeneğine birden fazla sayfa indeksini geçerek bunu başarabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
