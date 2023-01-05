---
title: Popola automaticamente i dati degli indicatori intelligenti in altri fogli di lavoro se i dati sono troppo grandi
type: docs
weight: 10
url: /it/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---
## **Possibili scenari di utilizzo**

A volte, si desidera popolare automaticamente i dati degli indicatori intelligenti in altri fogli di lavoro se sono troppo grandi. Supponiamo che l'origine dati contenga 1500000 record. Questi sono troppi record per un singolo foglio di lavoro, quindi puoi spostare il resto dei record nel foglio di lavoro successivo.

## **Popola automaticamente i dati degli indicatori intelligenti in altri fogli di lavoro se i dati sono troppo grandi**

Il seguente codice di esempio ha un'origine dati con 21 record. Vogliamo mostrare solo 15 record in un foglio di lavoro, quindi il resto dei record passerà automaticamente al secondo foglio di lavoro. Tieni presente che anche il secondo foglio di lavoro dovrebbe avere lo stesso tag marcatore intelligente e devi chiamare[**WorkbookDesigner.process(sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process(int,%20boolean) ) metodo per entrambi i fogli. Si prega di controllare[Microsoft File di accesso al database](60489777.accdb) utilizzato in questo codice così come il[file Excel di output](60489786.xlsx)generato dal codice per un riferimento.

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
