---
title: Popola automaticamente i dati del marcatore intelligente in altre schede se i dati sono troppo numerosi
type: docs
weight: 50
url: /it/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **Possibili Scenari di Utilizzo**
A volte si desidera popolare automaticamente i dati del marcatore intelligente in altre schede se sono troppo grandi. Supponiamo che la tua fonte dati abbia 1500000 record. Questi sono troppi record per un singolo foglio di lavoro, quindi è possibile spostare il resto dei record nel foglio di lavoro successivo. 
## **Popolare automaticamente i dati del marcatore intelligente in altre schede se i dati sono troppo grandi**
Il seguente codice di esempio ha una fonte dati che contiene 21 record. Vogliamo mostrare solo 15 record in un foglio di lavoro, quindi il resto dei record verrà spostato automaticamente nel secondo foglio di lavoro. Si noti che il secondo foglio di lavoro dovrebbe avere anche lo stesso tag del marcatore intelligente e è necessario chiamare il metodo [WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) per entrambi i fogli. Si prega di consultare il [file Excel di output](60489775.xlsx) generato dal codice per un riferimento.
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
