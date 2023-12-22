---
title: Satırda Maksimum Sütun Dizinini ve Sütunda Maksimum Satır Dizinini Alın
type: docs
weight: 600
url: /tr/net/get-max-index-in-row-and-column/
description: Aspose.Cells for .NET API aracılığıyla Satırda Maksimum Sütun Dizinini ve Sütunda Maksimum Satır Dizinini nasıl alacağınızı öğrenin.
keywords: Get Max Column Index in Row, Get Max Row Index in Column, Get Max Data Column Index in Row, Get Max Data Row Index in Column. 
---
##  **Olası Kullanım Senaryoları**
Satır veya sütunlardaki yalnızca bazı verileri değiştirmeniz gerektiğinde, satır ve sütunların veri aralığını bilmeniz gerekir. Aspose.Cells bu özelliği sunuyor. Bir satırdaki maksimum sütun indeksini elde etmek için,[Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) Ve[Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/) özelliklerini kullanın ve ardından[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) Maksimum sütun indeksini ve maksimum veri sütun indeksini elde etmek için özellik. Ancak bir sütunda maksimum satır indeksini ve maksimum satır veri indeksini elde etmek için, sütunda bir aralık oluşturmanız, ardından son hücreyi bulmak için aralığı geçmeniz ve son olarak[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) hücredeki öznitelik.

Aspose.Cells, hedeflerinize ulaşmanıza yardımcı olmak için aşağıdaki özellikleri ve yöntemleri sağlar.
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

##  **Aspose.Cells'i kullanarak Satırda Maksimum Sütun Dizinini ve Sütunda Maksimum Satır Dizinini alın**
Bu örnekte aşağıdakilerin nasıl yapılacağı gösterilmektedir:

1.  Yükle[örnek dosya](sample.xlsx).
1. Maksimum sütun dizinini ve maksimum veri sütunu dizinini alması gereken satırı alın.
1.  Elde etmek[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) hücredeki öznitelik.
1. Sütuna dayalı bir aralık oluşturun.
1. Yineleyiciyi ve geçiş aralığını alın.
1.  Elde etmek[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) hücredeki öznitelik.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}