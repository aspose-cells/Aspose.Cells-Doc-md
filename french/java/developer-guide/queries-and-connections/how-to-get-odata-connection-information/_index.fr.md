---
title: Comment obtenir les informations de connexion OData
type: docs
weight: 60
url: /fr/java/how-to-get-odata-connection-information/
---

## **Obtenir les informations de connexion OData**

Il peut y avoir des cas où les développeurs doivent extraire des informations OData du fichier Excel. Aspose.Cells fournit la propriété [**Workbook.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup) qui retourne les informations DataMashup présentes dans le fichier Excel. Cette information est représentée par la classe DataMashup. La classe DataMashup fournit la propriété PowerQueryFormulas qui retourne la collection PowerQueryFormulaCollction. À partir de la PowerQueryFormulaCollction, vous pouvez accéder à PowerQueryFormula et PowerQueryFormulaItem.

Le code suivant illustre l'utilisation de ces classes pour récupérer les informations OData.

Le fichier source utilisé dans l'extrait de code suivant est joint à titre de référence.

[Fichier source](ODataSample.xlsx)

### **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Sortie console**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
