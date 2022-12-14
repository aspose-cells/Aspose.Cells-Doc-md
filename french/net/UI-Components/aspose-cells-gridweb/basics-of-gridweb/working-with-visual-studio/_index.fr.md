---
title: Travailler avec Visual Studio
type: docs
weight: 20
url: /fr/net/working-with-visual-studio/
---
{{% alert color="primary" %}} 

Cette rubrique explique comment utiliser Aspose.Cells.GridWeb dans les applications ASP.NET à l'aide de Visual Studio.NET 2005. Cette rubrique est utile pour les développeurs de niveau débutant qui travaillent avec Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Utilisation de Aspose.Cells.GridWeb à l'aide de Visual Studio 2013**
Cette rubrique montre comment utiliser Aspose.Cells.GridWeb en créant un exemple de site Web dans Visual Studio 2013. Le processus a été divisé en étapes.
### **Étape 1 : Création d'un nouveau site Web**
1. Ouvrez Visual Studio 2013.
1.  Du**Dossier** menu, sélectionnez**Nouveau menu** , alors**Site Internet**. 

![tâche : image_autre_texte](working-with-visual-studio_1.png)


 La boîte de dialogue Nouveau site Web s'ouvre.

1.  Sélectionner**ASP.NET Site de formulaires Web** à partir des modèles installés par Visual Studio.
1.  Choisissez le mode HTTP pour l'emplacement du site Web.

![tâche : image_autre_texte](working-with-visual-studio_2.png)




1.  Spécifiez un emplacement où les fichiers du site Web seront créés et stockés.
 1. Cliquez sur**Parcourir** dans la boîte de dialogue Nouveau site Web.

![tâche : image_autre_texte](working-with-visual-studio_3.png)



 La boîte de dialogue Choisir un emplacement s'affiche.

1.  Clique le**IIS local** languette.
Tous les dossiers et applications Web stockés dans votre dossier racine IIS sont affichés (par exemple : C:\Inetpub\wwwroot).

![tâche : image_autre_texte](working-with-visual-studio_4.png)




1. Créez maintenant une nouvelle application Web dans votre IIS local où les fichiers du site Web seront stockés.
 La boîte de dialogue Choisir un emplacement vous permet de créer et de supprimer des applications Web ou des répertoires virtuels dans votre IIS local. Pour créer une application Web, cliquez sur un bouton comme indiqué ci-dessous dans la figure.

![tâche : image_autre_texte](working-with-visual-studio_5.png)



 Une nouvelle application Web avec le nom par défaut WebSite est créée.

1. Renommez l'application Web. Nous l'avons renommé GridWebOn2013.
1.  Cliquez sur**Ouvert**. 

![tâche : image_autre_texte](working-with-visual-studio_6.png)



 Vous revenez à la boîte de dialogue Nouveau site Web. Le chemin de l'emplacement du site Web est défini sur<http://localhost/GridWebOn2013>. 

1.  Cliquez sur**D'ACCORD** pour laisser Visual Studio créer un site Web.

![tâche : image_autre_texte](working-with-visual-studio_7.png)
### **Étape 2 : Vérification des vues source et conception d'une page Web**
 Un site Web par défaut aura été créé par Visual Studio 2013. Il contient une page Web default.aspx avec du texte factice et du balisage.

**Vue source de la page default.aspx** 

![tâche : image_autre_texte](working-with-visual-studio_8.png)



Toutes les pages Web (y compris ASP.NET) peuvent être ouvertes en deux modes. L'une est la vue source qui permet aux développeurs d'accéder et de modifier le code source. Le deuxième mode est la vue de conception qui peut être utilisée pour concevoir des pages Web de manière WYSIWYG. La capture d'écran ci-dessus montre une vue source de la page Web default.aspx. Pour afficher la vue de conception, cliquez sur**Concevoir**. 

**Mode conception de la page default.aspx** 

![tâche : image_autre_texte](working-with-visual-studio_9.png)




Supprimez la page Default.aspx ajoutée par Visual Studio et ajoutez une nouvelle page vierge Default.aspx.

![tâche : image_autre_texte](working-with-visual-studio_10.png)
### **Étape 3 : Ajout de Aspose.Cells.GridWeb à la page Web**
 Vous pouvez simplement ajouter le contrôle Aspose.Cells.GridWeb (ou GridWeb) à une page Web en le faisant glisser depuis la boîte à outils.

![tâche : image_autre_texte](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

 Si vous ne savez pas comment ajouter Aspose.Cells.GridWeb à la boîte à outils, reportez-vous à[Intégrer les contrôles de grille Aspose.Cells à Visual Studio.NET](/cells/fr/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

 Une fois que le contrôle GridWeb est déposé sur la page Web, il s'affichera comme ceci :

![tâche : image_autre_texte](working-with-visual-studio_12.png)



### **Étape 4 : Modifier la balise <!DOCTYPE>**
1.  Basculez vers la vue source et recherchez les éléments suivants**<!DOCTYPE>** tag dans le code source :

**ASP.NET**

{{< highlight "csharp" >}}



<!DOCTYPE html>



{{< /highlight >}}

1.  Sélectionnez la balise complète.

![tâche : image_autre_texte](working-with-visual-studio_13.png)




1.  Conserver, modifier ou supprimer le<!DOCTYPE>étiquette.
1.  Ou modifier le<!DOCTYPE> balise avec celle-ci :

{{< highlight "csharp" >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **Étape 5 : Redimensionner Aspose.Cells.GridWeb Control**
 Vous pouvez modifier la largeur et la hauteur du contrôle GridWeb après l'avoir fait glisser sur le site Web.

 En mode conception, vous pouvez redimensionner la largeur et la hauteur du GridWeb.

![tâche : image_autre_texte](working-with-visual-studio_14.png)



### **Étape 6 : Configuration des propriétés de Aspose.Cells.GridWeb**
 Configurez les propriétés Aspose.Cells.GridWeb en WYSIWYG en cliquant sur le**Propriétés** bouton sur le côté droit de Visual Studio 2013 IDE.
 Une boîte de dialogue Propriétés s'affiche.

![tâche : image_autre_texte](working-with-visual-studio_15.png)



Le volet Propriétés permet de configurer l'apparence de GridWeb et d'autres propriétés pour contrôler le comportement de GridWeb.
### **Étape 7 : Exécution de votre premier site Web contenant Aspose.Cells.GridWeb**
 Construire et exécuter le site Web.

1.  Exécutez le site Web directement à partir de Visual Studio en appuyant sur Ctrl + F5 ou en cliquant sur**Démarrer le débogage**. 

![tâche : image_autre_texte](working-with-visual-studio_16.png)

 Maintenant, vous pouvez commencer à jouer avec le contrôle GridWeb.

**Contrôle GridWeb en action** 

![tâche : image_autre_texte](working-with-visual-studio_17.png)
