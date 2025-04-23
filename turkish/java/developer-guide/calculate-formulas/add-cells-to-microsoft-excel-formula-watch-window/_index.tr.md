---
title: Microsoft Excel Formül İzleme Penceresine Hücreler Ekle
type: docs
weight: 20
url: /tr/java/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel İzleme Penceresi, hücre değerlerini ve formüllerini pencerede kolaylıkla izlemek için kullanışlı bir araçtır. Microsoft Excel'de, *Formüller > İzle* *Penceresi* tıklayarak *İzleme Penceresi* açabilirsiniz. İnceleme için hücre eklemek için *İzleme Ekle* düğmesini kullanabilirsiniz. Benzer şekilde, Aspose.Cells API'sını kullanarak *İzleme Penceresi*'ne hücre eklemek için [**Worksheet.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add-int-int-) yöntemini kullanabilirsiniz.

## **Microsoft Excel Formül İzleme Penceresine Hücreler Ekleme**

Aşağıdaki örnek kod, C1 ve E1 hücrelerinin formülünü ayarlar ve her ikisini de *İzleme Penceresi*'ne ekler. Ardından, işkitap (67338509.xlsx) olarak kaydeder. Çıktı Excel dosyasını açarsanız ve *İzleme Penceresi'ni* görüntüler, bu ekran görüntüsünde gösterildiği gibi her iki hücreyi göreceksiniz.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
{{< app/cells/assistant language="java" >}}
