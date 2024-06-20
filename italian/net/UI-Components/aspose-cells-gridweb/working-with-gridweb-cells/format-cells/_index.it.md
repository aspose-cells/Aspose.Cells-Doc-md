---
title: Formato Cella
type: docs
weight: 40
url: /it/net/aspose-cells-gridweb/format-grid-cell/
keywords: GridWeb, formato, stile
description: Questo articolo introduce come impostare o applicare lo stile format per una cella (GridCell) in GridWeb.
---

{{% alert color="primary" %}} 

Questo argomento fornisce una discussione dettagliata su come formattare le celle.

Si tratta della formattazione delle celle in modalità GUI utilizzando il controllo Aspose.Cells.GridWeb's Style dialog. Mostra anche come formattare le celle programmatticamente. Diverse impostazioni di formato come carattere, bordo e formato numerico sono discusse, illustrate con esempi.

{{% /alert %}} 
## **Formattazione Celle Utilizzando il Dialogo di Stile**
Le celle possono essere formattate [programmaticamente](/cells/it/net/aspose-cells-gridweb/format-cells/) ma il modo più semplice per formattare le celle nel controllo Aspose.Cells.GridWeb in modo WYSIWYG, è utilizzare il dialogo di stile.

Per utilizzare il dialogo di stile:
Selezionare un intervallo di celle, quindi fare clic con il pulsante destro del mouse e selezionare **Formato Cella**. 

**Selezionare Formato Cella** 

![todo:image_alt_text](format-cells_1.png)



Viene visualizzato il dialogo di stile. 

**Il dialogo di stile viene utilizzato per formattare le celle** 

![todo:image_alt_text](format-cells_2.png)

La finestra di dialogo Stile consente agli utenti di formattare le celle personalizzando i settaggi del carattere e del bordo.
### **Personalizzazione delle Impostazioni del Carattere**
Puoi personalizzare le seguenti impostazioni del carattere utilizzando la finestra di dialogo Stile:

- Nome del carattere, seleziona un carattere desiderato dalla lista.
- Stile del carattere, applica uno stile come grassetto, corsivo, ecc.
- Dimensione del carattere, seleziona una dimensione del carattere in punti.
- Sottolineatura, sottolinea il testo.
- Barrato, applica un effetto di barrato al testo.
- Allineamento orizzontale, seleziona l'allineamento orizzontale.
- Allineamento verticale, seleziona l'allineamento verticale.
- Colore del carattere, seleziona un colore del carattere.
- Sfondo, seleziona un colore per lo sfondo.

Puoi controllare le impostazioni del carattere selezionate in un'area di anteprima ridotta.

**Impostazioni del carattere personalizzate** 

![todo:image_alt_text](format-cells_3.png)
### **Personalizzazione delle Impostazioni del Bordo**
Il controllo consente anche agli utenti di disegnare un bordo intorno alle celle personalizzando le impostazioni del bordo nella finestra di dialogo Stile.

Per visualizzare le opzioni relative ai bordi:
Clicca su **Bordi** nella finestra di dialogo Stile.
Le opzioni relative ai bordi vengono visualizzate. 

**Opzioni del bordo nella finestra di dialogo di stile** 

![todo:image_alt_text](format-cells_4.png)

È possibile selezionare le seguenti opzioni di bordo dalla finestra di dialogo Stile:

- Stile linea di bordo, seleziona lo stile del bordo come solido, tratteggiato, ecc.
- Larghezza della linea di bordo, seleziona la larghezza del bordo in pixel.
- Colore linea di bordo, seleziona il colore della linea.
- Linee di bordo, seleziona la numerazione e il posizionamento delle linee di bordo.

**Impostazioni bordo personalizzate** 

![todo:image_alt_text](format-cells_5.png)
### **Applicare le impostazioni**
Fare clic su **OK** nella finestra di dialogo Stile per applicare le modifiche.

**Impostazioni carattere e bordo applicate** 

![todo:image_alt_text](format-cells_6.png)


## **Formattazione delle celle tramite API**
Le celle possono anche essere formattate programmaticamente con l'API Aspose.Cells.GridWeb. Ogni cella ha una proprietà Style, che rappresenta un oggetto GridTableItemStyle. Utilizza la proprietà Style per personalizzare le impostazioni del carattere e del bordo.
### **Impostazione carattere**
Per personalizzare le impostazioni del carattere programmaticamente:

1. Aggiungi il controllo Aspose.Cells.GridWeb a un modulo Web.
1. Accedi a un foglio di lavoro.
1. Accedi alla cella che stai formattando.
2. Accedi allo stile della cella.
3. Imposta la dimensione del carattere in punti.
4. Imposta lo stile del carattere.
5. Imposta i colori di primo piano e sfondo.
6. Imposta l'allineamento orizzontale e verticale.
7. Riporta lo stile alla cella.

**Output: impostazioni del carattere personalizzato mostrate in A1** 

![todo:image_alt_text](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **Impostazione dei bordi**
I bordi possono essere applicati a singole celle o a un intervallo.
#### **Singola Cellula**
Per impostare i bordi di una singola cella:

1. Aggiungi il controllo Aspose.Cells.GridWeb a un modulo Web.
1. Accedi a un foglio di lavoro.
1. Accedere alla cella che si sta per formattare.
1. Accedere all'oggetto stile della cella.
1. Impostare lo stile del bordo.
1. Impostare la larghezza del bordo in pixel.
1. Impostare il colore del bordo.
1. Impostare lo stile alla cella.

**Impostazioni personalizzate dei bordi su una singola cella** 

![todo:image_alt_text](format-cells_8.png)

{{% alert color="primary" %}} 

È possibile impostare stili diversi per ciascuna linea di confine con le proprietà Style.TopBorderStyle, Style.BottomBorderStyle, Style.LeftBorderStyle, Style.RightBorderStyle della cella.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **Intervallo di celle**
Per impostare i bordi su un intervallo di celle:

1. Aggiungi il controllo Aspose.Cells.GridWeb al tuo modulo Web
1. Accedere a un foglio di lavoro desiderato
1. Istanziare un oggetto della classe WebBorderStyle
1. Impostare lo stile del bordo come Solido o Tratteggiato eccetera.
1. Impostare la larghezza del bordo in pixel
1. Imposta il colore del bordo
1. Applica le impostazioni del bordo memorizzate nell'oggetto WebBorderStyle a un intervallo specifico di celle

**Un intervallo di celle con impostazioni del bordo personalizzate** 

![todo:image_alt_text](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **Impostare i formati numerici**
Aspose.Cells.GridWeb supporta l'impostazione dei formati numerici. Ci sono 59 formati numerici incorporati. Per visualizzarli, consulta questa [lista dei formati numerici supportati](/cells/it/net/aspose-cells-gridweb/list-of-supported-number-formats/).

Tutti i formati numerici incorporati sono nell'enumerazione NumberType. Per utilizzare un formato numerico incorporato, imposta il NumberType utilizzando il metodo SetNumberType di un oggetto cella su un formato numerico dall'enumerazione NumberType.

Per impostare un formato numerico personalizzato utilizza il metodo SetCustom della cella.

**Impostazioni del formato numerico applicate su B1 e B2** 

![todo:image_alt_text](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}
