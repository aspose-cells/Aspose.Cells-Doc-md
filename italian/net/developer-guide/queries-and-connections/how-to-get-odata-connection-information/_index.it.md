---
title: Come ottenere informazioni sulla connessione OData
type: docs
weight: 60
url: /it/net/how-to-get-odata-connection-information/
---
## **Ottieni informazioni sulla connessione OData**

 Potrebbero esserci casi in cui gli sviluppatori devono estrarre le informazioni OData dal file excel. Aspose.Cells fornisce il[**Cartella di lavoro.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup) proprietà che restituisce le informazioni DataMashup presenti nel file Excel. Questa informazione è rappresentata dal[**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) classe. Il[**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)la classe fornisce il[**Formule di PowerQuery**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) proprietà che restituisce il[**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) collezione. Dal[**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction), puoi accedere a[**Formula PowerQuery**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) e[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

Il frammento di codice seguente illustra l'utilizzo di queste classi per recuperare le informazioni OData.

Il file di origine utilizzato nel seguente frammento di codice è allegato come riferimento.

[File sorgente](96928098.xlsx)

### **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **Uscita console**

Nome connessione: Ordini

Nome: Fonte

Valore: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Nome: Orders_table

Valore: Fonte{[Name="Ordini",Signature="tabella"]}[Dati]