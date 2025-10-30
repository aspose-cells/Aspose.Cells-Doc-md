---
title: Adlar ve İndeksler
type: docs
weight: 10
url: /tr/cpp/names-and-indices/
---

## **Satır ve Sütun Dizilerinden Hücre Adı Alın**
Bir hücrenin adını bulmak mümkündür, verilen satır ve sütun dizini. Bu makale açıklar.
Aspose.Cells, geliştiricilere [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) yöntemi sağlar, bu yöntem geliştiricilere bir hücre adı sağlar ve onlar satır ve sütun indekslerini sağladığında bir hücre adı alabilirler.

{{% alert color="primary" %}} 

Microsoft Excel'in aksine, satır ve sütun indisleri 1'den başlamaz, Aspose.Cells satır ve sütun indislerini 0'dan başlatır.

{{% /alert %}} 

Aşağıdaki örnek kod belirli bir satır ve sütun indeksi verildiğinde [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) kullanmanın nasıl yapıldığını gösterir. Kod aşağıdaki çıktıyı oluşturur.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn-new.cpp" >}}
## **Hücre Adından Satır ve Sütun Dizilerini Alın**
Bir hücrenin adından satır ve sütun dizinini bulmak mümkündür. Bu makale açıklar.
Aspose.Cells, [CellsHelper.CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) yöntemini sağlar, bu yöntem geliştiricilere bir hücre adı sağlar ve onlar hücrenin adından satır ve sütun indeksini alabilirler.

{{% alert color="primary" %}} 

Microsoft Excel'in aksine, satır ve sütun indisleri 1'den başlamaz, Aspose.Cells satır ve sütun indislerini 0'dan başlatır.

{{% /alert %}} 

Aşağıdaki örnek kod belirli bir hücre adından [CellsHelper::CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) kullanmanın nasıl yapıldığını gösterir. Kod aşağıdaki çıktıyı oluşturur.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
