---
title: Çalışsayfaya Satır Ekleme veya Yerleştirme
type: docs
weight: 30
url: /tr/net/aspose-cells-griddesktop/add-or-insert-a-row-into-worksheet/
keywords: GridDesktop,insert,add,row,insert row,add row
description: Bu makale, GridDesktop ta satır ekleme veya yerleştirme işlemini tanıtır.
---

{{% alert color="primary" %}} 

Bir önceki konularımızdan birine benzer şekilde, bu konu Aspose.Cells.GridDesktop API'sını kullanarak çalışma zamanında çalışsayfalara satır ekleme ve yerleştirme özelliğini tanımlar. Eklemenin ve yerleştirmenin temel farkı, eklemenin çalışsayfanın satır koleksiyonunun sonuna satır eklenmesi olduğu yerde, yerleştirmenin bir satırın çalışsayfanın herhangi belirtilen konumuna eklenmesi olduğudur.

{{% /alert %}} 
## **Çalışsayfaya Satır Ekleme**
Çalışsayfaya yeni bir satır eklemek için lütfen aşağıdaki adımları izleyin:

- **Form**'unuza Aspose.Cells.GridDesktop kontrolünü ekleyin
- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- **Çalışsayıya** **Satır** ekle



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **Çalışsayıya Satır Eklemek**
Belirli bir konuma yeni bir satır eklemek için lütfen aşağıdaki adımları izleyin:

- **Form**'unuza Aspose.Cells.GridDesktop kontrolünü ekleyin
- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- **Satır**ı **Çalışsayısı**na (belirli bir konuma belirterek ekleyin)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
