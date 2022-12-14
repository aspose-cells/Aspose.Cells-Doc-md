---
title: Accéder et mettre à jour les portions de texte enrichi de Cell
linktitle: Texte de mise en forme enrichi
type: docs
weight: 440
url: /fr/java/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}} 

Aspose.Cells vous permet d'accéder et de mettre à jour les parties du texte enrichi de la cellule. Pour cela, vous pouvez utiliser les méthodes Cell.getCharacters() et Cell.setCharacters(). Ces méthodes renverront et accepteront le tableau d'objets FontSetting que vous pouvez utiliser pour accéder et mettre à jour diverses propriétés de police telles que le nom de la police, la couleur de la police, l'audace, etc.

{{% /alert %}} 
## **Accéder et mettre à jour les portions de texte enrichi de Cell**
 Le code suivant illustre l'utilisation des méthodes Cell.getCharacters() et Cell.setCharacters() à l'aide de la méthode[fichier excel source](5472937.xlsx) que vous pouvez télécharger à partir du lien fourni. Le fichier Excel source contient un texte enrichi dans la cellule A1. Il comporte 3 parties et chaque partie a une police différente. Nous allons accéder à ces parties et mettre à jour la première partie avec le nouveau nom de police. Enfin, il enregistre le classeur sous[fichier excel de sortie](5472930.xlsx) . Lorsque vous l'ouvrirez, vous constaterez que la police de la première partie du texte a changé pour**"Ariel"**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **Sortie console**
 Voici la sortie de la console de l'exemple de code ci-dessus en utilisant le[fichier excel source](5472937.xlsx).

{{< highlight "java" >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
