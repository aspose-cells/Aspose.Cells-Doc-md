---
title: Aggiungi Cell Convalide
type: docs
weight: 70
url: /it/net/add-cell-validations/
---
{{% alert color="primary" %}} 

Una delle funzionalità avanzate di Aspose.Cells.GridWeb consiste nell'aggiungere regole di convalida dell'input per le celle. Gli sviluppatori possono creare diversi tipi di regole di convalida per le celle per controllare e convalidare i valori di input. Questo argomento illustra i tipi di convalida supportati e come crearli.

{{% /alert %}} 
## **Tipi di convalide**
È possibile applicare tre tipi di convalide utilizzando Aspose.Cells.GridWeb:

- Convalida elenco.
- Convalida dell'elenco a discesa.
- Convalida dell'espressione personalizzata.

Ognuno è discusso in dettaglio di seguito.
### **Convalida elenco**
La convalida dell'elenco consente agli utenti di fornire l'input della cella digitando o selezionando un valore da un menu. Per creare una convalida elenco per una cella:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un Web Form.
1. Accedi a un foglio di lavoro.
1. Accedi alla cella a cui aggiungere la convalida.
1. Creare la convalida per la cella e specificare il tipo di convalida come Elenco.
1. Aggiungere valori per la convalida dell'elenco.

Il codice di esempio aggiunge una convalida elenco a C1. Quando un utente fa clic sulla cella, viene visualizzato un elenco.

**Output: selezione di un valore dall'elenco** 

![cose da fare:immagine_alt_testo](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **Convalida dell'elenco a discesa**
La convalida dell'elenco a discesa consente agli utenti di fornire input per le celle selezionando un valore da un elenco predefinito. Per creare una convalida dell'elenco a discesa:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un Web Form.
1. Accedi a un foglio di lavoro.
1. Accedi alla cella per cui creare la convalida.
1. Crea una convalida per la cella e specifica il tipo come DropDownList.
1. Aggiungere valori per la convalida.

Il codice di esempio aggiunge una convalida dell'elenco a discesa a C1. Quando un utente fa clic sulla cella, viene visualizzato un menu a discesa e gli utenti possono selezionare un valore da esso.

**Selezione di un valore da un menu a discesa** 

![cose da fare:immagine_alt_testo](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **Convalida dell'espressione personalizzata**
La convalida delle espressioni personalizzate consente agli sviluppatori di scrivere le proprie espressioni regolari personalizzate per convalidare i valori di input. Per creare una convalida dell'espressione personalizzata:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un Web Form.
1. Accedi a un foglio di lavoro.
1. Accedi alla cella per cui creare una convalida.
1. Crea una convalida per la cella e specifica il tipo come CustomExpression.
1. Imposta l'espressione regolare della convalida.

Il codice di esempio aggiunge una convalida dell'espressione personalizzata a C1. Gli utenti possono solo aggiungere una data nella cella secondo il formato specificato dall'espressione regolare.

**Aggiunta di un valore di data a C1 in base a un'espressione regolare** 

![cose da fare:immagine_alt_testo](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **Forzare la convalida**
Utilizzando Aspose.Cells.GridWeb, gli utenti possono inviare i dati di input a un server. Anche se sono presenti regole di convalida per celle diverse ma la proprietà ForceValidation del controllo GridWeb non è impostata su true, anche i dati di input errati verranno inviati al server e non viene forzata alcuna convalida. La proprietà ForceValidation di GridWeb è sempre impostata su true per impostazione predefinita.

 Quando la proprietà ForceValidation è true, il controllo non invia dati al server Web finché i valori di input di tutte le celle non sono validi. Ad esempio, se qualcuno inserisce un valore di input non valido in una cella o non inserisce un valore, viene attivata la convalida lato client e gli utenti non possono pubblicare dati anche se fanno clic su**Invia**.

**Valore di input errato evidenziato da GridWeb** 

![cose da fare:immagine_alt_testo](add-cell-validations_4.png)
