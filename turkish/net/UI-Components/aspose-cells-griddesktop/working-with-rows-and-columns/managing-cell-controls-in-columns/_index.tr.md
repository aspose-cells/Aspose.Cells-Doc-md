---
title: Sütunlarda Hücre Kontrolleri Yönetimi
type: docs
weight: 100
url: /tr/net/aspose-cells-griddesktop/manage-cell-controls-in-columns/
keywords: GridDesktop, kontroller, kontrol
description: Bu makale, sütunlarda kontrol ayarlamanın nasıl yapıldığını tanıtır.
---

{{% alert color="primary" %}} 

Bu konu, Aspose.Cells.GridDesktop API'sını kullanarak sütunlarda hücre kontrollerini yönetme konusunda bazı önemli kavramları tartışmaktadır. Geliştiricilere, çalışma sayfalarının sütunlarından hücre kontrollerine erişme, değiştirme ve kaldırma konusunda nasıl yapılabileceğini anlatacağız. Hadi bir göz atalım.

{{% /alert %}} 
## **Hücre Kontrollerine Erişme**
Varolan bir hücre kontrolüne sütundan erişip değiştirmek için geliştiriciler, bir **Aspose.Cells.GridDesktop.Data.GridColumn** özelliği olan **CellControl**'ü kullanabilir. Bir kez bir hücre kontrolüne erişildiğinde, geliştiriciler çalışma zamanında özelliklerini değiştirebilirler. Örneğin, aşağıdaki örnekte belirli bir **Aspose.Cells.GridDesktop.Data.GridColumn**'dan varolan bir **CheckBox** hücre kontrolüne eriştik ve Checked özelliğini değiştirdik.

**ÖNEMLİ:** CellControl özelliği, **CellControl** nesnesi formunda bir hücre kontrolü sağlar. Dolayısıyla, belirli bir türde hücre kontrolüne erişmeniz gerekiyorsa, örneğin **CheckBox** ise **CellControl** nesnesini **CheckBox** sınıfına dönüştürmeniz gerekir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Hücre Kontrollerini Kaldırma**
Varolan bir hücre kontrolünü kaldırmak isteyen geliştiriciler, istenen çalışma sayfasına erişip ardından **Aspose.Cells.GridDesktop.Data.GridColumn**'ın **RemoveCellControl** yöntemini kullanarak belirli sütundan hücre kontrolünü kaldırabilirler.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

**Çalışma Sayfasının Sütunları** koleksiyonundaki her bir sütun, bir **Aspose.Cells.GridDesktop.Data.GridColumn** sınıfının bir örneği tarafından temsil edilir.

{{% /alert %}}
