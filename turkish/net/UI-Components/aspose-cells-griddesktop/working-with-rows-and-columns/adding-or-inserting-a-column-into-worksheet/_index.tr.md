---
title: Çalışma Sayfasına Sütun Ekleme veya Ekleme
type: docs
weight: 10
url: /tr/net/adding-or-inserting-a-column-into-worksheet/
---
{{% alert color="primary" %}} 

Bu konuda, Aspose.Cells.GridDesktop'un API'ini kullanarak çalışma zamanında çalışma sayfalarına sütun ekleme ve ekleme temel özelliğini açıklayacağız. Toplama ve ekleme arasındaki temel fark, ek olarak, çalışma sayfasının sütunlar koleksiyonunun sonuna sütun eklenmesidir; burada, eklemede olduğu gibi, çalışma sayfasında belirtilen herhangi bir konuma sütun eklenebilir.

{{% /alert %}} 
## **Çalışma Sayfasına Sütun Ekleme**
Çalışma sayfasına yeni bir sütun eklemek için lütfen aşağıdaki adımları izleyin:

-  Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Ekle**Kolon** için**Çalışma kağıdı**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Çalışma Sayfasına Sütun Ekleme**
Çalışma sayfasına belirli bir konumda yeni bir sütun eklemek için lütfen aşağıdaki adımları izleyin:

-  Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Sokmak**Kolon** içine**Çalışma kağıdı** (ekleneceği sütunun dizinini belirterek belirli bir konumda)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
