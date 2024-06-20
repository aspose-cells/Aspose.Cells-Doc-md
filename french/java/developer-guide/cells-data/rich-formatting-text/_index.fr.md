---
title: Accéder et mettre à jour les parties du texte enrichi de la cellule
linktitle: Texte enrichi avec formatage
type: docs
weight: 440
url: /fr/java/access-and-update-the-portions-of-rich-text-of-cell/
---

{{% alert color="primary" %}} 

Aspose.Cells vous permet d'accéder et de mettre à jour les portions de texte enrichi de la cellule. À cette fin, vous pouvez utiliser les méthodes Cell.getCharacters() et Cell.setCharacters(). Ces méthodes retourneront et accepteront un tableau d'objets FontSetting que vous pouvez utiliser pour accéder et mettre à jour diverses propriétés de police telles que le nom de la police, la couleur de la police, la graisse, etc.

{{% /alert %}} 
## **Accéder et mettre à jour les parties du texte enrichi de la cellule**
Le code suivant démontre l'utilisation des méthodes Cell.getCharacters() et Cell.setCharacters() en utilisant le [fichier Excel source](5472937.xlsx) que vous pouvez télécharger à partir du lien fourni. Le fichier Excel source contient un texte enrichi dans la cellule A1. Il a 3 portions et chaque portion a une police différente. Nous accéderons à ces portions et mettrons à jour la première portion avec un nouveau nom de police. Enfin, il enregistre le classeur sous le nom de [fichier Excel de sortie](5472930.xlsx). Lorsque vous l'ouvrirez, vous constaterez que la police de la première portion du texte a changé en **"Arial"**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **Sortie console**
Voici la sortie console du code d'exemple ci-dessus en utilisant le [fichier Excel source](5472937.xlsx).

{{< highlight java >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
