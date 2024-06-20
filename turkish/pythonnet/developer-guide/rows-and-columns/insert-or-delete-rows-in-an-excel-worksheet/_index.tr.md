---
title: Bir Excel Çalışma Sayfasına Satır Ekle veya Sil
type: docs
weight: 20
url: /tr/python-net/insert-or-delete-rows-in-an-excel-worksheet/
description: Bu makale, Aspose.Cells for Python via .NET kitaplığı ile Excel çalışma sayfasına satır ekleme ve silme için python kodunu sağlar.
keywords: Python Excel Kütüphanesi, Python da excel çalışma sayfasına satır ekleme veya silme, Python da excel çalışma sayfasına satır ekleme veya silme, Python da excel e satır ekleme, Python da excel den satır silme, Python ile excel çalışma sayfasına satır ekleme veya silme, Python ile excel e satır ekleme veya silme, Python ile excel e satır ekleme, Python ile excel den satır silme
---

{{% alert color="primary" %}}

Yeni bir çalışma sayfası oluştururken veya mevcut bir çalışma sayfası üzerinde çalışırken, verileri karşılamak için ekstra satırlar veya sütunlar eklemeniz gerekebilir. Diğer zamanlarda, belirli pozisyonlardan satırları veya sütunları silmeniz gerekebilir.

{{% /alert %}}

Aspose.Cells for Python via .NET, satır ekleme ve silme için iki yöntem sunmaktadır: [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) ve [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/). Bu yöntemler, performans için optimize edilmiştir ve işi çok hızlı bir şekilde yapar.

Birkaç satır eklemek veya kaldırmak amacıyla, her zaman döngüde [**Cells.insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row) veya [**delete_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_row) yöntemlerini kullanmak yerine [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) ve [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/) yöntemlerini kullanmanızı öneririz.

Aspose.Cells for Python via .NET, Microsoft Excel'in işleyişi ile aynı şekilde çalışır. Satırlar veya sütunlar eklenirken, çalışma sayfası içeriği aşağıya ve sağa kaydırılır. Satırlar veya sütunlar çıkarıldığında, çalışma sayfası içeriği yukarı veya sola kaydırılır. Satırlar eklenip veya çıkarıldığında diğer çalışma sayfaları ve hücrelerdeki referanslar güncellenir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertDeleteRows-1.py" >}}
