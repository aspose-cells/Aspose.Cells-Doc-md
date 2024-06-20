---
title: Modifiche all API pubblica in Aspose.Cells 8.2.1
type: docs
weight: 80
url: /it/net/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.2.0 alla 8.2.1, che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunto metodo GetValidation() per la classe Cell**
La convalida dei dati è una delle funzionalità che i progettisti di fogli di calcolo utilizzano per impedire agli utenti di inserire valori non validi in una cella particolare. Con Aspose.Cells for .NET 8.2.1, l'API ha esposto un meccanismo semplice che identifica se è stata applicata una convalida dei dati su una cella. Utilizza il metodo GetValidation della classe Cell per acquisire eventuali convalide applicate. Se non c'è alcuna convalida, il metodo restituisce null. Allo stesso modo, è possibile utilizzare il metodo GetValidationInCell della classe ValidationCollection per acquisire la convalida applicata su una qualsiasi cella fornendo i suoi indici di riga e colonna.

{{% alert color="primary" %}} 

Si prega di consultare l'articolo dettagliato su [Ottieni la convalida applicata su una cella](/cells/it/net/get-validation-applied-on-a-cell/) per ulteriori informazioni.

{{% /alert %}}
## **Aggiunto metodo GetValidationValue() per la classe Cell**
Oltre a determinare se è stata applicata una convalida, è anche possibile verificare se un determinato valore soddisfa le regole di convalida dei dati per una cella particolare. Questa funzionalità è utile in scenari in cui si desidera verificare se il valore inserito nella cella soddisfa le regole di convalida dei dati immediatamente. L'API Aspose.Cells ha esposto il metodo GetValidationValue per la classe Cell. Se il valore inserito in una cella non soddisfa le regole di convalida dei dati, il metodo GetValidationValue per la classe Cell restituisce false.

{{% alert color="primary" %}} 

Si prega di consultare l'articolo dettagliato su [Verifica che il valore della cella soddisfi le regole di convalida dei dati](/cells/it/net/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Aggiunto sovraccarico del metodo ToPrinter(PrinterSettings printerSettings) per la classe WorkbookRender**
Puoi utilizzare il metodo sovraccaricato per rendere il workbook alla stampante tramite PrinterSettings.
