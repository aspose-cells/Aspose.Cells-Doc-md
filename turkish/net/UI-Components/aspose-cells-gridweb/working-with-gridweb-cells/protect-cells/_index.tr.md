---
title: Koruyun Cells
type: docs
weight: 50
url: /tr/net/protect-cells/
---
{{% alert color="primary" %}} 

Bu konuda, hücreleri korumaya yönelik birkaç teknik açıklanmaktadır. Bu tekniklerin kullanılması, geliştiricilerin, kullanıcıların bir çalışma sayfasındaki tüm veya seçili hücre aralığını düzenlemesini kısıtlamasına olanak tanır.

{{% /alert %}} 
## **Koruma Cells**
 Aspose.Cells.GridWeb, kontrol devredeyken hücrelerdeki koruma seviyesini kontrol etmek için birkaç farklı teknik sunar.[Düzenleme modu](/cells/tr/net/enable-different-gridweb-modes/#edit-mode) (varsayılan mod). Bu, hücreleri son kullanıcılar tarafından değiştirilmekten korur.
### **Tümünü Yapma Cells Salt Okunur**
Çalışma sayfasındaki tüm hücreleri salt okunur olarak ayarlamak için çalışma sayfasının SetAllCellsReadonly yöntemini çağırın.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Cells'in Tümünü Düzenlenebilir Hale Getirmek**
Tüm hücrelerden korumayı kaldırmak için çalışma sayfasının SetAllCellsEditable yöntemini çağırın. Bu yöntem, SetAllCellsReadonly yönteminin tersi etkiye sahiptir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Seçileni Yapma Cells Salt Okunur**
Yalnızca bir hücre aralığını korumak için:

1. Önce SetAllCellsEditable yöntemini çağırarak tüm hücreleri düzenlenebilir yapın.
1. Çalışma sayfasının SetReadonlyRange yöntemini çağırarak korunacak hücre aralığını belirtin. Bu yöntem, hücre aralığını belirtmek için satır ve sütun sayısını alır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Seçilen Cells Düzenlenebilir Hale Getiriliyor**
Bir hücre aralığının korumasını kaldırmak için:

1. SetAllCellsReadonly yöntemini çağırarak tüm hücreleri salt okunur yapın.
1. Çalışma sayfasının SetEditableRange yöntemini çağırarak düzenlenebilir olacak hücre aralığını belirtin. Bu yöntem, hücre aralığını belirtmek için satır ve sütun sayısını alır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
