---
title: Çalışma Sayfalarında Hücre Kontrollerini Yönetme
type: docs
weight: 130
url: /tr/net/aspose-cells-griddesktop/manage-cell-controls-in-worksheets/
keywords: GridDesktop, hücre kontrolü, kontrol, kontroller
description: Bu makale, GridDesktop taki hücre kontrolleriyle çalışmayı nasıl tanıtacağınızı açıklar.
---

{{% alert color="primary" %}} 

Bu konu, Aspose.Cells.GridDesktop'un API'sını kullanarak hücre kontrollerini yönetme konusunda bazı önemli kavramları tartışmaktadır. Geliştiricilerin çalışma sayfalarından hücre kontrolüne nasıl erişebileceklerini, değiştirebileceklerini ve kaldırabileceklerini açıklayacağız. Hadi bir göz atalım.

{{% /alert %}} 
## **Hücre Kontrollerine Erişme**
Geliştiriciler, çalışma sayfasındaki mevcut bir hücre kontrolüne erişmek ve değiştirmek için **Controls** koleksiyonundan belirli bir hücre kontrolüne erişebilirler. Hücre kontrolünün görüntülendiği hücreyi (hücre adını veya satır ve sütun numaralarını kullanarak) belirterek. Bir hücre kontrolüne eriştikten sonra, geliştiriciler çalışma zamanında özelliklerini değiştirebilirler. Örneğin, aşağıdaki örnekte, **CheckBox** hücre kontrolüne eriştik ve **Checked** özelliğini değiştirdik.

**ÖNEMLİ:** **Controls** koleksiyonu, **CellControl** nesneleri şeklinde tüm hücre kontrollerini içerir. Bu nedenle, örneğin **CheckBox** gibi belirli bir hücre kontrolüne erişmeniz gerekiyorsa, **CellControl** nesnesini **CheckBox** sınıfına dönüştürmeniz gerekecektir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Hücre Kontrollerini Kaldırma**
Mevcut bir hücre kontrolünü kaldırmak isteyen geliştiriciler, istenen bir çalışma sayfasına erişebilir ve ardından hücre kontrolünü, hücre kontrolünü içeren hücreyi (adını veya satır ve sütun numarasını kullanarak) **Controls** koleksiyonundan kaldırabilirler.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
