---
title: Vues de feuille de calcul
type: docs
weight: 40
url: /fr/net/worksheet-views/
---
## **Aperçu des sauts de page**

Toutes les feuilles de calcul peuvent être visualisées en deux modes :

- Vue normale.
- Aperçu des sauts de page.

La vue normale est la vue par défaut d'une feuille de calcul. L'aperçu des sauts de page est une vue d'édition qui affiche une feuille de calcul telle qu'elle sera imprimée. L'aperçu des sauts de page montre quelles données iront sur chaque page afin que vous puissiez ajuster la zone d'impression et les sauts de page. À l'aide de Aspose.Cells, les développeurs peuvent activer les modes d'affichage normal ou de saut de page.

### **Contrôle des modes d'affichage**

Aspose.Cells fournit un[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour activer les modes d'aperçu normal ou de saut de page, utilisez les[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer[**EstAperçuSautPage**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) propriété.[**EstAperçuSautPage**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'un**vrai** ou un**faux** évaluer.

#### **Activation de la vue normale**

 Définissez une feuille de calcul en vue normale en définissant le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer[**EstAperçuSautPage**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) propriété à**faux**.

#### **Activation de l'aperçu des sauts de page**

 Définissez n'importe quelle feuille de calcul sur l'aperçu des sauts de page en définissant le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer[**EstAperçuSautPage**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) propriété à**vrai**Cela fait passer la feuille de calcul de la vue normale à l'aperçu des sauts de page.

 Un exemple complet est donné ci-dessous qui montre comment utiliser le[**EstAperçuSautPage**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)propriété pour activer le mode d'aperçu des sauts de page pour la première feuille de calcul d'un fichier Excel.

Le fichier book1.xls est ouvert en créant une instance du[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classer. La vue est commutée sur l'aperçu des sauts de page pour la première feuille de calcul en définissant le[**EstAperçuSautPage**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)propriété à**vrai**. Le fichier modifié est enregistré sous output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **Facteur de zoom**

### **Utilisation d'Excel Microsoft**

Microsoft Excel fournit une fonctionnalité qui permet aux utilisateurs de définir le facteur de zoom ou d'échelle d'une feuille de calcul. Cette fonctionnalité aide les utilisateurs à voir le contenu de la feuille de calcul dans des vues plus petites ou plus grandes. Les utilisateurs peuvent définir le facteur de zoom sur n'importe quelle valeur.

### **Aspose.Cells et facteur de zoom**

Aspose.Cells permet aux développeurs de définir le facteur de zoom de la feuille de calcul.
Aspose.Cells fournit un[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour définir le facteur de zoom d'une feuille de calcul, utilisez la[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer'[**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)propriété. Le facteur de zoom est défini en attribuant une valeur numérique (entière) au[**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) propriété.

Un exemple complet est donné ci-dessous qui montre comment utiliser le[**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) propriété pour définir le facteur de zoom de la première feuille de calcul du fichier Excel.

Le fichier book1.xls est ouvert en créant une instance du[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classer. Le facteur de zoom de la première feuille de calcul est défini sur 75 et le fichier modifié est enregistré sous output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **Figer les volets**

### **Utilisation d'Excel Microsoft**

Figer les volets est une fonctionnalité fournie par Microsoft Excel. Le gel des volets vous permet de sélectionner des données pour qu'elles restent visibles lors du défilement dans une feuille de calcul.

### **Aspose.Cells & Figer les volets**

Aspose.Cells permet aux développeurs d'appliquer des volets de gel aux feuilles de calcul lors de l'exécution.

Aspose.Cells fournit un[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classer. La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour configurer les volets figés, appelez la classe Worksheet'[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)méthode. La[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)méthode prend les paramètres suivants :

- **Ligne**, l'index de ligne de la cellule à partir de laquelle le gel commencera.
- **Colonne**, l'index de colonne de la cellule à partir de laquelle le gel commencera.
- **Lignes gelées**, le nombre de lignes visibles dans le volet supérieur.
- **Colonnes gelées**, le nombre de colonnes visibles dans le volet de gauche

Le fichier book1.xls est ouvert en appelant le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)constructeur de la classe lors de son instanciation et quelques lignes et colonnes sont figées dans la première feuille de calcul. Le fichier modifié est enregistré sous output.xls.

 Un exemple complet est donné ci-dessous qui montre comment utiliser le[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)méthode pour figer les lignes et les colonnes (à partir de C4, représenté par la 4ème ligne et la 3ème colonne, où les lignes et les colonnes commencent à partir de l'index 0) de la première feuille de calcul du fichier Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **Volets divisés**

Si vous devez diviser l'écran pour obtenir deux vues différentes dans la même feuille de calcul, divisez les volets. Microsoft Excel offre une fonctionnalité très pratique qui vous permet de visualiser plus d'une copie de votre feuille de calcul et de pouvoir faire défiler chaque volet de votre feuille de calcul indépendamment : les volets fractionnés.

Les vitres fonctionnent simultanément. Si vous faites un changement dans l'un, le changement apparaît simultanément dans l'autre. Aspose.Cells fournit la fonctionnalité de volets divisés pour les utilisateurs.

### **Appliquer et supprimer des volets fractionnés**

#### **Fractionnement des volets**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) fournit un large éventail de propriétés et de méthodes pour gérer un fichier Excel. Pour implémenter des vues fractionnées, utilisez le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer'[**Diviser**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split) . Pour supprimer les volets fractionnés, utilisez le[**Supprimer le fractionnement**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)méthode.

Dans l'exemple, nous utilisons un fichier de modèle simple qui est chargé, puis la fonctionnalité de définition de volets fractionnés est appliquée sur une cellule de la première feuille de calcul. Le fichier mis à jour est enregistré.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

Après avoir exécuté le code ci-dessus, le fichier généré aura une vue fractionnée.

#### **Suppression de volets**

 Supprimez les volets fractionnés à l'aide de la[**Supprimer le fractionnement**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)méthode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **Sujets avancés**
- [Masquer l'affichage des valeurs zéro dans la feuille de calcul](/cells/fr/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Définir la couleur de l'onglet de la feuille de calcul](/cells/fr/net/set-worksheet-tab-color/)
- [Afficher et masquer le quadrillage et les en-têtes de colonne de ligne](/cells/fr/net/show-and-hide-gridlines-and-row-column-headers/)
- [Afficher et masquer les lignes, les colonnes et les barres de défilement](/cells/fr/net/show-and-hide-rows-columns-and-scroll-bars/)
- [Afficher et masquer les feuilles de calcul et les onglets](/cells/fr/net/show-and-hide-worksheets-and-tabs/)
- [Afficher des formules au lieu de valeurs dans une feuille de calcul](/cells/fr/net/show-formulas-instead-of-values-in-a-worksheet/)
- [Utiliser les options de vérification des erreurs](/cells/fr/net/use-error-checking-options/)

