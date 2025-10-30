---
title: Golang ile C++ kullanarak Hücre Index’ini alın
linktitle: Hücrelerin Endeksini Alın
type: docs
weight: 600
url: /tr/go-cpp/get-cells-index/
description: Satır, sütun veya hücre adı kullanarak satır veya sütun indeksinin nasıl alınacağı öğrenilir. Golang ve C++ kullanarak Aspose.Cells ile hücre adını satır ve sütun sıfır tabanlı indekslere dönüştürme
keywords: Hücrenin adı ile satır ve sütun endeksini alın, sütunun adı ile sütun endeksini alın, satırın adı ile satır endeksini alın, hücrenin adı ile endeksini alın.
---

{{% alert color="primary" %}}
Excel'in varsayılan görünümü, A1 tarzı referanstır; burada her sütun A, B, C... olarak tanımlanır ve hücreler A1, B2, C3 şeklinde adlandırılır.
Bu hücrenin hangi satır ve sütunda olduğunu bilmek isteyebilirsiniz.

{{% /alert %}}

## **Olası Kullanım Senaryoları**

Düzenli olarak satır ve sütun indeksleriyle belirli verileri manipüle etmeniz gerekiyorsa, bu hücrenin satır ve sütun indekslerini bilmeniz gerekir.
Aspose.Cells, satır ve sütun adından satır ve sütun indeksini almak için bu özelliği sunar.
Aspose.Cells, hedeflerinize ulaşmanıza yardımcı olacak aşağıdaki özellikleri ve yöntemleri sağlar:

- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/rownametoindex/)

Not: İndeksleme Aspose.Cells for C++'te sıfır tabanlıdır, ancak Satırın id'si MS Excel'de bir tabanındadır.

## **Aspose.Cells'ı Kullanarak Hücre İndekslerini Alın**

Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturun ve bazı verileri ekleyin.
1. İlk çalışsayfadaki belirli hücreyi bulun.
1. Hücrenin adına göre Satır dizinini ve Sütun dizinini alın.
1. Sütunun adına göre Sütun dizinini alın.
1. Satırın adına göre Satır dizinini alın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsIndex.go" >}}
