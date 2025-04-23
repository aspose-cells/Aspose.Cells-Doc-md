---
title: Modifiche all API pubblica in Aspose.Cells 8.2.1
type: docs
weight: 90
url: /it/java/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.2.0 alla 8.2.1, che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunto il metodo getValidation() per la classe Cell**
La convalida dei dati è una delle funzionalità che i designer di fogli elettronici utilizzano per impedire agli utenti di inserire valori non validi in una cella particolare. Con Aspose.Cells for Java 8.2.1, l'API ha esposto un meccanismo semplice che identifica se è stata applicata una convalida dei dati su una cella. Utilizzare il metodo getValidation della classe Cell per ottenere qualsiasi convalida applicata. Se non è presente alcuna convalida, il metodo restituisce null. Allo stesso modo, è possibile utilizzare il metodo getValidationInCell della classe ValidationCollection per ottenere la convalida applicata su una qualsiasi cella fornendo gli indici di riga e colonna.

{{% alert color="primary" %}} 

Si prega di controllare l'articolo dettagliato su [Ottenere la convalida applicata su una cella](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/) per ulteriori informazioni.

{{% /alert %}}
## **Aggiunto il metodo getValidationValue() per la classe Cell**
Oltre a determinare se è stata applicata una convalida, è possibile verificare se un determinato valore soddisfa le regole di convalida dei dati per una cella specifica. Questa funzionalità è utile in scenari in cui si desidera verificare se il valore inserito nella cella soddisfi le regole di convalida dei dati in modo dinamico. L'API di Aspose.Cells ha esposto il metodo getValidationValue per la classe Cell. Se il valore inserito in una cella non soddisfa le regole di convalida dei dati, il metodo getValidationValue per la classe Cell restituisce false.

{{% alert color="primary" %}} 

Si prega di controllare l'articolo dettagliato su [Verificare che il valore della cella soddisfi le regole di convalida dei dati](/cells/it/java/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Aggiunta sovraccarica al metodo toPrinter(PrinterSettings printerSettings) per la classe WorkbookRender**
Puoi utilizzare il metodo sovraccaricato per rendere il workbook alla stampante tramite PrinterSettings.
{{< app/cells/assistant language="java" >}}
