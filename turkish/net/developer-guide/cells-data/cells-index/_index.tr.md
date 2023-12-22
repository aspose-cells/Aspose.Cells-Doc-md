---
title: Cells Dizinini Alın
type: docs
weight: 600
url: /tr/net/get-cells-index/
description: Satır, sütun veya hücre adına göre satır veya sütunu nasıl alacağınızı öğrenin. Hücrenin adını sıfır tabanlı satır ve sütun indeksine dönüştürün.
keywords: Get Row index and Column index by the name of the cell, Get Column index by the name of the column, Get Row index by the name of the row, Get the index by the name of cell. 
---
{{% alert color="primary" %}}
Excel'in varsayılan görünümü A1 stili referanstır; her sütun A, B, C.... olarak tanımlanır ve hücreler A1, B2, C3... vb. olarak adlandırılır.
Bu hücrenin hangi satır ve sütunda olduğunu bilmek isteyebilirsiniz.

{{% /alert %}}


##  **Olası Kullanım Senaryoları**
 Çalışma sayfasındaki belirli bir veriyi yalnızca satır ve sütun dizinine göre değiştirmeniz gerektiğinde, o belirli hücrenin sütun ve sütun dizinlerini bilmeniz gerekir.
 Aspose.Cells, satır, sütun ve hücre adına göre satır ve sütun indeksi almak için bu özelliği sunar.
Aspose.Cells, hedeflerinize ulaşmanıza yardımcı olmak için aşağıdaki özellikleri ve yöntemleri sağlar.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

Not: Dizin oluşturma, .Net için Aspose.Cells'de sıfır tabanlıdır, ancak Satır kimliği MS Excel'de tek tabanlıdır.

##  **Aspose.Cells'i kullanarak Cells Dizinlerini alın**
Bu örnekte aşağıdakilerin nasıl yapılacağı gösterilmektedir:

1. Bir çalışma kitabı oluşturun ve bazı veriler ekleyin.
1. İlk çalışma sayfasındaki belirli hücreyi bulun.
1. Hücre adına göre Satır indeksini ve Sütun indeksini alın.
1. Sütun adına göre Sütun dizinini alın.
1. Satır adına göre Satır dizinini alın.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}