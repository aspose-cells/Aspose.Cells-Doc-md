---
title: Grafik Sayfası için PdfBookmarkEntry Oluşturma
type: docs
weight: 50
url: /tr/net/create-pdfbookmarkentry-for-chart-sheet/
---

## **Olası Kullanım Senaryoları**

Önceden, Aspose.Cells bir normal sayfa için [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) oluştururdu. Ancak şimdi Aspose.Cells, aynı zamanda bir grafik sayfası için de [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) oluşturabilir. Çünkü grafik sayfasının, A1 hücresi dışında başka hiçbir hücresi olmadığından, yalnızca A1 hücresi için [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) oluşturacaktır.

## **Grafik Tablosu için PdfBookmarkEntry Oluştur**

Aşağıdaki örnek kod, dört çalışma sayfası içeren [örnek Excel dosyasını](61767756.xlsx) yükler. Bunlardan ikisi normal çalışma sayfalarıdır ve diğer ikisi grafik çalışma sayfalarıdır. Aşağıdaki gibi dört yer imi girişi oluşturur

- Yer İmi-I
- Yer İmi-II-Chart1
- Yer İmi-III
- Yer İmi-IV-Chart2

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan [çıktı PDF'yi](61767757.pdf) göstermektedir.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-CreatePdfBookmarkEntryForChartSheet.cs" >}}
