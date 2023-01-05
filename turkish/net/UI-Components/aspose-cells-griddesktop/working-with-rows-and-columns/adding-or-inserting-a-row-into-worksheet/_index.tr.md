---
title: Çalışma Sayfasına Satır Ekleme veya Ekleme
type: docs
weight: 30
url: /tr/net/adding-or-inserting-a-row-into-worksheet/
---
{{% alert color="primary" %}} 

Önceki konularımızdan birine benzer şekilde, bu konu Aspose.Cells.GridDesktop'un API'ini kullanarak çalışma zamanında çalışma sayfalarına satır ekleme ve ekleme özelliğini açıklamaktadır. Toplama ve ekleme arasındaki temel fark, ek olarak, çalışma sayfasının satırlar koleksiyonunun sonuna bir satır eklenmesidir; burada, eklemede olduğu gibi, çalışma sayfasında belirtilen herhangi bir konuma bir satır eklenebilir.

{{% /alert %}} 
## **Çalışma Sayfasına Satır Ekleme**
Çalışma sayfasına yeni bir satır eklemek için lütfen aşağıdaki adımları izleyin:

-  Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Eklemek**Sıra** için**Çalışma kağıdı**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **Çalışma Sayfasına Satır Ekleme**
Çalışma sayfasına belirli bir konumda yeni bir satır eklemek için lütfen aşağıdaki adımları izleyin:

-  Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Sokmak**Sıra** içine**Çalışma kağıdı**(belirli bir konumda, ekleneceği satırın dizinini belirterek)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
