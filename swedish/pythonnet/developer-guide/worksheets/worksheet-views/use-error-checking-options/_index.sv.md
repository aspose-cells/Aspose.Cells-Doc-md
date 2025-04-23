---
title: Använda alternativ för felkontroll
type: docs
weight: 140
url: /sv/python-net/use-error-checking-options/
description: I denna artikel hittar du exempel på kod som programmässigt använder felkontrollalternativ i Excel arbetsblad, t.ex. nummer lagrade som text med hjälp av Aspose.Cells för Python via .NET API.
keywords: Python Excel biblioteket, Python lagra nummer som text i Excel, Hur man hanterar felkontroll i Excel med Python.
---

{{% alert color="primary" %}}

Microsoft Excel tillåter användare att definiera felkontrolloptioner och regler. Användare ser ofta felkontroller när de skapar formler, en liten triangel i det övre högra hörnet av en cell markeras när det är ett problem med en cell. Excel tillhandahåller information som hjälper användare att korrigera vanliga problem.

{{% /alert %}}

## **Typer av fel**

Fel som innebär att formeln inte kan returnera ett resultat - som att dela ett nummer med noll - kräver omedelbar uppmärksamhet och ett felvärde visas i cellen. Genom att klicka på den gröna triangeln visas ett utropstecken, genom att klicka på detta öppnas en lista över alternativ.

Felet kan åtgärdas med hjälp av alternativen eller ignoreras. Att ignorera ett fel innebär att felet inte kommer att visas i ytterligare felkontroller.

Aspose.Cells för Python via .NET tillhandahåller funktioner för felkontroll. [**ErrorCheckOption**](https://reference.aspose.com/cells/python-net/aspose.cells/errorcheckoption)-klassen hanterar olika typer av felkontroller, till exempel nummer lagrade som text, formelberäkningsfel och valideringsfel. Använd [**ErrorCheckType**](https://reference.aspose.com/cells/python-net/aspose.cells/errorchecktype)-enum för att ställa in önskad felkontroll.

## **Nummer som lagras som text**

Ibland kan nummer formateras och lagras i celler som text. Det kan orsaka problem med beräkningar eller producera förvirrande sorteringsordningar. Nummer som är formaterade som text är vänsterjusterade istället för högerjusterade i cellen. Om en formel som ska utföra en matematisk operation på celler inte returnerar ett värde, kontrollera justeringen i cellerna som formeln hänvisar till - vissa eller alla dessa celler kan vara nummer formaterade som text.

Du kan använda felkontrolloptionerna för att snabbt konvertera nummer som lagras som text till verkliga nummer.

1. På **Verktyg**-menyn klickar du på **Alternativ**.
1. Välj fliken Felkontroll. **Nummer lagrade som text**-alternativet är markerat som standard.
1. Inaktivera det.

Följande exempel visar hur man inaktiverar numren som lagras som text felkontroll för ett kalkylblad i mall XLS-filen med hjälp av Aspose.Cells för Python via .NET API:er.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ErrorCheckingOptions-1.py" >}}
