---
title: Microsoft Excel Formül İzleme Penceresine Hücreler Ekle
description: Aspose.Cells kitaplığını kullanarak Excel de formül izleme penceresine hücre eklemek için nasıl kullanılacağı. Mevcut bir Excel dosyasını yükleyerek veya yeni bir tane oluşturarak, içindeki hücreleri manipüle edebilir ve formüller belirleyebiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, Formül İzleme Penceresi, Hücreler, Ekleme
type: docs
weight: 60
url: /tr/net/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel İzleme Penceresi, hücre değerlerini ve formüllerini kolayca izlemek için kullanışlı bir araçtır. Microsoft Excel kullanarak *Formüller > İzle* *Penceresi*'ni tıklayarak *İzleme Penceresi*’ni açabilirsiniz. İçine bakılacak hücreleri eklemek için *İzle* düğmesini kullanabilirsiniz. Benzer şekilde, Aspose.Cells API'sını kullanarak hücreleri İzleme Penceresine eklemek için [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/net/aspose.cells/cellwatchcollection/methods/add/index) yöntemini kullanabilirsiniz.

## **Microsoft Excel Formül İzleme Penceresine Hücreler Ekleme**

Aşağıdaki örnek kod, C1 ve E1 hücrelerinin formülünü belirler ve her ikisini de İzleme Penceresine ekler. Daha sonra, çalışma kitabını [çıktı Excel dosyası](67338481.xlsx) olarak kaydeder. Çıktı Excel dosyasını açıp *İzleme Penceresi*’ne bakarsanız, her iki hücreyi aşağıdaki ekran görüntüsünde gösterildiği gibi görebilirsiniz.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.cs" >}}
