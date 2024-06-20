---
title: Applicare Filtro Avanzato di Microsoft Excel per Visualizzare Record che Soddisfano Criteri Complessi
type: docs
weight: 280
url: /it/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Scopri come applicare il filtro avanzato di Microsoft Excel per visualizzare record che soddisfano criteri complessi utilizzando l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Applicare Filtro Avanzato Python, Impostare Filtro Avanzato Python, Aggiungere Filtro Avanzato Python, Creare Filtro Avanzato Python, Come aggiungere un filtro avanzato a un range usando Python.
---

## **Possibili Scenari di Utilizzo**

Microsoft Excel consente di applicare *Filtro Avanzato* sui dati del foglio di lavoro per visualizzare record che soddisfano criteri complessi. È possibile applicare un Filtro Avanzato con Microsoft Excel tramite il comando *Dati > Avanzati* come mostrato in questa schermata.

![todo:image_alt_text](1.png)

Aspose.Cells per Python via .NET consente anche di applicare il Filtro Avanzato utilizzando il metodo [**Worksheet.advancedFilter()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/advanced_filter/#bool-str-str-str-bool). Proprio come Microsoft Excel, accetta i seguenti parametri.

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

![todo:image_alt_text](2.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyAdvancedFilterOfMicrosoftExcel.py" >}}
