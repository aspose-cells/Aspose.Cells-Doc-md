---
title: Aggiungi Validazione Cellule
type: docs
weight: 70
url: /it/net/aspose-cells-gridweb/add-cell-validations/
keywords: GridWeb,GridValidation,validazione elenco,validazione espressione personalizzata
description: Questo articolo introduce come aggiungere la validazione elenco,validazione elenco a discesa e validazione espressione personalizzata in GridWeb.
---

{{% alert color="primary" %}} 

Uno dei più avanzati feature di Aspose.Cells.GridWeb è aggiungere regole di validazione di input per le celle. Gli sviluppatori possono creare diversi tipi di regole di validazione per le celle per controllare e validare i valori di input. Questo argomento discute i tipi di validazioni supportate e come crearle.

{{% /alert %}} 
## **Tipi di Validazioni**
Possono essere applicati tre tipi di validazioni utilizzando Aspose.Cells.GridWeb:

- Convalida della lista.
- Convalida della lista a discesa.
- Convalida dell'espressione personalizzata.

Ogni tipo di convalida verrà discusso in dettaglio di seguito.
### **Convalida della lista**
La convalida della lista consente agli utenti di inserire un dato nella cella digitandolo o selezionandolo da un menu. Per creare una convalida della lista per una cella:

1. Aggiungi il controllo Aspose.Cells.GridWeb a un modulo Web.
1. Accedi a un foglio di lavoro.
1. Accedere alla cella a cui aggiungere la convalida.
1. Creare la convalida per la cell e specificare il tipo di convalida come Lista.
1. Aggiungere valori per la convalida della lista.

Il codice di esempio aggiunge una convalida della lista a C1. Quando un utente fa clic sulla cella, appare una lista.

**Output: selezionare un valore dalla lista** 

![todo:image_alt_text](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **Convalida della lista a discesa**
La convalida della lista a discesa consente agli utenti di fornire un input per le celle selezionando un valore da un elenco predefinito. Per creare una convalida della lista a discesa:

1. Aggiungi il controllo Aspose.Cells.GridWeb a un modulo Web.
1. Accedi a un foglio di lavoro.
1. Accedere alla cella per creare la convalida.
1. Creare una convalida per la cella e specificare il tipo come DropDownList.
1. Aggiungere valori per la convalida.

Il codice di esempio aggiunge una convalida della lista a discesa a C1. Quando un utente fa clic sulla cella, compare un elenco a discesa e gli utenti possono selezionare un valore da esso.

**Selezionare un valore da un elenco a discesa** 

![todo:image_alt_text](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **Convalida dell'espressione personalizzata**
La convalida dell'espressione personalizzata consente agli sviluppatori di scrivere le proprie espressioni regolari personalizzate per convalidare i valori di input. Per creare una convalida dell'espressione personalizzata:

1. Aggiungi il controllo Aspose.Cells.GridWeb a un modulo Web.
1. Accedi a un foglio di lavoro.
1. Accedere alla cella per creare una convalida.
1. Creare una convalida per la cella e specificare il tipo come CustomExpression.
1. Impostare l'espressione regolare della convalida.

Il codice di esempio aggiunge una convalida di espressione personalizzata a C1. Gli utenti possono inserire solo una data nella cella secondo il formato specificato dall'espressione regolare.

Aggiunta di un valore data a C1 secondo un'espressione regolare 

![todo:image_alt_text](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **Forzare la convalida**
Utilizzando Aspose.Cells.GridWeb, gli utenti possono inviare dati di input a un server. Anche se ci sono regole di convalida per diverse celle, se la proprietà ForceValidation del controllo GridWeb non è impostata su true, i dati di input errati verranno comunque inviati al server e nessuna convalida sarà forzata. La proprietà ForceValidation di GridWeb è sempre impostata su true per impostazione predefinita.

Quando la proprietà ForceValidation è true, il controllo non invia dati al server web fino a quando i valori di input di tutte le celle non sono validi. Ad esempio, se qualcuno inserisce un valore di input non valido in una cella, o non inserisce un valore, la convalida lato client viene attivata e gli utenti non possono inviare dati anche se fanno clic su **Invia**.

Valore di input errato evidenziato da GridWeb 

![todo:image_alt_text](add-cell-validations_4.png)
