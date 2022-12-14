---
title: Använd alternativ för felkontroll
type: docs
weight: 140
url: /sv/net/use-error-checking-options/
---
{{% alert color="primary" %}}

Microsoft Excel tillåter användare att definiera felkontrollalternativ och regler. Användare ser ofta felkontroller när de skapar formler, en liten triangel i det övre högra hörnet av en cell markerar när det finns ett problem med en cell. Excel tillhandahåller information som hjälper användare att åtgärda vanliga problem.

{{% /alert %}}

## **Typer av fel**

Fel som gör att formeln inte kan returnera ett resultat - som att dividera ett tal med noll - kräver omedelbar uppmärksamhet och ett felvärde visas i cellen. Om du klickar på den gröna triangeln visas ett utropstecken, om du klickar på detta öppnas en lista med alternativ.

Felet kan lösas med hjälp av alternativen eller ignoreras. Att ignorera ett fel innebär att det felet inte kommer att visas i ytterligare felkontroller.

Aspose.Cells ger felkontrollfunktioner. De[**ErrorCheckOption**](https://reference.aspose.com/cells/net/aspose.cells/errorcheckoption) class hanterar olika typer av felkontroller, till exempel siffror lagrade som text, formelberäkningsfel och valideringsfel. Använd[**ErrorCheckType**](https://reference.aspose.com/cells/net/aspose.cells/errorchecktype)uppräkning för att ställa in önskad felkontroll.

## **Siffror lagrade som text**

Ibland kan siffror formateras och lagras i celler som text. Detta kan orsaka problem med beräkningar eller skapa förvirrande sorteringsordningar. Siffror som är formaterade som text är vänsterjusterade istället för högerjusterade i cellen. Om en formel som ska utföra en matematisk operation på celler inte returnerar ett värde, kontrollera justeringen i cellerna som formeln refererar till – några eller alla av dessa celler kan vara siffror formaterade som text.

Du kan använda alternativen för felkontroll för att snabbt konvertera siffror som lagrats som text till reella siffror. I Microsoft Excel 2003:

1.  På**Verktyg** menyn, klicka**alternativ**.
1. Välj fliken Felkontroll.
   **Nummer lagras som text** alternativet är markerat som standard.
1. Inaktivera den.

Följande exempelkod visar hur du inaktiverar siffrorna som lagras som textfelkontrollalternativ för ett kalkylblad i mallens XLS-fil med Aspose.Cells API:er.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ErrorCheckingOptions-1.cs" >}}
