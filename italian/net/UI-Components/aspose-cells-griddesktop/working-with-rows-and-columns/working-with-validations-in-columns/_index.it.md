---
title: Lavorare con le Validazioni nelle Colonne
type: docs
weight: 80
url: /it/net/aspose-cells-griddesktop/work-with-validations-in-columns/
keywords: GridDesktop,validazione,validazioni
description: Questo articolo introduce come utilizzare le validazioni nelle colonne in GridDesktop.
---

{{% alert color="primary" %}} 

In uno dei nostri argomenti precedenti, abbiamo discusso delle validazioni ma questo era nel contesto di [Validazioni nei Fogli di Lavoro](/cells/it/net/working-with-validations-in-worksheets/) (per avere informazioni generali sulle validazioni e le modalità di validazione, gli sviluppatori possono fare riferimento a questo argomento). In questo argomento, spiegheremo le validazioni relativamente alle colonne. Utilizzando questa funzionalità, è possibile per gli sviluppatori applicare una regola di validazione su qualsiasi colonna del foglio di lavoro. Parliamone in dettaglio.

{{% /alert %}} 
## **Aggiunta della Validazione della Colonna**
Per aggiungere qualsiasi tipo di validazione a una colonna, seguire i passaggi seguenti:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedere a qualsiasi **Foglio di lavoro** desiderato
- **Aggiungi** una **Validazione** desiderata a qualsiasi colonna

**IMPORTANTE:** Per ulteriori informazioni sui tipi di validazione (o modalità di validazione come **Validazione Richiesta**, **Validazione Espressioni Regolari** e **Validazione Personalizzata**) e sull'implementazione della **Validazione Personalizzata**, si prega di fare riferimento a [Lavorare con le Validazioni nei Fogli di Lavoro.](/cells/it/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Accesso alla Validazione di Colonna**
Per accedere a una specifica validazione di colonna, si prega di seguire i passaggi seguenti:

- Accedi a un **Foglio di lavoro** desiderato
- Accedi a una specifica validazione di colonna nel **Foglio di Lavoro**
- Modifica gli attributi di **Validazione**, se desiderato



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **Rimozione della Validazione di Colonna**
Per rimuovere una specifica validazione di colonna dal foglio di lavoro, si prega di seguire i passaggi seguenti:

- Accedi a un **Foglio di lavoro** desiderato
- Rimuovi una specifica validazione di colonna dal **Foglio di Lavoro**



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
