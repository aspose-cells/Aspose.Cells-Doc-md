---
title: Zoom avant ou arrière sur la feuille de calcul dans GridDesktop
type: docs
weight: 160
url: /fr/net/zooming-in-or-out-on-the-worksheet-in-griddesktop/
---
{{% alert color="primary" %}} 

Parfois, lorsque vous travaillez avec vos données, vous souhaiterez peut-être agrandir le contenu à l'écran sans réellement modifier la taille de la police. Par exemple, vous avez peut-être formaté votre texte pour qu'il utilise une petite police. (Cela est souvent nécessaire pour obtenir toutes vos informations sur une impression.) Cependant, lorsque vous travaillez dans la feuille de calcul, la police est difficile à lire car elle est si petite.

Dans Microsoft Excel, un curseur de zoom est disponible pour zoomer rapidement et facilement sur les documents. Le curseur de zoom se trouve généralement dans le coin inférieur droit de la fenêtre du logiciel.

Aspose.Cells permet également aux développeurs de définir le facteur de zoom de la feuille de calcul, de sorte que le contenu doit apparaître selon la valeur de pourcentage souhaitée.

{{% /alert %}} 
## **Zoom avant ou arrière à l'aide de Aspose.Cells.GridDesktop**
Aspose.Cells fournit la classe Aspose.Cells.GridDesktop.Worksheet qui possède un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour définir le facteur de zoom d'une feuille de calcul, utilisez la propriété Zoom de la classe Worksheet. Le facteur de zoom est défini en affectant une valeur numérique (entier) à la propriété Zoom.

Nous construisons un curseur de zoom de type MS Excel à l'aide du contrôle TrackBar (.NET). Dans un projet WinForm, nous plaçons le contrôle Aspose.Cells.GridDesktop de Toolbox dans le formulaire et spécifions certaines propriétés pour définir son nom, sa taille ou d'autres aspects en conséquence. Maintenant, nous plaçons le contrôle TrackBar dans le coin inférieur droit sous le contrôle GridDesktop, nous mettons également un contrôle Label qui afficherait la valeur en pourcentage que vous spécifiez via la poignée du contrôle TrackBar. Nous ajoutons des lignes de code relatives dans l'événement Scroll de TrackBar, donc lorsque vous faites défiler le contrôle Trackbar, GridDesktop doit effectuer un zoom avant ou arrière pour afficher les données/contenus qu'il contient.

Un exemple complet est donné ci-dessous qui montre comment utiliser la propriété Zoom pour définir le facteur de zoom de la feuille de calcul active de GridDesktop. Nous importons d'abord un modèle de fichier Excel dans GridDesktop.

Écrivez le code ci-dessous dans l'événement Load du formulaire pour définir le modèle de fichier Excel dans GridDesktop et la valeur de la barre de suivi.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


Maintenant, copiez le code ci-dessous dans l'événement de défilement de piste et exécutez l'application. Vous remarquerez que le déplacement de la barre de suivi modifiera la propriété de zoom de la feuille de calcul.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
