---
title: Travailler avec Visual Studio
type: docs
weight: 20
url: /fr/net/aspose-cells-gridweb/work-with-visual-studio/
keywords: GridWeb,visualstudio
description: Cet article présente comment utiliser GridWeb dans Visual Studio.
---

{{% alert color="primary" %}} 

Ce sujet explique comment utiliser Aspose.Cells.GridWeb dans les applications ASP.NET à l'aide de Visual Studio.NET 2005. Ce sujet est utile pour les développeurs débutants travaillant avec Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Travailler avec Aspose.Cells.GridWeb en utilisant Visual Studio 2013**
Ce sujet montre comment utiliser Aspose.Cells.GridWeb en créant un site web exemple dans Visual Studio 2013. Le processus a été divisé en étapes.
### **Étape 1 : Création d'un nouveau site web**
1. Ouvrez Visual Studio 2013.
1. Dans le menu **Fichier**, sélectionnez **Nouveau menu**, puis **Site Web**. 

![todo:image_alt_text](working-with-visual-studio_1.png)


La boîte de dialogue Nouveau site Web s'ouvre. 

1. Sélectionnez **Site Web ASP.NET Web Forms** dans les modèles installés de Visual Studio.
1. Choisissez le mode HTTP pour l'emplacement du site web. 

![todo:image_alt_text](working-with-visual-studio_2.png)




1. Spécifiez un emplacement où les fichiers du site web seront créés et stockés. 
   1. Cliquez sur **Parcourir** dans la boîte de dialogue Nouveau site Web. 

![todo:image_alt_text](working-with-visual-studio_3.png)



La boîte de dialogue Choisir l'emplacement est affichée. 

1. Cliquez sur l'onglet **Local IIS**.
   Tous les dossiers et applications web stockés dans votre dossier racine IIS sont affichés (par exemple: C:\Inetpub\wwwroot). 

![todo:image_alt_text](working-with-visual-studio_4.png)




1. Créez maintenant une nouvelle application web dans votre IIS local où les fichiers du site web seront stockés.
   La boîte de dialogue Choisir l'emplacement vous permet de créer et de supprimer des applications web ou des répertoires virtuels dans votre IIS local. Pour créer une application web, cliquez sur un bouton comme indiqué ci-dessous dans la figure. 

![todo:image_alt_text](working-with-visual-studio_5.png)



Une nouvelle application web avec le nom par défaut WebSite est créée. 

1. Renommez l'application web. Nous l'avons renommée en GridWebOn2013.
1. Cliquez sur **Ouvrir**. 

![todo:image_alt_text](working-with-visual-studio_6.png)



You return to the New Web Site dialog. The path of web site location is set to <http://localhost/GridWebOn2013>. 

1. Cliquez sur **OK** pour permettre à Visual Studio de créer un site web. 

![todo:image_alt_text](working-with-visual-studio_7.png)
### **Étape 2: Vérification des modes Source & Design d'une page web**
Un site web par défaut aura été créé par Visual Studio 2013. Il contient une page web default.aspx avec du texte bidon et du balisage. 

**Vue source de la page default.aspx** 

![todo:image_alt_text](working-with-visual-studio_8.png)



Toutes les pages web (y compris ASP.NET) peuvent être ouvertes en deux modes. Le premier est la vue source qui permet aux développeurs d'accéder et de modifier le code source. Le deuxième mode est la vue design qui peut être utilisée pour concevoir des pages web de manière WYSIWYG. La capture d'écran ci-dessus montre une vue source de la page web default.aspx. Pour afficher la vue design, cliquez sur **Design**. 

**Vue design de la page default.aspx** 

![todo:image_alt_text](working-with-visual-studio_9.png)




Supprimez la page Default.aspx ajoutée par Visual Studio et ajoutez une nouvelle page Default.aspx vierge.

![todo:image_alt_text](working-with-visual-studio_10.png)
### **Étape 3 : Ajout de Aspose.Cells.GridWeb à la page Web**
Vous pouvez simplement ajouter le contrôle Aspose.Cells.GridWeb (ou GridWeb) à une page Web en le faisant glisser depuis la boîte à outils. 

![todo:image_alt_text](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

Si vous ne savez pas comment ajouter Aspose.Cells.GridWeb à la boîte à outils, consultez [Intégrer les contrôles de grille Aspose.Cells avec Visual Studio.NET](/cells/fr/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

Une fois que le contrôle GridWeb est déposé sur la page Web, il s'affichera comme ceci : 

![todo:image_alt_text](working-with-visual-studio_12.png)



### **Step 4: Change the <!DOCTYPE> tag**
1. Switch to source view and find the following **<!DOCTYPE>** tag in the source code: 

**ASP.NET**

{{< highlight csharp >}}



<!DOCTYPE html>



{{< /highlight >}}

1. Sélectionnez la balise complète. 

![todo:image_alt_text](working-with-visual-studio_13.png)




1. Retain, change or delete the <!DOCTYPE> tag.
1. Or modify the <!DOCTYPE> tag with the following one: 

{{< highlight csharp >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **Étape 5 : Redimensionner le contrôle Aspose.Cells.GridWeb**
Vous pouvez changer la largeur et la hauteur du contrôle GridWeb après l'avoir glissé sur le site Web. 

En mode design, vous pouvez redimensionner la largeur et la hauteur du GridWeb. 

![todo:image_alt_text](working-with-visual-studio_14.png)



### **Étape 6 : Configurer les propriétés de Aspose.Cells.GridWeb**
Configurez les propriétés de Aspose.Cells.GridWeb en WYSIWYG en cliquant sur le bouton **Propriétés** sur le côté droit de l'IDE Visual Studio 2013. 
Une boîte de dialogue de propriétés s'affiche. 

![todo:image_alt_text](working-with-visual-studio_15.png)



Le volet des propriétés permet de configurer l'apparence du GridWeb et d'autres propriétés pour contrôler le comportement du GridWeb.
### **Étape 7 : Exécuter votre premier site Web contenant Aspose.Cells.GridWeb**
Construisez et exécutez le site Web. 

1. Exécutez le site Web directement depuis Visual Studio en appuyant sur Ctrl+F5 ou en cliquant sur **Démarrer le débogage**. 

![todo:image_alt_text](working-with-visual-studio_16.png)

Maintenant, vous pouvez commencer à utiliser le contrôle GridWeb. 

**Le contrôle GridWeb en action** 

![todo:image_alt_text](working-with-visual-studio_17.png)
