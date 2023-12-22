---
title: Rechercher ou rechercher des données
type: docs
weight: 50
url: /fr/net/find-or-search-data/
description: Découvrez comment rechercher ou rechercher des cellules dans une feuille de calcul contenant des données spécifiées via le Aspose.Cells for .NET API.
keywords: Find data, Search data, Find Cells Containing a Formula, Search Cells Containing a Formula, Find Data or Formulas using FindOptions, Search Data or Formulas using FindOptions, Find or Search Cells Containing Specified String Value or Number, Find or Search cells contains specified data
---
{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de rechercher des cellules dans une feuille de calcul contenant des données spécifiées.

{{% /alert %}}

##  **Constatation Cells contenant des données spécifiées**

###  **Utilisation d'Excel Microsoft**

 Microsoft Excel permet aux utilisateurs de rechercher des cellules dans une feuille de calcul contenant des données spécifiées. Si vous sélectionnez**Modifier** du**Trouver** dans Microsoft Excel, vous verrez une boîte de dialogue dans laquelle vous pourrez spécifier la valeur de recherche.

Ici, nous recherchons la valeur « Oranges ». Aspose.Cells permet également aux développeurs de rechercher des cellules dans la feuille de calcul contenant des valeurs spécifiées.

###  **En utilisant le Aspose.Cells**

 Aspose.Cells propose un cours,[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , cela représente un fichier Excel Microsoft. Le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d’accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fournit un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection qui représente toutes les cellules de la feuille de calcul. Le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)La collection fournit plusieurs méthodes pour rechercher des cellules dans une feuille de calcul contenant des données spécifiées par l'utilisateur. Quelques-unes de ces méthodes sont discutées ci-dessous plus en détail.

{{% alert color="primary" %}}

Toutes les méthodes Find renvoient les références des cellules contenant les données spécifiées à rechercher.

{{% /alert %}}

##  **Recherche Cells contenant une formule**

 Les développeurs peuvent trouver une formule spécifiée dans la feuille de calcul en appelant le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la collection[**Trouver**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) méthode. Généralement, le[**Trouver**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)La méthode accepte trois paramètres :

- **Objet:**L'objet à rechercher. Le type doit être int,double,DateTime,string,bool.
- **Cellule précédente :**Cellule précédente avec le même objet. Ce paramètre peut être défini sur null si vous effectuez une recherche depuis le début.
- FindOptions : options permettant de rechercher l'objet requis.

Les exemples ci-dessous utilisent les données d'une feuille de calcul pour pratiquer les méthodes de recherche :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

##  **Recherche de données ou de formules à l'aide de FindOptions**

 Il est possible de trouver des valeurs spécifiées en utilisant le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la collection[**Trouver**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) méthode avec divers[**Rechercher des options**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . Généralement, le[**Trouver**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)La méthode accepte les paramètres suivants :

- *Valeur de recherche**, la donnée ou la valeur à rechercher.
- *Cellule précédente**, la dernière cellule contenant la même valeur. Ce paramètre peut être défini sur null lors d'une recherche depuis le début.
- *Rechercher des options**, les options de recherche.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

##  **Résultat Cells contenant une valeur de chaîne ou un numéro spécifié**

 Il est possible de trouver des valeurs de chaîne spécifiées en appelant la même chose[**Trouver**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) méthode trouvée dans le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection avec divers[**Rechercher des options**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 Spécifie le[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) et[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) propriétés. L'exemple de code suivant illustre comment utiliser ces propriétés pour rechercher des cellules avec différents nombres de chaînes au niveau**début** ou au**centre** ou au**fin** de la chaîne de la cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

##  **Sujets avancés**
- [Trouvez Cells avec un style spécifique](/cells/fr/net/find-cells-with-specific-style/)
- [Rechercher si la valeur de la cellule commence par un guillemet simple](/cells/fr/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Rechercher des données à l'aide des valeurs d'origine](/cells/fr/net/search-data-using-original-values/)
