---
title: Ange Delad Formel
type: docs
weight: 10
url: /sv/python-net/setting-shared-formula/
---

{{% alert color="primary" %}}

Om du vill lägga till en funktion i kalkbladet som gör några beräkningar. Denna artikel förklarar hur man uppnår detta med Aspose.Cells för Python via .NET.

{{% /alert %}}

## Ställa in delad formel med Aspose.Cells för Python via .NET

Anta att du har ett kalkylblad fyllt med data i det format som liknar det följande exempelkalkylbladet.

|**Ingångsfil med en kolumn eller data**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Du vill lägga till en funktion i B2 som ska beräkna försäljningsskatten för den första dataraden. Skatten är **9%**. Formeln som beräknar försäljningsskatten är: **"=A2*0.09"**. Denna artikel förklarar hur du tillämpar denna formel med Aspose.Cells för Python via .NET.

Aspose.Cells för Python via .NET tillåter dig att ange en formel med egenskapen [**Cell.formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula). Det finns två alternativ för att lägga till formler i andra celler (B3, B4, B5, osv.) i kolumnen.

Antingen gör du samma sak som för den första cellen och anger formeln för varje cell, uppdaterar cellreferensen därefter (A3*0.09, A4*0.09, A5*0.09, och så vidare). Detta kräver att cellreferenserna för varje rad uppdateras. Det kräver också att Aspose.Cells för Python via .NET parsar varje formel individuellt, vilket kan vara tidskrävande för stora kalkylblad och komplexa formler. Det lägger även till extra kodrader även om loopar kan minska detta något.

Ett annat tillvägagångssätt är att använda en **delad formel**. Med en delad formel uppdateras formlerna automatiskt för cellreferenser i varje rad så att momsen beräknas korrekt. [**Cell.set_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_shared_formula) metoden är mer effektiv än det första tillvägagångssättet.

Följande exempel visar hur du använder den.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSharedFormula-1.py" >}}

