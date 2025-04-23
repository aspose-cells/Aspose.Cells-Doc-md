---
title: Modifiche dell API pubblica in Aspose.Cells 8.5.1
type: docs
weight: 180
url: /it/java/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.5.0 a 8.5.1 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Comprende non solo nuovi e aggiornati metodi pubblici, [classi aggiunte etc.](/cells/it/java/public-api-changes-in-aspose-cells-8-5-1/), ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Aggiunto metodo Workbook.Dispose**
Aspose.Cells for Java 8.5.1 ha esposto il metodo Workbook.dispose per rilasciare le risorse non gestite dell'oggetto Workbook. Il pattern di smaltimento viene utilizzato solo per gli oggetti che accedono a risorse non gestite, come handle di file e pipe, handle del registro, handle di attesa o puntatori a blocchi di memoria non gestita. Questo perché il garbage collector è molto efficiente nel recuperare gli oggetti gestiti inutilizzati, ma non è in grado di recuperare gli oggetti non gestiti.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **Metodo Cell.getHeightOfValue Aggiunto**
Aspose.Cells for Java 8.5.1 ha esposto il metodo Cell.getHeightOfValue per ottenere l'altezza del valore della cella. Utilizzando questo metodo è possibile calcolare l'altezza del valore della cella e quindi impostare l'altezza della riga di quella cella di conseguenza. Consultare l'articolo dettagliato su [come calcolare l'altezza e la larghezza della cella](/cells/it/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Enumerazione TableDataSourceType Aggiunta**
Aspose.Cells for Java 8.5.1 ha esposto l'enumerazione com.aspose.cells.TableDataSourceType per recuperare il tipo di origine dati di un ListObject. L'enumerazione TableDataSourceType ha i seguenti campi. 

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **Aggiunta la proprietà ListObject.DataSourceType**
Con il rilascio della v8.5.1, l'API Aspose.Cells ha esposto la proprietà di sola lettura ListObject.DataSourceType che può essere utilizzata per rilevare il tipo di origine dati di un ListObject.

Ecco il caso d'uso più semplice.

**Java**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="java" >}}
