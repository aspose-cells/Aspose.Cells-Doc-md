---
title: Personalizza i parametri di inizializzazione
type: docs
weight: 10
url: /it/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
description: come personalizzare i parametri di inizializzazione nello script lato client Aspose.Cells.GridWeb.
---
{{% alert color="primary" %}} 

 Gli sviluppatori possono impostare un diverso valore del parametro di inizializzazione per eseguire un comportamento diverso per il controllo Aspose.Cells.GridWeb in acwmain.js.

{{% /alert %}} 
 
### **Parametri**
 
|**Parametro**|**Descrizione**|
|:- |:- |
|needInitAlignmentAdjust|se eseguire l'allineamento verticale per il contenuto della cella all'inizializzazione, ci vorrà del tempo per eseguire il lavoro di allineamento, se il foglio di lavoro ha celle grandi, le prestazioni saranno scarse, se l'utente non si preoccupa dell'allineamento verticale, può impostarlo su essere falso, il valore predefinito è vero|
|focusinside| se mettere a fuoco all'interno dell'intervallo di celle, il valore predefinito è true|
|copia_con_stile|se copiare con stile, il valore predefinito è false che significa copiare solo il contenuto della cella|
|useESCAsLeave|il comportamento predefinito quando si preme esc funziona come operazione di annullamento della modifica sulla cella, se impostiamo questo valore su true, lo tratteremo semplicemente come un tasto breve per lasciare la cella senza tornare al valore precedente e cambierà anche il modo di modifica interno in modalità di modifica rapida, il valore predefinito è false|
|needValidateall|se convalidare tutte le convalide sul foglio attivo quando si esegue la convalida, (nella pagina di controllo aspx set ForceValidation="True") . Il valore predefinito è falso|
|scrollToInvalidate|se scorrere e visualizzare la prima cella invalidata quando needValidateall è impostato su true. il valore predefinito è true.|
 
 
 L'output dell'esempio di codice è mostrato di seguito,Controllare il file[file excel di esempio](valign.xlsx):

**needInitAlignmentAdjust=true** 

![cose da fare:immagine_alt_testo](align_true.png)

**needInitAlignmentAdjust=falso** 

![cose da fare:immagine_alt_testo](align_false.png)

**focusinside=true** 
 all'interno della modalità di modifica: quando inserisci il testo, il vecchio valore della cella verrà comunque mantenuto

![cose da fare:immagine_alt_testo](focus_inside_true.png)

**focusinside=falso** 
modalità di modifica rapida: quando si inserisce il testo, il vecchio valore della cella verrà sovrascritto, se si desidera modificare in base al vecchio valore della cella, è possibile fare clic sulla cella

![cose da fare:immagine_alt_testo](focus_inside_false.png)

 
 