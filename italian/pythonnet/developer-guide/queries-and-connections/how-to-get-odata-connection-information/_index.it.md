---
title: Come ottenere informazioni sulla connessione OData
type: docs
weight: 60
url: /it/python-net/how-to-get-odata-connection-information/
---

## **Ottenere informazioni sulla connessione OData**

Potrebbe esserci il caso in cui gli sviluppatori devono estrarre le informazioni OData dal file excel. Aspose.Cells per Python via .NET fornisce la proprietà [**Workbook.data_mashup**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/data_mashup) che restituisce le informazioni DataMashup presenti nel file Excel. Queste informazioni sono rappresentate dalla classe [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup). La classe [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup) fornisce la proprietà [**power_query_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup/power_query_formulas) che restituisce la collezione [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/). Da [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/), puoi accedere a [**PowerQueryFormula**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformula) e [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulaitem).

Il seguente frammento di codice dimostra l'uso di queste classi per recuperare le informazioni OData.

Il file di origine utilizzato nello snippet di codice seguente è allegato per il tuo riferimento.

[File di origine](96928098.xlsx)

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-GetOdataDetails-1.py" >}}

### **Output della console**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}

