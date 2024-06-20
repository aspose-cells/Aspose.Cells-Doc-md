---
title: Modifiche dell API pubblica in Aspose.Cells 8.5.1
type: docs
weight: 170
url: /it/net/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.5.0 alla 8.5.1 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, [classi aggiunte etc.](/cells/it/net/public-api-changes-in-aspose-cells-8-5-1/), ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Aggiunto metodo Workbook.Dispose**
L'oggetto Workbook ora implementa l'interfaccia System.IDisposable che ha un singolo metodo Dispose. Puoi chiamare direttamente il metodo Workbook.Dispose o creare un oggetto Workbook in una struttura Using per chiamare automaticamente questo metodo.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call Dispose method

book.Dispose();

//Call Dispose method via Using statement

using (Workbook book = new Workbook())

{

    //do processing

}

{{< /highlight >}}


### **Aggiunto metodo Cell.GetHeightOfValue**
Aspose.Cells for .NET 8.5.1 ha esposto il metodo Cell.GetHeightOfValue per ottenere l'altezza del valore della cella. Utilizzando questo metodo puoi calcolare l'altezza del valore della cella e quindi impostare l'altezza della riga di quella cella rispettivamente. Controlla l'articolo dettagliato su [come calcolare l'altezza e la larghezza della cella](/cells/it/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Aggiunta Enumerazione TableDataSourceType**
Aspose.Cells for .NET 8.5.1 ha esposto l'enumerazione Aspose.Cells.Tables.TableDataSourceType per recuperare il tipo di origine dati di un ListObject. L'enumerazione TableDataSourceType ha i seguenti campi.

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Worksheet
1. TableDataSourceType.XML
### **Aggiunta la proprietà ListObject.DataSourceType**
Con il rilascio della v8.5.1, l'API Aspose.Cells ha esposto la proprietà di sola lettura ListObject.DataSourceType che può essere utilizzata per rilevare il tipo di origine dati di un ListObject.

Ecco il caso d'uso più semplice.

**C#**

{{< highlight csharp >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.Worksheets[0];

ListObject listObject = sheet.ListObjects[0];

if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.QueryTable)

{

    Console.WriteLine("Data Source Type is Query Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.SharePoint)

{

    Console.WriteLine("Data Source Type is SharePoint Linked List");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.Worksheet)

{

    Console.WriteLine("Data Source Type is Excel Worksheet Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.XML)

{

    Console.WriteLine("Data Source Type is XML");

}

{{< /highlight >}}
