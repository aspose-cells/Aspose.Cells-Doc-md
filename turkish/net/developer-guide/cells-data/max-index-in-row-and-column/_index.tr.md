---
title: Satırda Maksimum Sütun Endeksini ve Sütunda Maksimum Satır Endeksini Al
type: docs
weight: 600
url: /tr/net/get-max-index-in-row-and-column/
description: Aspose.Cells for .NET API aracılığıyla Satırda Maksimum Sütun İndeksini ve Sütunda Maksimum Satır İndeksini Nasıl Alınır öğrenin.
keywords: Satırda Maksimum Sütun İndeksini Alın, Sütunda Maksimum Satır İndeksini Alın, Satırda Maksimum Veri Sütun İndeksini Alın, Sütunda Maksimum Veri Satır İndeksini Alın. 
---

## **Olası Kullanım Senaryoları**
Yalnızca bazı verileri satırlarda veya sütunlarda değiştirmeniz gerektiğinde, satırların ve sütunların veri aralığını bilmeniz gerekir. Aspose.Cells bu özelliği sunar. Bir satırdaki maksimum sütun endeksini almak için [Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) ve [Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/) özelliklerini alabilir ve sonra [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) özelliğini kullanarak maksimum sütun endeksini ve maksimum veri sütun endeksini alabilirsiniz. Ancak, bir sütundaki maksimum satır endeksini ve maksimum satır veri endeksini almak için, sütun üzerinde bir aralık oluşturmanız, ardından aralığı dolaşmanız ve son olarak hücredeki [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) özniteliğini almanız gerekir.

Aspose.Cells, hedeflerinize ulaşmanıza yardımcı olmak için aşağıdaki özellikler ve yöntemleri sağlar.
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

## **Aspose.Cells Kullanarak Satırda Maksimum Sütun İndeksini ve Sütunda Maksimum Satır İndeksini Alın**
Bu örnek aşağıdakileri göstermektedir:

1. [Örnek dosyayı](örnek.xlsx) yükleyin.
1. Maksimum sütun dizinini ve maksimum veri sütun dizinini elde etmek için satırı alın.
1. Hücrede [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) özniteliğini alın.
1. Sütuna dayalı bir aralık oluşturun.
1. İteratörü alın ve aralığı gezin.
1. Hücrede [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) özniteliğini alın.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}
{{< app/cells/assistant language="csharp" >}}
