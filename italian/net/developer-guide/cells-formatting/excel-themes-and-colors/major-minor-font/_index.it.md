---
title: Intestazioni e carattere del tema del corpo
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo. Supporta l'impostazione dei caratteri dell'intestazione e del tema del corpo nei documenti Excel, consentendo agli utenti di personalizzare l'aspetto e lo stile del documento. Questo articolo introdurrà come utilizzare la libreria Aspose.Cells per lavorare con i caratteri dei temi di intestazione e corpo nei documenti Excel.
keywords: Aspose.Cells, Excel Document, Heading, Body, Theme Font, Appearance, Style
type: docs
weight: 120
url: /it/net/headings-and-body-theme-font/
---
{{% alert color="primary" %}}

 Il carattere predefinito cambierà automaticamente quando viene modificata l'impostazione di ripristino.

Se si modifica il carattere predefinito, vengono modificate anche l'altezza della riga e la larghezza della colonna e ciò potrebbe persino compromettere il layout della pagina.

Cosa ha causato la modifica del carattere predefinito?

Se è impostato il carattere del tema Excel, Excel passerà automaticamente da un carattere all'altro in base all'ambiente linguistico corrente.


{{% /alert %}}

##  **Intestazioni e carattere del tema del corpo in Excel**

In Excel, seleziona la scheda Home, fai clic sulla casella a discesa dei caratteri, vedrai "Caratteri del tema" con due caratteri del tema: Calibri Light (Intestazioni) e Calibri (Corpo) in alto con l'impostazione della regione inglese.

**![Caratteri del tema](Theme-Fonts.png)**

Se è selezionato Carattere tema, il nome del carattere verrà visualizzato in modo diverso nelle diverse regioni.
Se non vuoi che il carattere venga cambiato automaticamente nelle diverse regioni, non selezionare i due Font del tema.


##  **Modifica programmatica delle intestazioni e del carattere del corpo**
 Con Aspose.Cells per .Net, possiamo verificare se il carattere predefinito è il carattere del tema o impostare il carattere del tema con[**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/) proprietà.

Il codice di esempio seguente mostra come manipolare il carattere del tema.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


##  **Ottiene dinamicamente il carattere del tema locale in modo programmatico**
A volte, i nostri server e i computer degli utenti non si trovano nella stessa regione. Come possiamo ottenere lo stesso carattere desiderato dagli utenti per l'elaborazione dei file?

 Dobbiamo configurare le impostazioni regionali del sistema prima di caricare il file con[**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/) proprietà

Il seguente codice di esempio mostra come ottenere il carattere del tema locale.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}