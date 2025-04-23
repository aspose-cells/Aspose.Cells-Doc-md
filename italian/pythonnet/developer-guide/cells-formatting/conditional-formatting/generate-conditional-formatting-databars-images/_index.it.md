---
title: Genera immagini di formattazione condizionale DataBars
description: Aspose.Cells per Python via .NET è una libreria Python per lavorare con file di fogli di calcolo. Supporta la generazione di barre dei dati condizionali e immagini, consentendo agli utenti di personalizzare l aspetto del foglio di calcolo in base ai valori delle celle. Questo articolo introdurrà come usare Aspose.Cells per Python per generare barre e immagini di dati condizionali.
keywords: Aspose.Cells per Python via .NET, Formattazione condizionale, Barre dei dati, Immagini, Fogli di calcolo
type: docs
weight: 40
url: /it/python-net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

A volte, è necessario generare immagini di Barre dei dati di Formattazione condizionale. Puoi usare il metodo [**DataBar.to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image) di Aspose.Cells per generare queste immagini. Questo articolo mostra come generare un'immagine di una barra dati usando Aspose.Cells per Python via .NET.

{{% /alert %}}

Il seguente codice di esempio genera l'immagine DataBar della cella C1. Prima, accede all'oggetto della condizione di formato della cella, e poi da quell'oggetto, accede all'oggetto [**DataBar**](https://reference.aspose.com/cells/python-net/aspose.cells/databar) e utilizza il suo metodo [**to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image) per generare l'immagine della cella. Infine, salva l'immagine sul disco.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GenerateDatabarImage-1.py" >}}
