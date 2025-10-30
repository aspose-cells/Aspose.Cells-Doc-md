---
title: Golang ile C++ kullanarak Microsoft Excel Formül İzleme Penceresine Hücre Ekleme
linktitle: Formül İzleme Penceresine Hücreler Ekleyin
description: Excel de formül izleme penceresine hücre eklemek için Aspose.Cells for C++ kullanmayı öğrenin. Bir Excel dosyası yükleyin veya oluşturun, hücreleri manipüle edin, formüller ayarlayın ve düzenlenmiş dosyayı kaydedin.
keywords: Aspose.Cells, Excel, Formül İzleme Penceresi, Hücreler, Ekleme, C++
type: docs
weight: 60
url: /tr/go-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel İzleme Penceresi, hücre değerlerini ve formüllerini uygun şekilde izlemek için kullanışlı bir araçtır. Microsoft Excel'de *İzleme Penceresi*ni açmak için *Formüller > İzleme Penceresi* seçeneğine tıklayabilirsiniz. Bu pencerede *İzleme Ekle* düğmesi bulunur ve burada hücreler denetim için eklenebilir. Benzer şekilde, Aspose.Cells API kullanarak [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/go-cpp/cellwatchcollection/add_int_int/) metodunu kullanarak hücreleri İzleme Penceresine ekleyebilirsiniz.

## **Microsoft Excel Formül İzleme Penceresine Hücreler Ekleme**

Aşağıdaki örnek kod, hücrelerin C1 ve E1 formüllerini ayarlar ve ikisini de İzleme Penceresine ekler. Daha sonra çalışma kitabını [çıktı Excel dosyası](67338481.xlsx) olarak kaydeder. Çıkış Excel dosyasını açıp *İzleme Penceresi*ni görüntülediğinizde, her iki hücreyi de ekran görüntüsünde gösterildiği gibi göreceksiniz.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCellsToMicrosoftExcelFormulaWatchWindow.go" >}}
