---
title: Come ruotare il testo di Cell
type: docs
weight: 80
url: /it/net/how-to-rotate-text-of-cell/
description: C# codice per ruotare il testo di Cell con Aspose.Cells for .NET API
keywords: c# rotate text of Cell, c# programmatically rotate text of Cell in workbook, programmatically set cell rotation angle in workbook, c# how to rotate text of Cell in excel
---
##  **Ruota il testo di Cell in Aspose.Cells**

Aspose.Cells è un potente componente .NET e Java che consente agli sviluppatori di lavorare con i fogli di calcolo Excel a livello di codice. Una delle funzionalità fornite da Aspose.Cells è la possibilità di ruotare le celle, consentendoti di personalizzare l'orientamento del testo e migliorare la presentazione visiva dei tuoi dati. In questo documento esploreremo come ruotare le celle utilizzando Aspose.Cells.

##  **Come ruotare il testo di Cell in Excel**
Per ruotare una cella in Excel, è possibile utilizzare i seguenti passaggi:
1. Apri Excel e seleziona la cella o l'intervallo di celle che desideri ruotare.
1. Fai clic con il pulsante destro del mouse sulle celle selezionate e scegli "Formato Cells" dal menu contestuale. In alternativa, puoi andare alla scheda "Home" nella barra multifunzione di Excel, fare clic sul menu a discesa "Formato" nel gruppo "Cells" e selezionare "Formato Cells".
1. Nella finestra di dialogo "Formato Cells", vai alla scheda "Allineamento".
1. Nella sezione "Orientamento", vedrai le opzioni per ruotare il testo. È possibile inserire direttamente l'angolo di rotazione desiderato in gradi nella casella "Gradi". I valori positivi ruotano il testo in senso antiorario, mentre i valori negativi lo ruotano in senso orario.
<br>
![cose da fare:immagine_alt_testo](alignment.png)
1. Una volta selezionata la rotazione desiderata, fare clic su "OK" per applicare le modifiche. Le celle selezionate verranno ora ruotate in base all'angolo di rotazione o all'orientamento scelto.

##  **Come ruotare il testo di Cell utilizzando Aspose.Cells API**

[**Style.RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/rotationangle/) la proprietà rende conveniente ruotare le celle. Per ruotare le celle in Aspose.Cells, devi seguire questi passaggi:
1. Carica la cartella di lavoro di Excel
<br>
 Innanzitutto, devi caricare la cartella di lavoro di Excel utilizzando Aspose.Cells. Puoi utilizzare la classe Workbook per aprire un file Excel esistente o crearne uno nuovo.

1. Accedi al foglio di lavoro
<br>
Una volta caricata la cartella di lavoro, è necessario accedere al foglio di lavoro in cui si desidera ruotare le celle. È possibile accedere al foglio di lavoro tramite l'indice o il nome.

1. Ruota il testo dello Cell
<br>
 Ora che hai accesso al foglio di lavoro, puoi ruotare le celle modificando l'oggetto Stile delle celle desiderate. L'oggetto Stile consente di impostare varie opzioni di formattazione, inclusa la rotazione.

1. Salva la cartella di lavoro
<br>
Dopo aver ruotato le celle, puoi salvare nuovamente la cartella di lavoro modificata in un file o in un flusso utilizzando il metodo Salva.

##  **C# Codice Campione**

Consulta il codice seguente, crea un oggetto cartella di lavoro e imposta diversi angoli di rotazione per diverse celle. Lo screenshot mostra il risultato dopo l'esecuzione del codice di esempio.
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-rotate-text.cs" >}}
