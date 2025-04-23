---
title: Comment obtenir les informations de connexion OData
type: docs
weight: 60
url: /fr/python-net/how-to-get-odata-connection-information/
---

## **Obtenir les informations de connexion OData**

Il peut y avoir des cas où les développeurs doivent extraire des informations OData du fichier Excel. Aspose.Cells pour Python via .NET fournit la propriété [**Workbook.data_mashup**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/data_mashup) qui retourne les informations DataMashup présentes dans le fichier Excel. Ces informations sont représentées par la classe [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup). La classe [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup) fournit la propriété [**power_query_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup/power_query_formulas) qui retourne la collection [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/). À partir de [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/), vous pouvez accéder à [**PowerQueryFormula**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformula) et [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulaitem).

Le code suivant illustre l'utilisation de ces classes pour récupérer les informations OData.

Le fichier source utilisé dans l'extrait de code suivant est joint à titre de référence.

[Fichier source](96928098.xlsx)

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-GetOdataDetails-1.py" >}}

### **Sortie console**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}

