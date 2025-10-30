---
title: Converti il grafico in immagine localizzata con Node.js tramite C++
description: Impara come impostare le configurazioni di globalizzazione per i grafici usando Aspose.Cells for Node.js via C++. La nostra guida dimostra come configurare il grafico per supportare più lingue e formati regionali per visualizzare correttamente testo, date e numeri in diverse lingue.
keywords: Aspose.Cells for Node.js via C++, Grafici, Impostazioni di globalizzazione, Lingue multiple, Formati regionali, Visualizzazione, Testo, Date, Numeri.
linktitle: Imposta la regione localizzata
type: docs
weight: 50
url: /it/nodejs-cpp/convert-chart-to-localized-image/
alias: [/nodejs-cpp/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

In questo argomento, ti mostreremo come convertire un grafico in un'immagine localizzata, imparerai come impostare la regione localizzata per un grafico.

{{% /alert %}}

## **Scenario**

In quale scenario potremmo aver bisogno di impostare una regione localizzata per un grafico? 

Quando apri un file xlsx con un grafico in Excel, in questo caso, supponiamo che lo apri con impostazioni regionali spagnole, puoi vedere gli elementi nell'area del grafico, come il titolo del grafico, la legenda, sono tradotti in spagnolo. Ma quando salvi questo grafico come immagine con Aspose.Cells, potresti riscontrare il seguente problema: 

**![Problema globale](GlobalIssue.png)**

In questo scenario, la legenda del grafico nell'immagine di output non è la stessa di quella in Excel; rimane visualizzata in inglese per impostazione predefinita. Ora puoi risolvere questo problema impostando una regione localizzata per il grafico. Con le impostazioni corrette, i seguenti elementi verranno renderizzati in base alle tue impostazioni di localizzazione.

## **Elementi supportati**

Gli elementi seguenti nel grafico possono essere renderizzati in base alle tue impostazioni di localizzazione.

|**Elementi supportati**|**valore predefinito nell'ambiente inglese**|
| :- | :- |
|Nome titolo asse|Titolo asse|
|Nome unità asse|Centinaia, Migliaia...|
|Nome titolo grafico|Titolo grafico|
|Nome incremento legenda|Aumento|
|Nome decremento legenda|Diminuzione|
|Nome totale legenda|Totale|
|Altro nome|Altro|
|Nome serie|Serie|

## **Passaggi operativi**

Il seguente esempio ti mostrerà in dettaglio come impostare una regione localizzata per ottenere l'effetto desiderato.

- [Come Impostare la Regione Cinese per il Grafico](/cells/it/nodejs-cpp/convert-chart-to-image-for-chinese-region/)
- [Come Impostare la Regione Giapponese per il Grafico](/cells/it/nodejs-cpp/convert-chart-to-image-for-japanese-region/)


{{< app/cells/assistant language="nodejs-cpp" >}}
