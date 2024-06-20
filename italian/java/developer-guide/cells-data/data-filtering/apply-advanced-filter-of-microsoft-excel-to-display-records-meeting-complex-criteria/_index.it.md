---
title: Applicare Filtro Avanzato di Microsoft Excel per Visualizzare Record che Soddisfano Criteri Complessi
type: docs
weight: 190
url: /it/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---

## **Possibili Scenari di Utilizzo**
Microsoft Excel consente di applicare *Filtro Avanzato* sui dati del foglio di lavoro per visualizzare record che soddisfano criteri complessi. È possibile applicare un Filtro Avanzato con Microsoft Excel tramite il comando *Dati > Avanzati* come mostrato in questa schermata.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells consente anche di applicare il Filtro Avanzato utilizzando il metodo [Worksheet.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)). Come Microsoft Excel, accetta i seguenti parametri.

**isFilter**

Indica se filtrare l'elenco sul posto.

**listRange**

L'intervallo dell'elenco.

**criteriaRange**

L'intervallo dei criteri.

**copyTo**

L'intervallo in cui copiare i dati.

**uniqueRecordOnly**

Mostra o copia solo le righe uniche.
## **Applicare il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano criteri complessi**
Il codice di esempio seguente applica il filtro avanzato al [File Excel di esempio](48496702.xlsx) e genera il [File Excel di output](48496705.xlsx). La schermata mostra entrambi i file a scopo di confronto. Come si può vedere dalla schermata, i dati sono stati filtrati all'interno del file Excel di output secondo criteri complessi.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
