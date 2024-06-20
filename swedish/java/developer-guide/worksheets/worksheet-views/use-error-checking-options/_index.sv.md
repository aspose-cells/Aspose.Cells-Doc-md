---
title: Använda alternativ för felkontroll
type: docs
weight: 60
url: /sv/java/use-error-checking-options/
---

{{% alert color="primary" %}} 

Microsoft Excel låter användare definiera felkontrollalternativ och regler. Användare ser ofta felkontroller vid skapande av formler, en liten triangel i övre högra hörnet på en cell markeras om det finns ett problem med en cell. Excel tillhandahåller information som hjälper användare att korrigera vanliga problem.

{{% /alert %}} 
## **Typer av fel**
Fel som innebär att formeln inte kan returnera ett resultat - som att dividera ett tal med noll - kräver omedelbar uppmärksamhet och ett felvärde visas i cellen. Klicka på den gröna triangeln, ett utropstecken visas. Genom att klicka på detta öppnas en lista med alternativ. 

Felet kan åtgärdas med hjälp av alternativen eller ignoreras. Att ignorera ett fel innebär att felet inte kommer att visas i ytterligare felkontroller.

Aspose.Cells tillhandahåller funktioner för felkontroll. Klassen ErrorCheckOptions hanterar olika typer av felkontroller, till exempel nummer som lagras som text, formelberäkningsfel och valideringsfel. Använd enum ErrorCheckType för att ställa in önskad felkontroll.
## **Nummer som lagras som text**
Ibland kan nummer formateras och lagras i celler som text. Det kan orsaka problem med beräkningar eller producera förvirrande sorteringsordningar. Nummer som är formaterade som text är vänsterjusterade istället för högerjusterade i cellen. Om en formel som ska utföra en matematisk operation på celler inte returnerar ett värde, kontrollera justeringen i cellerna som formeln hänvisar till - vissa eller alla dessa celler kan vara nummer formaterade som text.

Du kan använda felkontrolloptionerna för att snabbt konvertera nummer som lagras som text till verkliga nummer.

1. På **Verktyg**-menyn klickar du på **Alternativ**.
1. Markera fliken för Felkontroll.
   **Alternativ för siffror sparade som text** alternativet är markerat som standard. 
1. Inaktivera det.
   Se nedanstående bild om hur den gröna triangeln visas för datan i MS Excel.

![todo:image_alt_text](use-error-checking-options_1.png)

Följande exempelkod visar hur man inaktiverar felkontrollen för siffror sparade som text för en arbetsbok i mallen XLS med hjälp av Aspose.Cells API. 

**Java**

{{< highlight csharp >}}

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
