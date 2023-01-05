---
title: Applica il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano i criteri complessi
type: docs
weight: 190
url: /it/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---
## **Possibili scenari di utilizzo**
 Microsoft Excel consente di applicare*Filtro avanzato* sui dati del foglio di lavoro per visualizzare i record che soddisfano criteri complessi. Puoi applicare il filtro avanzato con Microsoft Excel tramite il suo*Dati > Avanzate*comando come mostrato in questa schermata.

![cose da fare:immagine_alt_testo](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells consente inoltre di applicare il Filtro Avanzato utilizzando il[Foglio di lavoro.Filtro avanzato()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)) metodo. Proprio come Microsoft Excel, accetta i seguenti parametri.

**isFilter**

Indica se filtrare l'elenco in posizione.

**listRange**

L'intervallo di elenco.

**criteriIntervallo**

I criteri variano.

**copia a**

L'intervallo in cui copiare i dati.

**unicoRecordOnly**

Solo visualizzazione o copia di righe univoche.
## **Applica il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano i criteri complessi**
Il codice di esempio seguente applica il filtro avanzato su[Esempio di file Excel](48496702.xlsx) e genera il[File Excel di output](48496705.xlsx). Lo screenshot mostra entrambi i file per il confronto. Come puoi vedere all'interno dello screenshot, i dati sono stati filtrati all'interno del file Excel di output secondo criteri complessi.

![cose da fare:immagine_alt_testo](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **Codice d'esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
