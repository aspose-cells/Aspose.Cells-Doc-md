---
title: Impostare formule  Avviso per utenti non inglesi con C++
linktitle: Impostazione Formule  Avviso per gli Utenti Non Anglofoni
type: docs
weight: 10
url: /it/cpp/setting-formulas-notice-for-non-english-users/
description: Impara come impostare le formule in Aspose.Cells for C++ con stile in inglese (US) per utenti non inglesi.
---

{{% alert color="primary" %}} 

Aspose.Cells supporta la maggior parte delle formule/funzioni che fanno parte di Microsoft Excel. Gli sviluppatori possono usare queste formule con l'API o [designer di fogli di calcolo](/cells/it/cpp/what-is-a-designer-spreadsheet/). Aspose.Cells supporta un ampio insieme di formule matematiche, di stringa, booleane, data/ora, statistiche, database, ricerca e riferimento. Le formule devono essere specificate usando lo stile in inglese (US).

{{% /alert %}} 

## **Avviso per gli Utenti Non Anglofoni**
Ci sono due suggerimenti che gli utenti non anglofoni devono seguire quando creano formule con Aspose.Cells:

1. Le formule devono essere inserite in inglese. Per esempio, utilizzare l'inglese "=SUM()" e non il tedesco "=SUMME()".
1. Usa sempre una virgola (,) per delimitare i parametri della funzione. Per alcune opzioni di lingua o impostazioni, il delimitatore potrebbe essere un punto e virgola, ma Aspose.Cells utilizza la virgola in stile inglese. Ad esempio, usa "=SE (C5=0,0,C3/C4)" anziché "=SE(C5=0;0;C3/C4)".
