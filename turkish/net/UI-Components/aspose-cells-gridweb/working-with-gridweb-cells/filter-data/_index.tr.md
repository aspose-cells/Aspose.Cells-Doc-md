---
title: Verileri Filtrele
type: docs
weight: 80
url: /tr/net/filter-data/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb, otomatik filtreleme ve özel veri filtreleme özellikleri sağlar. Bu özellikler, bir çalışma sayfasında yalnızca bir listede görüntülemek istediğiniz öğeleri seçmeniz için bir yol sağlar. Ayrıca, bir listedeki öğeleri belirlenen kriterlere göre filtreleyebilirsiniz. Filtreleme özellikleriyle metni, sayıları veya tarihleri filtreleyin.

{{% /alert %}} 
## **Filtrelerle Çalışmak**
Bir çalışma sayfası için otomatik filtreyi etkinleştirmek üzere çalışma sayfası AddAutoFilter yöntemini kullanın. Bu metot satır, başlangıç ve bitiş kolon indekslerini kabul eder.

Özel filtreyi etkinleştirmek için, filtrenin uygulanması gereken satır dizinini ve özel filtreleme ölçütlerini kabul eden çalışma sayfası AddCustomFilter yöntemini kullanın.

Aşağıdaki örnek, hem otomatik hem de özel veri filtrelerini uygular. Örnekte, otomatik filtre özelliği etkinleştirilmiş ve filtrelenmiş satırlar bazı kriterlere göre aranmıştır.

**Girdi: ilk çalışma sayfasındaki veri listesi** 

![yapılacaklar:resim_alternatif_Metin](filter-data_1.jpg)

**Çıktı: otomatik filtreleme özelliğini etkinleştir** 

![yapılacaklar:resim_alternatif_Metin](filter-data_2.jpg)
### **Otomatik filtre**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **Özel Veri Filtresi**
**Kriterlere göre özel filtrelenmiş veriler** 

![yapılacaklar:resim_alternatif_Metin](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
