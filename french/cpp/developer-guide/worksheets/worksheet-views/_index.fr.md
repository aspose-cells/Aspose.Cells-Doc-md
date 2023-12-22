---
title: Vues de feuille de calcul
type: docs
weight: 40
url: /fr/cpp/worksheet-views/
---
##  **Aperçu des sauts de page**
Toutes les feuilles de calcul peuvent être visualisées selon deux modes :

- Vue normale.
- Aperçu des sauts de page.

La vue Normale est la vue par défaut d’une feuille de calcul. L'aperçu des sauts de page est une vue d'édition qui affiche une feuille de calcul telle qu'elle sera imprimée. L'aperçu des sauts de page montre les données qui seront placées sur chaque page afin que vous puissiez ajuster la zone d'impression et les sauts de page. À l'aide de Aspose.Cells, les développeurs peuvent activer les modes d'affichage normal ou de prévisualisation des sauts de page.
###  **Contrôler les modes d'affichage**
 Aspose.Cells propose un cours[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel Microsoft. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) La classe fournit un large éventail de méthodes pour gérer les feuilles de calcul. Pour activer les modes d'aperçu normal ou de saut de page, utilisez l'option[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) méthode du[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe.[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) renvoie une valeur booléenne, ce qui signifie qu'il ne peut stocker qu'un**vrai** ou**FAUX** valeur.
####  **Activation de l'affichage normal**
Définissez une feuille de calcul en affichage normal en définissant le[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)méthode du[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)classe à *false**.
####  **Activation de l'aperçu des sauts de page**
Définissez n'importe quelle feuille de calcul sur l'aperçu des sauts de page en définissant l'option[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)méthode du[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)classe à *true**. Cela fait passer la feuille de calcul de l’affichage normal à l’aperçu des sauts de page.

Un exemple complet est donné ci-dessous qui montre comment utiliser le[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)méthode pour activer le mode d’aperçu des sauts de page pour la première feuille de calcul d’un fichier Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
##  **Facteur de zoom**
###  **Utilisation d'Excel Microsoft**
Microsoft Excel fournit une fonctionnalité qui permet aux utilisateurs de définir le zoom ou le facteur de mise à l'échelle d'une feuille de calcul. Cette fonctionnalité aide les utilisateurs à voir le contenu de la feuille de calcul dans des vues plus petites ou plus grandes. Les utilisateurs peuvent définir le facteur de zoom sur n'importe quelle valeur.
###  **Aspose.Cells et facteur de zoom**
 Aspose.Cells permet également aux développeurs de définir le facteur de zoom de la feuille de calcul. Aspose.Cells propose un cours[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel Microsoft. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)La classe fournit un large éventail de méthodes pour gérer les feuilles de calcul. Pour définir le facteur de zoom d'une feuille de calcul, utilisez l'option[Définir le zoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) méthode du[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Le facteur de zoom est défini en attribuant une valeur numérique (entière) au[Définir le zoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)méthode.

Un exemple complet est donné ci-dessous qui montre comment utiliser le[Définir le zoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)méthode pour définir le facteur de zoom de la première feuille de calcul du fichier Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
##  **Figer les volets**
###  **Utilisation d'Excel Microsoft**
Geler les volets est une fonctionnalité fournie par Microsoft Excel. Le gel des volets vous permet de sélectionner les données qui resteront visibles lors du défilement dans une feuille de calcul.
###  **Aspose.Cells et vitres gelées**
 Aspose.Cells permet également aux développeurs d'appliquer des volets figés aux feuilles de calcul au moment de l'exécution. Aspose.Cells propose un cours[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel Microsoft. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)La classe fournit un large éventail de méthodes pour gérer les feuilles de calcul. Pour configurer les volets figés, appelez le[Geler les volets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)méthode du[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Le[Geler les volets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)La méthode prend les paramètres suivants :

- *Row**, l'index de ligne de la cellule à partir de laquelle le gel commencera.
- *Colonne**, l'index de colonne de la cellule à partir de laquelle le gel commencera.
- *Lignes gelées**, le nombre de lignes visibles dans le volet supérieur.
- *Colonnes gelées**, le nombre de colonnes visibles dans le volet de gauche

 Un exemple complet est donné ci-dessous qui montre comment utiliser le[Geler les volets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)méthode pour figer les lignes et les colonnes (à partir de C4, représenté par la 4ème ligne et la 3ème colonne, où les lignes et les colonnes commencent à partir de l'index 0) de la première feuille de calcul du fichier Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
##  **Volets divisés**
Si vous devez diviser l'écran pour obtenir deux vues différentes dans la même feuille de calcul, divisez les volets. Microsoft Excel offre une fonctionnalité très pratique qui vous permet d'afficher plusieurs copies de votre feuille de calcul et de pouvoir faire défiler chaque volet de votre feuille de calcul indépendamment : les volets divisés.

Les vitres fonctionnent simultanément. Si vous effectuez une modification dans l'un, la modification apparaît simultanément dans l'autre. Aspose.Cells fournit la fonctionnalité de volets divisés pour les utilisateurs.
###  **Application et suppression de volets divisés**
####  **Fractionnement des volets**
 Aspose.Cells propose un cours[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel Microsoft. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)La classe fournit un large éventail de méthodes pour gérer un fichier Excel. Pour implémenter des vues fractionnées, utilisez le[Diviser](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) méthode du[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Pour supprimer les volets divisés, utilisez le[SupprimerSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)méthode.

Dans l'exemple, nous utilisons un simple fichier modèle qui est chargé, puis la fonctionnalité de définition des volets divisés est appliquée sur une cellule de la première feuille de calcul. Le fichier mis à jour est enregistré.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
####  **Suppression des volets**
 Supprimez les volets divisés à l'aide de l'outil[SupprimerSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)méthode.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
