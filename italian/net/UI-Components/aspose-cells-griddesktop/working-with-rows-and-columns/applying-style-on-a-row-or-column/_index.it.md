---
title: Applicazione dello stile su una riga o colonna
type: docs
weight: 50
url: /it/net/applying-style-on-a-row-or-column/
---
{{% alert color="primary" %}} 

In questo argomento, discuteremo della modifica del carattere e del colore del carattere di righe e colonne di un foglio di lavoro. Questo è un livello base di funzionalità di formattazione offerto da Aspose.Cells.GridDesktop che consente agli sviluppatori di personalizzare la visualizzazione dei loro fogli di lavoro per renderli più presentabili.

{{% /alert %}} 
## **Applicazione dello stile su una colonna**
Per applicare uno stile personalizzato su una colonna utilizzando Aspose.Cells.GridDesktop, procedi nel seguente modo:

-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Accedi a**Colonna** su cui vogliamo applicare a**Stile**
-  Ottenere**Stile** del**Colonna**
-  Impostare**Stile** proprietà in base alle vostre esigenze personalizzate
-  Finalmente, set**Stile** del**Colonna** con quello aggiornato

 Ci sono molte proprietà e metodi utili offerti da**Stile** oggetto che può essere utilizzato dagli sviluppatori per personalizzare lo stile in base alle proprie esigenze.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Applicare lo stile su una riga**
Per applicare uno stile personalizzato su una riga utilizzando Aspose.Cells.GridDesktop, procedi nel seguente modo:

-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Accedi a**Riga** su cui vogliamo applicare a**Stile**
-  Ottenere**Stile** del**Riga**
-  Impostare**Stile** proprietà in base alle vostre esigenze personalizzate
-  Finalmente, set**Stile** del**Riga** con quello aggiornato

 Ci sono molte proprietà e metodi utili offerti da**Stile** oggetto che può essere utilizzato dagli sviluppatori per personalizzare lo stile in base alle proprie esigenze.



{{< highlight "csharp" >}}

 // Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

// Accessing the first row of the worksheet

Aspose.Cells.GridDesktop.Data.GridRow row = sheet.Rows[0];

// Getting the Style object for the row

Style style = row.GetStyle();

// Setting Style properties i.e. border, color, alignment, background color etc.

style.SetBorderLine(BorderType.Right, BorderLineType.Thick);

style.SetBorderColor(BorderType.Right, Color.Blue);

style.HAlignment = HorizontalAlignmentType.Centred;

style.Color = Color.Yellow;

// Setting the style of the row with the customized Style object

row.SetStyle(style);

{{< /highlight >}}
