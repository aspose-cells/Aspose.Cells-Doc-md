---
title: Come ruotare il testo della cella
type: docs
weight: 80
url: /it/python-net/how-to-rotate-text-of-cell/
description: Codice C# per ruotare il testo della cella con l API Aspose.Cells per Python via .NET
keywords: Python per ruotare il testo di una cella, script Python per ruotare programmaticamente il testo di una cella nel workbook, impostare l angolo di rotazione della cella programmaticamente nel workbook, come ruotare il testo di una cella in Excel usando Python
---

## **Ruota il testo della cella in Aspose.Cells per Python via .NET**

Aspose.Cells per Python via .NET è una potente componente .NET e Java che permette agli sviluppatori di lavorare con i fogli di calcolo Excel programmaticamente. Una delle funzionalità offerte da Aspose.Cells per Python via .NET è la possibilità di ruotare le celle, consentendo di personalizzare l'orientamento del testo e migliorare la presentazione visiva dei dati. In questo documento, esploreremo come ruotare le celle utilizzando Aspose.Cells per Python via .NET.

## **Come ruotare il testo della cella in Excel**
Per ruotare una cella in Excel, è possibile utilizzare i seguenti passaggi:
1. Apri Excel e seleziona la cella o l'intervallo di celle che desideri ruotare.
1. Fai clic con il pulsante destro del mouse sulla cella (o le celle) selezionata(e) e scegli "Formato celle" dal menu contestuale. In alternativa, puoi andare alla scheda "Home" nel nastro di Excel, fare clic sulla visualizzazione a discesa "Formato" nel gruppo "Celle" e selezionare "Formato celle".
1. Nella finestra di dialogo "Formato celle", passa alla scheda "Allineamento".
1. Nella sezione "Orientamento", vedrai le opzioni per ruotare il testo. Puoi inserire direttamente l'angolo di rotazione desiderato in gradi nella casella "Gradi". I valori positivi ruotano il testo in senso antiorario e i valori negativi lo ruotano in senso orario.
<br>
![todo:image_alt_text](alignment.png)
1. Una volta selezionata la rotazione desiderata, fai clic su "OK" per applicare le modifiche. La/e cella/e selezionata/e verranno ora ruotate in base all'angolo di rotazione o orientamento scelto.

## **Come ruotare il testo di una cella usando l'API Aspose.Cells per Python via .NET**

La proprietà [**Style.rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) rende conveniente ruotare le celle. Per ruotare le celle in Aspose.Cells per Python via .NET, è necessario seguire questi passaggi:
1. Carica il documento di lavoro di Excel
<br>
Innanzitutto, è necessario caricare il workbook Excel usando Aspose.Cells per Python via .NET. È possibile utilizzare la classe Workbook per aprire un file Excel esistente o crearne uno nuovo. 

1. Accedere al foglio di lavoro
<br>
Una volta caricato il workbook, è necessario accedere al foglio di lavoro in cui si desidera ruotare le celle. Puoi accedere al foglio di lavoro tramite l'indice o il nome. 

1. Ruotare il testo della cella
<br>
Ora che hai accesso al foglio di lavoro, puoi ruotare le celle modificando l'oggetto Style delle celle desiderate. L'oggetto Style ti consente di impostare diverse opzioni di formattazione, inclusa la rotazione. 

1. Salvare il workbook
<br>
Dopo aver ruotato le celle, puoi salvare il workbook modificato su un file o un flusso utilizzando il metodo Save.

## **Codice di esempio Python**

Si prega di consultare il codice seguente, crea un oggetto workbook e imposta diversi angoli di rotazione per diverse celle. La schermata mostra il risultato dopo l'esecuzione del codice di esempio.
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Cells-rotate-text.py" >}}

