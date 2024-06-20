---
title: Använda alternativ för felkontroll
type: docs
weight: 140
url: /sv/net/use-error-checking-options/
description: I den här artikeln hittar du exempelkod som programmatoriskt använder felkontrolloptions av Excel kalkylblad t.ex. Nummer som är lagrade som text med C# API eller .NET Library.
keywords: lagra nummer som text i excel med c#, felkontroll excel alternativ c#
---

{{% alert color="primary" %}}

Microsoft Excel tillåter användare att definiera felkontrolloptioner och regler. Användare ser ofta felkontroller när de skapar formler, en liten triangel i det övre högra hörnet av en cell markeras när det är ett problem med en cell. Excel tillhandahåller information som hjälper användare att korrigera vanliga problem.

{{% /alert %}}

## **Typer av fel**

Fel som innebär att formeln inte kan returnera ett resultat - som att dela ett nummer med noll - kräver omedelbar uppmärksamhet och ett felvärde visas i cellen. Genom att klicka på den gröna triangeln visas ett utropstecken, genom att klicka på detta öppnas en lista över alternativ.

Felet kan åtgärdas med hjälp av alternativen eller ignoreras. Att ignorera ett fel innebär att felet inte kommer att visas i ytterligare felkontroller.

Aspose.Cells tillhandahåller felkontrolloptionsfunktioner. [**ErrorCheckOption**](https://reference.aspose.com/cells/net/aspose.cells/errorcheckoption)-klassen hanterar olika typer av felkontroller, till exempel nummer lagrade som text, formelberäkningsfel och valideringsfel. Använd [**ErrorCheckType**](https://reference.aspose.com/cells/net/aspose.cells/errorchecktype)-uppräkningen för att ställa in önskad felkontroll.

## **Nummer som lagras som text**

Ibland kan nummer formateras och lagras i celler som text. Det kan orsaka problem med beräkningar eller producera förvirrande sorteringsordningar. Nummer som är formaterade som text är vänsterjusterade istället för högerjusterade i cellen. Om en formel som ska utföra en matematisk operation på celler inte returnerar ett värde, kontrollera justeringen i cellerna som formeln hänvisar till - vissa eller alla dessa celler kan vara nummer formaterade som text.

Du kan använda felkontrolloptionerna för att snabbt konvertera nummer som lagras som text till verkliga nummer.

1. På **Verktyg**-menyn klickar du på **Alternativ**.
1. Markera fliken för Felkontroll.
   **Alternativ för siffror sparade som text** alternativet är markerat som standard.
1. Inaktivera det.

Följande exempelkod visar hur man inaktiverar felkontrollen för siffror sparade som text för en arbetsbok i mallen XLS med hjälp av Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ErrorCheckingOptions-1.cs" >}}
