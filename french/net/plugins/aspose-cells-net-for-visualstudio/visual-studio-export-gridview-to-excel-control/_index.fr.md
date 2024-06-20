---
title: Contrôle d exportation de GridView vers Excel dans Visual Studio
type: docs
weight: 10
url: /fr/net/visual-studio-export-gridview-to-excel-control/
---

## **Introduction**
Le contrôle d'exportation de GridView vers Excel est un contrôle serveur ASP.NET qui permet d'exporter le contenu de GridView dans des feuilles de calcul Microsoft Excel ou OpenOffice en utilisant [Aspose.Cells](https://products.aspose.com/cells/net/). Il ajoute un bouton **Export vers Excel** en haut du contrôle GridView. En cliquant sur le bouton, le contenu du contrôle GridView est exporté dynamiquement dans une feuille de calcul Microsoft Excel ou OpenOffice et est automatiquement téléchargé vers l'emplacement de disque sélectionné par l'utilisateur en seulement quelques secondes.
### **Fonctionnalités du module**
Cette version initiale du contrôle offre les fonctionnalités suivantes :

- Obtenez une copie hors ligne de votre contenu GridView en ligne préféré pour l'édition, le partage et l'impression.
- Hérité du contrôle GridView par défaut ASP.NET et possède donc toutes ses fonctionnalités et propriétés.
- Exporter GridView vers Xlsx, Xlsb, Xls, Txt, Csv, Ods.
- Fonctionne avec toutes les versions de .NET à partir de .NET 2.0.
- Possibilité de personnaliser/localiser le texte du bouton d'exportation.
- Appliquer l'apparence de votre propre thème sur le bouton d'exportation à l'aide de css.
- Option pour ajouter un titre personnalisé en haut du document exporté
- Option pour enregistrer chaque document exporté sur le serveur à un chemin de disque configurable
- Option pour exporter la page actuelle ou toutes les pages lorsque le mode de pagination est activé

![todo:image_alt_text](visual-studio-export-gridview-to-excel-control_1.png)

Ce contrôle vous permet d'exporter la GridView dans les différents formats de fichiers suivants.

1. Exporter la GridView vers Excel
1. Exporter la GridView vers Xlsx
1. Exporter la GridView vers Xlsb
1. Exporter la GridView vers Xls
1. Exporter la GridView vers Txt
1. Exporter la GridView vers Csv
1. Exporter la GridView vers Ods
## **Configuration requise et plateformes prises en charge**
### **Configuration requise**
Le contrôle Export GridView To Excel pour Visual Studio peut être utilisé sur tout système comportant IIS et le framework .NET 2.0 ou supérieur installé.
### **Plateformes prises en charge**
Le contrôle Export GridView To Excel pour Visual Studio est pris en charge par toutes les versions d'ASP.NET fonctionnant sur le framework .NET 2.0 ou supérieur. Vous pouvez utiliser l'une des versions de Visual Studio suivantes pour utiliser ce contrôle dans vos applications ASP.NET

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013
## **Téléchargement**
Vous pouvez télécharger le contrôle Export GridView To Excel à partir de l'un des emplacements suivants

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Export_GridView_Excel)
## **Installer**
Il est très simple et facile d'installer le contrôle Export GridView To Excel, veuillez suivre ces étapes simples
### **Pour Visual Studio 2010, 2012 et 2013**
1. Extraire le fichier zip téléchargé
1. Double-cliquez sur le fichier VSIX Aspose.Excel.GridViewExport.vsix
1. Une boîte de dialogue apparaîtra vous montrant les versions de Visual Studio disponibles et prises en charge installées sur votre machine
1. Sélectionnez celles auxquelles vous souhaitez ajouter le contrôle Export GridView To Excel
1. Cliquez sur Installer

Vous obtiendrez une boîte de dialogue de succès une fois l'installation terminée.

**Remarque :** Veuillez vous assurer de redémarrer Visual Studio pour que les modifications prennent effet.
### **Pour Visual Studio 2005, 2008 et les éditions Express**
Veuillez suivre ces étapes pour intégrer le contrôle Export GridView To Excel dans Visual Studio pour un glisser-déposer facile, tout comme d'autres contrôles ASP.NET

1. Extraire le fichier zip téléchargé
1. Assurez-vous d'exécuter Visual Studio en tant qu'administrateur

Dans le menu Outils, cliquez sur Choisir les éléments de la boîte à outils.

1. Cliquez sur Parcourir. 
   La boîte de dialogue Ouvrir apparaît.
1. Accédez au dossier extrait et sélectionnez Aspose.Excel.GridViewExport.dll
1. Cliquez sur OK.

Lorsque vous ouvrez un contrôle aspx ou ascx dans la boîte à outils de gauche, vous verrez ExportGridViewToWord sous l'onglet Général

