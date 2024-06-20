---
title: FAQ
type: docs
weight: 400
url: /fr/net/grid-faq/
---

## **Y a-t-il une limite dans la version d'évaluation des contrôles Aspose.Cells Grid?**
Non, il n'y a aucune limitation des fonctionnalités dans la version d'évaluation de ces contrôles.

La version d'évaluation fournit toutes les fonctionnalités de la version sous licence, sauf qu'elle ajoute une feuille de calcul supplémentaire (contenant **Avertissement de copyright d'évaluation**) aux fichiers de sortie.


## **Il existe de nombreux contrôles de grille disponibles sur le marché. Pourquoi devrais-je acheter les contrôles de grille Aspose.Cells?**
Eh bien, les contrôles de grille Aspose.Cells sont très bien tarifés pour être abordables pour tous les types d'utilisateurs. À un prix très raisonnable,

il vous propose une suite de deux contrôles pour travailler sur les applications Windows et Web. 

De plus, ce n'est pas simplement une grille ordinaire, c'est votre **Visionneuse, éditeur et créateur de feuilles de calcul** en même temps. 

Vous ne pouvez pas seulement le lier à n'importe quel type de source de données (comme les contrôles de grille normaux), mais aussi créer et gérer des fichiers Excel. Il fournit également un **moteur de calcul de formules** puissant et riche pour calculer non seulement des fonctions intégrées (prises en charge par les contrôles de grille Aspose.Cells), mais aussi des formules personnalisées définies par vous. Il y a bien plus de fonctionnalités de la suite de grilles Aspose.Cells qui ne peuvent être listées ici, veuillez vous référer à la page Types d'édition pour une liste plus détaillée des fonctionnalités.

## **J'ai récemment acheté ma licence pour les contrôles de grille Aspose.Cells. Comment puis-je utiliser cette licence dans mon application avec le contrôle de grille Aspose.Cells?**
Veuillez consulter la page [Licence](/cells/fr/net/licensing/) des contrôles de grille Aspose.Cells. 

Il fournit des détails complets sur la manière d'utiliser la licence avec les contrôles de grille Aspose.Cells dans vos applications.



## **Comment puis-je déployer mon projet/solution web basé sur Aspose.Cells.GridWeb sur le serveur ?**
Si vous devez déployer l'application web contenant le contrôle GridWeb, vous copieriez le répertoire "acw_client" dans le dossier de votre projet au moins, votre application web (déployée sur le serveur) ne pourrait pas le trouver.

Vous pouvez toujours spécifier le chemin de script en ajoutant les lignes de code suivantes dans la section de configuration (par exemple dans le fichier web.config de votre projet VS.NET). Le dossier "acw_client" contient des fichiers et Aspose.Cells.GridWeb utilise ce dossier pour gérer sa configuration interne, il contient des scripts, des fichiers d'image et d'autres fichiers pour spécifier le comportement de GridWeb et effectuer d'autres opérations. Le fichier de configuration est utilisé pour empêcher le contrôle d'utiliser les ressources client intégrées (images, scripts, etc.), ce qui est utile dans certains cas/scénarios.

**XML**

{{< highlight csharp >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

Le chemin est toujours lié au répertoire du projet. Vous ne devriez pas utiliser de répertoire qui se trouve en dehors du répertoire du projet. Il est donc nécessaire de copier le répertoire "acw_client" (dans votre dossier d'installation GridWeb) dans le répertoire du projet.

{{% /alert %}} 
## **Exécution de Aspose.Cell.GridWeb dans Internet Explorer**
Actuellement, Aspose.Cells.GridWeb ne prend plus en charge Internet Explorer, c'est un navigateur trop ancien. 
Nous prenons en charge Chrome, Edge, Firefox, Safari, Opera



