---
title: Çalışma Sayfasındaki Boş Satır ve Sütunları Silme
type: docs
weight: 300
url: /tr/net/delete-blank-rows-and-columns-in-a-worksheet/
---

{{% alert color="primary" %}}

Bir çalışma sayfasından tüm boş satır ve sütunları silmek mümkündür. Bu, örneğin, bir Microsoft Excel dosyasından bir PDF dosyası oluştururken yalnızca veri veya ilgili nesneler içeren satır ve sütunları dönüştürmek istediğinizde faydalıdır.

Boş satır ve sütunları silmek için aşağıdaki Aspose.Cells yöntemlerini kullanın:

1. Boş satırları silmek için [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows) yöntemini kullanın. Silinecek boş satırlar için, [**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) sadece doğru olmalıdır, ayrıca bu satırlarda herhangi bir hücre için görünür bir yorum tanımlanmamış olmalı ve bunlarla kesişen bir pivota tablonun olmaması gerekir.
1. Boş sütunları silmek için [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns) yöntemini kullanın.

{{% /alert %}}

Boş Satırları Silme için C# kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

Boş Sütunları Silme için C# kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
