---
title: İsimler ve İndeksler
type: docs
weight: 10
url: /tr/cpp/names-and-indices/
---
## **Satır ve Sütun İndekslerinden Cell Adını Alın**
Satır ve sütun dizini verilen bir hücrenin adını bulmak mümkündür. Bu makale nasıl yapılacağını açıklıyor.
Aspose.Cells, geliştiricilerin satır ve sütun dizini sağlaması durumunda bir hücrenin adını almasına olanak tanıyan ICellsHelper.CellIndexToName_i yöntemini sağlar.

{{% alert color="primary" %}} 

Satır ve sütun indekslerinin 1'den başladığı Microsoft Excel'in aksine, Aspose.Cells, satır ve sütun indekslerini 0'dan saymaya başlar.

{{% /alert %}} 

Aşağıdaki örnek kod, bilinen bir satır ve sütun dizini verilen bir hücrenin adına erişmek için ICellsHelper.CellIndexToName_i'nin nasıl kullanılacağını gösterir. Kod aşağıdaki çıktıyı üretir.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn.cpp" >}}
## **Cell Adından Satır ve Sütun İndekslerini Alın**
Adından hücrenin satır ve sütun indeksini bulmak mümkündür. Bu makale nasıl yapılacağını açıklıyor.
Aspose.Cells, geliştiricilerin hücrenin adından bir satır ve sütun dizini almasına olanak tanıyan ICellsHelper.CellNameToIndex_i yöntemini sağlar.

{{% alert color="primary" %}} 

Satır ve sütun indekslerinin 1'den başladığı Microsoft Excel'in aksine, Aspose.Cells, satır ve sütun indekslerini 0'dan saymaya başlar.

{{% /alert %}} 

Aşağıdaki örnek kod, hücrenin adından satır ve sütun dizinini almak için CellsHelper.CellNameToIndex'in nasıl kullanılacağını gösterir. Kod aşağıdaki çıktıyı üretir.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName.cpp" >}}
