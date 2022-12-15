---
title: Modifiche all'API pubblica in Aspose.Cells 8.2.2
type: docs
weight: 90
url: /it/net/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.2.1 alla 8.2.2 che potrebbero interessare gli sviluppatori di moduli/applicazioni.

{{% /alert %}} 
## **API aggiunte**
### **Proprietà BuiltInDocumentPropertyCollection.Version Aggiunta**
La nuova proprietà Version è stata aggiunta alla classe BuiltInDocumentPropertyCollection per consentire agli sviluppatori di recuperare la versione dell'applicazione che ha creato un determinato foglio di calcolo.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato[Ottieni la versione dell'applicazione che ha creato il foglio di calcolo](/cells/it/net/get-the-version-number-of-the-application-that-created-the-excel-document/) per maggiori informazioni.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **Proprietà Chart.Worksheet aggiunto**
Prima del rilascio di Aspose.Cells 8.2.2, non era possibile recuperare l'istanza del foglio di lavoro da un oggetto grafico in esso contenuto. Aspose.Cells 8.2.2 ha colmato questa lacuna fornendo la proprietà Chart.Worksheet.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato[Ottieni Foglio di lavoro del grafico](/cells/it/net/get-worksheet-of-the-chart/) per maggiori informazioni.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
