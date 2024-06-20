---
title: Exportation de données depuis Grid
type: docs
weight: 60
url: /fr/net/aspose-cells-griddesktop/export-data-from-grid/
keywords: GridDesktop,export, données, exporter des données
description: Cet article présente comment exporter des données dans GridDesktop.
---

{{% alert color="primary" %}} 

Dans notre précédent sujet, nous avons parlé de l'importation du contenu d'un DataTable dans le contrôle Aspose.Cells.GridDesktop, mais nous n'avons pas mentionné que Aspose.Cells.GridDesktop prend également en charge le processus inverse. Ainsi, dans ce sujet, nous discuterons de l'exportation des données à l'intérieur du contrôle Aspose.Cells.GridDesktop vers un DataTable.

{{% /alert %}} 
## **Exportation du contenu de la grille**
### **Exporter vers un DataTable spécifique**
Pour exporter le contenu de la grille vers un objet DataTable spécifique, veuillez suivre les étapes ci-dessous : Ajoutez le contrôle Aspose.Cells.GridDesktop à votre **Formulaire**.

- Créez un objet DataTable spécifique selon vos besoins.
- Exportez les données d'une **Feuille de calcul** sélectionnée vers votre objet DataTable spécifié.

Dans l'exemple ci-dessous, nous avons créé un objet DataTable spécifique avec quatre colonnes à l'intérieur. Enfin, nous avons exporté les données de la feuille de travail (à partir de la première cellule avec 69 lignes et 4 colonnes) vers un objet DataTable déjà créé par nous.

**Exemple :**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Exportation vers un nouveau DataTable**
Parfois, les développeurs peuvent ne pas être intéressés à créer leur propre objet DataTable et pourraient simplement avoir besoin d'exporter les données de la feuille de travail vers un nouvel objet DataTable. Ce serait le moyen le plus rapide pour les développeurs d'exporter simplement les données de la feuille de travail.

Dans l'exemple ci-dessous, nous avons essayé une manière différente d'expliquer l'utilisation de la méthode ExportDataTable. Nous avons pris comme référence la feuille de travail qui est actuellement active, puis nous avons exporté les données complètes de cette feuille de travail active vers un nouvel objet DataTable. Maintenant, cet objet DataTable peut être utilisé de la manière dont un développeur le souhaite. Par exemple, un développeur peut lier cet objet DataTable à un DataGrid pour afficher les données.

**Exemple :**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

Dans le cas ci-dessus, nous utiliserons une version surchargée de la méthode ExportDataTable qui renverra simplement un nouvel objet DataTable contenant les données exportées depuis la feuille de travail.

{{% /alert %}}
