---
title: Modifiche all API pubblica in Aspose.Cells 8.2.2
type: docs
weight: 100
url: /it/java/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.2.1 alla 8.2.2 che potrebbero interessare agli sviluppatori di moduli/applicazioni.

{{% /alert %}} 
## **API aggiunte**
### **Aggiunta Proprietà Version per la classe BuiltInDocumentPropertyCollection**
La nuova proprietà Version è stata aggiunta alla classe BuiltInDocumentPropertyCollection per permettere ai programmatori di ottenere o impostare la versione dell'applicazione per un determinato foglio di calcolo.

{{% alert color="primary" %}} 

Si prega di controllare l'articolo dettagliato su [Ottieni la versione dell'applicazione che ha creato il foglio di calcolo](/cells/it/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Aggiunta proprietà Worksheet a Chart**
Prima del rilascio di Aspose.Cells 8.2.2, non era possibile recuperare l'istanza del foglio di lavoro da un oggetto Chart contenuto. Aspose.Cells 8.2.2 ha colmato questa lacuna fornendo la proprietà Chart.Worksheet.

{{% alert color="primary" %}} 

Si prega di controllare l'articolo dettagliato [Ottieni Foglio di Lavoro del Grafico](/cells/it/java/get-worksheet-of-the-chart/) per ulteriori informazioni.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
