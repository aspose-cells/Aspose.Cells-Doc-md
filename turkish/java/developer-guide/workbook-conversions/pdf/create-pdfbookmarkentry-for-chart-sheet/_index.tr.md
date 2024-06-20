---
title: Grafik Sayfası için PdfBookmarkEntry Oluşturma
type: docs
weight: 50
url: /tr/java/create-pdfbookmarkentry-for-chart-sheet/
---

## **Olası Kullanım Senaryoları**

Daha öncesinde, Aspose.Cells normal bir sayfa için [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) oluştururdu. Ancak şimdi Aspose.Cells ayrıca bir grafik sayfası için de [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) oluşturabilir. Çünkü grafik sayfasında A1 hücresi dışında başka herhangi bir hücre bulunmaz, bu yüzden sadece A1 hücresi için [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) oluşturur.

## **Grafik Tablosu için PdfBookmarkEntry Oluştur**

Aşağıdaki örnek kod, dört sayfayı içeren [örnek Excel dosyasını](61767772.xlsx) yüklüyor. Bunlardan ikisi normal sayfalar ve diğer ikisi chart sayfalarıdır. Aşağıdaklarda belirtilen gibi dört sayfa yer imi oluşturur

- Yer İmi-I
- Yer İmi-II-Chart1
- Yer İmi-III
- Yer İmi-IV-Chart2

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan [çıktı PDF'sini](61767771.pdf) gösterir.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
