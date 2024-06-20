---
title: Accedere e aggiornare le porzioni di testo arricchito della cella
linktitle: Formattazione del testo arricchito
type: docs
weight: 40
url: /it/net/access-and-update-the-portions-of-rich-text-of-cell/
description: Scopri come accedere e aggiornare le porzioni di testo formattato di una cella attraverso l API Aspose.Cells for .NET.
keywords: Accedere e aggiornare il testo formattato ricco della cella, ottenere il testo formattato ricco della cella, modificare il testo formattato ricco della cella, accedere al testo formattato ricco della cella, aggiornare il testo formattato ricco della cella, modificare il testo formattato ricco della cella
---

{{% alert color="primary" %}}

Aspose.Cells ti consente di accedere e aggiornare le porzioni di testo formattato della cella. A questo scopo, puoi utilizzare i metodi [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) e [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters). Questi metodi restituiranno e accetteranno l'array di [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) oggetti che potrai utilizzare per accedere e aggiornare varie proprietà del font come nome del font, colore del font, grassetto, ecc.

{{% /alert %}}

## **Accedere e aggiornare le porzioni di testo arricchito della cella**

Il codice seguente mostra l'utilizzo dei metodi [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) e [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) utilizzando il [file excel di origine](5112369.xlsx) che puoi scaricare dal link fornito. Il file excel di origine ha un testo formattato in ricco nella cella A1. Ha 3 porzioni e ogni porzione ha un font diverso. Il seguente frammento di codice accede a queste porzioni e aggiorna la prima porzione con un nuovo nome di font. Infine, salva il file di lavoro come [file excel di output](5112366.xlsx). Quando lo apri, troverai che il font della prima porzione del testo è stato cambiato in **"Arial"**.

### Codice C# per accedere e aggiornare le porzioni di testo arricchito della cella

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### Uscita della console generata dal codice di esempio

Ecco l'output della console del codice di esempio utilizzando il [file excel di origine](5112369.xlsx).

{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

