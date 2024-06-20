---
title: Impostazione Formule  Avviso per gli Utenti Non Anglofoni
type: docs
weight: 10
url: /it/net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells supporta la maggior parte delle formule/funzioni che fanno parte di Microsoft Excel. Gli sviluppatori possono utilizzare queste formule con l'API o [fogli di calcolo di progettazione](/cells/it/net/what-is-a-designer-spreadsheet/). Aspose.Cells supporta un vasto insieme di formule matematiche, stringa, Booleano, data/ora, statistiche, database, riferimento e ricerca. Le formule dovrebbero essere specificate utilizzando lo stile inglese (USA).

{{% /alert %}} 
## **Avviso per gli Utenti Non Anglofoni**
Ci sono due suggerimenti che gli utenti non anglofoni devono seguire quando creano formule con Aspose.Cells:

1. Le formule devono essere inserite in inglese. Per esempio, utilizzare l'inglese "=SUM()" e non il tedesco "=SUMME()".
1. Utilizzare sempre una virgola (,) per delimitare i parametri delle funzioni. Per alcune opzioni o impostazioni linguistiche, il delimitatore per i parametri delle funzioni è un punto e virgola ma Aspose.Cells utilizza la virgola nello stile inglese. Per esempio, utilizzare "=IF(C5=0,0,C3/C4)" e non "=IF(C5=0;0;C3/C4)"
