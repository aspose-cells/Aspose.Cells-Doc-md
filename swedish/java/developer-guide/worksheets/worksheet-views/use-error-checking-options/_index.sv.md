---
title: Använd alternativ för felkontroll
type: docs
weight: 60
url: /sv/java/use-error-checking-options/
---
{{% alert color="primary" %}} 

Microsoft Excel tillåter användare att definiera felkontrollalternativ och regler. Användare ser ofta felkontroller när de skapar formler, en liten triangel i det övre högra hörnet av en cell markerar när det finns ett problem med en cell. Excel tillhandahåller information som hjälper användare att åtgärda vanliga problem.

{{% /alert %}} 
## **Typer av fel**
Fel som gör att formeln inte kan returnera ett resultat - som att dividera ett tal med noll - kräver omedelbar uppmärksamhet och ett felvärde visas i cellen. Om du klickar på den gröna triangeln visas ett utropstecken, om du klickar på detta öppnas en lista med alternativ.

Felet kan lösas med hjälp av alternativen eller ignoreras. Att ignorera ett fel innebär att det felet inte kommer att visas i ytterligare felkontroller.

Aspose.Cells ger felkontrollfunktioner. Klassen ErrorCheckOptions hanterar olika typer av felkontroller, till exempel nummer lagrade som text, formelberäkningsfel och valideringsfel. Använd ErrorCheckType-uppräkningen för att ställa in önskad felkontroll.
## **Numbers Lagrat som text**
Ibland kan siffror formateras och lagras i celler som text. Detta kan orsaka problem med beräkningar eller skapa förvirrande sorteringsordningar. Numbers som är formaterade som text är vänsterjusterade istället för högerjusterade i cellen. Om en formel som ska utföra en matematisk operation på celler inte returnerar ett värde, kontrollera justeringen i cellerna som formeln refererar till – några eller alla av dessa celler kan vara siffror formaterade som text.

Du kan använda alternativen för felkontroll för att snabbt konvertera siffror som lagrats som text till reella siffror. I Microsoft Excel 2003:

1.  På**Verktyg** menyn, klicka**alternativ**.
1. Välj fliken Felkontroll.
   **Nummer lagras som text** alternativet är markerat som standard.
1. Inaktivera den.
 Se bilden nedan om hur den gröna triangeln visas för data i MS Excel.

![todo:image_alt_text](use-error-checking-options_1.png)

 Följande exempelkod visar hur du inaktiverar siffrorna som lagras som textfelkontrollalternativ för ett kalkylblad i mallen XLS-filen med hjälp av Aspose.Cells-API:erna.

**Java**

{{< highlight "csharp" >}}

 //Create a workbook and opening a template spreadsheet

Workbook workbook = new Workbook("d:\\files\\Book1.xls");

//Get the first worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Instantiate the error checking options

ErrorCheckOptionCollection opts = sheet.getErrorCheckOptions();

int index = opts.add();

ErrorCheckOption opt = opts.get(index);

//Disable the numbers stored as text option

opt.setErrorCheck(ErrorCheckType.TEXT_NUMBER, false);

//Set the range

opt.addRange(CellArea.createCellArea(0, 0, 65535, 255));

//Save the Excel file

workbook.save("d:\\files\\out_test.xls");



{{< /highlight >}}
