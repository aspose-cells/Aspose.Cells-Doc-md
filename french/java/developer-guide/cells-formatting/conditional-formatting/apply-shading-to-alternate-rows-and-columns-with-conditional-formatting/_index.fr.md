---
title: Appliquer un ombrage aux lignes et colonnes alternées avec une mise en forme conditionnelle
type: docs
weight: 10
url: /fr/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}} 

Les API Aspose.Cells offrent les moyens d'ajouter et de manipuler des règles de mise en forme conditionnelle pour l'objet [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Ces règles peuvent être adaptées de plusieurs façons pour obtenir la mise en forme souhaitée en fonction de conditions ou de règles. Cet article démontrera l'utilisation de l'API Aspose.Cells for Java pour appliquer un ombrage aux lignes et colonnes alternées à l'aide de règles de mise en forme conditionnelle et des fonctions intégrées d'Excel.

{{% /alert %}} 
## **Appliquer un ombrage aux lignes et colonnes alternées à l'aide de la mise en forme conditionnelle**
Cet article utilise les fonctions intégrées d'Excel telles que ROW, COLONNE et MOD. Voici quelques détails sur ces fonctions pour une meilleure compréhension du code fourni ci-dessous.

- La fonction **ROW()** retourne le numéro de ligne d'une référence de cellule. Si la référence est omise, elle suppose que la référence est l'adresse de la cellule dans laquelle la fonction ROW a été entrée.
- La fonction **COLUMN()** retourne le numéro de colonne d'une référence de cellule. Si la référence est omise, elle suppose que la référence est l'adresse de la cellule dans laquelle la fonction COLUMN a été entrée.
- La fonction **MOD()** retourne le reste après la division d'un nombre par un diviseur, où le premier paramètre de la fonction est la valeur numérique dont vous souhaitez trouver le reste et le deuxième paramètre est le nombre utilisé pour diviser le paramètre de nombre. Si le diviseur est 0, alors il retournera l'erreur #DIV/0!.

Commençons par écrire un peu de code pour atteindre l'objectif à l'aide de l'API Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



La capture d'écran suivante montre la feuille de calcul résultante chargée dans l'application Excel.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

Pour appliquer l'ombrage aux colonnes alternatives, il vous suffit de changer la formule **=MOD(ROW(),2)=0** en **=MOD(COLUMN(),2)=0**, c'est-à-dire; au lieu d'obtenir l'index de ligne, modifier la formule pour récupérer l'index de colonne. 
La feuille de calcul résultante, dans ce cas, ressemblera à l'image suivante.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
