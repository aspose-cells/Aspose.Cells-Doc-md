---
title: Créer des tableaux croisés dynamiques et des graphiques croisés dynamiques
type: docs
weight: 20
url: /fr/net/create-pivot-tables-and-pivot-charts/
---
{{% alert color="primary" %}}

Un tableau croisé dynamique est un résumé interactif des enregistrements. Par exemple, vous pouvez avoir des centaines d'entrées de facture dans une liste d'une feuille de calcul. Un tableau croisé dynamique permet de totaliser les factures par client, produit ou date. Avec Microsoft Excel, il est possible de réorganiser rapidement les informations dans le tableau croisé dynamique en faisant glisser les boutons vers une nouvelle position.

Un tableau croisé dynamique est une représentation graphique interactive des données d'un tableau croisé dynamique. Les graphiques croisés dynamiques ont été introduits dans Excel 2000. L'utilisation d'un graphique croisé dynamique facilite encore la compréhension des données puisque le tableau croisé dynamique crée automatiquement des sous-totaux et des totaux.

 Aspose.Cells prend en charge[tableaux croisés dynamiques](/cells/fr/net/create-pivot-tables-and-pivot-charts/) et[tableaux croisés dynamiques](/cells/fr/net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Ajout de tableaux croisés dynamiques et de graphiques**

Aspose.Cells fournit un ensemble spécial de classes utilisées pour créer des tableaux croisés dynamiques. Ces classes sont utilisées pour créer et définir des objets PivotTable, qui agissent comme les blocs de construction de base d'un objet PivotTable :

- PivotField, un champ dans un rapport de tableau croisé dynamique.
- PivotFields, une collection de tous les objets PivotField dans un tableau croisé dynamique.
- Tableau croisé dynamique, un rapport de tableau croisé dynamique sur une feuille de calcul.
- Tableaux croisés dynamiques, une collection de tous les objets de tableau croisé dynamique de la feuille de calcul.

### **Préparation à l'utilisation Aspose.Cells**

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger Aspose.Cells](https://downloads.aspose.com/cells/net).
 1. Installez-le sur votre ordinateur de développement.
 Tout[Aspose](http://www.aspose.com/) les composants, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il injecte uniquement des filigranes dans les documents produits. Pour utiliser le composant dans toute sa capacité, vous devez disposer d'une licence valide.
1. Créer un projet :
 1. Démarrez Visual Studio.Net.
 1. Créez une nouvelle application console.
1. Ajoutez des références :
 Ajoutez une référence au composant Aspose.Cells dans votre projet, par exemple ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Ajout d'un tableau croisé dynamique**

Pour créer un tableau croisé dynamique à l'aide de Aspose.Cells :

1. Ajoutez des données aux cellules d'une feuille de calcul à l'aide de la méthode PutValue/setValue d'un objet Cell. Vous utilisez également un fichier modèle déjà rempli de données. Les données seront utilisées comme source de données du tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode add de la collection PivotTables (encapsulée dans l'objet Worksheet).
1. Accédez au nouvel objet PivotTable à partir de la collection PivotTables en transmettant son index. # Utilisez n'importe lequel des objets de tableau croisé dynamique encapsulés dans l'objet PivotTable pour gérer le tableau.

Des exemples de code sont donnés ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Ajout d'un tableau croisé dynamique**

Pour créer un graphique croisé dynamique à l'aide de Aspose.Cells :

1. Ajoutez un graphique.
1. Définissez le PivotSource du graphique pour faire référence à un tableau croisé dynamique existant dans la feuille de calcul.
1. Définissez d'autres attributs.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

