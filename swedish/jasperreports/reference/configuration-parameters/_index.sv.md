---
title: Konfigurationsparametrar
type: docs
weight: 10
url: /sv/jasperreports/configuration-parameters/
---
{{% alert color="primary" %}} 

 Följande tabell listar konfigurationsparametrarna.

{{% /alert %}} 

|**Parameternamn** |**Beskrivning** |
|:- |:- |
| FORMAT_TYPE| Kan ställas in på "EXCEL97TO2003" eller "EXCEL2007" för att generera filer i Microsoft Excel 79 0 2003 eller Excel 2007.|
|ÄR_ETT_SIDA_PER_ ARK| Ett booleskt värde som anger om varje rapportsida ska skrivas till ett annat XLS-kalkylblad.|
|ÄR_TA BORT_TÖMMA_PLATS_ BETWEEN_ROWS| Ett booleskt värde som anger om de tomma blanksteg som kan visas mellan rader ska tas bort eller inte.|
|ÄR_TA BORT_TÖMMA_PLATS_ BETWEEN_COLUMNS|Ett booleskt värde som anger om de tomma mellanslag som kan visas mellan kolumner ska tas bort eller inte.|
|ÄR_VIT_ PAGE_BACKGROUND| Ett booleskt värde som anger om sidbakgrunden ska vara vit eller standard XLS-bakgrundsfärg. Vad XLS-bakgrundsfärgen är kan variera beroende på XLS-visningsprogrammets egenskaper eller operativsystemets färgschema.|
|ÄR_UPPTÄCKA, DETEKTERA_ CELL_TYPE| Flagga används för att indikera om exportören ska ta hänsyn till typen av de ursprungliga textfältsuttrycken och ställa in celltyperna och värdena därefter.|
| SHEET_NAMES|En rad strängar som representerar anpassade arknamn. Detta är användbart när det används med IS_ETT_SIDA_PER_ SHEET parameter.|
|ÄR_FONT_STORLEK_FIXERA_ AKTIVERAD| Flagga för att minska teckenstorleken så att texten passar in i den angivna cellhöjden.|
|MAXIMAL_RADER_ PER_SHEET|Ett heltalsvärde som anger det maximala antalet rader som får visas i ett ark. När det är inställt skapas ett nytt ark för de återstående raderna som ska visas. Negativa värden eller noll betyder att ingen gräns har satts.|
|ÄR_STRUNTA I_ GRAFIK| Flagga endast för att ignorera grafiska element och exportera textelement.|
|ÄR_KOLLAPS_ ROW_SPAN| Flagga för kollapsande radspann och undvik att slå samman celler över rader.|
|ÄR_STRUNTA I_ CELL_BORDER| Flagga för att ignorera cellkanten.|
|ÄR_ANVÄNDA SIG AV_ EXCEL_CHART| Flagga för att använda redigerbart diagram i Microsoft Excel-format snarare än statiska bilder. Standardvärdet är sant.|

