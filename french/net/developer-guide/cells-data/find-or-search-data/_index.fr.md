---
title: Trouver ou rechercher des données
type: docs
weight: 50
url: /fr/net/find-or-search-data/
description: Apprendre à trouver ou rechercher des cellules dans une feuille de calcul contenant des données spécifiées via l API Aspose.Cells for .NET
keywords: Trouver des données, Rechercher des données, Trouver des cellules contenant une formule, Rechercher des cellules contenant une formule, Trouver des données ou des formules à l aide de FindOptions, Rechercher des données ou des formules à l aide de FindOptions, Trouver ou rechercher des cellules contenant une valeur ou un nombre spécifié, Trouver ou rechercher des cellules contenant des données spécifiées
---

{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de trouver des cellules dans une feuille de calcul contenant des données spécifiées.

{{% /alert %}}

## **Recherche de cellules contenant des données spécifiées**

### **Utilisation de Microsoft Excel**

Microsoft Excel permet aux utilisateurs de trouver des cellules dans une feuille de calcul contenant des données spécifiées. Si vous sélectionnez **Modifier** dans le menu **Rechercher** de Microsoft Excel, vous verrez une boîte de dialogue où vous pouvez spécifier la valeur de recherche.

Ici, nous recherchons la valeur "Oranges". Aspose.Cells permet également aux développeurs de trouver des cellules dans la feuille de calcul contenant des valeurs spécifiées.

### **Utilisation d'Aspose.Cells**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) qui représente toutes les cellules de la feuille de calcul. La collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) propose plusieurs méthodes pour trouver des cellules dans une feuille de calcul contenant des données spécifiées. Quelques-unes de ces méthodes sont discutées ci-dessous en détail.

{{% alert color="primary" %}}

Toutes les méthodes de recherche renvoient les références des cellules contenant les données spécifiées à rechercher.

{{% /alert %}}

## **Recherche de cellules contenant une formule**

Les développeurs peuvent trouver une formule spécifiée dans la feuille de calcul en appelant la méthode [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) de la collection [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index). En général, la méthode [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) accepte trois paramètres :

- **Objet :** L'objet à rechercher. Le type doit être int, double, DateTime, chaîne, booléen.
- **Cellule précédente :** Cellule précédente avec le même objet. Ce paramètre peut être défini sur null si la recherche est effectuée depuis le début.
- FindOptions: Options pour trouver l'objet requis.

Les exemples ci-dessous utilisent les données de la feuille de calcul pour apprendre les méthodes de recherche.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **Recherche de données ou de formules à l'aide de FindOptions**

Il est possible de trouver des valeurs spécifiées en utilisant la méthode [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) avec divers [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions). En général, la méthode [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) accepte les paramètres suivants :

- **Valeur de recherche**, les données ou la valeur à rechercher.
- **Cellule précédente**, la dernière cellule qui contient la même valeur. Ce paramètre peut être défini sur null lors de la recherche depuis le début.
- **Options de recherche**, les options de recherche.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Recherche des cellules contenant une valeur de chaîne spécifiée ou un nombre.**

Il est possible de trouver des valeurs de chaîne spécifiées en appelant la même méthode [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) trouvée dans la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) avec divers [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

Spécifiez les propriétés [**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) et [**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype). L'exemple de code suivant illustre comment utiliser ces propriétés pour trouver des cellules avec un nombre varié de chaînes au **début** ou au **centre** ou à la **fin** de la chaîne de la cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **Sujets avancés**
- [Rechercher des cellules avec un style spécifique](/cells/fr/net/find-cells-with-specific-style/)
- [Trouver si la valeur de la cellule commence par un guillemet simple](/cells/fr/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Rechercher des données en utilisant des valeurs originales](/cells/fr/net/search-data-using-original-values/)
{{< app/cells/assistant language="csharp" >}}
