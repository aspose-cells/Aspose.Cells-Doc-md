---
title: Automatisk anpassning av rader och kolumner
type: docs
weight: 20
url: /sv/python-net/autofit-rows-and-columns/
description: Denna artikel visar hur man automatiskt justerar rader, kolumner, rader för sammanslagna celler och rad i en cellräckvidd med Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Python Autofit rader, Python Autofit kolumner, Python Autofit rad i en cellräckvidd, Python Autofit rader för sammanslagna celler.
---

{{% alert color="primary" %}}

Microsoft Excel låter användarna automatiskt ändra bredd och höjd på celler efter innehållet. Denna funktion är också tillgänglig genom Aspose.Cells för Python via .NET så utvecklare kan ändra dimensionerna på en cell vid körning.

{{% /alert %}}

## **Autostorlek**

Aspose.Cells för Python via .NET tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-samling som tillåter åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. Denna artikel tittar på att använda [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-klassen för att automatiskt justera rader eller kolumner.

### **AutoFit Row - Enkelt**

Det mest raka tillvägagångssättet för att automatiskt justera bredd och höjd för en rad är att anropa klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) metoden [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int). Metoden [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) tar en radindex (av raden som ska ändras) som parameter.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsandColumns-1.py" >}}

### **Hur man Autofitrad i ett område av celler**

En rad består av många kolumner. Aspose.Cells för Python via .NET tillåter utvecklare att automatiskt anpassa en rad baserad på innehållet i en cellräckvidd inom raden genom att anropa en överbelastad version av [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int) metoden. Den tar följande parametrar:

- **Radindex**, index för raden som ska autofit.
- **Första kolumnindex**, index för radens första kolumn.
- **Sista kolumnindex**, index för radens sista kolumn.

Metoden [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int) kontrollerar innehållet i alla kolumner i raden och anpassar sedan raden automatiskt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowinSpecificRange-1.py" >}}

### **Hur man Autofittar kolumn i ett område av celler**

En kolumn består av många rader. Det är möjligt att automatiskt justera en kolumn baserad på innehållet i ett område av celler i kolumnen genom att anropa en överlagrad version av metoden [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) som tar följande parametrar:

- **Kolumnindex**, index för kolumnen som ska autofit.
- **Första radindex**, index för kolumnens första rad.
- **Sista radindex**, index för kolumnens sista rad.

Metoden [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) kontrollerar innehållet i alla rader i kolumnen och anpassar sedan kolumnen automatiskt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitColumninSpecificRange-1.py" >}}

### **Hur man Autofittar rader för sammanfogade celler**

Med Aspose.Cells for Python via .NET är det möjligt att autofit-rader även för celler som har sammanfogats med hjälp av [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) API. [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) klass tillhandahåller [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) egenskap som kan användas för att autofit-rader för sammanfogade celler. [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) accepterar [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype) uppräkningsbar som har följande medlemmar.

- INGEN: Ignorera sammanfogade celler.
- FÖRSTA_RADEN: Utvidgar bara höjden på första raden.
- SISTA_RADEN: Utvidgar bara höjden på sista raden.
- VARJE_RAD: Utvidgar bara höjden på varje rad.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsforMergedCells-1.py" >}}

{{% alert color="primary" %}}

Du kan även försöka att använda de överlagrade versionerna av [**auto_fit_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_rows/#int-int-aspose.cells.AutoFitterOptions) och [**auto_fit_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_columns/#int-int-aspose.cells.AutoFitterOptions) metoder som accepterar ett område av rader/kolumner och en instans av [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) för att automatiskt anpassa de valda raderna/kolumnerna med din önskade  [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) i enlighet.

Signaturerna för ovanstående metoder är som följer:

1. autofit_rader(start_rad, slut_rad, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) alternativ)
1. auto_fit_columns(first_column, last_column, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions))

{{% /alert %}}

## **Viktigt att veta**

{{% alert color="primary" %}}

Om en cell är sammanfogad kommer inte AutoFit-metoderna att appliceras, vilket är samma beteende som i Microsoft Excel. Du kan komma runt detta genom att använda auto filter API. Dessutom, om texten i en cell är radbryten, kommer inte metoden [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) att tillämpas heller. En annan sak du behöver veta är att *AutoFit*-metoderna tar lång tid. Så, du bör anropa dessa metoder så sällan som möjligt för att säkerställa effektiviteten i din applikation.

{{% /alert %}}

## **Fortsatta ämnen**
- [Automatisk justering av rader för sammanfogade celler](/cells/sv/python-net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="python-net" >}}
