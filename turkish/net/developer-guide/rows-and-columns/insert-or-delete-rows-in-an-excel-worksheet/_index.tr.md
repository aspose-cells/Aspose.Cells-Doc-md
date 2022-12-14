---
title: Excel Çalışma Sayfasına Satır Ekleme veya Silme
type: docs
weight: 20
url: /tr/net/insert-or-delete-rows-in-an-excel-worksheet/
description: Bu makale, Excel çalışma sayfasına satır eklemek ve silmek için C# kodunu sağlar.
keywords: c# insert or delete rows in excel worksheet, c# insert or delete rows in excel, c# insert rows in excel, c# delete rows in excel, insert or delete rows in excel worksheet with c#, insert or delete rows in excel with c#, insert rows in excel with c#, delete rows in excel with c#
---
{{% alert color="primary" %}}

Yeni bir çalışma sayfası oluştururken veya mevcut bir çalışma sayfasıyla çalışırken, verileri barındırmak için fazladan satır veya sütun eklemeniz gerekebilir. Diğer zamanlarda, çalışma sayfasında belirtilen konumlardaki satırları veya sütunları silmeniz gerekebilir.

{{% /alert %}}

 Aspose.Cells, satır eklemek ve silmek için iki yöntem sunar:[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) ve[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). Bu yöntemler performans için optimize edilmiştir ve işi çok hızlı bir şekilde yapar.

 Bir dizi satır eklemek veya çıkarmak için her zaman[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) ve[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) yöntemleri kullanmak yerine[**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) veya[**Sırayı sil**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow)bir döngüdeki yöntemler.

Aspose.Cells, Microsoft Excel'in yaptığı gibi çalışır. Satır veya sütun eklendiğinde, çalışma sayfası içeriği aşağı ve sağa kaydırılır. Satır veya sütunlar kaldırıldığında, çalışma sayfası içeriği yukarı veya sola kaydırılır. Diğer çalışma sayfalarındaki ve hücrelerdeki referanslar, satırlar eklendiğinde veya kaldırıldığında güncellenir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
