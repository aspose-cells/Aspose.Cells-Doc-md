---
title: Satırda Maksimum Sütun Endeksini ve Sütunda Maksimum Satır Endeksini Al
type: docs
weight: 600
url: /tr/nodejs-cpp/get-max-index-in-row-and-column/
description: Aspose.Cells for Node.js via C++ API aracılığıyla Satırdaki Maksimum Sütun İndeksi ve Sütundaki Maksimum Satır İndeksi Nasıl Alınır öğrenin.
keywords: Node.js C++ aracılığıyla Satırda Maksimum Sütun İndeksi Al, Sütunda Maksimum Satır İndeksi Al, Satırdaki Maksimum Veri Sütunu İndeksi Al, Sütundaki Maksimum Veri Satırı İndeksi Al.
---

## **Olası Kullanım Senaryoları**
Satır veya sütunlarda sadece veriyle işlem yapmanız gerekiyorsa, satır ve sütunların veri aralığını bilmeniz gerekir. Aspose.Cells for Node.js via C++ bu özelliği sunar. Bir satırda maksimum sütun indeksini almak için [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--) ve [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--) yöntemlerini edinebilir ve sonra [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) yöntemini kullanarak maksimum sütun ve veri sütunu indekslerini alabilirsiniz. Ancak, sütundaki maksimum satır ve satır verisi indeksini almak için, önce sütun üzerinde bir aralık oluşturmanız, aralığı tarayarak son hücreyi bulmanız ve sonunda hücrede [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) metodunu çağırmanız gerekir.

Aspose.Cells for Node.js via C++, aşağıdaki özellikler ve metodlar sağlar.
- [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--)
- [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)
- [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)
- [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)

## **Satırda Maksimum Sütun İndeksi ve Sütunda Maksimum Satır İndeksi Alın**
Bu örnek aşağıdakileri göstermektedir:

1. [Örnek dosyayı](örnek.xlsx) yükleyin.
1. Maksimum sütun dizinini ve maksimum veri sütun dizinini elde etmek için satırı alın.
1. Hücrede [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) metodunu çağırın.
1. Sütuna dayalı bir aralık oluşturun.
1. İteratörü alın ve aralığı gezin.
1. Hücrede [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) metodunu çağırın.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-max-index-in-row-and-column.js" >}}

