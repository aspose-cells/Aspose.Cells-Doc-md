---
title: Vues de feuille de calcul
type: docs
weight: 40
url: /fr/cpp/worksheet-views/
---
## **Aperçu des sauts de page**
Toutes les feuilles de calcul peuvent être visualisées en deux modes :

- Vue normale.
- Aperçu des sauts de page.

La vue normale est la vue par défaut d'une feuille de calcul. L'aperçu des sauts de page est une vue d'édition qui affiche une feuille de calcul telle qu'elle sera imprimée. L'aperçu des sauts de page montre quelles données iront sur chaque page afin que vous puissiez ajuster la zone d'impression et les sauts de page. À l'aide de Aspose.Cells, les développeurs peuvent activer les modes d'affichage normal ou de saut de page.
### **Contrôle des modes d'affichage**
 Aspose.Cells fournit une classe[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) qui représente un fichier Excel Microsoft. Le[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe contient un[Feuilles de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) La classe fournit un large éventail de méthodes de gestion des feuilles de calcul. Pour activer les modes d'aperçu normal ou de saut de page, utilisez les[EstAperçuSautPage](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) méthode de la[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe.[EstAperçuSautPage](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) renvoie une valeur booléenne, ce qui signifie qu'il ne peut stocker qu'un**vrai** ou alors**faux** évaluer.
#### **Activation de la vue normale**
Définissez une feuille de calcul en vue normale en définissant le[EstAperçuSautPage](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)méthode de la[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe à**faux**.
#### **Activation de l'aperçu des sauts de page**
Définissez n'importe quelle feuille de calcul sur l'aperçu des sauts de page en définissant le[EstAperçuSautPage](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)méthode de la[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe à**vrai**Cela fait passer la feuille de calcul de la vue normale à l'aperçu des sauts de page.

 Un exemple complet est donné ci-dessous qui montre comment utiliser le[EstAperçuSautPage](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)pour activer le mode d'aperçu des sauts de page pour la première feuille de calcul d'un fichier Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview.cpp" >}}
## **Facteur de zoom**
### **Utilisation d'Excel Microsoft**
Microsoft Excel fournit une fonctionnalité qui permet aux utilisateurs de définir le facteur de zoom ou d'échelle d'une feuille de calcul. Cette fonctionnalité aide les utilisateurs à voir le contenu de la feuille de calcul dans des vues plus petites ou plus grandes. Les utilisateurs peuvent définir le facteur de zoom sur n'importe quelle valeur.
### **Aspose.Cells et facteur de zoom**
 Aspose.Cells permet également aux développeurs de définir le facteur de zoom de la feuille de calcul. Aspose.Cells fournit une classe[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) qui représente un fichier Excel Microsoft. Le[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe contient un[Feuilles de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)La classe fournit un large éventail de méthodes de gestion des feuilles de calcul. Pour définir le facteur de zoom d'une feuille de calcul, utilisez la[Zoom](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec) méthode de la[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe Le facteur de zoom est défini en attribuant une valeur numérique (entière) à la[Zoom](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)méthode.

 Un exemple complet est donné ci-dessous qui montre comment utiliser le[Zoom](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)méthode pour définir le facteur de zoom de la première feuille de calcul du fichier Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor.cpp" >}}
## **Figer les volets**
### **Utilisation d'Excel Microsoft**
Figer les volets est une fonctionnalité fournie par Microsoft Excel. Le gel des volets vous permet de sélectionner des données pour qu'elles restent visibles lors du défilement dans une feuille de calcul.
### **Aspose.Cells & Figer les volets**
 Aspose.Cells permet également aux développeurs d'appliquer des volets de gel aux feuilles de calcul lors de l'exécution. Aspose.Cells fournit une classe[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) qui représente un fichier Excel Microsoft. Le[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe contient un[Feuilles de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)La classe fournit un large éventail de méthodes de gestion des feuilles de calcul. Pour configurer les volets figés, appelez le[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)méthode de la[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Le[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)méthode prend les paramètres suivants :

- **Ligne**, l'index de ligne de la cellule à partir de laquelle le gel commencera.
- **Colonne**, l'index de colonne de la cellule à partir de laquelle le gel commencera.
- **Lignes gelées**, le nombre de lignes visibles dans le volet supérieur.
- **Colonnes gelées**, le nombre de colonnes visibles dans le volet de gauche

 Un exemple complet est donné ci-dessous qui montre comment utiliser le[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)méthode pour figer les lignes et les colonnes (à partir de C4, représenté par la 4ème ligne et la 3ème colonne, où les lignes et les colonnes commencent à partir de l'index 0) de la première feuille de calcul du fichier Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes.cpp" >}}
## **Volets divisés**
Si vous devez diviser l'écran pour obtenir deux vues différentes dans la même feuille de calcul, divisez les volets. Microsoft Excel offre une fonctionnalité très pratique qui vous permet de visualiser plus d'une copie de votre feuille de calcul et de pouvoir faire défiler chaque volet de votre feuille de calcul indépendamment : les volets fractionnés.

Les vitres fonctionnent simultanément. Si vous faites un changement dans l'un, le changement apparaît simultanément dans l'autre. Aspose.Cells fournit la fonctionnalité de volets divisés pour les utilisateurs.
### **Appliquer et supprimer des volets fractionnés**
#### **Fractionnement des volets**
 Aspose.Cells fournit une classe[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) qui représente un fichier Excel Microsoft. Le[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)fournit un large éventail de méthodes pour gérer un fichier Excel. Pour implémenter des vues fractionnées, utilisez le[Diviser](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a0e581a3a9528a767c57008521ee02b6f) méthode de la[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Pour supprimer les volets fractionnés, utilisez le[Supprimer le fractionnement](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)méthode.

Dans l'exemple, nous utilisons un fichier de modèle simple qui est chargé, puis la fonctionnalité de définition de volets fractionnés est appliquée sur une cellule de la première feuille de calcul. Le fichier mis à jour est enregistré.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes.cpp" >}}
#### **Suppression de volets**
 Supprimez les volets fractionnés à l'aide de la[Supprimer le fractionnement](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)méthode.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes.cpp" >}}
