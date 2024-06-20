---
title: Come ottenere informazioni sulla connessione OData
type: docs
weight: 60
url: /it/net/how-to-get-odata-connection-information/
---

## **Ottenere informazioni sulla connessione OData**

Potrebbero esserci casi in cui gli sviluppatori devono estrarre informazioni OData dal file di Excel. Aspose.Cells fornisce la proprietà [**Workbook.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup) che restituisce le informazioni di DataMashup presenti nel file di Excel. Queste informazioni sono rappresentate dalla classe [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup). La classe [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) fornisce la proprietà [**PowerQueryFormulas**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) che restituisce la collezione [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction). Dal [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction), è possibile accedere a [**PowerQueryFormula**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) e [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

Il seguente frammento di codice dimostra l'uso di queste classi per recuperare le informazioni OData.

Il file di origine utilizzato nello snippet di codice seguente è allegato per il tuo riferimento.

[File di origine](96928098.xlsx)

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **Output della console**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
