---  
title: Obtenez tous les indices des lignes masquées après le rafraîchissement de l AutoFilter 
type: docs  
weight: 320  
url: /fr/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Apprenez à obtenir tous les indices de lignes masquées après avoir rafraîchi le filtre automatique en utilisant l API Aspose.Cells for Node.js via C++.  
keywords: Obtenir tous les indices de lignes masquées après le rafraîchissement du filtre automatique Node.js via C++, Obtenir tous les indices de lignes masquées après le rafraîchissement du filtre automatique Node.js via C++, Récupérer tous les indices de lignes masquées après le rafraîchissement du filtre automatique Node.js via C++  
---  

## **Scénarios d'utilisation possibles**  

Lorsque vous appliquez le filtre automatique sur les cellules de la feuille de calcul, certaines lignes sont automatiquement masquées. Mais il se peut que certaines lignes soient déjà masquées manuellement par l'utilisateur Excel et ne soient pas masquées par un filtre automatique. Il est donc difficile de savoir quelles lignes sont masquées par le filtre automatique et lesquelles sont masquées manuellement par l'utilisateur Excel. Aspose.Cells for Node.js via C++ traite ce problème en utilisant le tableau [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-). Cette méthode renvoie les indices des lignes qui sont masquées par le filtre automatique et pas manuellement par l'utilisateur Excel.  

## **Obtenir tous les indices des lignes masquées après le rafraîchissement de l'Autofiltre**  

Veuillez voir le code exemple suivant qui charge le fichier Excel [exemple](64716909.xlsx) contenant certaines lignes masquées manuellement par l'utilisateur Excel. Le code applique le filtre automatique et le rafraîchit en utilisant la méthode [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-) qui retourne les indices des lignes masquées par le filtre automatique. Il affiche ensuite les indices des lignes masquées sur la console avec les noms et valeurs des cellules.  

## **Code d'exemple**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.js" >}}


## **Sortie console**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
