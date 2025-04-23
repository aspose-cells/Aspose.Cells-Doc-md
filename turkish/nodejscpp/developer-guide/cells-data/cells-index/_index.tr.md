---
title: Hücrelerin Endeksini Alın
type: docs
weight: 600
url: /tr/nodejs-cpp/get-cells-index/
description: Satırın veya sütunun adını kullanarak satır veya sütunun nasıl alınacağını öğrenin. Hücrenin adını sıfırdan başlayarak satır ve sütun endeksine dönüştürün.
keywords: Hücrenin adı ile satır ve sütun endeksini alın, sütunun adı ile sütun endeksini alın, satırın adı ile satır endeksini alın, hücrenin adı ile endeksini alın. 
---

{{% alert color="primary" %}}
Excel'in varsayılan görünümü A1 stili referanstır, her sütun A, B, C..... şeklinde adlandırılır ve hücreler A1, B2, C3... ve benzeri şekilde adlandırılır.
Bu hücrenin hangi satır ve sütun olduğunu bilmek isteyebilirsiniz.

{{% /alert %}}


## **Olası Kullanım Senaryoları**
Yalnızca belirli bir veriyi çalışsayısında satır ve sütun endeksi tarafından yönlendirmeniz gerektiğinde, o belirli hücrenin sütun ve satır endekslerini bilmeniz gerekir. 
Aspose.Cells for Node.js via C++, satır, sütun ve hücre adlarıyla satır ve sütun indekslerini alabileceğiniz özelliği sunar. 
Aspose.Cells for Node.js via C++, aşağıdaki özellikler ve metodlar sağlar.
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowNameToIndex-string-)

Not: Aspose.Cells for Node.js via C++'te indeksleme sıfır tabanlıdır, ancak MS Excel'de Satırın kimliği bir tabanındadır.

## **Aspose.Cells for Node.js via C++ kullanarak Hücreler Dizini Alma**
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturun ve bazı verileri ekleyin.
1. İlk çalışsayfadaki belirli hücreyi bulun.
1. Hücrenin adına göre Satır dizinini ve Sütun dizinini alın.
1. Sütunun adına göre Sütun dizinini alın.
1. Satırın adına göre Satır dizinini alın.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-get-index.js" >}}
