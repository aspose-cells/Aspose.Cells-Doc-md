---
title: Tema dei Titoli e del Testo
linktitle: Tema dei Titoli e del Testo
description: Aspose.Cells è una libreria Node.js per lavorare con i file di fogli di calcolo. Supporta la configurazione dei caratteri del tema di intestazione e corpo nei documenti Excel, consentendo agli utenti di personalizzare l aspetto e lo stile del documento. Questo articolo introdurrà come usare la libreria Aspose.Cells per lavorare con i caratteri del tema di intestazione e corpo nei documenti Excel.
keywords: Aspose.Cells, Documento Excel, Intestazione, Corpo, Carattere del tema, Aspetto, Stile, Node.js tramite C++
type: docs
weight: 120
url: /it/nodejs-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Il font predefinito cambierà automaticamente quando viene modificata l'impostazione della regione.

Se viene modificato il font predefinito, verrà modificata anche l'altezza della riga e la larghezza della colonna, e potrebbe persino disordinare la disposizione della pagina.

Cos'ha causato il cambiamento del font predefinito?

Se il font del tema di Excel è impostato, Excel passerà automaticamente tra diversi font in base all'ambiente linguistico corrente.

{{% /alert %}}

## **Titoli e Corpo del Tema del Testo in Excel**

In Excel, seleziona la scheda Home, clicca sulla casella a discesa del carattere, vedrai "Caratteri del tema" con due caratteri di tema: Calibri Light (Intestazioni) e Calibri (Corpo) nella parte superiore con impostazione della regione in inglese.

**![Font del Tema](Theme-Fonts.png)**

Se è selezionato il Carattere del tema, il nome del carattere verrà visualizzato diversamente in diverse regioni. Se non vuoi che il carattere cambi automaticamente nelle diverse regioni, non selezionare i due caratteri del tema.

## **Modifica dei font di intestazioni e corpo tramite codice**
Con Aspose.Cells for Node.js via C++, possiamo verificare se il carattere predefinito è un carattere del tema o impostare il carattere del tema con il metodo [**Font.setSchemeType(FontSchemeType)**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSchemeType-fontschemetype-).

Il codice di esempio seguente mostra come manipolare il carattere del tema.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-HeadingsAndBodyThemeFont.js" >}}



## **Ottieni dinamicamente il font del tema locale tramite codice**
A volte, i nostri server e i computer degli utenti non si trovano nella stessa regione. Come possiamo ottenere lo stesso font desiderato dagli utenti per l'elaborazione dei file?

Dobbiamo impostare le impostazioni regionali del sistema prima di caricare il file con il metodo [**LoadOptions.setRegion(CountryCode)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setRegion-countrycode-).

Il codice di esempio seguente mostra come ottenere il font del tema locale.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetLocalThemeFont.js" >}}

