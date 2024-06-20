---
title: Çalışma Sayfasına Koruma Ekleme
type: docs
weight: 130
url: /tr/net/aspose-cells-griddesktop/adding-cell-protection-in-worksheet/
keywords: GridDesktop, koruma
description: Bu makale, GridDesktop ta Çalışma Sayfasındaki hücreleri nasıl koruyacağınızı tanıtır.
---

{{% alert color="primary" %}} 

Aspose.Cells for GridDesktop, çalışma sayfasındaki hücreleri korumanıza olanak tanır. Öncelikle çalışma sayfanızı korumalısınız, ardından istediğiniz hücreleri koruyabilirsiniz. Çalışma sayfasını korumak için, lütfen **Worksheet.Protected** özelliğini true olarak ayarlayın, sonra **Worksheet.SetProtected()** metoduyla hücre aralığını koruyun.

{{% /alert %}} 
## **Aspose.Cells.GridDesktop Kullanarak Hücreyi Koruma Altına Alma**
Aşağıdaki örnek kod, GridDesktop'ın aktif çalışma sayfasındaki **A1:B1** aralığındaki tüm hücreleri korur. Bu aralıktaki bir hücreye çift tıkladığınızda, düzenleme işlemi yapılamaz. Bu hücreleri salt okunur yapar.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
