---  
title: Trouver ou rechercher des données
type: docs  
weight: 50  
url: /fr/nodejs-cpp/find-or-search-data/  
description: Apprenez comment rechercher ou trouver des cellules dans une feuille de calcul qui contiennent des données spécifiées via l’API Aspose.Cells for Node.js via C++.  
keywords: Recherche de données Node.js via C++, Recherche de données Node.js via C++, Recherche de cellules contenant une formule Node.js via C++, Recherche de cellules contenant une formule Node.js via C++, Recherchez des données ou des formules en utilisant FindOptions Node.js via C++, Recherche de données ou formules en utilisant FindOptions Node.js via C++, Recherche ou exploration de cellules contenant une valeur ou un nombre spécifique Node.js via C++, Recherche ou exploration de cellules contenant des données spécifiques  
---  

{{% alert color="primary" %}}  
Microsoft Excel permet aux utilisateurs de rechercher des cellules dans une feuille de calcul contenant des données spécifiques.  
{{% /alert %}}  

## **Recherche de cellules contenant des données spécifiées**  

### **Utilisation de Microsoft Excel**  

Microsoft Excel permet aux utilisateurs de rechercher des cellules dans une feuille de calcul contenant des données spécifiques. Si vous sélectionnez **Modifier** dans le menu **Rechercher** dans Microsoft Excel, vous verrez une boîte de dialogue où vous pouvez spécifier la valeur de recherche.  

Ici, nous recherchons la valeur "Oranges". Aspose.Cells permet également aux développeurs de trouver des cellules dans la feuille de calcul contenant des valeurs spécifiées.  

### **Utilisation de Aspose.Cells for Node.js via C++**  

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d’accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit une collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) qui représente toutes les cellules dans la feuille. La collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) offre plusieurs méthodes pour rechercher des cellules dans une feuille contenant des données saisies par l’utilisateur. Certaines de ces méthodes sont abordées ci-dessous en détail.  

{{% alert color="primary" %}}  
Toutes les méthodes de recherche renvoient les références des cellules contenant les données spécifiées à rechercher.  
{{% /alert %}}  

## **Recherche de cellules contenant une formule**  

Les développeurs peuvent trouver une formule spécifique dans la feuille de calcul en appelant la méthode [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Généralement, la méthode [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) accepte trois paramètres :  

- **Objet :** L’objet à rechercher. Le type doit être int, double, DateTime, string, bool.  
- **Cellule précédente :** Cellule précédente contenant le même objet. Ce paramètre peut être défini à null si la recherche commence depuis le début.  
- **Options de recherche :** Options pour rechercher l’objet requis.  

Les exemples ci-dessous utilisent les données de la feuille de calcul pour apprendre les méthodes de recherche.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainFormula.js" >}}


## **Recherche de données ou de formules à l'aide de FindOptions**  

Il est possible de rechercher des valeurs spécifiées en utilisant la méthode [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) avec diverses [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions). Généralement, la méthode [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) accepte les paramètres suivants :  

- **Valeur de recherche**, les données ou la valeur à rechercher.  
- **Cellule précédente**, la dernière cellule qui contient la même valeur. Ce paramètre peut être défini sur null lors de la recherche depuis le début.  
- **Options de recherche**, les options de recherche.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindDataUsingFindOptions.js" >}}


## **Recherche des cellules contenant une valeur de chaîne spécifiée ou un nombre.**  

Il est possible de rechercher des valeurs de chaîne spécifiées en appelant la même méthode [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) trouvée dans la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) avec diverses [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions).  

Spécifiez les propriétés [**FindOptions.setLookInType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookInType-lookintype-) et [**FindOptions.setLookAtType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookAtType-lookattype-). Le code d’exemple suivant montre comment utiliser ces propriétés pour rechercher des cellules avec divers nombres de chaînes au **début**, au **centre** ou à la **fin** de la chaîne de la cellule.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainSpecifyString.js" >}}



## **Sujets avancés**  
- [Rechercher des cellules avec un style spécifique](/cells/fr/nodejs-cpp/find-cells-with-specific-style/)  
- [Trouver si la valeur de la cellule commence par un guillemet simple](/cells/fr/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Rechercher des données en utilisant des valeurs originales](/cells/fr/nodejs-cpp/search-data-using-original-values/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
