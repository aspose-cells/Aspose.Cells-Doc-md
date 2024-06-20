---
title: Impostazioni per il workbook
type: docs
weight: 250
url: /it/net/aspose-cells-gridweb/aspose-cells-gridweb/workbook-settings/
description: Questo articolo descrive le impostazioni del workbook in GridWeb.
keywords: GridWeb, impostazioni
---


Ci sono alcune impostazioni che possiamo specificare impostando GridWorkbookSettings :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/GridWorkbookSettings)

|**Nome** |**Descrizione** |
| :- | :- |
|MaxIteration | Ottiene o imposta il numero massimo di iterazioni per risolvere un riferimento circolare, il valore predefinito è 100. |
|Iteration | Ottiene o imposta se utilizzare l'iterazione per risolvere i riferimenti circolari. |
|ForceFullCalculate | Ottiene o imposta se calcola completamente ogni volta che viene attivato un calcolo. |
|CreateCalcChain | Ottiene o imposta se creare una catena di formule calcolate. Il valore predefinito è falso. |
|ReCalculateOnOpen | Ottiene o imposta se ricalcolare tutte le formule all'apertura del file. |
|PrecisionAsDisplayed | True se i calcoli in questo documento verranno eseguiti utilizzando solo la precisione dei numeri come vengono visualizzati |
|Date1904 | Ottiene o imposta un valore che rappresenta se il documento utilizza il sistema di date 1904. |
|CheckCustomNumberFormat | Ottiene o imposta se controllare il formato numerico personalizzato quando si imposta Style.Custom. |
|Author | Ottiene e imposta l'autore del file. |



Ad esempio, il seguente codice imposta ReCalculateOnOpen su false per impedire il calcolo all'apertura del file:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 il seguente codice imposta l'autore per il file:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}


