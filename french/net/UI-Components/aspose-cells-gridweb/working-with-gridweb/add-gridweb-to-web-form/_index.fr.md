---
title: Ajoutez GridWeb au formulaire Web
type: docs
weight: 10
url: /fr/net/aspose-cells-gridweb/add-gridweb-to-web-form/
keywords: GridWeb,webform,form
description: Cet article présente comment travailler avec un formulaire web dans GridWeb.
---

{{% alert color="primary" %}} 

Ce sujet fournit un guide étape par étape de base pour les débutants afin de les aider à créer et utiliser le contrôle Aspose.Cells.GridWeb dans les applications web.

{{% /alert %}} 
## **Créer et utiliser le contrôle Aspose.Cells.GridWeb**
### **Étape 1: Créer un projet d'application web**
Tout d'abord, créez un projet d'application web dans lequel utiliser le contrôle Aspose.Cells.GridWeb:

1. Ouvrez Visual Studio.
1. Dans le menu **Fichier**, sélectionnez **Nouveau** suivi de **Projet**. 

![todo:image_alt_text](add-gridweb-to-web-form_1.png)



Une boîte de dialogue Nouveau projet apparaît.

1. Sélectionnez **Application web ASP.NET** pour le langage souhaité. 

![todo:image_alt_text](add-gridweb-to-web-form_2.png)

1. Sélectionnez le modèle **Formulaires Web**. 

![todo:image_alt_text](add-gridweb-to-web-form_3.png)

1. Ajoutez un nouveau formulaire web au projet.
### **Étape 2: Intégrer le contrôle dans le formulaire web**
Faites glisser et déposez le contrôle Aspose.Cells.GridWeb depuis la boîte à outils Visual Studio vers le formulaire web. 

![todo:image_alt_text](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

Pour savoir comment ajouter les contrôles Aspose.Cells Grid à la Boîte à outils Visual Studio, veuillez lire [Intégrer les contrôles Aspose.Cells.Grid avec Visual Studio.NET](/cells/fr/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/).

{{% /alert %}} 

Lorsque le contrôle a été ajouté au formulaire, il est rendu comme ceci: 

![todo:image_alt_text](add-gridweb-to-web-form_5.png)
### **Étape 3: Redimensionner le contrôle**
Le formulaire est rendu à une taille par défaut. Ajustez la taille en faisant glisser les bords ou les coins. 

![todo:image_alt_text](add-gridweb-to-web-form_6.png)
### **Étape 4: Définir les propriétés du contrôle**
Le contrôle Aspose.Cells.GridWeb peut également être configuré en utilisant diverses propriétés. 

![todo:image_alt_text](add-gridweb-to-web-form_7.png)

Il est possible d'ajuster de nombreuses propriétés de la commande avec la boîte de dialogue Propriétés. Les propriétés de base comprennent la hauteur, la largeur, la couleur et les styles visuels. Les propriétés avancées incluent le mode d'édition, le mode de session et le mode double-clic. De plus, il est possible de définir des gestionnaires d'événements personnalisés dans la boîte de dialogue Propriétés.

Il existe également quelques outils de configuration supplémentaires pour Aspose.Cells.GridWeb qui peuvent être vus en bas de la boîte de dialogue Propriétés sous forme d'hyperliens, ou en cliquant avec le bouton droit sur la commande GridWeb pour les trouver. Ces outils de configuration comprennent :

- Boutons de commande personnalisés
#### **Boutons de commande personnalisés**
Pour ouvrir l'éditeur de boutons de commande personnalisés :
Cliquez avec le bouton droit sur la commande GridWeb et sélectionnez **Boutons de commande personnalisés**. 

![todo:image_alt_text](add-gridweb-to-web-form_8.png)



La boîte de dialogue de l'éditeur de boutons de commande personnalisés s'affiche. 

![todo:image_alt_text](add-gridweb-to-web-form_9.png)

La boîte de dialogue permet aux développeurs d'ajouter et de supprimer des boutons de commande personnalisés dans la commande GridWeb.


### **Important**
Aspose.Cells.GridWeb fournit également ses fichiers de ressources avec la commande. Le dossier "acw_client" est un dossier (@ votre répertoire d'installation) qui contient des fichiers et Aspose.Cells.GridWeb utilise ce dossier pour gérer sa configuration interne et autres fonctionnalités. Il contient des fichiers de scripts, des fichiers image et d'autres fichiers pour spécifier le comportement de GridWeb et effectuer d'autres opérations. Le fichier de configuration est utilisé pour gérer les ressources clients intégrées (images, scripts, etc.). De plus, lorsque vous devez déployer l'application web comportant la commande GridWeb, vous devriez également copier le répertoire "acw_client" dans votre projet au moins votre application web (déployée sur le serveur) ne pourrait pas le trouver. Vous pouvez toujours spécifier le dossier de ressources en ajoutant les lignes de code suivantes dans la section de configuration (par exemple dans le fichier web.config de votre projet VS.NET) :



|<p>{{< highlight java >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
| :- |


{{% alert color="primary" %}}

Le chemin est toujours lié au répertoire du projet. Vous ne devriez pas utiliser de répertoire qui se trouve à l'extérieur du répertoire du projet. Il est donc nécessaire de copier le répertoire "acw_client" (@ votre répertoire d'installation GridWeb) dans le répertoire/sous-répertoire du projet.

{{% /alert %}}
### **Étape 5 : Exécution de l'application web**
Exécutez l'application en appuyant sur Ctrl+F5 ou en cliquant sur le bouton **Démarrer**. 

Lorsque l'application s'exécute dans un navigateur, la page WebForm1.aspx s'affiche, contenant maintenant une commande Aspose.Cells.GridWeb vide. Ajoutez des valeurs aux cellules en cliquant dessus. Il est également possible d'effectuer d'autres tâches comme changer la hauteur d'une ligne ou la largeur d'une colonne, copier (Ctrl+C) ou couper (Ctrl+X) des données de cellule dans le presse-papiers et coller (Ctrl+V) des données dans une cellule. Pour effectuer plus d'opérations, cliquez avec le bouton droit sur la commande pour voir la liste complète des options. 

**Menu contextuel de la commande GridWeb** 

![todo:image_alt_text](add-gridweb-to-web-form_10.png)
