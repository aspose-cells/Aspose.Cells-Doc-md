---
title: Çalışsayfaya Sütun Eklemek veya Yerleştirmek
type: docs
weight: 10
url: /tr/net/aspose-cells-griddesktop/add-or-insert-a-column-into-worksheet/
keywords: GridDesktop,ekle,ekele,sütun ekle,satır ekle
description: Bu makale, GridDesktop ta sütun eklemeyi veya ekleme işlemini tanıtır.
---

{{% alert color="primary" %}} 

Bu konuda, Aspose.Cells.GridDesktop API'sını kullanarak çalışma zamanında çalışsayfalara sütun eklemenin ve yerleştirmenin temel özelliğini tanımlayacağız. Eklemenin ve yerleştirmenin temel farkı, eklemenin sütunun çalışsayfanın sütun koleksiyonunun sonuna eklenmesi olduğu yerde, yerleştirmenin sütunun çalışsayfanın herhangi belirtilen konumuna eklenmesi olduğudur.

{{% /alert %}} 
## **Çalışsayfaya Sütun Eklemek**
Çalışsayfaya yeni bir sütun eklemek için lütfen aşağıdaki adımları izleyin:

- **Form**'unuza Aspose.Cells.GridDesktop kontrolünü ekleyin
- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- **Çalışsayfa**'ya **Sütun** ekleyin



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Çalışsayfaya Sütun Ekleme**
Belirli bir konuma yeni bir sütun eklemek için lütfen aşağıdaki adımları izleyin:

- **Form**'unuza Aspose.Cells.GridDesktop kontrolünü ekleyin
- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- **Çalışsayfaya** **Sütun** ekleyin (yerleştirmek için konumun dizinini belirterek)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
