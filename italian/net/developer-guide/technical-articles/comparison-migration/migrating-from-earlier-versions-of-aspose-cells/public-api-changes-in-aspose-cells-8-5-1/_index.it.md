---
title: Pubblico API Modifiche Aspose.Cells 8.5.1
type: docs
weight: 170
url: /it/net/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

 Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.5.0 alla 8.5.1 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati,[classi aggiunte ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-5-1/), ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Metodo Workbook.Dispose aggiunto**
L'oggetto Workbook ora implementa l'interfaccia System.IDisposable che dispone di un singolo metodo Dispose. È possibile chiamare direttamente il metodo Workbook.Dispose o creare un oggetto Workbook in una struttura Using per chiamare automaticamente questo metodo.

**C#**

{{< highlight "csharp" >}}

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


### **Metodo Cell.GetHeightOfValue aggiunto**
 Aspose.Cells for .NET 8.5.1 ha esposto il metodo Cell.GetHeightOfValue per ottenere l'altezza del valore della cella. Utilizzando questo metodo è possibile calcolare l'altezza del valore della cella e quindi impostare rispettivamente l'altezza della riga di quella cella. Controlla l'articolo dettagliato su[come calcolare l'altezza e la larghezza della cella](/cells/it/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Enumerazione TableDataSourceType aggiunto**
Aspose.Cells for .NET 8.5.1 ha esposto l'enumerazione Aspose.Cells.Tables.TableDataSourceType per recuperare il tipo di origine dati di un ListObject. L'enumerazione TableDataSourceType come campi seguenti.

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Foglio di lavoro
1. TableDataSourceType.XML
### **Proprietà ListObject.DataSourceType aggiunto**
Con il rilascio di v8.5.1, Aspose.Cells API ha esposto la proprietà ListObject.DataSourceType di sola lettura che può essere utilizzata per rilevare il tipo di origine dati di un ListObject.

Ecco lo scenario di utilizzo più semplice.

**C#**

{{< highlight "csharp" >}}

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
