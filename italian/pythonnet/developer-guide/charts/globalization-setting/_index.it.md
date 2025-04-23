---
title: Converti grafico in immagine localizzata con Python via .NET
linktitle: Imposta la regione localizzata
type: docs
weight: 50
url: /it/python-net/convert-chart-to-localized-image/
alias: [/python-net/how-to-set-globalization-configuration-for-chart/]
description: Impara come impostare le configurazioni di globalizzazione per i grafici usando Aspose.Cells per Python via .NET. Configura i grafici per supportare più lingue e formati regionali per una corretta visualizzazione di testo, date e numeri.
keywords: Aspose.Cells per Python via .NET, Grafici, Impostazioni di Globalizzazione, Lingue Multiple, Formati Regionali, Visualizzazione, Testo, Date, Numeri.
---

{{% alert color="primary" %}}

In questo argomento, ti mostreremo come convertire un grafico in un'immagine localizzata e come impostare la regione localizzata per un grafico.

{{% /alert %}}

## **Scenario**

Quando potresti aver bisogno di impostare la regione localizzata per un grafico?

Se apri un file XLSX contenente un grafico in Excel con impostazioni regionali spagnole, elementi come il titolo del grafico e la legenda appaiono in spagnolo. Tuttavia, salvando questo grafico come immagine usando Aspose.Cells, questi elementi potrebbero rimanere in inglese per impostazione predefinita:

**![Problema globale](GlobalIssue.png)**

Ciò accade perché la legenda del grafico nell'immagine di output non corrisponde alla localizzazione di Excel. Puoi risolvere questo problema configurando le impostazioni di regione localizzata del grafico.

## **Elementi supportati**

I seguenti elementi del grafico verranno visualizzati secondo le impostazioni di localizzazione:

| **Elementi Supportati** | **Valore Predefinito (Inglese)** |
|-----------------------------|-----------------------------------|
| Nome del titolo dell'asse | Titolo dell'asse |
| Nome dell'unità dell'asse | Centinaia, Migliaia... |
| Nome del titolo del grafico | Titolo del grafico |
| Nome dell'aumenta legenda | Aumento |
| Nome della diminuzione legenda | Diminuzione |
| Nome totale legenda | Totale |
| Nome Altro | Altro |
| Nome della serie | Serie |

