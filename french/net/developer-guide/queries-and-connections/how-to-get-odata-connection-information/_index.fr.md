---
title: Comment obtenir les informations de connexion OData
type: docs
weight: 60
url: /fr/net/how-to-get-odata-connection-information/
---

## **Obtenir les informations de connexion OData**

Il peut y avoir des cas où les développeurs doivent extraire des informations OData du fichier Excel. Aspose.Cells fournit la propriété [**Workbook.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup) qui renvoie les informations DataMashup présentes dans le fichier Excel. Ces informations sont représentées par la classe [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup). La classe [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) fournit la propriété [**PowerQueryFormulas**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) qui renvoie la collection [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction). À partir du [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction), vous pouvez accéder à [**PowerQueryFormula**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) et [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

Le code suivant illustre l'utilisation de ces classes pour récupérer les informations OData.

Le fichier source utilisé dans l'extrait de code suivant est joint à titre de référence.

[Fichier source](96928098.xlsx)

### **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **Sortie console**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
