---
title: Vues de feuille de calcul
type: docs
weight: 10
url: /fr/java/worksheet-views/
---
## **Aperçu des sauts de page**
Toutes les feuilles de calcul peuvent être visualisées en deux modes :

- Vue normale.
- Aperçu des sauts de page.

Une vue normale est la vue par défaut d'une feuille de calcul. L'aperçu des sauts de page est une vue d'édition qui affiche une feuille de calcul telle qu'elle sera imprimée. L'aperçu des sauts de page montre quelles données iront sur chaque page afin que vous puissiez ajuster la zone d'impression et les sauts de page. À l'aide de Aspose.Cells, les développeurs peuvent activer les modes d'affichage normal ou de saut de page.
### **Contrôle des modes d'affichage**
 Aspose.Cells fournit un[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer. La[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour activer les modes d'aperçu normal ou de saut de page, utilisez les[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)méthode.
#### **Activation de la vue normale**
Définissez n'importe quelle feuille de calcul en vue normale à l'aide de la[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) méthode de la[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe et passage**faux** comme paramètre.
#### **Activation de l'aperçu des sauts de page**
Définissez n'importe quelle feuille de calcul sur l'aperçu des sauts de page à l'aide de la[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)méthode de la[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe et passage**vrai**comme paramètre.

 Un exemple complet est donné ci-dessous qui démontre l'utilisation de la[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)pour activer le mode d'aperçu des sauts de page pour la première feuille de calcul du fichier Excel.

Dans la capture d'écran ci-dessous, vous pouvez voir que le fichier Book1.xls est en mode Normal.

**Book1.xls : feuille de calcul avant modification** 

![tâche : image_autre_texte](worksheet-views_1.png)

 Book1.xls est ouvert avec le[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)classe et le mode passe à l'aperçu des sauts de page pour la première feuille de calcul. Le fichier modifié est enregistré sous output.xls.

**Output.xls : feuille de calcul après modification** 

![tâche : image_autre_texte](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **Facteur de zoom**
Microsoft Excel fournit une fonctionnalité qui permet aux utilisateurs de définir le facteur de zoom ou d'échelle d'une feuille de calcul. Cette fonctionnalité aide les utilisateurs à voir le contenu de la feuille de calcul dans des vues plus petites ou plus grandes. Les utilisateurs peuvent définir le facteur de zoom sur n'importe quelle valeur.

**Réglage du facteur de zoom à l'aide d'Excel Microsoft** 

![tâche : image_autre_texte](worksheet-views_3.png)

Aspose.Cells permet également aux développeurs de définir le facteur de zoom de la feuille de calcul.
### **Contrôle du facteur de zoom**
Aspose.Cells fournit un[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer. La[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour définir le facteur de zoom d'une feuille de calcul, utilisez la[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[définirZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)méthode.

 Un exemple complet est donné ci-dessous qui montre comment utiliser le[définirZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)méthode pour définir le facteur de zoom de la première feuille de calcul dans un fichier Excel.

Dans la capture d'écran ci-dessous, vous pouvez voir le fichier Book1.xls dans la vue par défaut.

**Book1.xls : feuille de calcul avant modification** 

![tâche : image_autre_texte](worksheet-views_4.png)

 Le fichier Book1.xls s'ouvre avec le[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class et le facteur de zoom de la première feuille de calcul est défini sur 75. Le fichier modifié est enregistré sous output.xls.

**Output.xls : feuille de calcul après modification** 

![tâche : image_autre_texte](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **Figer les volets**
Figer les volets est une fonctionnalité fournie par Microsoft Excel. Le gel des volets vous permet de sélectionner des données pour qu'elles restent visibles lors du défilement dans une feuille de calcul.

**Utilisation des volets de gel dans Microsoft Excel** 

![tâche : image_autre_texte](worksheet-views_6.png)

Aspose.Cells permet également aux développeurs d'appliquer des volets de gel aux feuilles de calcul lors de l'exécution.

Aspose.Cells fournit un[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer. La[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour configurer les volets figés, appelez le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\) ) méthode. La[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) prend les paramètres suivants :

- **Ligne**, l'index de ligne de la cellule à partir de laquelle le gel commencera.
- **Colonne**, l'index de colonne de la cellule à partir de laquelle le gel commencera.
- **Lignes gelées**, le nombre de lignes visibles dans le volet supérieur.
- **Colonnes gelées**, le nombre de colonnes visibles dans le volet de gauche

 Un exemple complet est donné ci-dessous qui montre comment utiliser le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) méthode pour figer les lignes et les colonnes (à partir de C4, représenté par la 4e ligne et la 3e colonne, où les lignes et les colonnes commencent à partir de 0 index) de la première feuille de calcul du fichier Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


Dans la capture d'écran ci-dessous, vous pouvez voir le fichier Book1.xls sans volets de gel.

**Book1.xls : vue feuille de calcul avant toute modification** 

![tâche : image_autre_texte](worksheet-views_7.png)

 Le fichier Book1.xls s'ouvre avec le[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)classe, puis quelques lignes et colonnes sont figées sur la première feuille de calcul. Le fichier modifié est enregistré sous output.xls.

**Outlook.xls : vue de la feuille de calcul après modification** 

![tâche : image_autre_texte](worksheet-views_8.png)
## **Volets divisés**
Si vous devez diviser l'écran pour obtenir deux vues différentes dans la même feuille de calcul, divisez les volets. Microsoft Excel offre une fonctionnalité très pratique qui vous permet de visualiser plus d'une copie de votre feuille de calcul et de pouvoir faire défiler chaque volet de votre feuille de calcul indépendamment : les volets fractionnés.

Les vitres fonctionnent simultanément. Si vous faites un changement dans l'un, le changement apparaît simultanément dans l'autre. Aspose.Cells fournit la fonctionnalité de volets divisés pour les utilisateurs.
### **Appliquer et supprimer des volets fractionnés**
#### **Fractionnement des volets**
Aspose.Cells fournit un[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)La classe fournit un large éventail de propriétés et de méthodes pour gérer les fichiers Excel. Pour implémenter des vues fractionnées, utilisez le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[diviser](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\) ) méthode. Pour supprimer les volets fractionnés, utilisez le[supprimerSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) méthode.

Dans l'exemple, nous utilisons un fichier de modèle simple qui est chargé, puis la fonctionnalité de définition de volets fractionnés est appliquée sur une cellule de la première feuille de calcul. Le fichier mis à jour est enregistré.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



Après avoir exécuté le code ci-dessus, le fichier généré a une vue fractionnée.

**Fractionner les volets dans le fichier de sortie** 

![tâche : image_autre_texte](worksheet-views_9.png)
#### **Suppression de volets**
 Les développeurs peuvent supprimer les volets fractionnés à l'aide de l'outil[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[supprimerSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) méthode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **Sujets avancés**
- [Masquer l'affichage des valeurs zéro dans la feuille de calcul](/cells/fr/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Définir la couleur de l'onglet de la feuille de calcul](/cells/fr/java/set-worksheet-tab-color/)
- [Afficher et masquer les éléments](/cells/fr/java/show-and-hide-elements/)
- [Afficher des formules au lieu de valeurs dans une feuille de calcul](/cells/fr/java/show-formulas-instead-of-values-in-a-worksheet/)
- [Utiliser les options de vérification des erreurs](/cells/fr/java/use-error-checking-options/)
