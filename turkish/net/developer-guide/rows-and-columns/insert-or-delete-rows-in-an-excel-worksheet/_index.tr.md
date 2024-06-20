---
title: Bir Excel Çalışma Sayfasına Satır Ekle veya Sil
type: docs
weight: 20
url: /tr/net/insert-or-delete-rows-in-an-excel-worksheet/
description: Bu makale, Excel çalışma sayfasına satır eklemek ve silmek için C# kodunu sağlar.
keywords: c# excel çalışma sayfasında satır ekleme veya silme, c# excel de satır ekleme veya silme, c# excel de satır ekleme, c# excel de satır silme, C# ile excel çalışma sayfasında satır ekleme veya silme, C# ile excel de satır ekleme veya silme, C# ile excel de satır ekleme, C# ile excel de satır silme
---

{{% alert color="primary" %}}

Yeni bir çalışma sayfası oluştururken veya mevcut bir çalışma sayfası üzerinde çalışırken, verileri karşılamak için ekstra satırlar veya sütunlar eklemeniz gerekebilir. Diğer zamanlarda, belirli pozisyonlardan satırları veya sütunları silmeniz gerekebilir.

{{% /alert %}}

Aspose.Cells, satırları eklemek ve silmek için iki yöntem sunar: [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) ve [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). Bu yöntemler, performans için optimize edilmiştir ve işi çok hızlı bir şekilde yapar.

Birkaç satır eklemek veya kaldırmak amacıyla, her zaman döngüde [**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) veya [**DeleteRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow) yöntemlerini kullanmak yerine [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) ve [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) yöntemlerini kullanmanızı öneririz.

Aspose.Cells, Microsoft Excel'in çalışma şekliyle aynı şekilde çalışır. Satırlar veya sütunlar eklenirse, çalışma sayfası içeriği aşağıya ve sağa kaydırılır. Satırlar veya sütunlar kaldırıldığında, çalışma sayfası içeriği yukarı veya sola kaydırılır. Satırlar eklenip kaldırıldığında diğer çalışma sayfaları ve hücrelerdeki referanslar güncellenir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
