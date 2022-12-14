---
title: Utilisation des sparklines et des paramètres Format 3D
type: docs
weight: 40
url: /fr/java/using-sparklines-and-settings-3d-format/
---
## **Utiliser des graphiques sparkline**
Microsoft Excel 2010 peut analyser les informations de plus de façons que jamais auparavant. Il permet aux utilisateurs de suivre et de mettre en évidence les tendances importantes des données grâce à de nouveaux outils d'analyse et de visualisation des données. Les graphiques sparkline sont des mini-graphiques que vous pouvez placer à l'intérieur des cellules afin de pouvoir afficher les données et le graphique sur le même tableau. Lorsque les graphiques sparkline sont utilisés correctement, l'analyse des données est plus rapide et plus précise. Ils fournissent également une vue simple des informations, évitant les feuilles de calcul surchargées avec beaucoup de graphiques occupés.

Aspose.Cells fournit un API pour manipuler les sparklines dans les feuilles de calcul.
### **Sparklines dans Microsoft Excel**
Pour insérer des sparklines dans Microsoft Excel 2010 :

1. Sélectionnez les cellules où vous souhaitez que les sparklines apparaissent. Pour faciliter leur visualisation, sélectionnez des cellules à côté des données.
1.  Cliquez sur**Insérer** sur le ruban, puis choisissez**colonne** dans le**Sparklines** groupe.
1. Sélectionnez ou entrez la plage de cellules de la feuille de calcul contenant les données source. Les graphiques apparaîtront.

Sparklines vous aide à voir les tendances, par exemple, le record de victoires ou de défaites pour une ligue de softball. Sparklines peut même résumer toute la saison de chaque équipe de la ligue.
### **Sparklines utilisant Aspose.Cells**
 Les développeurs peuvent créer, supprimer ou lire des sparklines (dans le fichier de modèle) à l'aide du API fourni par Aspose.Cells. Les classes qui gèrent les sparklines sont contenues dans le[Aspose.Cells.Charts](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)espace de noms, vous devez donc importer cet espace de noms avant d'utiliser ces fonctionnalités.

En ajoutant des graphiques personnalisés pour une plage de données donnée, les développeurs ont la liberté d'ajouter différents types de petits graphiques aux zones de cellules sélectionnées.

L'exemple ci-dessous illustre la fonctionnalité Sparklines. L'exemple montre comment :

1. Ouvrez un fichier modèle simple.
1. Lire les informations sparklines pour une feuille de calcul.
1. Ajoutez de nouveaux graphiques sparkline pour une plage de données donnée à une zone de cellule.
1. Enregistrez le fichier Excel sur le disque.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparkLine.java" >}}
## **Réglage du format 3D**
Vous aurez peut-être besoin de styles de graphique 3D pour obtenir uniquement les résultats de votre scénario. Aspose.Cells fournit le API pertinent pour appliquer le formatage Microsoft Excel 2007 3D.

Un exemple complet est donné ci-dessous pour montrer comment créer un graphique et appliquer le formatage Microsoft Excel 2007 3D. Après avoir exécuté l'exemple de code, un histogramme (avec effets 3D) sera ajouté à la feuille de calcul.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat.java" >}}
