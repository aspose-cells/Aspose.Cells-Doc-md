---
title: Hücreleri Koruma
type: docs
weight: 50
url: /tr/net/aspose-cells-gridweb/protect-cells/
keywords: GridWeb, koru, saltoku, düzenlenebilir
description: Bu makale, GridWeb de hücreleri korumanın nasıl yapılacağını tanıtır.
---

{{% alert color="primary" %}} 

Bu konu, hücreleri koruma için birkaç teknik açıklar. Bu teknikleri kullanarak geliştiricilerin çalışma sayfasındaki tüm hücreleri veya seçili hücrelerin düzenlenmesini kullanıcılardan kısıtlamasına izin verir.

{{% /alert %}} 
## **Hücreleri Koruma**
Aspose.Cells.GridWeb, denetim [Düzenleme modundayken](/cells/tr/net/aspose-cells-gridweb/enable-different-gridweb-modes/#edit-mode) (varsayılan mod) hücrelerin koruma seviyesini kontrol etmek için birkaç farklı teknik sağlar. Bu, hücrelerin son kullanıcılar tarafından değiştirilmesini engeller.
### **Tüm Hücreleri Salt Okunur Yapma**
Tüm hücreleri salt okunur olarak ayarlamak için, çalışma sayfasının SetAllCellsReadonly yöntemini çağırın.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Tüm Hücreleri Düzenlenebilir Yapma**
Tüm hücrelerden korumayı kaldırmak için, çalışma sayfasının SetAllCellsEditable yöntemini çağırın. Bu yöntem, SetAllCellsReadonly yönteminin zıt etkisi vardır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Seçilen Hücreleri Salt Okunur Yapma**
Yalnızca belirli bir hücre aralığını korumak için:

1. İlk olarak, SetAllCellsEditable yöntemini çağırarak tüm hücreleri düzenlenebilir hale getirin.
1. Belirli hücre aralığını belirtmek için çalışma sayfasının SetReadonlyRange yöntemini çağırın. Bu yöntem, hücre aralığını belirtmek için satır ve sütun sayısını alır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Seçilen Hücreleri Düzenlenebilir Yapma**
Bir hücre aralığını korumayı kaldırmak için:

1. SetAllCellsReadonly yöntemini çağırarak tüm hücreleri salt okunur hale getirin.
1. Belirli hücre aralığını belirtmek için çalışma sayfasının SetEditableRange yöntemini çağırın. Bu yöntem, hücre aralığını belirtmek için satır ve sütun sayısını alır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
