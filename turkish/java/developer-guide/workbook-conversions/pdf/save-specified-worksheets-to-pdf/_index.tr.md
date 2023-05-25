---
title: Belirtilen Çalışma Sayfalarını PDF'e Kaydet
type: docs
weight: 51
url: /tr/java/save-specified-worksheets-to-pdf/
---
 Varsayılan olarak, Aspose.Cells tümünü kaydet**görünür** çalışma kitabındaki çalışma sayfalarını pdf dosyasına dönüştürme. İle**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** seçeneği ile belirtilen çalışma sayfalarını pdf dosyasına kaydedebilirsiniz. örneğin, aktif çalışma sayfasını pdf'ye kaydedebilir, tüm çalışma sayfalarını (hem görünür hem de gizli çalışma sayfaları) pdf'ye kaydedebilir, özel çoklu çalışma sayfalarını pdf'ye kaydedebilirsiniz.

##  **Etkin Çalışma Sayfasını PDF'e Kaydet**

 Yalnızca aktif sayfayı pdf olarak dışa aktarmak istiyorsanız, bunu geçerek başarabilirsiniz.**[`SheetSet.Active`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--)** ile**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** seçenek.

 `Sheet2` sayfası, kaynak dosyanın aktif sayfasıdır.[sayfa kümesi örneği.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

##  **Tüm Çalışma Sayfalarını PDF'e Kaydet**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--)** bir çalışma kitabındaki görünür sayfaları gösterir ve**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** bir çalışma kitabındaki hem görünür sayfalar hem de gizli/görünmez sayfalar dahil olmak üzere tüm sayfaları gösterir. Tüm sayfaları pdf olarak dışa aktarmak istiyorsanız, sadece geçebilirsiniz.**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** ile**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** seçenek.

 kaynak dosya[sayfa kümesi örneği.xlsx](sheetset-example.xlsx) gizli sayfa `Sheet3` ile dört sayfayı da içerir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

##  **Belirtilen Çalışma Sayfalarını PDF'e Kaydet**
 İstenen/özel birden çok sayfayı pdf'ye aktarmak istiyorsanız, bunu birden çok sayfa dizini ileterek elde edebilirsiniz.**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** seçenek.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

E-tablonuz formüller içeriyorsa, e-tabloyu PDF biçimine dönüştürmeden hemen önce [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--)'i aramak en iyisidir. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}
