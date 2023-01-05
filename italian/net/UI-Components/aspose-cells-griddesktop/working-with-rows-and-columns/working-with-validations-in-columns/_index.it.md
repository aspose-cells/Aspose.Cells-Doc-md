---
title: Utilizzo delle convalide nelle colonne
type: docs
weight: 80
url: /it/net/working-with-validations-in-columns/
---
{{% alert color="primary" %}} 

 In uno dei nostri argomenti precedenti, abbiamo discusso delle convalide, ma questo era nel contesto di[Convalide nei fogli di lavoro](/cells/it/net/working-with-validations-in-worksheets/) (per avere informazioni generali sulla validazione e sulle modalità di validazione, gli sviluppatori possono fare riferimento a questo argomento). In questo argomento, spiegheremo le convalide rispetto alle colonne. Utilizzando questa funzione, è possibile per gli sviluppatori applicare una regola di convalida su qualsiasi colonna del foglio di lavoro. Discutiamolo in dettaglio.

{{% /alert %}} 
## **Aggiunta della convalida della colonna**
Per aggiungere qualsiasi tipo di convalida a una colonna, procedi nel seguente modo:

-  Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
-  Accedi a qualsiasi desiderato**Foglio di lavoro**
- **Aggiungere** un desiderato**Convalida** a qualsiasi colonna

**IMPORTANTE:**Per ulteriori informazioni sui tipi di convalida (o modalità di convalida come**È richiesta la convalida**, **Convalida delle espressioni regolari** e**Convalida personalizzata** ) e l'attuazione**Convalida personalizzata** , per favore riferisci a[Utilizzo delle convalide nei fogli di lavoro.](/cells/it/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Accesso alla convalida della colonna**
Per accedere alla convalida di una colonna specifica, procedi nel seguente modo:

-  Accedi a un file desiderato**Foglio di lavoro**
-  Accedi a una colonna specifica**Convalida** nel**Foglio di lavoro**
-  Modificare**Convalida** attributi, se lo si desidera



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **Rimozione della convalida della colonna**
Per rimuovere una convalida di colonna specifica dal foglio di lavoro, procedi nel seguente modo:

-  Accedi a un file desiderato**Foglio di lavoro**
-  Rimuovi una colonna specifica**Convalida** dal**Foglio di lavoro**



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