![todo:image_alt_text](visual-studio-export-gridview-to-excel-control_2.png)
## **En utilisant**
Une fois installé, il est très facile de commencer à utiliser ce contrôle dans vos applications ASP.NET

|**Pour .NET Framework 4.0 et versions ultérieures** |**Pour .NET Framework 2.0 et versions ultérieures** |** |
| :- | :- | :- |
|Pour les applications s'exécutant dans .NET Framework 4.0 et versions ultérieures dans Visual Studio 2010 et versions ultérieures, vous devriez voir le contrôle **ExportGridViewToExcel** dans l'onglet **Aspose** dans la barre d'outils comme indiqué ci-dessous. Vous pouvez simplement faire glisser-déposer ce contrôle sur votre page ASP.NET, contrôle ou page maître, comme n'importe quel autre contrôle .NET, et commencer. |Pour utiliser ce contrôle dans les applications s'exécutant dans .NET 2.0 dans n'importe quelle version de Visual Studio, assurez-vous d'avoir ajouté ExportGridViewToExcel à votre boîte à outils comme indiqué dans les instructions sur ﻿[8.1.2.1 Téléchargement et installation]() sous la rubrique **Pour Visual Studio 2005, 2008 et les éditions Express** <br>Vous devriez voir le contrôle **ExportGridViewToExcel** dans l'onglet **Général** dans la barre d'outils, comme indiqué ci-dessous. Vous pouvez simplement faire glisser-déposer ce contrôle sur votre page ASP.NET, contrôle ou page maître, comme n'importe quel autre contrôle .NET, et commencer. | |
|<p>![todo:image_alt_text](picture2.png)</p><p></p>|<p>![todo:image_alt_text](picture3.png)</p><p></p>| |
### **Ajout manuel du contrôle ExportGridViewToExcel**
Si vous rencontrez des problèmes en utilisant les méthodes ci-dessus qui utilisent la Boîte à outils Visual Studio, vous pouvez ajouter manuellement ce contrôle à votre application ASP.NET s'exécutant sur n'importe quelle version de .NET supérieure à 2.0

1. Si vous utilisez Visual Studio, assurez-vous de l'exécuter en tant qu'administrateur
1. Ajoutez une référence à **Aspose.Excel.GridViewExport.dll** disponible dans le package de téléchargement extrait dans votre projet ASP.NET ou votre application web. Assurez-vous que votre application web/Visual Studio a un accès complet à ce dossier, sinon vous pourriez obtenir une exception d'accès refusé.
1. Ajoutez cette ligne en haut de la page, du contrôle ou de la page maître 

{{< highlight java >}}

 <%@ Register assembly="Aspose.Excel.GridViewExport" namespace="Aspose.Excel.GridViewExport" tagprefix="aspose" %>

{{< /highlight >}}

1. Ajoutez ce qui suit à l'endroit de votre page ASP.NET, contrôle ou page maîtresse où vous souhaitez ajouter le contrôle 

{{< highlight java >}}

 <aspose:ExportGridViewToExcel ID="ExportGridViewToExcel1" runat="server"></aspose:ExportGridViewToExcel>

{{< /highlight >}}
### **FAQ**
Questions fréquemment posées et problèmes que vous pourriez rencontrer lors de l'utilisation de ce contrôle

|**#** |**Question** |**Réponse** |
| :- | :- | :- |
|1 |Je ne vois pas le contrôle ExportGridViewToExcel dans la Boîte à outils |<p>**Visual Studio 2010 et ultérieur** </p><p>1. Assurez-vous d'avoir installé ce contrôle à l'aide du fichier d'extension VSIX trouvé dans le package téléchargé. Pour vérifier, allez dans Outils -> Extensions et mises à jour. Sous Installé, vous devriez voir 'Aspose Export Export GridView To Excel Control'. Si vous ne le voyez pas, veuillez essayer de le réinstaller</p><p>2. Assurez-vous que votre application web s'exécute dans .NET Framework 4.0 ou une version ultérieure, pour les versions inférieures du .NET Framework, veuillez vérifier la méthode alternative ci-dessus. <br>   **Anciennes versions de Visual Studio**</p><p>3. Assurez-vous d'avoir ajouté manuellement ce contrôle à votre Boîte à outils comme indiqué ci-dessus.</p>|
|2 |Je reçois une erreur 'Accès refusé' lors de l'exécution de l'application |<p>1. Si vous rencontrez ce problème en production, assurez-vous de copier à la fois Aspose.Excel.dll et Aspose.Excel.GridViewExport.dll dans votre dossier bin.</p><p>2. Si vous utilisez Visual Studio, assurez-vous de l'exécuter en tant qu'administrateur, même si vous êtes déjà connecté en tant qu'administrateur.</p>|
### **Propriétés du contrôle Aspose .NET Export GridView To Excel**
Les propriétés suivantes sont exposées pour configurer et utiliser les fonctionnalités offertes par ce contrôle

