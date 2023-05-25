---
title: Copia le impostazioni di impostazione della pagina dal foglio di lavoro di origine nel foglio di lavoro di destinazione
type: docs
weight: 80
url: /it/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: In questo articolo viene illustrato come utilizzare il codice di esempio della libreria C# API o .NET per copiare le impostazioni di Imposta pagina dal foglio di lavoro di origine nel foglio di lavoro di destinazione a livello di codice.
keywords: copy page setup settings c#, copy page setup settings to target worksheet c#
---
##  **Possibili scenari di utilizzo**

Quando aggiungi un nuovo foglio a una cartella di lavoro, contiene le *Impostazioni di impostazione pagina* predefinite. Potrebbero esserci momenti in cui è necessario trasferire le impostazioni ([**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) da un foglio di lavoro a un altro foglio di lavoro. Questo documento spiega come copiare le impostazioni di Imposta pagina da un foglio di lavoro a un altro utilizzando le API Aspose.Cells.

##  **Copia le impostazioni di impostazione della pagina dal foglio di lavoro di origine nel foglio di lavoro di destinazione**

Il seguente codice di esempio illustra come copiare*Impostazioni di configurazione della pagina*da un foglio di lavoro all'altro utilizzando[**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy)metodo. Consultare il seguente codice di esempio e il relativo output della console per un riferimento.

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

##  **Uscita console**

{{< highlight "java" >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
