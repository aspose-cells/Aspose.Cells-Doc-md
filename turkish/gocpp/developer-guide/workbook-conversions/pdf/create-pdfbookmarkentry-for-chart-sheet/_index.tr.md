---
title: Grafik Sayfası için PdfBookmarkEntry oluşturma Golang ve C++ ile
linktitle: Grafik Sayfası için PdfBookmarkEntry Oluşturma
type: docs
weight: 50
url: /tr/go-cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Aspose.Cells for C++ kullanarak grafik sayfaları için PdfBookmarkEntry oluşturmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Önceden, Aspose.Cells bir normal sayfa için [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) oluştururdu. Ancak şimdi Aspose.Cells, aynı zamanda bir grafik sayfası için de [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) oluşturabilir. Çünkü grafik sayfasının, A1 hücresi dışında başka hiçbir hücresi olmadığından, yalnızca A1 hücresi için [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) oluşturacaktır.

## **Grafik Tablosu için PdfBookmarkEntry Oluştur**

Aşağıdaki örnek kod, dört sayfa içeren [örnek Excel dosyasını](61767756.xlsx) yükler. İki tanesi normal sayfalar, diğer ikisi grafik sayfalarıdır. Aşağıdaki gibi dört yer imi girişleri oluşturur:

- Yer İmi-I
- Yer İmi-II-Chart1
- Yer İmi-III
- Yer İmi-IV-Chart2

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan [çıktı PDF'yi](61767757.pdf) göstermektedir.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePdfbookmarkentryForChartSheet.go" >}}
