---
title: Veri Filtreleme
type: docs
weight: 80
url: /tr/net/aspose-cells-gridweb/filter-data/
keywords: Bu makale, GridWeb de verileri nasıl filtreleyeceğinizi tanıtır.
description: Bu makale, GridWeb deki verileri nasıl filtreleyeceğinizi tanıtıyor.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb, otomatik filtre ve özel veri filtresi özellikleri sağlar. Bu özellikler, çalışma sayfasında yalnızca listelemek istediğiniz öğeleri seçmenize olanak tanır. Ayrıca, liste öğelerini belirli kriterlere göre filtreleyebilirsiniz. Filtre metni, sayılar veya tarihlerle filtreleme özelliklerini kullanarak verileri filtreleyebilirsiniz.

{{% /alert %}} 
## **Filtrelerle Çalışma**
Çalışma sayfası için otomatik filtrelemeyi etkinleştirmek için AddAutoFilter yöntemini kullanın. Bu yöntem, satır, başlangıç ve bitiş sütun dizinlerini kabul eder.

Özel filtrelemeyi etkinleştirmek için AddCustomFilter yöntemini kullanın. Bu yöntem, filtrenin uygulanacağı satır dizinini ve özel filtreleme kriterlerini kabul eder.

Aşağıdaki örnek, hem otomatik hem de özel veri filtrelerini uygular. Örnekte, otomatik filtre özelliği etkinleştirilir ve filtrelenmiş satırlar belirli kriterlere göre aranır.

**Giriş: İlk çalışma sayfasındaki veri listesi** 

![todo:image_alt_text](filter-data_1.jpg)

**Çıkış: Otomatik filtre özelliğini etkinleştirin** 

![todo:image_alt_text](filter-data_2.jpg)
### **Otomatik Filtre**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **Özel Veri Filtresi**
**Kriterlere dayalı özel filtrelenmiş veri** 

![todo:image_alt_text](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
