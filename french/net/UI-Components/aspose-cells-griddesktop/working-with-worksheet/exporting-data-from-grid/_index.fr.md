---
title: Exportation de données à partir de la grille
type: docs
weight: 60
url: /fr/net/exporting-data-from-grid/
---
{{% alert color="primary" %}} 

Dans notre rubrique précédente, nous avons parlé de l'importation du contenu d'un DataTable dans le contrôle Aspose.Cells.GridDesktop, mais nous n'avons délibérément pas mentionné que Aspose.Cells.GridDesktop prend également en charge le processus inverse. Ainsi, dans cette rubrique, nous discuterons de l'exportation des données à l'intérieur du contrôle Aspose.Cells.GridDesktop vers un DataTable.

{{% /alert %}} 
## **Exportation du contenu de la grille**
### **Exportation vers un DataTable spécifique**
 Pour exporter le contenu de la grille vers un objet DataTable spécifique, veuillez suivre les étapes ci-dessous :Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**.

- Créez un objet DataTable spécifique selon vos besoins.
-  Exporter les données d'un**Feuille de travail** à votre objet DataTable spécifié.

Dans l'exemple ci-dessous, nous avons créé un objet DataTable spécifique contenant quatre colonnes. Enfin, nous avons exporté les données de la feuille de calcul (à partir de la première cellule avec 69 lignes et 4 colonnes) vers un objet DataTable déjà créé par nous.

**Exemple:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Exportation vers une nouvelle table de données**
Parfois, les développeurs peuvent ne pas être intéressés par la création de leur propre objet DataTable et peuvent avoir simplement besoin d'exporter les données de la feuille de calcul vers un nouvel objet DataTable. Ce serait un moyen plus rapide pour les développeurs d'exporter simplement les données de la feuille de calcul.

Dans l'exemple ci-dessous, nous avons essayé une manière différente d'expliquer l'utilisation de la méthode ExportDataTable. Nous avons pris la référence de la feuille de calcul actuellement active, puis nous avons exporté les données complètes de cette feuille de calcul active vers un nouvel objet DataTable. Désormais, cet objet DataTable peut être utilisé de la manière souhaitée par un développeur. Juste pour une instance, un développeur peut lier cet objet DataTable à un DataGrid pour afficher les données.

**Exemple:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

Dans le cas ci-dessus, nous utiliserons une version surchargée de la méthode ExportDataTable qui renverra simplement un nouvel objet DataTable contenant les données exportées de la feuille de calcul.

{{% /alert %}}
