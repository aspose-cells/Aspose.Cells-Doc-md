---
title: FAQ
type: docs
weight: 400
url: /fr/net/grid-faq/
---
## **Existe-t-il une limitation dans la version d'évaluation de Aspose.Cells Grid Controls ?**
 Non, il n'y a pas de limitation de fonctionnalités dans la version d'évaluation de Aspose.Cells Grid Controls. La version d'évaluation fournit toutes les fonctionnalités de la version sous licence, sauf qu'elle ajoute une feuille de travail supplémentaire (contenant**Avertissement relatif aux droits d'auteur** ) aux fichiers de sortie.
## **Il y a tellement de contrôles Grid disponibles sur le marché. Pourquoi devrais-je acheter Aspose.Cells Grid Controls ?**
 Eh bien, les commandes de grille Aspose.Cells sont très abordables pour être abordables pour tous les types d'utilisateurs. À un prix très raisonnable, il vous fournit une suite de deux contrôles pour travailler sur les applications Windows et Web. De plus, ce n'est pas qu'une simple Grille, c'est votre**Visionneuse, éditeur et créateur de feuilles de calcul** à la fois. Vous pouvez non seulement le lier à n'importe quel type de source de données (comme les contrôles de grille normaux), mais également créer et gérer des fichiers Excel. Il fournit également un fort et riche**Moteur de calcul de formule** pour calculer non seulement les fonctions intégrées (prises en charge par Aspose.Cells Grid Controls) mais également les formules personnalisées que vous avez définies. Il y a beaucoup plus de fonctionnalités de la suite Grid Aspose.Cells qui ne peuvent pas être couvertes ici, veuillez vous référer à la page Types d'édition pour une liste de fonctionnalités plus détaillée.
## **J'ai récemment acheté ma licence pour Aspose.Cells Grid Controls. Comment puis-je utiliser cette licence dans mon application avec Aspose.Cells Grid Control ?**
Veuillez vous référer au[Licence](/cells/fr/net/licensing/) page des commandes de grille Aspose.Cells. Il fournit des détails complets sur l'utilisation de la licence avec Aspose.Cells Grid Controls dans vos applications.
## **Les contrôles de grille Aspose.Cells sont-ils pris en charge sur Visual Studio.NET 2005 ?**
Oui, les contrôles de grille Aspose.Cells sont entièrement pris en charge sur Visual Studio.NET 2005 et les versions ultérieures.
## **J'utilise le contrôle Aspose.Cells.GridWeb sur mon site Web à l'aide de Visual Studio.NET 2005. Mais cela ne fonctionne pas du tout. Quel est le problème?**
 Aspose.Cells.GridWeb prend en charge les deux**Système de fichiers** et**HTTP** modes de Visual Studio.NET 2005. Si vous êtes toujours confus, veuillez consulter un guide étape par étape pour Travailler avec Aspose.Cells.GridWeb à l'aide de Visual Studio.NET 2005.
## **Comment puis-je déployer mon projet/solution Web basé sur Aspose.Cells.GridWeb sur le serveur ?**
Si vous avez besoin de déployer l'application Web ayant le contrôle GridWeb, vous devez copier le "acw_client" dans votre dossier de projet, à moins que votre application Web (déployée sur le serveur) ne puisse le trouver. Vous pouvez toujours spécifier le chemin de script en ajoutant les lignes de code suivantes dans la section de configuration (par exemple, dans le fichier web.config de votre projet VS.NET)._client" est un dossier qui contient des fichiers et Aspose.Cells. GridWeb utilise ce dossier pour gérer sa configuration interne, il contient des fichiers de scripts, des fichiers image et d'autres fichiers pour spécifier le comportement de GridWeb et définir d'autres opérations. Le fichier de configuration est utilisé pour empêcher le contrôle de en utilisant les ressources client embarquées (images, scripts, etc.) ce qui est utile dans certains cas/scénarios.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

Le chemin est toujours lié au répertoire du projet. Vous ne devez pas utiliser de répertoire en dehors du répertoire du projet. Il faut donc copier le répertoire "acw_client" (@ votre dossier d'installation de GridWeb) dans le répertoire du projet.

{{% /alert %}} 
## **Exécution de Aspose.Cell.GridWeb dans Internet Explorer 10 ou 11**
 Actuellement, Aspose.Cells.GridWeb ne fonctionne pas très bien sur Internet Explorer 10 ou 11, vous devez donc utiliser le mode de compatibilité d'IE8/9 pour travailler avec le type de navigateur IE10/11. Vous devez ajouter la ligne suivante de**<méta>** balise dans la section d'en-tête dans**.aspx** page:



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-FAQ-RunGridWebInIE-RunGridWebIE.aspx" >}}

