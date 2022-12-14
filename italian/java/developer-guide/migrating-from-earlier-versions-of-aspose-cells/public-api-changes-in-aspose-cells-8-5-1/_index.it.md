---
title: Pubblico API Modifiche Aspose.Cells 8.5.1
type: docs
weight: 180
url: /it/java/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

 Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.5.0 alla 8.5.1 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati,[classi aggiunte ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-5-1/), ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Metodo Workbook.Dispose aggiunto**
Aspose.Cells for Java 8.5.1 ha esposto il metodo Workbook.dispose per rilasciare le risorse non gestite dell'oggetto Workbook. Il modello Dispose viene utilizzato solo per oggetti che accedono a risorse non gestite, ad esempio handle di file e pipe, handle di registro, handle di attesa o puntatori a blocchi di memoria non gestita. Questo perché il Garbage Collector è molto efficiente nel recuperare oggetti gestiti inutilizzati, ma non è in grado di recuperare oggetti non gestiti.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **Metodo Cell.getHeightOfValue aggiunto**
 Aspose.Cells for Java 8.5.1 ha esposto il metodo Cell.getHeightOfValue per ottenere l'altezza del valore della cella. Utilizzando questo metodo è possibile calcolare l'altezza del valore della cella e quindi impostare rispettivamente l'altezza della riga di quella cella. Controlla l'articolo dettagliato su[come calcolare l'altezza e la larghezza della cella](/cells/it/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Enumerazione TableDataSourceType aggiunto**
Aspose.Cells for Java 8.5.1 ha esposto l'enumerazione com.aspose.cells.TableDataSourceType per recuperare il tipo di origine dati di un ListObject. L'enumerazione TableDataSourceType come campi seguenti.

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **Proprietà ListObject.DataSourceType aggiunto**
Con il rilascio di v8.5.1, Aspose.Cells API ha esposto la proprietà ListObject.DataSourceType di sola lettura che può essere utilizzata per rilevare il tipo di origine dati di un ListObject.

Ecco lo scenario di utilizzo più semplice.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.getWorksheets().get(0);

ListObject listObject = sheet.getListObjects().get(0);

if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.QUERY_TABLE)

{

	System.out.println("Data Source Type is Query Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.SHARE_POINT)

{

	System.out.println("Data Source Type is SharePoint Linked List");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.WORKSHEET)

{

	System.out.println("Data Source Type is Excel Worksheet Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.XML)

{

	System.out.println("Data Source Type is XML");

}

{{< /highlight >}}
