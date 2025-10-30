---
title: Asse data
description: Scopri come gestire l asse delle date in Aspose.Cells per Python via .NET. La nostra guida ti aiuterà a comprendere come lavorare con vari formati di data, scale temporali e frequenze delle etichette.
keywords: Aspose.Cells per Python via .NET, asse delle date, gestione, formati di data, scale temporali, frequenze delle etichette.
type: docs
weight: 200
url: /it/python-net/date-axis/
---

## **Possibili Scenari di Utilizzo**
Quando si crea un grafico dai dati del foglio di lavoro che utilizza date, e le date sono tracciate lungo l'asse orizzontale (categoria) nel grafico, Aspose.cells cambia automaticamente l'asse categoria in un asse data (scala temporale).
Un asse data visualizza le date in ordine cronologico a intervalli o unità di base specifici, come il numero di giorni, mesi o anni, anche se le date sul foglio di lavoro non sono in ordine sequenziale o nelle stesse unità di base.
Per impostazione predefinita, Aspose.cells determina le unità di base per l'asse data in base alla differenza più piccola tra due date in dati sul foglio di lavoro. Ad esempio, se si hanno dati relativi ai prezzi delle azioni in cui la differenza più piccola tra le date è di sette giorni, Excel imposta l'unità di base su giorni, ma è possibile modificare l'unità di base a mesi o anni se si desidera vedere le performance dell'azione su un periodo più lungo.

## **Gestire l'Asse Data come Microsoft Excel**
Si prega di vedere il seguente codice di esempio che crea un nuovo file Excel e inserisce i valori del grafico nel primo foglio di lavoro. 
Poi aggiungiamo un grafico e impostiamo il tipo del [**Axis**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis) 
a [**TIME_SCALE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/categorytype/) e quindi impostiamo le unità di base su Giorni.

![todo:image_alt_text](excel.png)

## **Codice di Esempio**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DateAxis.py" >}}
{{< app/cells/assistant language="python-net" >}}
