---
title: Skydda celler
type: docs
weight: 50
url: /sv/net/aspose-cells-gridweb/protect-cells/
keywords: GridWeb, skydda, skrivskyddad, redigerbar
description: Den här artikeln introducerar hur man skyddar celler i GridWeb.
---

{{% alert color="primary" %}} 

Det här ämnet beskriver några tekniker för att skydda celler. Genom att använda dessa tekniker kan utvecklare begränsa användarna från att redigera alla eller ett urval av celler i ett arbetsblad.

{{% /alert %}} 
## **Skydda celler**
Aspose.Cells.GridWeb tillhandahåller några olika tekniker för att kontrollera skyddsnivån för celler när kontrollen är i [Redigeringsläge](/cells/sv/net/aspose-cells-gridweb/enable-different-gridweb-modes/#edit-mode) (standardläget). Detta skyddar celler från att ändras av slutanvändare.
### **Göra alla celler enbart läsbara**
För att göra alla celler i ett arbetsblad som enbart läsbara, använd arbetsbladets SetAllCellsReadonly-metod.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Göra alla celler redigerbara**
För att ta bort skyddet från alla celler, ring arbetsbladets SetAllCellsEditable-metod. Denna metod har motsatt effekt jämfört med SetAllCellsReadonly-metoden.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Gör utvalda celler skrivskyddade**
För att skydda endast ett cellintervall:

1. Först gör alla celler redigerbara genom att ringa SetAllCellsEditable-metoden.
1. Ange cellintervallet som ska skyddas genom att ringa arbetsbladets SetReadonlyRange-metod. Denna metod tar antalet rader och kolumner för att ange cellintervallet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Gör utvalda celler redigerbara**
För att ta bort skydd från ett cellintervall:

1. Gör alla celler skrivskyddade genom att ringa SetAllCellsReadonly-metoden.
1. Ange cellintervallet som ska vara redigerbart genom att ringa arbetsbladets SetEditableRange-metod. Denna metod tar antalet rader och kolumner för att ange cellintervallet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
