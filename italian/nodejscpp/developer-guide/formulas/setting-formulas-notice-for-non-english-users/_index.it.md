---
title: Impostare formule  Notifica per utenti non inglesi con Node.js tramite C++
linktitle: Impostazione Formule  Avviso per gli Utenti Non Anglofoni
type: docs
weight: 10
url: /it/nodejs-cpp/setting-formulas-notice-for-non-english-users/
---  

{{% alert color="primary" %}} 

Aspose.Cells supporta la maggior parte delle formule/funzioni di Microsoft Excel. Gli sviluppatori possono usare queste formule tramite l'API o i [fogli di calcolo designer](/cells/it/nodejs-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells supporta un vasto insieme di formule matematiche, stringa, booleane, data/ora, statistiche, database, ricerca e riferimento. Le formule devono essere specificate in inglese (Stile US).

{{% /alert %}} 

## **Avviso per gli Utenti Non Anglofoni**
Ci sono due suggerimenti che gli utenti non anglofoni devono seguire quando creano formule con Aspose.Cells:

1. Le formule devono essere inserite in inglese. Per esempio, utilizzare l'inglese "=SUM()" e non il tedesco "=SUMME()".
1. Usa sempre una virgola (,) per delimitare i parametri della funzione. Per alcune opzioni di lingua o impostazioni, il delimitatore potrebbe essere un punto e virgola, ma Aspose.Cells utilizza la virgola in stile inglese. Ad esempio, usa "=SE (C5=0,0,C3/C4)" anziché "=SE(C5=0;0;C3/C4)".  
