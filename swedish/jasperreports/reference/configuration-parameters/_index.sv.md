---
title: Konfigureringsparametrar
type: docs
weight: 10
url: /sv/jasperreports/configuration-parameters/
---

{{% alert color="primary" %}} 

Följande tabell listar konfigureringsparametrarna. 

{{% /alert %}} 

|**Parameternamn** |**Beskrivning** |
| :- | :- |
|FORMAT_TYPE |Kan ställas in till "EXCEL97TO2003" eller "EXCEL2007" för att generera Microsoft Excel 79 0 2003 eller Excel 2007-formatfiler. |
|IS_ONE_PAGE_PER_SHEET |Ett booleskt värde som specifierar om varje rapportssida ska skrivas till ett annat XLS-ark. |
|IS_REMOVE_EMPTY_SPACE_BETWEEN_ROWS |Ett booleskt värde som specifierar om de tomma utrymmena som kan förekomma mellan rader ska tas bort eller inte. |
|IS_REMOVE_EMPTY_SPACE_BETWEEN_COLUMNS |Ett booleskt värde som specifierar om de tomma utrymmena som kan förekomma mellan kolumner ska tas bort eller inte. |
|IS_WHITE_PAGE_BACKGROUND |Ett booleskt värde som specifierar om sidans bakgrund ska vara vit eller standard XLS-bakgrundsfärg. Vilken bakgrundsfärg XLS har kan variera beroende på XLS-visningsinställningar eller operativsystemets färgschema. |
|IS_DETECT_CELL_TYPE |Flagga som används för att ange om exportören ska ta hänsyn till originaltextfältuttryckens typ och ställa in celltyper och värden därefter. |
|SHEET_NAMES |En matris av strängar som representerar anpassade bladnamn. Detta är användbart när det används med IS_ONE_PAGE_PER_SHEET-parametern. |
|IS_FONT_SIZE_FIX_ENABLED |Flagga för att minska teckensnittets storlek så att texten passar i den angivna cellhöjden. |
|MAXIMUM_ROWS_PER_SHEET |Ett heltal som anger det maximala antalet rader som är tillåtet att visas i ett ark. När det är inställt skapas ett nytt ark för de återstående raderna som ska visas. Negativa värden eller noll betyder att ingen gräns har ställts in.
|IS_IGNORE_GRAPHICS |Flagga för att ignorera grafiska element och exportera endast textelement.
|IS_COLLAPSE_ROW_SPAN |Flagga för att kollapsa radspänning och undvika att sammanfoga celler över rader.
|IS_IGNORE_CELL_BORDER |Flagga för att ignorera cellgränsen.
|IS_USE_EXCEL_CHART |Flagga för att använda redigerbar diagram i Microsoft Excel-format istället för statiska bilder. Standardvärdet är sant.

