---
title: Appliquer un ombrage à d'autres lignes et colonnes avec une mise en forme conditionnelle
type: docs
weight: 10
url: /fr/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}} 

 Aspose.Cells Les API permettent d'ajouter et de manipuler des règles de mise en forme conditionnelle pour[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) objet. Ces règles peuvent être adaptées de plusieurs manières pour obtenir le formatage souhaité en fonction de conditions ou de règles. Cet article démontrera l'utilisation de Aspose.Cells for Java API pour appliquer un ombrage à d'autres lignes et colonnes à l'aide de règles de mise en forme conditionnelle et des fonctions intégrées d'Excel.

{{% /alert %}} 
## **Appliquer l'ombrage aux autres lignes et colonnes à l'aide de la mise en forme conditionnelle**
Cet article utilise les fonctions intégrées d'Excel telles que ROW, COLUMN & MOD. Voici quelques détails sur ces fonctions pour une meilleure compréhension de l'extrait de code fourni à l'avance.

- **LIGNE()** La fonction renvoie le numéro de ligne d'une référence de cellule. Si la référence est omise, il suppose que la référence est l'adresse de cellule dans laquelle la fonction ROW a été entrée.
- **COLONNE()**La fonction renvoie le numéro de colonne d'une référence de cellule. Si la référence est omise, il suppose que la référence est l'adresse de cellule dans laquelle la fonction COLONNE a été entrée.
- **MOD()** La fonction renvoie le reste après qu'un nombre a été divisé par un diviseur, où le premier paramètre de la fonction est la valeur numérique dont vous souhaitez trouver le reste et le deuxième paramètre est le nombre utilisé pour diviser le paramètre nombre. Si le diviseur est 0, alors il renverra le #DIV/0 ! Erreur.

Commençons à écrire du code pour atteindre l'objectif avec l'aide de Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



L'instantané suivant montre la feuille de calcul résultante chargée dans l'application Excel.

![tâche : image_autre_texte](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

 Pour appliquer l'ombrage aux colonnes alternatives, il vous suffit de modifier la formule**=MOD(LIGNE(),2)=0** comme**=MOD(COLONNE(),2)=0** , C'est; au lieu d'obtenir l'index de ligne, modifiez la formule pour récupérer l'index de colonne.
La feuille de calcul résultante, dans ce cas, ressemblera à l'image suivante.

![tâche : image_autre_texte](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
