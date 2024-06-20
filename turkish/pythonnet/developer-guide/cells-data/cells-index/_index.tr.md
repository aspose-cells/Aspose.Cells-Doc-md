---
title: Hücrelerin Endeksini Alın
type: docs
weight: 600
url: /tr/python-net/get-cells-index/
description: Aspose.Cells Python via .NET API si ile satırın adı olan veya sütunun adı olan bir yapıyı satır ve sütun endeksine nasıl çevireceğinizi, sütun veya hücreleri öğrenebilirsiniz. Aspose.Cells Python via .NET API si ile sütun ve satır endeksini alın.
keywords: Python Excel, Python kullanarak bir hücrenin adıyla satır endeksini ve sütun endeksini alın, Python kullanarak sütun adıyla sütun endeksini alın, Python kullanarak satır adıyla satır endeksini alın, Python kullanarak hücre adıyla endeks alın. 
---

{{% alert color="primary" %}}
Excel'in varsayılan görünümü A1 stili referanstır, her sütun A, B, C..... şeklinde adlandırılır ve hücreler A1, B2, C3... ve benzeri şekilde adlandırılır.
Bu hücrenin hangi satır ve sütun olduğunu bilmek isteyebilirsiniz.

{{% /alert %}}


## **Olası Kullanım Senaryoları**
Yalnızca belirli bir veriyi çalışsayısında satır ve sütun endeksi tarafından yönlendirmeniz gerektiğinde, o belirli hücrenin sütun ve satır endekslerini bilmeniz gerekir. 
Aspose.Cells Python via .NET, satırın, sütunun ve hücrenin adıyla satır ve sütun endeksini almanıza yardımcı olmak için aşağıdaki özellikler ve yöntemleri sağlar. 
Aspose.Cells for Python via .NET hedeflerinize ulaşmanıza yardımcı olacak aşağıdaki özelliklere ve yöntemlere sahiptir.
- [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)
- [**CellsHelper.column_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_index_to_name/#int)
- [**CellsHelper.column_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_name_to_index/#str)
- [**CellsHelper.row_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_index_to_name/#int)
- [**CellsHelper.row_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_name_to_index/#str)

Not: Python via .NET İçin Aspose.Cells'te indeksleme sıfırdan başlar, ancak MS Excel'de Satırın kimliği bir tabana dayalıdır.

## **İstenilen hücre dizinlerini Almak için Aspose.Cells for Python Excel Kütüphanesi**
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturun ve bazı verileri ekleyin.
1. İlk çalışsayfadaki belirli hücreyi bulun.
1. Hücrenin adına göre Satır dizinini ve Sütun dizinini alın.
1. Sütunun adına göre Sütun dizinini alın.
1. Satırın adına göre Satır dizinini alın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-get-index.py" >}}
