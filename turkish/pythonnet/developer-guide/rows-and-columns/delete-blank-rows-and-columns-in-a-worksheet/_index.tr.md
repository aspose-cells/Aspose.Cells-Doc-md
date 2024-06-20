---
title: Çalışma Sayfasındaki Boş Satır ve Sütunları Silme
type: docs
weight: 300
url: /tr/python-net/delete-blank-rows-and-columns-in-a-worksheet/
description: Bu makale, Aspose.Cells for Python via .NET kütüphanesi ile bir çalışma sayfasındaki boş satır ve sütunları nasıl sileceğinizi açıklar.
keywords: Python Excel Kütüphanesi, Python boş Satırları Silme, Python boş Satır Kaldırma, Python boş Sütunları Silme, Python boş Sütun Kaldırma, Python boş satır ve sütunları silme veya kaldırma.
---

{{% alert color="primary" %}}

Bir çalışma sayfasından tüm boş satır ve sütunları silmek mümkündür. Bu, örneğin, bir Microsoft Excel dosyasından bir PDF dosyası oluştururken yalnızca veri veya ilgili nesneler içeren satır ve sütunları dönüştürmek istediğinizde faydalıdır.

Boş satır ve sütunları silmek için aşağıdaki Aspose.Cells yöntemlerini kullanın:

1. Boş satırları silmek için [**Cells.delete_blank_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_rows) yöntemini kullanın. Silinecek boş satırlar için, [**Row.is_blank**](https://reference.aspose.com/cells/python-net/aspose.cells/row/is_blank/) sadece doğru olmalıdır, ayrıca bu satırlarda herhangi bir hücre için görünür bir yorum tanımlanmamış olmalı ve bunlarla kesişen bir pivota tablonun olmaması gerekir.
1. Boş sütunları silmek için [**Cells.delete_blank_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_columns) yöntemini kullanın.

{{% /alert %}}

Boş Satırları Silme için C# kodu

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankRows-1.py" >}}

Boş Sütunları Silme için C# kodu

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankColumns-1.py" >}}
