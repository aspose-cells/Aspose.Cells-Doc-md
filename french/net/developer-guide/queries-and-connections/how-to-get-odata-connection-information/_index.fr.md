---
title: Comment obtenir les informations de connexion OData
type: docs
weight: 60
url: /fr/net/how-to-get-odata-connection-information/
---
## **Obtenir les informations de connexion OData**

 Il peut arriver que les développeurs aient besoin d'extraire des informations OData du fichier Excel. Aspose.Cells fournit le[**Workbook.DataMashupWorkbook.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup) propriété qui renvoie les informations DataMashup présentes dans le fichier Excel. Ces informations sont représentées par le[**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) classe. Le[**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)la classe fournit la[**Formules PowerQuery**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) propriété qui renvoie le[**PowerQueryFormulaColctionPowerQueryFormulaColction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) le recueil. Du[**PowerQueryFormulaColctionPowerQueryFormulaColction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction), vous pouvez accéder à[**PowerQueryFormulaPowerQueryFormulaPowerQueryFormulaPowerQueryFormulaPowerQueryFormula**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) et[**PowerQueryFormulaItemPowerQueryFormulaItemPowerQueryFormulaItemPowerQueryFormulaItemPowerQueryFormulaItemPowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

L'extrait de code suivant illustre l'utilisation de ces classes pour récupérer les informations OData.

Le fichier source utilisé dans l'extrait de code suivant est joint pour votre référence.

[Fichier source](96928098.xlsx)

### **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **Sortie console**

Nom de la connexion : Commandes

Nom : source

Valeur : OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Nom : Orders_table

Valeur : Source{[Name="Commandes",Signature="table"]}[Données]