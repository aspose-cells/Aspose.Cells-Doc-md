---
title: Applicare lo stile su una riga o colonna
type: docs
weight: 50
url: /it/net/aspose-cells-griddesktop/apply-style-on-a-row-or-column/
keywords: GridDesktop, stile, riga, colonna
description: Questo articolo introduce come applicare lo stile su una riga o colonna in GridDesktop.
---

{{% alert color="primary" %}} 

In questo argomento, discuteremo del cambiamento del font e del colore del font delle righe e delle colonne di un foglio di lavoro. Si tratta di una funzionalità di formattazione di base offerta da Aspose.Cells.GridDesktop che consente agli sviluppatori di personalizzare la visualizzazione dei propri fogli di lavoro per renderli più presentabili.

{{% /alert %}} 
## **Applicare stile su una colonna**
Per applicare uno stile personalizzato a una colonna utilizzando Aspose.Cells.GridDesktop, seguire i passaggi seguenti:

- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Accedere a una **Colonna** su cui desideriamo applicare uno **Stile**
- Ottenere lo **Stile** della **Colonna**
- Impostare le proprietà dello **Stile** secondo le proprie esigenze personalizzate
- Infine, impostare lo **Stile** della **Colonna** con quello aggiornato

Ci sono molte proprietà e metodi utili offerti dall'oggetto **Stile** che possono essere utilizzati dagli sviluppatori per personalizzare lo stile secondo le proprie esigenze.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Applicare stile su una riga**
Per applicare uno stile personalizzato a una riga utilizzando Aspose.Cells.GridDesktop, seguire i passaggi seguenti:

- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Accedere a una **Riga** su cui desideriamo applicare uno **Stile**
- Ottenere lo **Stile** della **Riga**
- Impostare le proprietà dello **Stile** secondo le proprie esigenze personalizzate
- Infine, impostare lo **Stile** della **Riga** con quello aggiornato

Ci sono molte proprietà e metodi utili offerti dall'oggetto **Stile** che possono essere utilizzati dagli sviluppatori per personalizzare lo stile secondo le proprie esigenze.



{{< highlight csharp >}}

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
