---
title: Golang ile C++ üzerinden Satırdaki Maksimum Sütun Endeksi ve Sütundaki Maksimum Satır Endeksi Nasıl Alınır
linktitle: Satırda Maksimum Sütun Endeksini ve Sütunda Maksimum Satır Endeksini Al
type: docs
weight: 600
url: /tr/go-cpp/get-max-index-in-row-and-column/
description: Aspose.Cells for C++ API kullanarak satırda maksimum sütun indeksini ve sütunda maksimum satır indeksini nasıl alacağınızı öğrenin.
keywords: Satırda Maksimum Sütun İndeksini Alın, Sütunda Maksimum Satır İndeksini Alın, Satırda Maksimum Veri Sütun İndeksini Alın, Sütunda Maksimum Veri Satır İndeksini Alın.
---

## **Olası Kullanım Senaryoları**
 Satırlarda veya Sütunlarda bazı verileri manipüle etmeniz gerekiyorsa, satır ve sütunların veri aralığını bilmeniz gerekir. Aspose.Cells bu özelliği sunar. Bir satırdaki maksimum sütun indeksini almak için, [Row.GetLastCell()](https://reference.aspose.com/cells/go-cpp/row/getlastcell/) ve [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/) özelliklerini elde edebilir ve ardından [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) özelliğini kullanarak maksimum sütun indeksini ve maksimum veri sütunu indeksini alabilirsiniz. Ancak, bir sütundaki maksimum satır indeksini ve maksimum satır veri indeksini almak için, sütun üzerinde bir aralık oluşturmalı, sonra aralığı gezerek son hücreyi bulmalı ve sonunda hücredeki [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) özelliğini elde etmelisiniz.

Aspose.Cells, hedeflerinize ulaşmanıza yardımcı olmak için aşağıdaki özellikler ve yöntemleri sağlar.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/go-cpp/cell/getrow/)

## **Aspose.Cells Kullanarak Satırda Maksimum Sütun İndeksini ve Sütunda Maksimum Satır İndeksini Alın**
Bu örnek aşağıdakileri göstermektedir:

1. [Örnek dosyayı](örnek.xlsx) yükleyin.
1. Maksimum sütun dizinini ve maksimum veri sütun dizinini elde etmek için satırı alın.
1. Hücredeki [Cell.GetColumn()](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/) özniteliğini alın.
1. Sütuna dayalı bir aralık oluşturun.
1. İteratörü alın ve aralığı gezin.
1. Hücredeki [Cell.GetRow()](https://reference.aspose.com/cells/go-cpp/cell/getrow/) özniteliğini alın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MaxIndexInRowAndColumn.go" >}}