|**Nom de la propriété** |**Type** |**Exemple/Valeurs possibles** |**Description** |
| :- | :- | :- | :- |
|ExportButtonText |chaîne de caractères |Exporter vers Excel |Vous pouvez utiliser cette propriété pour remplacer le texte par défaut existant |
|ExportButtonCssClass |chaîne de caractères |btn btn-principal |Classe CSS appliquée à la div extérieure du bouton d'exportation. Pour appliquer du CSS sur le bouton, vous pouvez utiliser .votreClass input |
|ExportFileHeading |chaîne de caractères |<h4>Exemple de rapport d'exportation de la GridView</h4> |Vous pouvez utiliser des balises HTML pour ajouter du style à votre en-tête |
|ExportOutputFormat |énumération |Xlsx, Xlsb, Xls, Txt, Csv, Ods |Format de sortie du document exporté. Les formats pris en charge sont Xlsx, Xlsb, Xls, Txt, Csv, Ods |
|ExportOutputPathOnServer |chaîne de caractères |c: <br>temp |Chemin d'accès au disque de sortie local sur le serveur où une copie de l'exportation est automatiquement enregistrée. L'application doit avoir un accès en écriture à ce chemin. |
|ExportDataSource |objet |allRowsDataTable |Définit l'objet à partir duquel ce contrôle de liaison de données récupère sa liste d'éléments de données. L'objet doit contenir toutes les données à exporter. Cette propriété est utilisée en plus de la propriété DataSource normale et est utile lorsque la pagination personnalisée est activée et que la page actuelle ne récupère que les lignes à afficher à l'écran. |
|LicenseFilePath |chaîne de caractères | |Chemin d'accès local sur le serveur au fichier de licence. Par exemple, c: <br>inetpub <br>Aspose.Cells.lic |
Un exemple de contrôle Exporter la GridView vers Excel avec toutes les propriétés utilisées est présenté ci-dessous

{{< highlight java >}}

 <aspose:ExportGridViewToExcel Width="800px" ID="ExportGridViewToExcel1" ExportButtonText="Export to Excel"

    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExcelOutputFormat="xlsx"

    ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h1>Example Report</h1>"

    OnPageIndexChanging="ExportGridViewToExcel1_PageIndexChanging" PageSize="5" AllowPaging="True"

    LicenseFilePath="c:\inetpub\Aspose.Cells.lic" runat="server" CellPadding="4"

    ForeColor="#333333" GridLines="Both">

</aspose:ExportGridViewToExcel>


{{< /highlight >}}
## **Démo vidéo**
Veuillez consulter [la vidéo](https://www.youtube.com/watch?v=_fSq_3TP1oM) ci-dessous pour voir le module en action.
## **Soutenir, étendre et contribuer**
### **Soutien**
Dès les premiers jours d'Aspose, nous savions que le simple fait de fournir de bons produits à nos clients ne suffirait pas. Nous devions également offrir un bon service. Nous sommes nous-mêmes des développeurs et comprenons à quel point il est frustrant de voir un problème technique ou une bizarrerie dans le logiciel vous empêcher de faire ce que vous devez faire. Nous sommes ici pour résoudre les problèmes, pas pour en créer.

C'est pourquoi nous offrons un support gratuit. Toute personne qui utilise notre produit, qu'elle l'ait acheté ou qu'elle l'utilise en évaluation, mérite toute notre attention et notre respect.

Vous pouvez signaler tout problème ou suggestion concernant ce contrôle en utilisant l'une des plateformes suivantes

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
### **Élargir et contribuer**
Aspose .NET Export GridView To Excel Control pour Visual Studio est open source et son code source est disponible sur les principaux sites de codage social répertoriés ci-dessous. Les développeurs sont encouragés à télécharger le code source et à étendre la fonctionnalité selon leurs propres besoins.
#### **Code source**
Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins)
#### **Comment configurer le code source**
Vous devez avoir les éléments suivants installés pour ouvrir et étendre le code source

- Visual Studio 2010

Veuillez suivre ces étapes simples pour commencer

1. Téléchargez/clônez le code source.
1. Ouvrez Visual Studio 2010 et choisissez **Fichier** > **Ouvrir un projet**
1. Accédez au code source le plus récent que vous avez téléchargé et ouvrez **Aspose.Excel.GridViewExport.sln**
#### **Aperçu du code source**
Il y a trois projets dans la solution

- Aspose.Excel.GridViewExport - Contient le package VSIX et le contrôle serveur pour .NET 4.0.
- Aspose.Excel.GridViewExport_DotNet_2.0 - Contrôle GridView étendu pour .NET 2.0
- Aspose.Excel.GridViewExport.Website - Projet Web pour tester le contrôle GridView exportable vers Excel
