---
title: Popola automaticamente i dati del marcatore intelligente in altre schede se i dati sono troppo numerosi
type: docs
weight: 10
url: /it/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **Possibili Scenari di Utilizzo**

A volte, desideri popolare automaticamente i dati del marcatore intelligente in altre schede se sono troppo numerosi. Supponiamo che la tua fonte dati abbia 1500000 record. Questi sono troppi record per un singolo foglio di lavoro, quindi puoi spostare il resto dei record nel foglio di lavoro successivo.

## **Auto Popolare i Dati di Smart Marker in Altri Fogli di Lavoro se i Dati sono Troppo Numerosi**

Il seguente codice di esempio ha una fonte dati che ha 21 record. Vogliamo mostrare solo 15 record in un foglio di lavoro, quindi il resto dei record verrà automaticamente spostato nel secondo foglio di lavoro. Si noti che il secondo foglio di lavoro dovrebbe avere lo stesso tag di marcatore intelligente e è necessario chiamare il metodo [**WorkbookDesigner.process(sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process-int-boolean-) per entrambi i fogli. Controlla anche il file [Microsoft Access Database](60489777.accdb) utilizzato in questo codice così come il [file di Excel di output](60489786.xlsx) generato dal codice per un riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
{{< app/cells/assistant language="java" >}}
