---
title: Impostazione delle formule - Avviso per gli utenti non inglesi
type: docs
weight: 20
url: /it/java/setting-formulas-notice-for-non-english-users/
---
{{% alert color="primary" %}} 

 Aspose.Cells supporta la maggior parte delle formule/funzioni che fanno parte di Microsoft Excel. Gli sviluppatori possono utilizzare queste formule con l'API o[fogli di calcolo del progettista](/cells/it/java/what-is-a-designer-spreadsheet/). Aspose.Cells supporta un vasto set di formule matematiche, stringhe, booleane, data/ora, statistiche, database, di ricerca e di riferimento. Le formule devono essere specificate utilizzando lo stile inglese (USA).

Ci sono due suggerimenti che gli utenti non inglesi devono seguire quando creano formule con Aspose.Cells:

1. Le formule devono essere inserite in inglese.
 Ad esempio, usa l'inglese "=SUM()" non il tedesco "=SUMME()".
1. Utilizzare sempre una virgola (,) per delimitare i parametri della funzione.
 Per alcune opzioni o impostazioni della lingua, il delimitatore per i parametri della funzione è un punto e virgola ma Aspose.Cells utilizza la virgola in stile inglese. Ad esempio, usa "=IF (C5=0,0,C3/C4)" non "=IF(C5=0;0;C3/C4)"

{{% /alert %}}
