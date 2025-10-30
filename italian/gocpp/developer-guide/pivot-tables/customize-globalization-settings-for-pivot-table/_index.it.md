---
title: Personalizza le impostazioni di globalizzazione per la tabella pivot con Golang tramite C++
linktitle: Personalizza le impostazioni di globalizzazione per la tabella pivot
type: docs
weight: 50
url: /it/go-cpp/customize-globalization-settings-for-pivot-table/
description: Impara come personalizzare le impostazioni di globalizzazione della pivot table usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

A volte si desidera personalizzare il testo *Totale Pivot, Sub Totale, Totale Generale, Tutti gli Elementi, Elementi Multipli, Etichette di colonna, Etichette di riga, Valori Vuoti* secondo le proprie esigenze. Aspose.Cells for C++ consente di personalizzare le impostazioni di globalizzazione della pivot table per gestire tali scenari. È inoltre possibile utilizzare questa funzione per cambiare le etichette in altre lingue come arabo, hindi, polacco, ecc.

## **Personalizza le impostazioni di globalizzazione per la tabella pivot**

Il seguente esempio di codice spiega come personalizzare le impostazioni di globalizzazione per la pivot table in C++. Crea una classe *CustomPivotTableGlobalizationSettings* derivata dalla classe base [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/pivotglobalizationsettings/) e sovrascrive tutti i metodi necessari. Questi metodi restituiscono testi personalizzati per vari elementi della pivot table. Il codice quindi assegna questa implementazione alla proprietà [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/). L'esempio carica un [file Excel di origine](40468488.xlsx), aggiorna i dati della pivot e lo salva come [file PDF di output](40468487.pdf). La schermata sotto mostra le etichette personalizzate nell'output.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizeGlobalizationSettingsForPivotTable.go" >}}
