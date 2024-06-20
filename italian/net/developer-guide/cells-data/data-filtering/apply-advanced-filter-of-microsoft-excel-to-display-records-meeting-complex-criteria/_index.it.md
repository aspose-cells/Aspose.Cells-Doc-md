---
title: Applicare Filtro Avanzato di Microsoft Excel per Visualizzare Record che Soddisfano Criteri Complessi
type: docs
weight: 280
url: /it/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Scopri come applicare il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano criteri complessi utilizzando l API Aspose.Cells for .NET.
keywords: Applica Filtro Avanzato, Imposta Filtro Avanzato, Aggiungi Filtro Avanzato, Crea Filtro Avanzato, Come aggiungere Filtro Avanzato a un intervallo 
---

## **Possibili Scenari di Utilizzo**

Microsoft Excel consente di applicare *Filtro Avanzato* sui dati del foglio di lavoro per visualizzare record che soddisfano criteri complessi. È possibile applicare un Filtro Avanzato con Microsoft Excel tramite il comando *Dati > Avanzati* come mostrato in questa schermata.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Anche Aspose.Cells ti consente di applicare il Filtro Avanzato utilizzando il metodo [**Worksheet.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter). Proprio come Microsoft Excel, accetta i seguenti parametri.

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

Il seguente codice di esempio applica il filtro avanzato sul [File Excel di Esempio](48496692.xlsx) e genera il [File Excel di Output](48496691.xlsx). La schermata mostra entrambi i file a scopo di confronto. Come si può vedere nella schermata, i dati sono stati filtrati all'interno del file Excel di output secondo criteri complessi.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
