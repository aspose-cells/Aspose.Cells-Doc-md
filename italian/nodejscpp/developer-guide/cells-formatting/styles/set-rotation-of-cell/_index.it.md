---  
title: Come ruotare il testo della cella
linktitle: Come ruotare il testo della cella  
type: docs  
weight: 80  
url: /it/nodejs-cpp/how-to-rotate-text-of-cell/  
description: Impara come ruotare il testo di una cella programmativamente usando Aspose.Cells for Node.js via C++.  
keywords: node.js ruota testo della cella, Programma Node.js per ruotare programmaticamente il testo di una cella nel workbook, imposta manualmente l angolo di rotazione della cella nel workbook, come ruotare il testo di una cella in Excel con Node.js  
---  

## **Ruota il testo della cella in Aspose.Cells for Node.js via C++**

Aspose.Cells è una potente componente Node.js che consente agli sviluppatori di lavorare con fogli di calcolo Excel programmaticamente. Una delle funzionalità offerte da Aspose.Cells è la capacità di ruotare le celle, permettendo di personalizzare l'orientamento del testo e migliorare la presentazione visiva dei dati. In questo documento, esploreremo come ruotare le celle usando Aspose.Cells.

## **Come ruotare il testo della cella in Excel**
Per ruotare una cella in Excel, è possibile utilizzare i seguenti passaggi:
1. Apri Excel e seleziona la cella o l'intervallo di celle che desideri ruotare.
1. Fai clic con il pulsante destro del mouse sulla cella (o le celle) selezionata(e) e scegli "Formato celle" dal menu contestuale. In alternativa, puoi andare alla scheda "Home" nel nastro di Excel, fare clic sulla visualizzazione a discesa "Formato" nel gruppo "Celle" e selezionare "Formato celle".
1. Nella finestra di dialogo "Formato celle", passa alla scheda "Allineamento".
1. Nella sezione "Orientamento", vedrai le opzioni per ruotare il testo. Puoi inserire direttamente l'angolo di rotazione desiderato in gradi nella casella "Gradi". I valori positivi ruotano il testo in senso antiorario e i valori negativi lo ruotano in senso orario.
<br>
![todo:image_alt_text](alignment.png)
1. Una volta selezionata la rotazione desiderata, fai clic su "OK" per applicare le modifiche. La/e cella/e selezionata/e verranno ora ruotate in base all'angolo di rotazione o orientamento scelto.

## **Come ruotare il testo della cella utilizzando l'API di Aspose.Cells**

La proprietà [**Style.setRotationAngle(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-) rende comodo ruotare le celle. Per ruotare le celle in Aspose.Cells, è necessario seguire questi passaggi:
1. Carica il documento di lavoro di Excel  
<br>
Prima di tutto, è necessario caricare il workbook di Excel utilizzando Aspose.Cells. Puoi utilizzare la classe Workbook per aprire un file Excel esistente o crearne uno nuovo. 

1. Accedere al foglio di lavoro  
<br>
Una volta caricato il workbook, è necessario accedere al foglio di lavoro in cui si desidera ruotare le celle. Puoi accedere al foglio di lavoro tramite l'indice o il nome. 

1. Ruotare il testo della cella  
<br>
Ora che hai accesso al foglio di lavoro, puoi ruotare le celle modificando l'oggetto Style delle celle desiderate. L'oggetto Style ti consente di impostare diverse opzioni di formattazione, inclusa la rotazione. 

1. Salvare il workbook  
<br>
Dopo aver ruotato le celle, puoi salvare il workbook modificato su un file o un flusso utilizzando il metodo Save.

## **Codice di esempio Node.js**

Vedi il seguente codice, crea un oggetto workbook e imposta diversi angoli di rotazione per varie celle. Lo screenshot mostra il risultato dopo l'esecuzione del codice di esempio.
<br>
<img src="rotation.png" width=80% />

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-SetRotationOfCell.js" >}}


