---
title: Applicare il Filtro Avanzato di Microsoft Excel per visualizzare i record che soddisfano criteri complessi con Golang tramite C++
linktitle: Applicare Filtro Avanzato di Microsoft Excel per Visualizzare Record che Soddisfano Criteri Complessi
type: docs
weight: 280
url: /it/go-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Impara come applicare il filtro avanzato di Microsoft Excel per visualizzare record che soddisfano criteri complessi usando l API Aspose.Cells for C++.
keywords: Applica Filtro Avanzato, Imposta Filtro Avanzato, Aggiungi Filtro Avanzato, Crea Filtro Avanzato, Come aggiungere Filtro Avanzato a un intervallo
---

## **Possibili Scenari di Utilizzo**

Microsoft Excel ti permette di applicare *Filtro Avanzato* sui dati del foglio di lavoro per visualizzare record che soddisfano criteri complessi. Puoi applicare il filtro avanzato con Microsoft Excel tramite il comando *Dati > Avanzate* come mostrato in questo screenshot.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells consente anche di applicare il filtro avanzato usando il metodo [**GetAdvancedFilter()**](https://reference.aspose.com/cells/go-cpp/worksheet/getadvancedfilter/). Come Microsoft Excel, accetta i seguenti parametri.

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

Il seguente esempio di codice applica il filtro avanzato sul [File Excel di esempio](48496692.xlsx) e genera il [File Excel di output](48496691.xlsx). Lo screenshot mostra entrambi i file per confronto. Come si può vedere nello screenshot, i dati sono stati filtrati all'interno del file Excel di output secondo criteri complessi.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyAdvancedFilterOfMicrosoftExcelToDisplayRecordsMeetingComplexCriteria.go" >}}
