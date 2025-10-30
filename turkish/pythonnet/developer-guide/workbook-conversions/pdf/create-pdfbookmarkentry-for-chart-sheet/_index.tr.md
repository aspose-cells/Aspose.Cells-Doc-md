---
title: Grafik Sayfası için PdfBookmarkEntry Oluşturma
type: docs
weight: 50
url: /tr/python-net/create-pdfbookmarkentry-for-chart-sheet/
description: Aspose.Cells for Python via .NET API ile Grafik Sayfası için PdfBookmarkEntry Oluşturmayı Öğrenin.
keywords: Python ile Grafik Sayfası için PdfBookmarkEntry Oluştur, Python kullanarak Grafik Sayfası için PdfBookmarkEntry Ekle, Python ile Grafik Sayfası için PdfBookmarkEntry Ekleme, Python da Grafik Sayfası için PdfBookmarkEntry
---

## **Olası Kullanım Senaryoları**

Daha önce Aspose.Cells for Python via .NET normal bir çalışma sayfası için [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) oluştururdu. Fakat şimdi Aspose.Cells for Python via .NET aynı zamanda grafik sayfa için de [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) oluşturabilir. Grafik sayfada yalnızca A1 hücresi dışında hiçbir hücre olmadığından, yalnızca A1 için [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) oluşturacaktır.

## **Grafik Tablosu için PdfBookmarkEntry Oluştur**

Aşağıdaki örnek kod, dört çalışma sayfası içeren [örnek Excel dosyasını](61767756.xlsx) yükler. Bunlardan ikisi normal çalışma sayfalarıdır ve diğer ikisi grafik çalışma sayfalarıdır. Aşağıdaki gibi dört yer imi girişi oluşturur

- Yer İmi-I
- Yer İmi-II-Chart1
- Yer İmi-III
- Yer İmi-IV-Chart2

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan [çıktı PDF'yi](61767757.pdf) göstermektedir.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-CreatePdfBookmarkEntryForChartSheet.py" >}}
{{< app/cells/assistant language="python-net" >}}
