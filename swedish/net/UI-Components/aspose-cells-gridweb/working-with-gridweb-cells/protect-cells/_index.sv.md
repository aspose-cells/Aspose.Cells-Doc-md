---
title: Skydda Cells
type: docs
weight: 50
url: /sv/net/protect-cells/
---
{{% alert color="primary" %}} 

Det här ämnet beskriver några tekniker för att skydda celler. Genom att använda dessa tekniker kan utvecklare begränsa användare från att redigera alla eller ett utvalt cellområde i ett kalkylblad.

{{% /alert %}} 
## **Skyddar Cells**
 Aspose.Cells.GridWeb tillhandahåller några olika tekniker för att kontrollera skyddsnivån på celler när kontrollen är i[Redigeringsläge](/cells/sv/net/enable-different-gridweb-modes/#edit-mode) (standardläget). Detta skyddar celler från att modifieras av slutanvändare.
### **Gör allt Cells Endast läsning**
Om du vill ställa in alla celler i ett kalkylblad till skrivskyddade anropar du kalkylbladets SetAllCellsReadonly-metod.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Gör allt Cells redigerbart**
Om du vill ta bort skyddet från alla celler, anropar du kalkylbladets SetAllCellsEditable-metod. Denna metod har motsatt effekt mot SetAllCellsReadonly-metoden.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Göra valda Cells Endast läsning**
Så här skyddar du endast ett antal celler:

1. Gör först alla celler redigerbara genom att anropa metoden SetAllCellsEditable.
1. Ange intervallet av celler som ska skyddas genom att anropa kalkylbladets SetReadonlyRange-metod. Denna metod tar antalet rader och kolumner för att specificera cellintervallet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Gör valda Cells redigerbara**
Så här tar du bort skyddet av en rad celler:

1. Gör alla celler läsbara genom att anropa SetAllCellsReadonly-metoden.
1. Ange intervallet av celler som ska redigeras genom att anropa kalkylbladets SetEditableRange-metod. Denna metod tar antalet rader och kolumner för att specificera cellintervallet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
