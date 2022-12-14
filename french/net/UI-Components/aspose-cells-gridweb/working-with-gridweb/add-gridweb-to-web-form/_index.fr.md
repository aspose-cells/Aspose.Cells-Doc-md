---
title: Ajouter GridWeb au formulaire Web
type: docs
weight: 10
url: /fr/net/add-gridweb-to-web-form/
---
{{% alert color="primary" %}} 

Cette rubrique fournit un guide étape par étape de base pour les débutants afin de les aider à créer et à utiliser le contrôle Aspose.Cells.GridWeb dans les applications Web.

{{% /alert %}} 
## **Création et utilisation de Aspose.Cells.GridWeb Control**
### **Étape 1 : Création d'un projet d'application Web**
Commencez par créer un projet d'application Web dans lequel utiliser le contrôle Aspose.Cells.GridWeb :

1. Ouvrez Visual Studio.
1.  Du**Dossier** menu, sélectionnez**Nouveau** suivie par**Projet**. 

![tâche : image_autre_texte](add-gridweb-to-web-form_1.png)



Une boîte de dialogue Nouveau projet apparaît.

1.  Sélectionner**Application Web ASP.NET** pour la langue souhaitée.

![tâche : image_autre_texte](add-gridweb-to-web-form_2.png)

1.  Sélectionner**Formulaires Web** modèle.

![tâche : image_autre_texte](add-gridweb-to-web-form_3.png)

1. Ajoutez un nouveau formulaire Web au projet.
### **Étape 2 : Intégrer le contrôle au formulaire Web**
 Faites glisser et déposez le contrôle Aspose.Cells.GridWeb de la boîte à outils Visual Studio vers le formulaire Web.

![tâche : image_autre_texte](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

 Pour savoir comment ajouter des contrôles de grille Aspose.Cells à la boîte à outils Visual Studio, veuillez lire[Intégrer Aspose.Cells.Grid Controls avec Visual Studio.NET](/cells/fr/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/).

{{% /alert %}} 

 Lorsque le contrôle a été ajouté au formulaire, il est rendu comme ceci :

![tâche : image_autre_texte](add-gridweb-to-web-form_5.png)
### **Étape 3 : Contrôle de redimensionnement**
Le formulaire est rendu à une taille par défaut. Ajustez la taille en faisant glisser les bordures ou les coins.

![tâche : image_autre_texte](add-gridweb-to-web-form_6.png)
### **Étape 4 : Définition des propriétés de contrôle**
 Le contrôle Aspose.Cells.GridWeb peut également être configuré à l'aide de diverses propriétés.

![tâche : image_autre_texte](add-gridweb-to-web-form_7.png)

Il est possible d'ajuster de nombreuses propriétés du contrôle avec la boîte de dialogue Propriétés. Les propriétés de base incluent la hauteur, la largeur, la couleur et les styles visuels. Les propriétés avancées incluent le mode édition, le mode session et le mode double-clic. De plus, il est possible de définir des gestionnaires d'événements personnalisés dans la boîte de dialogue Propriétés.

Il existe également des outils de configuration supplémentaires pour Aspose.Cells.GridWeb qui peuvent être vus au bas de la boîte de dialogue Propriétés sous forme d'hyperliens, ou faites un clic droit sur le contrôle GridWeb pour les trouver. Ces outils de configuration comprennent :

- Boutons de commande personnalisés
#### **Boutons de commande personnalisés**
Pour ouvrir l'éditeur de boutons de commande personnalisés :
 Cliquez avec le bouton droit sur le contrôle GridWeb et sélectionnez**Boutons de commande personnalisés**. 

![tâche : image_autre_texte](add-gridweb-to-web-form_8.png)



 La boîte de dialogue Éditeur de collection CustomCommandButton s'affiche.

![tâche : image_autre_texte](add-gridweb-to-web-form_9.png)

La boîte de dialogue permet aux développeurs d'ajouter et de supprimer des boutons de commande personnalisés dans le contrôle GridWeb.


### **Important**
Aspose.Cells.GridWeb fournit également ses fichiers de ressources avec le contrôle. Le "acw_client" est un dossier (@ votre répertoire d'installation) qui contient des fichiers et Aspose.Cells.GridWeb utilise ce dossier pour gérer sa configuration interne et d'autres fonctionnalités, il contient des fichiers de scripts, des fichiers image et d'autres fichiers pour spécifier le comportement de GridWeb et définir d'autres opérations. Le config est utilisé pour gérer les ressources client embarquées (images, scripts, etc.) De plus, lorsque vous avez besoin de déployer l'application Web ayant le contrôle GridWeb, vous devez également copier le fichier "acw_client" dans votre dossier de projet, à moins que votre application Web (déployée sur le serveur) ne puisse le trouver. Vous pouvez toujours spécifier le dossier de ressources en ajoutant les lignes de code suivantes dans la section de configuration (par exemple, dans le fichier web.config de votre Projet VS.NET):



|<p>{{< highlight "java" >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
|:- |


{{% alert color="primary" %}}

Le chemin est toujours lié au répertoire du projet. Vous ne devez pas utiliser de répertoire en dehors du répertoire du projet. Il faut donc copier le répertoire "acw_client" (@ votre dossier d'installation de GridWeb) dans le répertoire/sous-répertoire du projet.

{{% /alert %}}
### **Étape 5 : Exécution de l'application Web**
 Exécutez l'application en appuyant sur Ctrl+F5 ou en cliquant sur le**Commencer** bouton.

 Lorsque l'application s'exécute dans un navigateur, la page WebForm1.aspx s'affiche, contenant désormais un contrôle Aspose.Cells.GridWeb vide. Ajoutez des valeurs aux cellules en cliquant dessus. Il est également possible d'effectuer d'autres tâches comme modifier la hauteur d'une ligne ou la largeur d'une colonne, copier (Ctrl+C) ou couper (Ctrl+X) des données de cellule dans le presse-papiers et coller (Ctrl+V) des données dans la cellule . Pour effectuer plus d'opérations, cliquez avec le bouton droit sur le contrôle pour voir la liste complète des options.

**Menu contextuel du champ GridWeb** 

![tâche : image_autre_texte](add-gridweb-to-web-form_10.png)
