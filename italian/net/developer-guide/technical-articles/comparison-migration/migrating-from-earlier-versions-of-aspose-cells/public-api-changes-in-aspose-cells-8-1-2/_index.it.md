---
title: Cambiamenti nell API pubblica in Aspose.Cells 8.1.2
type: docs
weight: 60
url: /it/net/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche apportate all'API di Aspose.Cells dalla versione 8.1.1 alla 8.1.2, che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunto il supporto per l'avviso se si verificano sostituzioni di caratteri**
Con Aspose.Cells for .NET 8.1.2, le classi WarningInfo, WarningType, l'interfaccia IWarningCallback e le proprietà SaveOptions.WarningCallback, ImageOrPrintOptions.WarningCallback sono state aggiunte per consentire all'utente di ricevere avvisi nel caso si verifichi una sostituzione del carattere durante la conversione dei fogli di calcolo in immagini o formato PDF. 

{{% alert color="primary" %}} 

Si prega di controllare l'articolo dettagliato su [Ottenere Avvisi per la Sostituzione dei Caratteri durante la Rendering di Fogli di Calcolo](http://aspose.com/docs/display/cellsnet/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)

{{% /alert %}}
## **Proprietà PdfSaveOptions.ChartImageType Obsoleta Eliminata**
Aspose.Cells for .NET 8.1.2 ha rimosso la proprietà obsoleta PdfSaveOptions.ChartImageType dall'API pubblica.
