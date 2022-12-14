---
title: Rendre les caractères supplémentaires Unicode dans le PDF de sortie par Aspose.Cells
type: docs
weight: 690
url: /fr/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---
{{% alert color="primary" %}} 

Les caractères Unicode normaux ont une longueur de 2 octets tandis que les caractères supplémentaires Unicode ont une longueur de 4 octets. Aspose.Cells prend désormais en charge le rendu de ces caractères Unicode à 4 octets.

Dans la norme de caractères Unicode, les caractères supplémentaires sont les caractères auxquels sont attribués des points de code allant de U+10000 à U+10FFFF. En d'autres termes, ce sont les caractères Unicode supérieurs à U+FFFF.

- En UTF-8, ces caractères font chacun 4 octets.
- En UTF-16, ces caractères nécessitent 2 substituts (unités de 16 bits).

{{% /alert %}} 
## **Rendre les caractères supplémentaires Unicode dans le PDF de sortie par Aspose.Cells**
 La capture d'écran suivante montre comment Aspose.Cells a rendu le[fichier excel source](5473390.xlsx) dans le[PDF de sortie](5473391.pdf)Comme vous pouvez le voir, les trois caractères supplémentaires Unicode ont été rendus exactement de la même manière que par Microsoft Excel.

![tâche : image_autre_texte](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

Vous pouvez utiliser cet exemple de code pour convertir le[fichier excel source](5473390.xlsx) dans[PDF de sortie](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
