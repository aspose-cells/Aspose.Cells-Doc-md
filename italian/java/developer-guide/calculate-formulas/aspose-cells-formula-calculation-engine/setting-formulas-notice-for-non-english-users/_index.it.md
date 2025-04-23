---
title: Impostazione Formule  Avviso per gli Utenti Non Anglofoni
type: docs
weight: 20
url: /it/java/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells supporta la maggior parte delle formule/funzioni che fanno parte di Microsoft Excel. Gli sviluppatori possono utilizzare queste formule con API o [fogli elettronici di progettazione](/cells/it/java/what-is-a-designer-spreadsheet/). Aspose.Cells supporta un'ampia gamma di formule matematiche, stringa, booleane, data/ora, statistiche, database, ricerca e riferimento. Le formule devono essere specificate utilizzando lo stile inglese (USA).

Ci sono due suggerimenti che gli utenti non anglofoni devono seguire quando creano formule con Aspose.Cells:

1. Le formule devono essere inserite in inglese.
   Ad esempio, utilizzare l'inglese "=SUM()" e non il tedesco "=SUMME()".
1. Utilizzare sempre una virgola (,) per delimitare i parametri della funzione.
   Per alcune opzioni o impostazioni linguistiche, il delimitatore per i parametri della funzione è un punto e virgola, ma Aspose.Cells utilizza la virgola nello stile inglese. Ad esempio, utilizzare "=SE(C5=0,0,C3/C4)" e non "=SE(C5=0;0;C3/C4)" 

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
