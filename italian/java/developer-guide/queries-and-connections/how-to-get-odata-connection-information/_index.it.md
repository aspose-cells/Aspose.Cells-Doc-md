---
title: Come ottenere informazioni sulla connessione OData
type: docs
weight: 60
url: /it/java/how-to-get-odata-connection-information/
---

## **Ottenere informazioni sulla connessione OData**

Potrebbero esserci casi in cui gli sviluppatori devono estrarre informazioni OData dal file excel. Aspose.Cells fornisce la proprietà [**Workbook.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup) che restituisce le informazioni sulla DataMashup presenti nel file Excel. Queste informazioni sono rappresentate dalla classe DataMashup. La classe DataMashup fornisce la proprietà PowerQueryFormulas che restituisce la raccolta PowerQueryFormulaCollction. Dalla PowerQueryFormulaCollction, puoi accedere a PowerQueryFormula e PowerQueryFormulaItem.

Il seguente frammento di codice dimostra l'uso di queste classi per recuperare le informazioni OData.

Il file di origine utilizzato nello snippet di codice seguente è allegato per il tuo riferimento.

File di origine (ODataSample.xlsx)

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Output della console**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
