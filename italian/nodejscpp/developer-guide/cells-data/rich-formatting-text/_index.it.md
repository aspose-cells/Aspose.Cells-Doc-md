---
title: Accedere e aggiornare le porzioni di testo arricchito della cella
linktitle: Formattazione del testo arricchito
type: docs
weight: 40
url: /it/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Impara come Accedere e Aggiornare le Parti del Testo Ricco della Cella tramite l API Aspose.Cells for Node.js via C++.
keywords: Accedere e aggiornare il testo formattato ricco della cella, ottenere il testo formattato ricco della cella, modificare il testo formattato ricco della cella, accedere al testo formattato ricco della cella, aggiornare il testo formattato ricco della cella, modificare il testo formattato ricco della cella
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ consente di accedere e aggiornare le parti del testo ricco della cella. Per questo scopo, puoi utilizzare i metodi [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) e [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-). Questi metodi restituiranno e accetteranno un array di oggetti [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) che puoi usare per accedere e aggiornare varie proprietà del font come nome, colore, grassetto, ecc.

{{% /alert %}}

## **Accedere e aggiornare le porzioni di testo arricchito della cella**

Il seguente codice mostra come usare i metodi [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) e [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-) usando il [file Excel di origine](5112369.xlsx) che puoi scaricare dal link fornito. Il file Excel di origine contiene un testo ricco nella cella A1 con 3 parti, ciascuna con un font diverso. Il codice seguente accede a queste parti e aggiorna la prima con un nuovo nome di font. Infine, salva il workbook come [file Excel di output](5112366.xlsx). Quando lo aprirai, vedrai che il font della prima parte del testo è stato cambiato in **"Arial"**.

### Codice Nodejs per accedere e aggiornare le parti del Testo Ricco della Cella

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "UpdateRichTextCells-1.js" >}}

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

{{< app/cells/assistant language="nodejs-cpp" >}}
