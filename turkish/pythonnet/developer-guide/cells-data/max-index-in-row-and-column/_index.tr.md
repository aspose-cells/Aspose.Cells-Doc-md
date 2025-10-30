---
title: Satırda Maksimum Sütun Endeksini ve Sütunda Maksimum Satır Endeksini Al
type: docs
weight: 600
url: /tr/python-net/get-max-index-in-row-and-column/
description: Sadece bazı verileri işlemeniz gerektiğinde, satır ve sütunların veri aralığını bilmelisiniz. Aspose.Cells for Python via .NET bu özelliği sunar. Bir satırdaki maksimum sütun endeksini elde etmek için [Row.last_cell](https //reference.aspose.com/cells/python net/aspose.cells/row/last_cell/) ve [Row.last_data_cell](https //reference.aspose.com/cells/python net/aspose.cells/row/last_data_cell/) özelliklerini alabilir ve sonra maksimum sütun endeksini ve maksimum veri sütun endeksini elde etmek için [Cell.column](https //reference.aspose.com/cells/python net/aspose.cells/cell/column/) özelliğini kullanabilirsiniz. Ancak maksimum satır endeksini ve maksimum sütun veri endeksini bir sütun üzerinde elde etmek için bir aralık oluşturmanız, ardından aralığı dolaşmanız ve en son hücreyi bulmanız ve en sonunda hücre üzerindeki [Cell.row](https //reference.aspose.com/cells/python net/aspose.cells/cell/row/) özniteliğini elde etmeniz gerekir.
keywords: Python Excel Kütüphanesi, Satırda Maksimum Sütun İndeksini Alma, Sütunda Maksimum Satır İndeksini Alma, Satırda Maksimum Veri Sütun İndeksini Alma, Sütunda Maksimum Veri Satır İndeksini Alma. 
---

## **Olası Kullanım Senaryoları**
Yalnızca bazı veriler üzerinde işlem yapmanız gerekiyorsa, satır ve sütunların veri aralığını bilmeniz gerekmektedir. Aspose.Cells for Python via .NET bu özelliği sunar. Bir satırdaki maksimum sütun endeksini elde etmek için [Row.last_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/) ve [Row.last_data_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/) özelliklerini elde edebilir ve ardından maksimum sütun endeksini ve maksimum veri sütun endeksini elde etmek için [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) özelliğini kullanabilirsiniz. Ancak sütundaki maksimum satır endeksini ve maksimum satır veri endeksini elde etmek için, sütunda bir aralık oluşturmanız, ardından aralığı dolaşarak son hücreyi bulmanız ve en sonunda [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) özelliğini elde etmek gerekmektedir.

Aspose.Cells for Python via .NET hedeflerinize ulaşmanıza yardımcı olacak aşağıdaki özelliklere ve yöntemlere sahiptir.
- [**Row.last_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/)
- [**Row.last_data_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/)
- [**Cell.column**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/)
- [**Cell.row**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/)

## **Aspose.Cells for Python Excel Kütüphanesi Kullanarak Satırda Maksimum Sütun Endeksini ve Sütunda Maksimum Satır Endeksini Alma**
Bu örnek aşağıdakileri göstermektedir:

1. [Örnek dosyayı](örnek.xlsx) yükleyin.
1. Maksimum sütun dizinini ve maksimum veri sütun dizinini elde etmek için satırı alın.
1. Hücredeki [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) özniteliğini alın.
1. Sütuna dayalı bir aralık oluşturun.
1. İteratörü alın ve aralığı gezin.
1. Hücredeki [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) özniteliğini alın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Cells-max-index-of-row-and-column.py" >}}
{{< app/cells/assistant language="python-net" >}}
