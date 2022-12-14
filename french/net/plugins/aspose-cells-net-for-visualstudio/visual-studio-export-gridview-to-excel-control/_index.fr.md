---
title: Contrôle Visual Studio Exporter GridView vers Excel
type: docs
weight: 10
url: /fr/net/visual-studio-export-gridview-to-excel-control/
---
## **Introduction**
 Export GridView To Excel Control est un contrôle serveur ASP.NET qui permet d'exporter le contenu de GridView dans Microsoft Excel ou des feuilles de calcul OpenOffice à l'aide[Aspose.Cells](https://products.aspose.com/cells/net/) . Il ajoute**Exporter vers Excel** bouton en haut du contrôle GridView. Cliquer sur le bouton exporte dynamiquement le contenu du contrôle GridView vers une feuille de calcul Excel ou OpenOffice Microsoft, puis télécharge automatiquement le fichier exporté vers l'emplacement du disque sélectionné par l'utilisateur en quelques secondes seulement.
### **Caractéristiques des modules**
Cette version initiale du contrôle offre les fonctionnalités suivantes :

- Obtenez une copie hors ligne de votre contenu GridView en ligne préféré pour l'édition, le partage et l'impression.
- Hérité du contrôle GridView ASP.NET par défaut et possède donc toutes ses fonctionnalités et propriétés.
- Exportez GridView vers Xlsx, Xlsb, Xls, Txt, Csv, Ods.
- Fonctionne avec toutes les versions .NET à partir de .NET 2.0.
- Possibilité de personnaliser/localiser le texte du bouton Exporter.
- Appliquez l'apparence de votre propre thème sur le bouton Exporter en utilisant css.
- Option pour ajouter un en-tête personnalisé en haut du document exporté
- Option pour enregistrer chaque document exporté sur le serveur sur un chemin de disque configurable
- Option pour exporter la page actuelle ou toutes les pages lorsque la pagination est activée

![tâche : image_autre_texte](visual-studio-export-gridview-to-excel-control_1.png)

Ce contrôle vous permet d'exporter GridView dans les différents formats de fichiers suivants.

1. Exporter GridView vers Excel
1. Exporter GridView vers Xlsx
1. Exporter GridView vers Xlsb
1. Exporter GridView vers Xls
1. Exporter GridView vers Txt
1. Exporter GridView vers Csv
1. Exporter GridView vers Ods
## **Configuration système requise et plates-formes prises en charge**
### **Configuration requise**
Exporter GridView vers Excel Control pour Visual Studio peut être utilisé sur n'importe quel système sur lequel IIS et .NET framework 2.0 ou supérieur sont installés.
### **Plates-formes prises en charge**
Exporter GridView vers Excel Control for Visual Studio est pris en charge par toutes les versions d'ASP.NET exécutées sur .NET framework 2.0 ou supérieur. Vous pouvez utiliser l'une des versions de Visual Studio suivantes pour utiliser ce contrôle dans vos applications ASP.NET

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013
## **Téléchargement**
Vous pouvez télécharger Export GridView To Excel Control à partir de l'un des emplacements suivants

- [ GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Export_GridView_Excel)
## **Installation**
Il est très simple et facile d'installer Export GridView To Excel Control, veuillez suivre ces étapes simples
### **Pour Visual Studio 2010, 2012 et 2013**
1. Extraire le fichier zip téléchargé
1. Double-cliquez sur le fichier VSIX Aspose.Excel.GridViewExport.vsix
1. Une boîte de dialogue apparaîtra vous montrant les versions disponibles et prises en charge de Visual Studio installées sur votre machine
1. Sélectionnez ceux auxquels vous souhaitez ajouter le contrôle Export GridView To Excel.
1. Cliquez sur Installer

Vous obtiendrez une boîte de dialogue de réussite une fois l'installation terminée.

**Noter:** Assurez-vous de redémarrer Visual Studio pour que les modifications prennent effet.
### **Pour les éditions Visual Studio 2005, 2008 et Express**
Veuillez suivre ces étapes pour intégrer le contrôle Export GridView vers Excel dans Visual Studio pour un glisser-déposer facile, tout comme les autres contrôles ASP.NET.

1. Extraire le fichier zip téléchargé
1. Assurez-vous d'exécuter Visual Studio en tant qu'administrateur

Dans le menu Outils, cliquez sur Choisir les éléments de la boîte à outils.

1.  Cliquez sur Parcourir.
 La boîte de dialogue Ouvrir s'affiche.
1. Accédez au dossier extrait et sélectionnez Aspose.Excel.GridViewExport.dll
1. Cliquez sur OK.

Lorsque vous ouvrez un contrôle aspx ou ascx dans la boîte à outils de gauche, vous verrez ExportGridViewToWord sous l'onglet Général

![tâche : image_autre_texte](visual-studio-export-gridview-to-excel-control_2.png)
## **Utilisant**
Une fois installé, il est très facile de commencer à utiliser ce contrôle dans vos applications ASP.NET

|**Pour .NET framework 4.0 et supérieur** |**Pour .NET framework 2.0 et supérieur** |** |
|:- |:- |:- |
| Pour les applications exécutées dans .NET framework 4.0 et supérieur dans Visual Studio 2010 et supérieur, vous devriez voir**ExportGridViewToExcel**contrôle dans**Aspose** Tab dans la barre d'outils comme indiqué ci-dessous. Vous pouvez simplement faire glisser ce contrôle sur votre page, contrôle ou page maître ASP.NET comme n'importe quel autre contrôle .NET et commencer.|Pour utiliser ce contrôle dans les applications exécutées en .NET 2.0 dans n'importe quelle version de Visual Studio, assurez-vous d'avoir ajouté ExportGridViewToExcel à votre boîte à outils conformément aux instructions sur ﻿[8.1.2.1 Téléchargement et installation]() sous rubrique**Pour les éditions Visual Studio 2005, 2008 et Express** <br> Tu devrais voir**ExportGridViewToExcel**contrôle dans**Général** Tab dans la barre d'outils comme indiqué ci-dessous. Vous pouvez simplement faire glisser ce contrôle sur votre page, contrôle ou page maître ASP.NET comme n'importe quel autre contrôle .NET et commencer.||
|<p>![tâche : image_autre_texte](picture2.png)</p><p></p>|<p>![tâche : image_autre_texte](picture3.png)</p><p></p>||
### **Ajout manuel du contrôle ExportGridViewToExcel**
Si vous rencontrez des problèmes lors de l'utilisation des méthodes ci-dessus qui utilisent Visual Studio Toolbox, vous pouvez ajouter manuellement ce contrôle à votre application ASP.NET exécutée sur n'importe quel framework .NET supérieur à 2.0.

1. Si vous utilisez Visual Studio, assurez-vous de l'exécuter en tant qu'administrateur
1.  Ajouter une référence à**Aspose.Excel.GridViewExport.dll**disponible dans le package de téléchargement extrait de votre projet ASP.NET ou de votre application Web. Assurez-vous que votre application Web/Visual Studio dispose d'un accès complet à ce dossier, sinon vous risquez d'obtenir une exception d'accès refusé.
1.  Ajoutez cette ligne en haut de la page, du contrôle ou de la MasterPage

{{< highlight "java" >}}

 <%@ Register assembly="Aspose.Excel.GridViewExport" namespace="Aspose.Excel.GridViewExport" tagprefix="aspose" %>

{{< /highlight >}}

1.  Ajoutez ce qui suit à un emplacement de votre page, contrôle ou page principale ASP.NET où vous souhaitez ajouter le contrôle

{{< highlight "java" >}}

 <aspose:ExportGridViewToExcel ID="ExportGridViewToExcel1" runat="server"></aspose:ExportGridViewToExcel>

{{< /highlight >}}
### **FAQ**
Questions et problèmes courants auxquels vous pourriez être confronté lors de l'utilisation de ce contrôle

|**#** |**Question** |**Réponse** |
|:- |:- |:- |
|1 | Je ne vois pas le contrôle ExportGridViewToExcel dans Toolbox|<p>**Visual Studio 2010 et supérieur** </p><p>1. Assurez-vous que vous avez installé ce contrôle à l'aide du fichier d'extension VSIX trouvé dans le package téléchargé. Pour vérifier, allez dans Outils -> Extension et mises à jour. Sous installé, vous devriez voir 'Aspose Exporter Exporter GridView vers Excel Control'. Si vous ne le voyez pas, essayez de le réinstaller</p><p>2. Assurez-vous que votre application Web s'exécute dans le framework .NET 4.0 ou supérieur, pour les versions inférieures du framework .NET, veuillez vérifier la méthode alternative ci-dessus.<br>   **Anciennes versions de Visual Studio**</p><p>3. Assurez-vous d'avoir ajouté manuellement ce contrôle à votre boîte à outils conformément aux instructions ci-dessus.</p>|
|2 | J'obtiens l'erreur "Accès refusé" lors de l'exécution de l'application|<p>1. Si vous rencontrez ce problème en production, assurez-vous de copier à la fois Aspose.Excel.dll et Aspose.Excel.GridViewExport.dll dans votre dossier bin.</p><p>2. Si vous utilisez Visual Studio, assurez-vous de l'exécuter en tant qu'administrateur même si vous êtes déjà connecté en tant qu'administrateur.</p>|
### **Aspose .NET Exporter GridView vers les propriétés de contrôle Excel**
Les propriétés suivantes sont exposées pour configurer et utiliser les fonctionnalités intéressantes fournies par ce contrôle

|**Nom de la propriété** |**Taper** |**Exemple/Valeurs possibles** |**La description** |
|:- |:- |:- |:- |
| ExportButtonText| chaîne de caractères| Exporter vers Excel| Vous pouvez utiliser cette propriété pour remplacer le texte par défaut existant|
|ExportButtonCssClass| chaîne de caractères| btn btn-primaire| Classe CSS appliquée à la div externe du bouton d'exportation. Pour appliquer css sur le bouton, vous pouvez utiliser l'entrée .yourClass|
| ExportFileHeading| chaîne de caractères|<h4>Exemple de rapport d'exportation GridView</h4> | Vous pouvez utiliser des balises html pour ajouter du style à votre titre|
| ExportOutputFormat| énumération| Xlsx, Xlsb, Xls, Txt, Csv, Od| Format de sortie du document exporté. Les formats pris en charge sont Xlsx, Xlsb, Xls, Txt, Csv, Ods|
| ExportOutputPathOnServer| chaîne de caractères| c :<br> temp| Sortie locale Chemin du disque sur le serveur où une copie de l'exportation est automatiquement enregistrée. L'application doit avoir un accès en écriture à ce chemin.|
| ExportDataSource| objet| allRowsDataTableallRowsDataTable|Définit l'objet à partir duquel ce contrôle de liaison de données récupère sa liste d'éléments de données. L'objet doit contenir toutes les données à exporter. Cette propriété est utilisée en plus de la propriété DataSource normale et est utile lorsque la pagination personnalisée est activée et que la page actuelle récupère uniquement les lignes à afficher à l'écran.|
| LicenseFilePath| chaîne de caractères|| Chemin local sur le serveur vers le fichier de licence. Par exemple c :<br> inetpub<br> Aspose.Cells.lic|
Un exemple de contrôle Export GridView vers Excel avec toutes les propriétés utilisées est illustré ci-dessous

{{< highlight "java" >}}

 <aspose:ExportGridViewToExcel Width="800px" ID="ExportGridViewToExcel1" ExportButtonText="Export to Excel"

    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExcelOutputFormat="xlsx"

    ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h1>Example Report</h1>"

    OnPageIndexChanging="ExportGridViewToExcel1_PageIndexChanging" PageSize="5" AllowPaging="True"

    LicenseFilePath="c:\inetpub\Aspose.Cells.lic" runat="server" CellPadding="4"

    ForeColor="#333333" GridLines="Both">

</aspose:ExportGridViewToExcel>


{{< /highlight >}}
## **Démo vidéo**
 Vérifiez s'il vous plaît[la vidéo](https://www.youtube.com/watch?v=_fSq_3TP1oM) ci-dessous pour voir le module en action.
## **Soutenir, étendre et contribuer**
### **Soutien**
Dès les premiers jours du Aspose, nous savions que donner à nos clients de bons produits ne suffirait pas. Nous devions également fournir un bon service. Nous sommes nous-mêmes des développeurs et comprenons à quel point il est frustrant lorsqu'un problème technique ou une bizarrerie du logiciel vous empêche de faire ce que vous devez faire. Nous sommes ici pour résoudre les problèmes, pas pour les créer.

C'est pourquoi nous proposons une assistance gratuite. Toute personne qui utilise notre produit, qu'elle l'ait acheté ou utilise une évaluation, mérite toute notre attention et notre respect.

Vous pouvez consigner tout problème ou suggestion lié à ce contrôle à l'aide de l'une des plates-formes suivantes

- [ GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
### **Prolonger et contribuer**
Aspose .NET Exporter GridView vers Excel Control for Visual Studio est open source et son code source est disponible sur les principaux sites Web de codage social répertoriés ci-dessous. Les développeurs sont encouragés à télécharger le code source et à étendre les fonctionnalités selon leurs propres besoins.
#### **Code source**
Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants

- [ GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins)
#### **Comment configurer le code source**
Vous devez avoir installé les éléments suivants pour ouvrir et étendre le code source

- Visual Studio 2010

Veuillez suivre ces étapes simples pour commencer

1. Téléchargez/clonez le code source.
1.  Ouvrez Visual Studio 2010 et choisissez**Dossier** > **Projet ouvert**
1.  Accédez au dernier code source que vous avez téléchargé et ouvrez**Aspose.Excel.GridViewExport.sln**
#### **Présentation du code source**
Il y a trois projets dans la solution

- Aspose.Excel.GridViewExport - Contient le package VSIX et le contrôle du serveur for .NET 4.0.
- Aspose.Excel.GridViewExport_Point net_2.0 - Contrôle GridView étendu for .NET 2.0
- Aspose.Excel.GridViewExport.Website - Projet Web pour tester le contrôle Excel Exportable GridView
