---
title: Comment mettre une feuille de calcul à l échelle
type: docs
weight: 130
url: /fr/net/how-to-scale-a-worksheet/
description: Cet article vous montre un code expliquant comment mettre une feuille de calcul à l échelle en utilisant la bibliothèque Aspose.Cells.
keywords: C# mettre une feuille de calcul à l échelle, Comment mettre une feuille de calcul à l échelle en utilisant C#, Mettre une feuille de calcul à l échelle en C#.
---

## **Scénarios d'utilisation possibles**
Mettre une feuille de calcul à l'échelle peut être utile pour diverses raisons, selon le contexte dans lequel vous travaillez. Voici quelques raisons courantes de mettre une feuille de calcul à l'échelle :
1. Adapter à la page : Pour que tout le contenu tienne sur une seule page ou un nombre spécifique de pages lors de l'impression, facilitant ainsi la lecture et la gestion sans avoir à feuilleter plusieurs pages.

1. Présentation : Pour rendre la feuille de calcul plus organisée et professionnelle, particulièrement lors de sa diffusion à d'autres lors de réunions ou rapports.

1. Lisibilité : Pour ajuster la taille du texte et des autres éléments pour une meilleure lisibilité, en particulier pour les personnes qui pourraient avoir du mal à lire des polices plus petites.

1. Gestion de l'espace : Pour optimiser l'utilisation de l'espace sur une feuille de calcul, garantissant ainsi qu'il n'y a pas d'espaces blancs inutiles et que toutes les informations importantes sont visibles sans devoir faire défiler excessivement.

1. Visualisation des données : Dans le cas des graphiques, mettre à l'échelle peut aider à les rendre plus compréhensibles en ajustant la taille pour s'adapter à l'espace disponible de manière appropriée.

1. Cohérence : Pour maintenir une apparence et une sensation cohérentes sur plusieurs feuilles de calcul ou documents, ce qui est particulièrement important dans des environnements professionnels et éducatifs.

## **Comment mettre une feuille de calcul à l'échelle dans Excel**
Mettre une feuille de calcul à l'échelle dans Excel peut vous aider à adapter votre contenu sur une seule page ou un nombre spécifié de pages lors de l'impression. Voici les étapes pour mettre une feuille de calcul à l'échelle :

1. Ouvrez votre feuille de calcul : Ouvrez la feuille de calcul Excel que vous souhaitez mettre à l'échelle.

1. Accédez à l'onglet Mise en page : Cliquez sur l'onglet Mise en page dans le Ruban.

1. Groupe Mise à l'échelle : Dans l'onglet Mise en page, trouvez le groupe Mise à l'échelle. Vous avez ici des options pour ajuster l'échelle. Largeur : Cette option vous permet de spécifier combien de pages de large la feuille de calcul imprimée sera. Hauteur : Cette option vous permet de spécifier combien de pages de hauteur la feuille de calcul imprimée sera. Échelle : Vous pouvez également définir un pourcentage d'échelle personnalisé ici.
<br>
<img src="1.png" width=60% />

1. Ajustez la largeur et la hauteur : Définissez la largeur et la hauteur sur le nombre de pages souhaité. Par exemple, définissez les deux sur 1 page si vous voulez que la feuille de calcul tienne sur une seule page.

1. Ajustez le pourcentage d'échelle (si nécessaire) : Si vous préférez définir un pourcentage d'échelle spécifique, ajustez la boîte Échelle. Par exemple, le définir à 50% rendra tout à moitié plus petit.


## **Comment mettre à l'échelle une feuille de calcul en utilisant C#**
Aspose.Cells est une bibliothèque puissante pour travailler avec des fichiers Excel de manière programmable. Pour mettre à l'échelle une feuille de calcul en utilisant Aspose.Cells, vous devez suivre ces étapes : charger le [fichier d'exemple](sample.xlsx) et ajuster les paramètres d'impression pour que le contenu s'adapte au nombre de pages souhaité ou à un pourcentage spécifique de la taille originale.

### **Exemple : Ajuster à la page**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-fit-to-page.cs" >}}
<br>
<img src="3.png" width=60% />

### **Exemple : Mettre à l'échelle en pourcentage**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-scale-to-percentage.cs" >}}
<br>
<img src="2.png" width=60% />
