---
title: Utilisation de Sparklines et réglages du format 3D
type: docs
weight: 40
url: /fr/python-net/using-sparklines-and-settings-3d-format/
---

## **Utilisation des sparklines**
Microsoft Excel 2010 peut analyser les informations de plus de façons que jamais. Il permet aux utilisateurs de suivre et de mettre en évidence les tendances importantes des données avec de nouveaux outils d'analyse et de visualisation des données. Les sparklines sont des mini-graphiques que vous pouvez placer à l'intérieur des cellules afin de visualiser les données et le graphique sur la même table. Lorsque les sparklines sont utilisés correctement, l'analyse des données est plus rapide et plus directe. Ils offrent également une vue simple des informations, évitant les feuilles de calcul surchargées avec de nombreux graphiques complexes.

Aspose.Cells pour Python via .NET offre une API pour manipuler les sparklines dans les feuilles de calcul.
### **Sparklines dans Microsoft Excel**
Pour insérer des sparklines dans Microsoft Excel 2010 :

1. Sélectionnez les cellules où vous souhaitez voir apparaître les sparklines. Pour les rendre faciles à visualiser, sélectionnez les cellules à côté des données.
1. Cliquez sur **Insérer** dans le ruban, puis choisissez **colonne** dans le groupe **Sparklines**.
1. Sélectionnez ou saisissez la plage de cellules dans la feuille de calcul contenant les données source. Les graphiques apparaîtront.

Les Sparklines vous aident à visualiser les tendances, par exemple le bilan de victoires ou de défaites pour une ligue de softball. Les Sparklines peuvent même résumer l'ensemble de la saison de chaque équipe dans la ligue.
### **Sparklines avec Aspose.Cells pour Python via .NET**
Les développeurs peuvent créer, supprimer ou lire des sparklines (dans le fichier modèle) en utilisant l’API fournie par Aspose.Cells pour Python via .NET. Les classes qui gèrent les sparklines se trouvent dans l’espace de noms [aspose.cells.charts](https://reference.aspose.com/cells/python-net/aspose.cells.charts), il est donc nécessaire d’importer cet espace de noms avant d’utiliser ces fonctionnalités.

En ajoutant des graphiques personnalisés pour une plage de données donnée, les développeurs ont la liberté d'ajouter différents types de petits graphiques à des zones de cellules sélectionnées.

L'exemple ci-dessous illustre la fonctionnalité des Sparklines. L'exemple montre comment :

1. Ouvrir un fichier modèle simple.
1. Lire les informations des sparklines pour une feuille de calcul.
1. Ajouter de nouvelles sparklines pour une plage de données donnée à une zone de cellules.
1. Enregistrez le fichier Excel sur le disque.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-UsingSparklines-1.py" >}}
## **Réglage du format 3D**
Vous pourriez avoir besoin de styles de graphique 3D pour obtenir uniquement les résultats pour votre scénario. Aspose.Cells pour Python via .NET fournit l’API pertinente pour appliquer la mise en forme 3D de Microsoft Excel 2007.

Un exemple complet est donné ci-dessous pour démontrer comment créer un graphique et appliquer le format 3D de Microsoft Excel 2007. Après l'exécution du code d'exemple, un graphique en colonnes (avec effets 3D) sera ajouté à la feuille de calcul.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-Applying3DFormat-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
