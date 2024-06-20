---
title: Personalizza i parametri di inizializzazione
type: docs
weight: 10
url: /it/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
keywords: GridWeb, personalizza, personalizza parametri
description: come personalizzare i parametri di inizializzazione nello script lato client di Aspose.Cells.GridWeb.
---

{{% alert color="primary" %}} 

Gli sviluppatori possono impostare un valore di parametro di inizializzazione diverso per eseguire un comportamento diverso per il controllo Aspose.Cells.GridWeb in acwmain.js.  

{{% /alert %}} 

### **Parametri**

| **Parametro** | **Descrizione** |
| :- | :- |
|needInitAlignmentAdjust| se fare l'allineamento verticale per il contenuto della cella all'inizializzazione, comporterà del tempo per fare il lavoro di allineamento, se il foglio di lavoro ha celle grandi, le prestazioni saranno scarse, se all'utente non importa l'allineamento verticale, allora può impostarlo su false, il valore predefinito è true |
|focusinside| se focalizzarsi all'interno dello span di celle, il valore predefinito è true |
|copy_with_style| se copiare con stile, il valore predefinito è false che significa copiare solo il contenuto della cella |
|useESCAsLeave| il comportamento predefinito quando si preme esc funziona come operazione annulla modifica sulla cella, se impostiamo questo valore su true, lo tratteremo solo come un tasto rapido per lasciare la cella senza tornare al valore precedente e cambierà anche il modo di modifica interna in modo rapido, il valore predefinito è false |
|needValidateall| se convalidare tutte le convalide sul foglio attivo quando si effettua la convalida, (nella pagina di controllo aspx impostare ForceValidation="True"). il valore predefinito è false |
|scrollToInvalidate| se scorrere e portare la prima cella non valida in visualizzazione quando needValidateall impostato su true. il valore predefinito è true. |


L'output dell'esempio di codice è mostrato di seguito, controllare il [file excel di esempio](valign.xlsx):

**needInitAlignmentAdjust=true** 

![todo:image_alt_text](align_true.png)

**needInitAlignmentAdjust=false** 

![todo:image_alt_text](align_false.png)

**focusinside=true** 
modo di modifica interno - quando si inserisce il testo, il vecchio valore della cella verrà comunque conservato   

![todo:image_alt_text](focus_inside_true.png)

**focusinside=false** 
modo di modifica veloce: quando si inserisce del testo, il valore della cella precedente verrà sovrascritto; se si desidera modificare in base al valore precedente della cella, è possibile fare clic sulla cella

![todo:image_alt_text](focus_inside_false.png)



