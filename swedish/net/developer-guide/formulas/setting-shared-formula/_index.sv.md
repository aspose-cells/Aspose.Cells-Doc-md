---
title: Ange Delad Formel
type: docs
weight: 10
url: /sv/net/setting-shared-formula/
---

{{% alert color="primary" %}}

Om du vill lägga till en funktion i kalkylblad som kommer att göra beräkningar. Detta artikel förklarar hur du uppnår denna uppgift med hjälp av Aspose.Cells.

{{% /alert %}}

## Ange delad formel med Aspose.Cells

Anta att du har ett kalkylblad fyllt med data i det format som liknar det följande exempelkalkylbladet.

|**Ingångsfil med en kolumn eller data**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Du vill lägga till en funktion i B2 som kommer att beräkna momsen för den första dataraden. Skatten är **9%**. Formeln som beräknar momsen är: **"=A2*0.09"**. Den här artikeln förklarar hur man tillämpar denna formel med Aspose.Cells.

Aspose.Cells låter dig ange en formel med hjälp av [**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) egenskap. Det finns två alternativ för att lägga till formler till de andra cellerna (B3, B4, B5, etc.) i kolumnen.

Antingen gör du det du gjorde för den första cellen, effektivt att sätta formeln för varje cell, uppdatera cellreferensen därefter (A3*0.09, A4*0.09, A5*0.09 och så vidare). Detta kräver att cellreferenserna för varje rad uppdateras. Det kräver också att Aspose.Cells analyserar varje formel individuellt, vilket kan vara tidskrävande för stora kalkylblad och komplexa formler. Det lägger också till extra kodrader även om loopar kan minska dem något.

Ett annat tillvägagångssätt är att använda en **delad formel**. Med en delad formel uppdateras formlerna automatiskt för cellreferenser i varje rad så att momsen beräknas korrekt. [**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index) metoden är mer effektiv än det första tillvägagångssättet.

Följande exempel visar hur du använder den.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
