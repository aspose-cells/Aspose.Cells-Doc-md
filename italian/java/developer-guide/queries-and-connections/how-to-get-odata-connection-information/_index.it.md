---
title: Come ottenere informazioni sulla connessione OData
type: docs
weight: 60
url: /it/java/how-to-get-odata-connection-information/
---
## **Ottieni informazioni sulla connessione OData**

Potrebbero esserci casi in cui gli sviluppatori devono estrarre le informazioni OData dal file excel. Aspose.Cells fornisce il[**Cartella di lavoro.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup)proprietà che restituisce le informazioni DataMashup presenti nel file Excel. Queste informazioni sono rappresentate dalla classe DataMashup. La classe DataMashup fornisce la proprietà PowerQueryFormulas che restituisce la raccolta PowerQueryFormulaCollction. Da PowerQueryFormulaCollction è possibile accedere a PowerQueryFormula e PowerQueryFormulaItem.

Il frammento di codice seguente illustra l'utilizzo di queste classi per recuperare le informazioni OData.

Il file di origine utilizzato nel seguente frammento di codice è allegato come riferimento.

[File sorgente](ODataSample.xlsx)

### **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Uscita console**

Nome connessione: Ordini

Nome: Fonte

Valore: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Nome: Orders_table

Valore: Fonte{[Name="Ordini",Signature="tabella"]}[Dati]