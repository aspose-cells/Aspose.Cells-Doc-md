---
title: Formato Cells
type: docs
weight: 40
url: /it/net/format-grid-cells/
---
{{% alert color="primary" %}} 

Questo argomento fornisce una discussione dettagliata su come formattare le celle.

Copre la formattazione delle celle in modalità GUI utilizzando la finestra di dialogo Stile del controllo Aspose.Cells.GridWeb. Mostra anche come formattare le celle a livello di codice. Vengono discusse diverse impostazioni di formato come carattere, bordo e formato numerico, illustrate con esempi.

{{% /alert %}} 
## **Formattazione Cells Utilizzo della finestra di dialogo Stile**
 Cells può essere formattato[programmaticamente](/cells/it/net/format-cells/)ma il modo più semplice per formattare le celle nel controllo Aspose.Cells.GridWeb in modo WYSIWYG è utilizzare la finestra di dialogo Stile.

Per utilizzare la finestra di dialogo Stile:
 Seleziona un intervallo di celle, quindi fai clic con il pulsante destro del mouse e seleziona**Formato Cell**. 

**Selezionando il formato Cell** 

![cose da fare:immagine_alt_testo](format-cells_1.png)



 Viene visualizzata la finestra di dialogo Stile.

**La finestra di dialogo Stile viene utilizzata per formattare le celle** 

![cose da fare:immagine_alt_testo](format-cells_2.png)

La finestra di dialogo Stile consente agli utenti di formattare le celle personalizzando le impostazioni del carattere e del bordo.
### **Personalizzazione delle impostazioni dei caratteri**
È possibile personalizzare le seguenti impostazioni dei caratteri utilizzando la finestra di dialogo Stile:

- Nome carattere, selezionare il carattere desiderato dall'elenco.
- Stile del carattere, applica uno stile del carattere come grassetto, corsivo ecc.
- Dimensione carattere, selezionare una dimensione del carattere in punti.
- Sottolineare, sottolineare il testo.
- Barrato, applica un effetto barrato al testo.
- Allineamento orizzontale, selezionare l'allineamento orizzontale.
- Allineamento verticale, selezionare l'allineamento verticale.
- Colore carattere, seleziona un colore per il carattere.
- Sfondo, seleziona un colore per lo sfondo.

È possibile controllare le impostazioni dei caratteri selezionati in una piccola area di anteprima.

**Impostazioni dei caratteri personalizzate** 

![cose da fare:immagine_alt_testo](format-cells_3.png)
### **Personalizzazione delle impostazioni del bordo**
Il controllo consente inoltre agli utenti di tracciare un bordo attorno alle celle personalizzando le impostazioni del bordo nella finestra di dialogo Stile.

Per visualizzare le opzioni relative ai bordi:
 Clic**frontiere** nella finestra di dialogo Stile.
 Vengono visualizzate le opzioni relative al bordo.

**Opzioni del bordo nella finestra di dialogo dello stile** 

![cose da fare:immagine_alt_testo](format-cells_4.png)

Le seguenti opzioni di bordo possono essere selezionate dalla finestra di dialogo Stile:

- Stile della linea del bordo, seleziona lo stile del bordo come solido, tratteggiato ecc.
- Larghezza della linea del bordo, selezionare la larghezza del bordo in pixel.
- Colore della linea del bordo, selezionare il colore della linea.
- Linee di confine, selezionare la numerazione e il posizionamento delle linee di confine.

**Impostazioni del bordo personalizzate** 

![cose da fare:immagine_alt_testo](format-cells_5.png)
### **Applicazione delle impostazioni**
 Clic**OK** nella finestra di dialogo Stile per applicare le modifiche.

**Impostazioni di carattere e bordo applicate** 

![cose da fare:immagine_alt_testo](format-cells_6.png)


## **Formattazione Cells Utilizzo di API**
Cells può anche essere formattato a livello di codice con Aspose.Cells.GridWeb API. Ogni cella ha una proprietà Style, che rappresenta un oggetto GridTableItemStyle. Utilizzare la proprietà Style per personalizzare le impostazioni del carattere e del bordo.
### **Impostazione carattere**
Per personalizzare le impostazioni dei caratteri a livello di programmazione:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un Web Form.
1. Accedi a un foglio di lavoro.
1. Accedi alla cella che stai formattando.
1. Accedi allo stile della cella.
1. Imposta la dimensione del carattere in punti.
1. Imposta lo stile del carattere.
1. Imposta i colori di primo piano e di sfondo.
1. Imposta l'allineamento orizzontale e verticale.
1. Reimposta lo stile sulla cella.

**Output: impostazioni dei caratteri personalizzate mostrate in A1** 

![cose da fare:immagine_alt_testo](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **Impostazione dei confini**
I bordi possono essere applicati a singole celle o a un intervallo.
#### **Singolo Cell**
Per impostare i bordi di una singola cella:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un Web Form.
1. Accedi a un foglio di lavoro.
1. Accedi alla cella che stai per formattare.
1. Accedi all'oggetto Style della cella.
1. Imposta lo stile del bordo.
1. Imposta la larghezza del bordo in pixel.
1. Imposta il colore del bordo.
1. Imposta lo stile sulla cella.

**Impostazioni del bordo personalizzate su una singola cella** 

![cose da fare:immagine_alt_testo](format-cells_8.png)

{{% alert color="primary" %}} 

È possibile impostare stili diversi per ogni linea di bordo con le proprietà Style.TopBorderStyle, Style.BottomBorderStyle, Style.LeftBorderStyle, Style.RightBorderStyle della cella.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **Gamma di Cells**
Per impostare i bordi su un intervallo di celle:

1. Aggiungere il controllo Aspose.Cells.GridWeb al modulo Web
1. Accedi a un foglio di lavoro desiderato
1. Crea un'istanza di un oggetto della classe WebBorderStyle
1. Imposta lo stile del bordo su solido o tratteggiato ecc.
1. Imposta la larghezza del bordo in pixel
1. Imposta il colore del bordo
1. Applica le impostazioni del bordo memorizzate nell'oggetto WebBorderStyle a un intervallo di celle specificato

**Un intervallo di celle con impostazioni del bordo personalizzate** 

![cose da fare:immagine_alt_testo](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **Impostazione dei formati numerici**
 Aspose.Cells.GridWeb supporta l'impostazione dei formati numerici. Ci sono 59 formati numerici incorporati. Per vederli, fare riferimento a questo[elenco dei formati numerici supportati](/cells/it/net/list-of-supported-number-formats/).

Tutti i formati numerici incorporati si trovano nell'enumerazione NumberType. Per utilizzare un formato numerico predefinito, impostare il metodo NumberType utilizzando SetNumberType dell'oggetto di una cella su un formato numerico dall'enumerazione NumberType.

Per impostare un formato numerico personalizzato utilizzare il metodo SetCustom della cella.

**Impostazioni del formato numerico applicate a B1 e B2** 

![cose da fare:immagine_alt_testo](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}
