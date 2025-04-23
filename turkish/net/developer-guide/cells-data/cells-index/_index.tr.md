---
title: Hücrelerin Endeksini Alın
type: docs
weight: 600
url: /tr/net/get-cells-index/
description: Satırın veya sütunun adını kullanarak satır veya sütunun nasıl alınacağını öğrenin. Hücrenin adını sıfırdan başlayarak satır ve sütun endeksine dönüştürün.
keywords: Hücrenin adı ile satır ve sütun endeksini alın, sütunun adı ile sütun endeksini alın, satırın adı ile satır endeksini alın, hücrenin adı ile endeksini alın. 
---

{{% alert color="primary" %}}
Excel'in varsayılan görünümü A1 stili referanstır, her sütun A, B, C..... şeklinde adlandırılır ve hücreler A1, B2, C3... ve benzeri şekilde adlandırılır.
Bu hücrenin hangi satır ve sütun olduğunu bilmek isteyebilirsiniz.

{{% /alert %}}


## **Olası Kullanım Senaryoları**
Yalnızca belirli bir veriyi çalışsayısında satır ve sütun endeksi tarafından yönlendirmeniz gerektiğinde, o belirli hücrenin sütun ve satır endekslerini bilmeniz gerekir. 
Aspose.Cells, satır, sütun ve hücrenin adıyla satır ve sütun endeksini almanızı sağlayan bu özelliği sunar. 
Aspose.Cells, hedeflerinize ulaşmanıza yardımcı olmak için aşağıdaki özellikler ve yöntemleri sağlar.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

Not: Aspose.Cells for .Net'te dizinleme sıfırdan başlar, ancak MS Excel'de Satır'ın kimliği bir artırla başlar.

## **Aspose.Cells'ı Kullanarak Hücre İndekslerini Alın**
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturun ve bazı verileri ekleyin.
1. İlk çalışsayfadaki belirli hücreyi bulun.
1. Hücrenin adına göre Satır dizinini ve Sütun dizinini alın.
1. Sütunun adına göre Sütun dizinini alın.
1. Satırın adına göre Satır dizinini alın.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}
{{< app/cells/assistant language="csharp" >}}
