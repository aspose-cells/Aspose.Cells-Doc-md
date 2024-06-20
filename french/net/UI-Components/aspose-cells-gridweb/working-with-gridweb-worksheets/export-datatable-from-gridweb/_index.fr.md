---
title: Exporter DataTable depuis GridWeb
type: docs
weight: 70
url: /fr/net/aspose-cells-gridweb/export-datatable-from-gridweb/
keywords: GridWeb, export
description: Cet article présente comment exporter un DataTable dans GridWeb.
---

{{% alert color="primary" %}} 

[Importer DataView dans GridWeb](/cells/fr/net/aspose-cells-gridweb/import-dataview-to-gridweb/) aborde l'importation du contenu d'une DataView dans le contrôle Aspose.Cells.GridWeb. Ce sujet traite de l'exportation des données depuis le contrôle Aspose.Cells.GridWeb vers un DataTable.

{{% /alert %}} 
## **Exportation des données de la feuille de calcul**
### **Vers un DataTable spécifique**
Pour exporter les données de la feuille de calcul vers un objet DataTable spécifique :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Créez un objet DataTable spécifique.
1. Exportez les données des cellules sélectionnées vers l'objet DataTable spécifié.

L'exemple ci-dessous crée un objet DataTable spécifique avec quatre colonnes. Les données de la feuille de calcul sont exportées à partir de la première cellule avec toutes les lignes et colonnes visibles dans la feuille de calcul, vers un objet DataTable déjà créé.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **Vers un nouveau DataTable**
Parfois, vous ne voulez pas créer un objet DataTable mais simplement besoin d'exporter les données de la feuille de calcul vers un nouvel objet DataTable.

L'exemple ci-dessous essaie une façon différente de montrer l'utilisation de la méthode Export. Il prend la référence de la feuille de calcul active et exporte les données complètes de cette feuille de calcul vers un nouvel objet DataTable. L'objet DataTable peut maintenant être utilisé de la manière que vous voulez. Par exemple, il est possible de lier l'objet DataTable à un GridView pour visualiser les données.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}
