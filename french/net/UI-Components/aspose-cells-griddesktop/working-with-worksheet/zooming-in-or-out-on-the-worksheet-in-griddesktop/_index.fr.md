---
title: Zoom avant ou arrière sur la feuille de calcul dans GridDesktop
type: docs
weight: 160
url: /fr/net/aspose-cells-griddesktop/zoom-in-or-out-on-the-worksheet-in-griddesktop/
keywords: GridDesktop, zoom, zoom avant, zoom arrière
description: Cet article présente comment zoomer avant ou arrière dans GridDesktop.
---

{{% alert color="primary" %}} 

Parfois, lorsque vous travaillez avec vos données, vous pouvez souhaiter agrandir le contenu à l'écran sans changer réellement la taille de la police. Par exemple, vous avez peut-être formaté votre texte pour qu'il utilise une petite police. (Cela est souvent nécessaire pour obtenir toutes vos informations sur une impression.) Cependant, lors du travail dans la feuille de calcul, la police est difficile à lire car elle est si petite.

Dans Microsoft Excel, un curseur de zoom est disponible pour zoomer avant et arrière dans les documents rapidement et facilement. Le curseur de zoom est généralement dans le coin inférieur droit de la fenêtre du logiciel.

Aspose.Cells permet également aux développeurs de définir le facteur de zoom de la feuille de calcul, de sorte que le contenu doit apparaître selon la valeur de pourcentage souhaitée.

{{% /alert %}} 
## **Zoomer avant ou arrière en utilisant Aspose.Cells.GridDesktop**
Aspose.Cells fournit la classe Aspose.Cells.GridDesktop.Worksheet qui possède un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour définir le facteur de zoom d'une feuille de calcul, utilisez la propriété Zoom de la classe Worksheet. Le facteur de zoom est défini en attribuant une valeur numérique (entière) à la propriété Zoom.

Nous créons un curseur de zoom similaire à MS Excel en utilisant le contrôle TrackBar (.NET). Dans un projet WinForm, nous plaçons le contrôle Aspose.Cells.GridDesktop depuis la boîte à outils sur le formulaire et spécifions certaines propriétés pour définir son nom, sa taille ou d'autres aspects en conséquence. Maintenant, nous plaçons le contrôle TrackBar dans le coin inférieur droit en dessous du contrôle GridDesktop, nous plaçons également un contrôle Label qui affichera la valeur en pourcentage que vous spécifiez via le contrôle TrackBar. Nous ajoutons des lignes de code relatives à l'événement de défilement du TrackBar, donc lorsque vous faites défiler le contrôle TrackBar, GridDesktop devrait zoomer avant ou arrière pour afficher les données/contenus qui s'y trouvent.

Un exemple complet est donné ci-dessous qui démontre comment utiliser la propriété Zoom pour définir le facteur de zoom de la feuille de calcul active de GridDesktop. Nous importons d'abord un fichier Excel modèle dans GridDesktop.

Écrivez le code ci-dessous dans l'événement Load du formulaire pour définir le fichier Excel modèle dans GridDesktop et la valeur de la trackbar.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


Maintenant, copiez le code ci-dessous à l'intérieur de l'événement de défilement de la piste et exécutez l'application. Vous remarquerez que le déplacement de la piste de défilement modifiera la propriété de zoom de la feuille de calcul.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
