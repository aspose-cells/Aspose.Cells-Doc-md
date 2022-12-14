---
title: Cell Denetimlerini Sütunlarda Yönetme
type: docs
weight: 100
url: /tr/net/managing-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

Bu konuda, Aspose.Cells.GridDesktop API kullanılarak sütunlardaki hücre denetimlerini yönetmeyle ilgili bazı önemli kavramlar ele alınmaktadır. Geliştiricilerin çalışma sayfalarının sütunlarından hücre denetimlerine nasıl erişebileceğini, bunları değiştirebileceğini ve kaldırabileceğini açıklayacağız. Hadi bir göz atalım.

{{% /alert %}} 
## **Cell Kontrollerine Erişim**
 Sütundaki mevcut bir hücre kontrolüne erişmek ve değiştirmek için, geliştiriciler bir hücrenin CellControl özelliğini kullanabilir.**Aspose.Cells.GridDesktop.Data.GridColumn** . Bir hücre kontrolüne erişildiğinde, geliştiriciler çalışma zamanında özelliklerini değiştirebilir. Örneğin, aşağıda verilen örnekte, mevcut bir**Onay Kutusu** Belirli bir hücreden kontrol**Aspose.Cells.GridDesktop.Data.GridColumn** ve Checked özelliğini değiştirdi.

**ÖNEMLİ:** CellControl özelliği, şu şekilde bir hücre denetimi sağlar:**Hücre Kontrolü**nesne. Bu nedenle, belirli bir hücre kontrolü türüne erişmeniz gerekirse, diyelim ki**Onay Kutusu** o zaman şunu yazmanız gerekecek:**Hücre Kontrolü** itiraz etmek**Onay Kutusu** sınıf.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Cell Denetimlerini Kaldırma**
 Mevcut bir hücre denetimini kaldırmak için, geliştiriciler yalnızca istenen bir çalışma sayfasına erişebilir ve ardından**Kaldırmak** kullanarak belirli sütundan hücre kontrolü**Hücre Denetimini Kaldır** yöntemi**Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

 Her sütundaki**Sütunlar** koleksiyonu**Çalışma kağıdı** bir örneği ile temsil edilir**Aspose.Cells.GridDesktop.Data.GridColumn** sınıf.

{{% /alert %}}
