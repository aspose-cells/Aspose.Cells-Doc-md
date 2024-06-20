---
title: Lägg till cellformler
type: docs
weight: 30
url: /sv/net/aspose-cells-gridweb/add-cell-formula/
keywords: GridWeb, formel
description: Den här artikeln introducerar hur man lägger till formel i cell i GridWeb.
---

{{% alert color="primary" %}} 

Den mest värdefulla funktionen som erbjuds av Aspose.Cells.GridWeb är stöd för formler eller funktioner. Aspose.Cells.GridWeb har sin egen Formula Engine som beräknar formlerna i arbetsblad. Aspose.Cells.GridWeb stöder både inbyggda och användardefinierade funktioner eller formler. Detta ämne diskuterar lägg till formler i celler med hjälp av Aspose.Cells.GridWeb API i detalj.

{{% /alert %}} 
## **Lägga till formler i celler**
### **Hur man lägger till och beräknar en formel?**
Det är möjligt att lägga till, komma åt och modifiera formler i celler genom att använda en cells Formula-egenskap. Aspose.Cells.GridWeb stöder användardefinierade formler från enkla till komplexa. Ett stort antal inbyggda funktioner eller formler (liknande Microsoft Excel) levereras också med Aspose.Cells.GridWeb. För att se den fullständiga listan över inbyggda funktioner, vänligen hänvisa till denna [lista över stödda funktioner.](/cells/sv/net/aspose-cells-gridweb/list-of-supported-functions/)

{{% alert color="primary" %}} 

Formelsyntaxen ska vara kompatibel med Microsoft Excel syntax. Till exempel måste alla formler börja med ett lika med-tecken (=).

För att lägga till en formel dynamiskt kommer Aspose.Cells.GridWeb att känna igen den som en formel även om du inte använder ett "="-tecken, men om slutanvändarna arbetar i GUI måste de använda "="-tecknet.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**Formel tillagd till cell B3 men inte beräknad av GridWeb** 

![todo:image_alt_text](add-cell-formulas_1.png)

På den ovanstående skärmbilden kan du se att en formel har lagts till B3 men har ännu inte beräknats. För att beräkna alla formler, ring GridWeb-kontrollens GridWorksheetCollections CalculateFormula-metod efter att ha lagt till formler på arbetsblad, som visas nedan.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

Användare kan också beräkna formler genom att klicka på **Skicka**.

**Klicka på Submit-knappen i GridWeb** 

![todo:image_alt_text](add-cell-formulas_2.png)

**VIKTIGT**: Om en användare klickar på **Spara** eller **Ångra**-knapparna, eller arbetsbladets flikar, beräknas alla formler automatiskt av GridWeb.

**Formelresultat efter beräkning** 

![todo:image_alt_text](add-cell-formulas_3.png)

{{% /alert %}} 
### **Referera till celler från andra arbetsblad**
Med Aspose.Cells.GridWeb är det möjligt att referera till värden som lagras i olika arbetsblad i deras formler och skapa komplexa formler.

Syntaxen för att referera till en cells värde från ett annat arbetsblad är ArkNamn!CellNamn.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
