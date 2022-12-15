---
title: Lägg till Cell Formler
type: docs
weight: 30
url: /sv/net/add-cell-formulas/
---
{{% alert color="primary" %}} 

Den mest värdefulla funktionen som erbjuds av Aspose.Cells.GridWeb är stöd för formler eller funktioner. Aspose.Cells.GridWeb har sin egen Formula Engine som beräknar formlerna i kalkylblad. Aspose.Cells.GridWeb stöder både inbyggda och användardefinierade funktioner eller formler. Det här ämnet diskuterar hur man lägger till formler i celler med Aspose.Cells.GridWeb API i detalj.

{{% /alert %}} 
## **Lägger till formler till Cells**
### **Hur lägger man till och beräknar en formel?**
 Det är möjligt att lägga till, komma åt och ändra formler i celler genom att använda en cells formelegenskap. Aspose.Cells.GridWeb stöder användardefinierade formler som sträcker sig från enkla till komplexa. Men ett stort antal inbyggda funktioner eller formler (liknande Microsoft Excel) levereras också med Aspose.Cells.GridWeb. För att se hela listan över inbyggda funktioner, se denna[lista över funktioner som stöds.](/cells/sv/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

Formelsyntaxen bör vara kompatibel med Microsoft Excel-syntax. Till exempel måste alla formler börja med ett likhetstecken (=).

För att lägga till en formel dynamiskt kommer Aspose.Cells.GridWeb att känna igen den som en formel även om du inte använder ett **=**-tecken, men om slutanvändare som arbetar i GUI måste han använda "="-tecknet.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**Formel har lagts till i B3-cellen men inte beräknats av GridWeb** 

![todo:image_alt_text](add-cell-formulas_1.png)

I ovanstående skärmdump kan du se att en formel har lagts till i B3 men inte har beräknats ännu. För att beräkna alla formler, anrop GridWeb-kontrollens GridWorksheetCollections CalculateFormula-metod efter att ha lagt till formler till kalkylblad som visas nedan.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

 Användare kan också beräkna formler genom att klicka**Skicka in**.

**Klicka på knappen Skicka på GridWeb** 

![todo:image_alt_text](add-cell-formulas_2.png)

**VIKTIG** : Om en användare klickar på**Spara** eller**Ångra** knappar, eller arkflikarna, beräknas alla formler automatiskt av GridWeb.

**Formelresultat efter beräkning** 

![todo:image_alt_text](add-cell-formulas_3.png)

{{% /alert %}} 
### **Refererar till Cells från andra arbetsblad**
Med hjälp av Aspose.Cells.GridWeb är det möjligt att referera värden lagrade i olika kalkylblad i deras formler, vilket skapar komplexa formler.

Syntaxen för att referera till ett cellvärde från ett annat kalkylblad är SheetName!CellName.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
