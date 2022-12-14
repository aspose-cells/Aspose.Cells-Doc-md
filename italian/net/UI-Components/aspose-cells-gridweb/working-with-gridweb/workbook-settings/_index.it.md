---
title: Impostazioni per la cartella di lavoro
type: docs
weight: 250
url: /it/net/aspose-cells-gridweb/workbook-settings/
description: Questo articolo descrive le impostazioni della cartella di lavoro per GridWeb.
keywords: settings
---
Ci sono alcune impostazioni che possiamo specificare set GridWorkbookSettings :

 
- **[GridWorkbookSettings](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/GridWorkbookSettings)**

|**Nome** |**Descrizione** |
|:- |:- |
| MaxIterazione| Ottiene o imposta il numero massimo di iterazioni per risolvere un riferimento circolare, il valore predefinito è 100.|
| Iterazione| Ottiene o imposta se utilizzare l'iterazione per risolvere i riferimenti circolari.|
| ForceFullCalcola| Ottiene o imposta se esegue il calcolo completo ogni volta che viene attivato un calcolo.|
| CreateCalcChain|Ottiene o imposta se creare una catena di formule calcolate. L'impostazione predefinita è false.|
| Ricalcola all'apertura| Ottiene o imposta se ricalcolare tutte le formule all'apertura del file.|
| Precisione come visualizzato| True se i calcoli in questa cartella di lavoro verranno eseguiti utilizzando solo la precisione dei numeri così come vengono visualizzati|
| Data 1904| Ottiene o imposta un valore che indica se la cartella di lavoro utilizza il sistema di data 1904.|
| CheckCustomNumberFormat| Ottiene o imposta se controllare il formato numerico personalizzato durante l'impostazione di Style.Custom.|
| Autore| Ottiene e imposta l'autore del file.|
 


Ad esempio, il codice seguente imposta ReCalculateOnOpen su false per arrestare il caculate all'apertura del file:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 il codice seguente imposta l'autore del file:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}
 
 