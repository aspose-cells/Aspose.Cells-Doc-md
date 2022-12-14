---
title: Formater la feuille de calcul Cells dans un classeur
type: docs
weight: 2000
url: /fr/net/format-worksheet-cells-in-a-workbook/
---
{{% alert color="primary" %}}

Cet article montre comment :

1. Utilisez des styles pour formater rapidement les données.
1. Mettre en forme les cellules en lignes et en colonnes.
1. Utilisez des bordures et des couleurs pour mettre en valeur les données.
1. Appliquez des formats numériques pour mettre en valeur les données.
1. Utilisez des polices et des attributs pour mettre en évidence les données.
1. Mettre en forme les données dans une plage nommée.
1. Modifier l'alignement et l'orientation des données.
1. Définissez la hauteur de ligne et la largeur de colonne.

 L'exemple de projet exécute toutes ces tâches et fournit aux développeurs une description détaillée de la façon de créer un classeur, d'ajouter des données et d'appliquer la mise en forme à l'aide de[Aspose.Cells](https://products.aspose.com/cells/net/).

{{% /alert %}}

## **Formatage des données**

Le formatage est utilisé pour distinguer les différents types d'informations et pour afficher clairement les données.

Un format représente un style et est défini comme un ensemble de caractéristiques, telles que les polices et les tailles de police, les formats de nombre, les bordures de cellule, l'ombrage de cellule, l'indentation, l'alignement et l'orientation du texte. Les bordures offrent d'autres moyens de mettre en évidence les informations. Une bordure est une ligne tracée autour d'une cellule ou d'un groupe de cellules.

Les formats numériques rendent également les données plus significatives. En appliquant différents formats de nombres, vous pouvez modifier l'apparence des nombres sans modifier le nombre derrière l'apparence.

Aspose.Cells vous permet de tracer facilement des bordures autour des cellules et des plages. Il vous permet également d'appliquer des polices et d'ombrer des cellules. Le composant est suffisamment efficace pour vous permettre de formater une ligne ou une colonne complète, de définir des alignements, d'envelopper et de faire pivoter du texte dans des cellules. Aspose.Cells prend également en charge tous les formats numériques pris en charge par Microsoft Excel.

Cet article montre comment créer une application console dans Visual Studio.Net qui génère un rapport annuel sur les ventes. Le classeur est créé à partir de zéro, puis les données sont insérées et la feuille de calcul est formatée. Nous montrons comment créer une application console simple qui crée un classeur Excel (vous pouvez également utiliser un fichier modèle), insérer des données de vente dans la première feuille de calcul, formater les données et enregistrer un fichier Excel.

### **Traiter**

Vous trouverez ci-dessous les étapes à suivre pour créer une feuille de calcul et formater différentes cellules dans différentes lignes et colonnes d'une feuille de calcul.

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger](https://downloads.aspose.com/cells/net) Aspose.Cells for .NET.
 1. Installez-le sur votre ordinateur de développement.
1. Créez un projet et ajoutez des références :
 1. Démarrez Visual Studio.Net.
 1. Créez une nouvelle application console.
 1. Ajoutez une référence à Aspose.Cells, par exemple …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Ajoutez le code suivant au projet :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FormatWorksheetCells-1.cs" >}}
