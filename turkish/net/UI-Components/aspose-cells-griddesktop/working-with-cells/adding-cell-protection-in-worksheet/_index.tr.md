---
title: Çalışma Sayfasına Cell Koruması Ekleme
type: docs
weight: 130
url: /tr/net/adding-cell-protection-in-worksheet/
---
{{% alert color="primary" %}} 

GridDesktop için Aspose.Cells, hücrelerinizi bir çalışma sayfasında korumanıza olanak tanır. Önce çalışma sayfanızı korumanız gerekir, ardından çalışma sayfasında istediğiniz hücreleri koruyabilirsiniz. Çalışma sayfasını korumak için lütfen ayarlayın**Çalışma Sayfası.Korumalı** özelliği true olarak değiştirin, ardından kullanın**Worksheet.SetProtected()** hücre aralığını koruma yöntemi.

{{% /alert %}} 
## **Cell'i Aspose.Cells.GridDesktop kullanarak koruyun**
 Aşağıdaki örnek kod, aralıktaki tüm hücreleri korur**A1:B1** GridDesktop'un aktif çalışma sayfasının. Bu aralıktaki herhangi bir hücreye çift tıkladığınızda düzenleme yapamayacaksınız. Bu hücreleri salt okunur yapacaktır.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
