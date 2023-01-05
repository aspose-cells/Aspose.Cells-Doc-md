---
title: Comment obtenir les informations de connexion OData
type: docs
weight: 60
url: /fr/java/how-to-get-odata-connection-information/
---
## **Obtenir les informations de connexion OData**

Il peut arriver que les développeurs aient besoin d'extraire des informations OData du fichier Excel. Aspose.Cells fournit le[**Workbook.DataMashupWorkbook.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup)propriété qui renvoie les informations DataMashup présentes dans le fichier Excel. Ces informations sont représentées par la classe DataMashup. La classe DataMashup fournit la propriété PowerQueryFormulas qui renvoie la collection PowerQueryFormulaCollction. À partir de PowerQueryFormulaCollction, vous pouvez accéder à PowerQueryFormula et PowerQueryFormulaItem.

L'extrait de code suivant illustre l'utilisation de ces classes pour récupérer les informations OData.

Le fichier source utilisé dans l'extrait de code suivant est joint pour votre référence.

[Fichier source](ODataSample.xlsx)

### **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Sortie console**

Nom de la connexion : Commandes

Nom : source

Valeur : OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Nom : Orders_table

Valeur : Source{[Name="Commandes",Signature="table"]}[Données]