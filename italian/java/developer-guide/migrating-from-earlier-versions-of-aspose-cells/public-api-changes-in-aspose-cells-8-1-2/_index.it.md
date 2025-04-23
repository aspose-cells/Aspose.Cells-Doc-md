---
title: Cambiamenti nell API pubblica in Aspose.Cells 8.1.2
type: docs
weight: 70
url: /it/java/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche apportate all'API di Aspose.Cells dalla versione 8.1.1 alla 8.1.2, che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunto il supporto per l'avviso se si verificano sostituzioni di caratteri**
Con Aspose.Cells for Java 8.1.2, le classi WarningInfo e WarningType, l'interfaccia IWarningCallback, le proprietà SaveOptions.WarningCallback e ImageOrPrintOptions.WarningCallback sono state aggiunte per consentire agli sviluppatori di ricevere avvisi quando si verificano sostituzioni di caratteri durante la conversione dei fogli di calcolo in immagini, XPS e PDF. 

{{% alert color="primary" %}} 

Si prega di controllare l'articolo dettagliato su [Ottenere Avvisi per la Sostituzione di Caratteri durante la Renderizzazione dei Fogli di Lavoro](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) per ulteriori informazioni.

{{% /alert %}}
## **Proprietà PdfSaveOptions.ChartImageType Obsoleta Eliminata**
Aspose.Cells for Java 8.1.2 ha rimosso la proprietà obsoleta PdfSaveOptions.ChartImageType dall'API pubblica.
{{< app/cells/assistant language="java" >}}
