---
title: Rendere una pagina PDF per foglio di lavoro di Excel  Conversione di Excel in PDF
type: docs
weight: 100
url: /it/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}} 

Quando si lavora con grandi file di Microsoft Excel (ad esempio un documento di lavoro che ha molti fogli, ognuno con 50 colonne e 300 o più righe di dati), potrebbe essere necessario che l'output in PDF mostri una pagina per foglio di lavoro, indipendentemente dalle dimensioni del foglio di lavoro. Questo significa che ogni pagina è probabile che abbia dimensioni della pagina radicalmente diverse. Questo può essere ottenuto utilizzando Aspose.Cells for .NET.

{{% /alert %}} 

Si prega di vedere il seguente codice di esempio che converte un file di Excel con più fogli di lavoro in PDF.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

Se l'opzione [OnePagePerSheet](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) è impostata su **true**, tutto il contenuto del foglio viene reso in una pagina PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Se il foglio di calcolo contiene formule, è meglio chiamare [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) appena prima del rendering del foglio di calcolo in PDF. Ciò garantisce che i valori dipendenti dalle formule vengano ricalcolati e i valori corretti siano resi in PDF.

{{% /alert %}}
