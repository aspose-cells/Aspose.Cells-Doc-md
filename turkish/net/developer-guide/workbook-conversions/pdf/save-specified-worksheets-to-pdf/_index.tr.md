---
title: Belirtilen Çalışma Sayfalarını PDF'e Kaydet
type: docs
weight: 140
url: /tr/net/save-specified-worksheets-to-pdf/
---
 Varsayılan olarak, Aspose.Cells tümünü kaydet**görünür** çalışma kitabındaki çalışma sayfalarını pdf dosyasına dönüştürme. İle**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** seçeneği ile belirtilen çalışma sayfalarını pdf dosyasına kaydedebilirsiniz. örneğin, aktif çalışma sayfasını pdf'ye kaydedebilir, tüm çalışma sayfalarını (hem görünür hem de gizli çalışma sayfaları) pdf'ye kaydedebilir, özel çoklu çalışma sayfalarını pdf'ye kaydedebilirsiniz.

##  **Etkin Çalışma Sayfasını PDF'e Kaydet**

 Yalnızca aktif sayfayı pdf olarak dışa aktarmak istiyorsanız, bunu geçerek başarabilirsiniz.**[`SheetSet.Active`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/)** ile**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** seçenek.

 `Sheet2` sayfası, kaynak dosyanın aktif sayfasıdır.[sayfa kümesi örneği.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

##  **Tüm Çalışma Sayfalarını PDF'e Kaydet**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/)** bir çalışma kitabındaki görünür sayfaları gösterir ve**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)** bir çalışma kitabındaki hem görünür sayfalar hem de gizli/görünmez sayfalar dahil olmak üzere tüm sayfaları gösterir. Tüm sayfaları pdf olarak dışa aktarmak istiyorsanız, sadece geçebilirsiniz.**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)** ile**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** seçenek.

 kaynak dosya[sayfa kümesi örneği.xlsx](sheetset-example.xlsx) gizli sayfa `Sheet3` ile dört sayfayı da içerir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

##  **Belirtilen Çalışma Sayfalarını PDF'e Kaydet**
 İstenen/özel birden çok sayfayı pdf'ye aktarmak istiyorsanız, bunu birden çok sayfa dizini ileterek elde edebilirsiniz.**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** seçenek.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

E-tablonuz formüller içeriyorsa, e-tabloyu PDF biçimine dönüştürmeden hemen önce [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)'i aramak en iyisidir. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}
