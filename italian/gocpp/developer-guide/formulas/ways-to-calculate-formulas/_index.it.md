---
title: Modi per Calcolare le Formule
type: docs
weight: 30
url: /it/go-cpp/ways-to-calculate-formulas/
---

## **Introduzione**

Aspose.Cells ha un motore di calcolo delle formule integrato. Può non solo ricalcolare le formule importate dai modelli del designer ma supporta anche il calcolo dei risultati delle formule aggiunte in fase di esecuzione.

## **Aggiungere Formule & Calcolare i Risultati**

Aspose.Cells supporta la maggior parte delle formule o funzioni che fanno parte di Microsoft Excel. Possono essere utilizzate tramite l'API o utilizzando i fogli di calcolo del designer. Aspose.Cells supporta un vasto insieme di formule matematiche, stringhe, booleani, date/orario, statistiche, ricerca e riferimento.

Utilizzare il metodo Cell.SetFormula per aggiungere una formula a una cella. Quando si applica una formula a una cella, iniziare sempre la stringa con un segno uguale (=) come si fa quando si crea una formula in Microsoft Excel. Utilizzare una virgola (,) per delimitare i parametri della funzione.

Per calcolare i risultati delle formule, chiamare il metodo Workbook.CalculateFormula() che elabora tutte le formule incorporate in un file Excel. Si prega di controllare il seguente codice di esempio che aggiunge la formula e ne calcola i risultati. Si prega di controllare il [file di Excel di output](38109185.xlsx) generato con questo codice.

**Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingFormulasAndCalculatingResults.go" >}}

## **Calcolare le Formule Solo una Volta**

Quando si chiama Workbook.CalculateFormula() per calcolare i valori delle formule in un modello di cartella di lavoro, Aspose.Cells crea una catena di calcolo. Aumenta le prestazioni quando le formule vengono calcolate per la seconda o terza volta.

Tuttavia, se il modello contiene molte formule, la prima volta che la formula viene calcolata può consumare molto tempo di elaborazione della CPU e memoria.

Aspose.Cells ti consente di disattivare la creazione di una catena di calcolo, utile quando si vuole calcolare le formule solo una volta.

Si prega di chiamare Workbook.GetISettings().SetCreateCalcChain() con il parametro false. È possibile utilizzare il [file Excel fornito](38109186.xlsx) per testare questo codice.

**Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculatingFormulasOnceOnly.go" >}}
