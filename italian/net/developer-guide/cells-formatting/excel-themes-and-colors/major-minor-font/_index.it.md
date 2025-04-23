---
title: Tema dei Titoli e del Testo
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli elettronici. Supporta l impostazione dei font dei titoli e del testo nei documenti Excel, consentendo agli utenti di personalizzare l aspetto e lo stile del documento. Questo articolo illustrerà come utilizzare la libreria Aspose.Cells per lavorare con i font dei titoli e del corpo del tema in documenti Excel.
keywords: Aspose.Cells, Documento Excel, Titolo, Corpo, Tema del Testo, Aspetto, Stile
type: docs
weight: 120
url: /it/net/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Il font predefinito cambierà automaticamente quando viene modificata l'impostazione della regione. 

Se viene modificato il font predefinito, verrà modificata anche l'altezza della riga e la larghezza della colonna, e potrebbe persino disordinare la disposizione della pagina.

Cos'ha causato il cambiamento del font predefinito?

Se il font del tema di Excel è impostato, Excel passerà automaticamente tra diversi font in base all'ambiente linguistico corrente.


{{% /alert %}}

## **Titoli e Corpo del Tema del Testo in Excel**

In Excel, seleziona la scheda Home, fai clic sulla casella a discesa del font, vedrai "Font del Tema" con due font del tema: Calibri Light (Titoli) e Calibri (Corpo) in alto con l'impostazione della regione in inglese.

**![Font del Tema](Theme-Fonts.png)**

Se viene selezionato un Font del Tema, il nome del font verrà visualizzato in modo diverso in diverse regioni.
Se non si desidera che il font cambi automaticamente in diverse regioni, non selezionare i due Font del Tema.


## **Cambiare i Font di Titoli e Corpo Programmaticamente**
Con Aspose.Cells per .Net, possiamo verificare se il font predefinito è un font del tema o impostare il font del tema con la proprietà [**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/).

Il seguente codice di esempio mostra come manipolare il font del tema.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


## **Ottieni dinamicamente il Font del Tema Locale Programmaticamente**
A volte, i nostri server e i computer degli utenti non si trovano nella stessa regione. Come possiamo ottenere lo stesso font desiderato dagli utenti per l'elaborazione dei file?

Dobbiamo impostare le impostazioni regionali di sistema prima di caricare il file con la proprietà [**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/).

Il codice di esempio seguente mostra come ottenere il font del tema locale.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}
{{< app/cells/assistant language="csharp" >}}
