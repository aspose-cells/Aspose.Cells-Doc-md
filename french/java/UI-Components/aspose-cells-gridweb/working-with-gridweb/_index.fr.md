---
title: Travailler avec GridWeb
type: docs
weight: 20
url: /fr/java/working-with-gridweb/
---
##  **Ouverture d'un fichier Excel Microsoft**

Le contrôle Aspose.Cells.GridWeb peut ouvrir et charger des fichiers Excel Microsoft - complets avec des données, un formatage, des graphiques, des images, etc. Cette rubrique explique comment.

Pour ouvrir un fichier Excel à l'aide du contrôle GridWeb :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire ou une page Web.
1. Importez le fichier Excel en spécifiant le chemin du fichier.
1. Exécutez l'application ou ouvrez la page.

Pour charger le contenu d'un fichier Excel vers le contrôle Aspose.Cells.GridWeb, vous devez appeler la méthode importExcelFile pour spécifier le chemin du fichier Excel. Après cela, le contrôle GridWeb trouvera automatiquement le fichier à partir du chemin spécifié et y affichera son contenu. Un extrait de code qui charge le contenu d'un fichier Excel est fourni ci-dessous.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

L'extrait de code ci-dessus peut être utilisé comme vous le souhaitez. Par exemple, pour charger automatiquement un fichier Excel lors du chargement d'un formulaire Web, ajoutez ce code à l'événement Page_Load du formulaire que vous avez spécifié vous-même.

**Un fichier Excel est chargé dans GridWeb**

![tâche : image_alt_text](working-with-gridweb_1.png)

##  **Enregistrement d'un fichier Excel Microsoft**

Il est possible de créer de nouveaux fichiers Excel Microsoft ou de manipuler des fichiers Excel existants, sur des sites Web en mode GUI à l'aide du contrôle Aspose.Cells.GridWeb. Les fichiers peuvent ensuite être enregistrés dans des fichiers Excel. Aspose.Cells.GridWeb sert efficacement d'éditeur de feuille de calcul en ligne. Cette rubrique décrit comment enregistrer le contenu de la grille dans des fichiers Excel.

###  **Enregistrer sous forme de fichier**

Pour enregistrer le contenu du champ Aspose.Cells.GridWeb sous forme de fichier Excel :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire ou une page Web.
1. Enregistrez votre travail sous forme de fichier Excel à un chemin spécifié.
1. Exécutez l'application ou ouvrez la page.

L'exemple de code ci-dessous illustre comment enregistrer le contenu de la grille dans un fichier Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

 L'extrait de code ci-dessus peut être utilisé de plusieurs manières. Une méthode courante consiste à ajouter un bouton qui enregistre le contenu de la grille dans un fichier Excel lorsque vous cliquez dessus. Aspose.Cells.GridWeb offre une approche plus simple pour la tâche. Aspose.Cells.GridWeb a un événement appelé SaveCommand. L'extrait de code ci-dessus peut être ajouté au gestionnaire d'événements de l'événement SaveCommand, ce qui permet aux utilisateurs d'enregistrer leur travail en cliquant sur le bouton intégré Aspose.Cells.GridWeb.**Sauvegarder** bouton.

##  **Redimensionnement de Aspose.Cells.GridWeb et de sa barre d'en-tête**

Cet article explique comment redimensionner GridWeb au moment de l'exécution à l'aide du Aspose.Cells.GridWeb API. Il explique également comment redimensionner les barres d'en-tête du contrôle Aspose.Cells.GridWeb pour rendre leurs données plus faciles à lire.

###  **Modification de la largeur et de la hauteur de Aspose.Cells.GridWeb**

La modification de la largeur et de la hauteur du contrôle Aspose.Cells.GridWeb est une fonctionnalité simple mais importante. Le contrôle Aspose.Cells.GridWeb est représenté par la classe GridWeb dans le API. Pour redimensionner la largeur et la hauteur du contrôle GridWeb, utilisez simplement ses propriétés width et height.

{{% alert color="primary" %}}

La largeur et la hauteur du champ peuvent être définies en pixels ou en points.

{{% /alert %}}

Le résultat de l’extrait de code qui suit est présenté ci-dessous.

**Modification de la largeur et de la hauteur du contrôle GridWeb**

![tâche : image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

###  **Modification de la largeur et de la hauteur de la barre d'en-tête**

Le contrôle Aspose.Cells.GridWeb contient deux barres d’en-tête comme suit :

- Barre d'en-tête supérieure, cette barre d'en-tête représente les colonnes A, B, C, D, etc.
- Barre d'en-tête gauche, cette barre d'en-tête représente les lignes 1, 2, 3, 4, etc.

Ces deux barres d’en-tête sont présentées ci-dessous.

**Barres d'en-tête**

![tâche : image_alt_text](working-with-gridweb_3.png)

Modifiez la hauteur de la barre d’en-tête supérieure et la largeur de la barre d’en-tête gauche à l’aide respectivement des propriétés HeaderBarHeight et HeaderBarWidth du contrôle GridWeb. La figure ci-dessous montre le résultat de l'exemple de code qui suit.

**Modification de la largeur et de la hauteur de la barre d'en-tête**

![tâche : image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

##  **Travailler avec les événements Aspose.Cells.GridWeb**

Tous les développeurs doivent être familiers avec les événements et leur objectif. Les événements sont utilisés pour envoyer des notifications de modifications pouvant survenir dans un contrôle ou une classe. Aspose.Cells.GridWeb comporte plusieurs événements qui peuvent être utilisés pour effectuer des tâches spécifiques lorsque certaines modifications se produisent dans le contrôle.

Cette rubrique fournit une introduction à tous les événements pris en charge par le contrôle Aspose.Cells.GridWeb ainsi que quelques détails sur la façon de gérer ces événements.

###  **Introduction aux événements de grille**

Le contrôle Aspose.Cells.GridWeb prend en charge plusieurs événements qui offrent davantage de contrôle pour effectuer des opérations lorsque des événements spécifiques sont déclenchés dans le contrôle. Une liste complète des événements pris en charge par le contrôle Aspose.Cells.GridWeb est disponible ci-dessous.

|**Événements**|**Description**|
| :- | :- |
|CommandeCellule|Se produit lorsque l'on clique sur le lien hypertexte de commande d'une cellule. Lorsque cet événement est déclenché, son paramètre e.Argument fournit le nom de la commande.|
|CellDoubleClick|Se produit lorsque vous double-cliquez sur la cellule.|
|ColonneSupprimée|Se produit lorsqu'un utilisateur supprime une colonne d'une feuille de calcul à l'aide du menu côté client.|
|Suppression de colonnes|Se produit lorsqu'un utilisateur tente de supprimer une colonne d'une feuille de calcul à l'aide du menu côté client.|
|ColonneDoubleClick|Se produit lorsque l'on double-clique sur l'en-tête de colonne.|
|ColonneInsérée|Se produit lorsqu'un utilisateur insère une colonne dans une feuille de calcul à l'aide du menu côté client.|
|Commande personnalisée|Se produit lorsqu'un utilisateur clique sur un bouton de commande personnalisé.|
|Charger des données personnalisées|Se produit lorsque la propriété EnableSession du contrôle est définie sur false et doit charger les données de la feuille de calcul. Vous pouvez gérer cet événement en mode sans session pour charger les données d'une feuille de calcul à partir d'un fichier ou d'une base de données.|
|PageIndexModifié|Se produit lorsque l’index de page de feuille du contrôle est modifié.|
|LigneSupprimée|Se produit lorsqu'un utilisateur supprime une ligne de la feuille de calcul à l'aide du menu côté client.|
|Suppression de lignes|Se produit lorsqu'un utilisateur tente de supprimer une ligne d'une feuille de calcul à l'aide du menu côté client.|
|LigneDoubleClic|Se produit lorsque l'on double-clique sur l'en-tête de ligne.|
|LigneInsérée|Se produit lorsqu'un utilisateur insère une ligne dans la feuille de calcul à l'aide du menu côté client.|
|Enregistrer la commande| Se produit lorsque le**Sauvegarder** le bouton est cliqué.|
|FeuilleOngletClic|Se produit lorsqu'un onglet de feuille est cliqué.|
|SoumettreCommand| Se produit lorsque le**Soumettre** le bouton est cliqué.|
|Annuler la commande| Se produit lorsque le**annuler** le bouton est cliqué.|
|AjaxCallFini|Se déclenche lorsque la mise à jour AJAX du contrôle est terminée. (EnableAJAX doit être défini sur true).|
|CellModifiedOnAjax|Se déclenche lorsque la cellule est modifiée lors d'un appel AJAX.|
|AprèsColumnFilter|Se déclenche lorsque le filtre est appliqué sur une colonne.|

###  **Gestion des événements de grille**

Pour effectuer une opération spécifique sur le déclenchement d'un événement spécifique, nous devons créer un gestionnaire d'événements. Un gestionnaire d'événements effectue la tâche souhaitée lorsqu'un certain événement est déclenché. L'exemple qui suit montre comment gérer un simple événement de grille.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

##  **Travailler avec des événements de double-clic**

Aspose.Cells.GridWeb contient trois types d'événements de double-clic :

- CellDoubleClick, déclenché lorsqu'un double-clic sur une cellule.
- ColumnDoubleClick, déclenché lorsqu'un en-tête de colonne est double-cliqué.
- RowDoubleClick, déclenché lorsqu'un en-tête de ligne est double-cliqué.

Cette rubrique explique comment activer les événements de double-clic dans Aspose.Cells.GridWeb. Il aborde également la création de gestionnaires d'événements pour ces événements.

###  **Activation des événements de double-clic**

Tous les types d'événements de double-clic peuvent être activés côté client en définissant la propriété EnableDoubleClickEvent du contrôle GridWeb sur true.

{{% alert color="primary" %}}

Par défaut, la propriété EnableDoubleClickEvent est définie sur false. Cela signifie que les événements de double-clic ne sont pas activés par défaut. Pour implémenter de tels événements, activez d’abord la fonctionnalité.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

Une fois les événements de double-clic activés, il est possible de créer des gestionnaires d'événements pour tous les événements de double-clic. Ces gestionnaires d'événements effectuent des tâches spécifiques lorsqu'un événement de double-clic donné est déclenché.

###  **Gestion des événements de double-clic**

####  **Double-cliquez sur Cell**

Le gestionnaire d'événements pour l'événement CellDoubleClick fournit un argument de type CellEventArgs, qui fournit les informations complètes sur la cellule sur laquelle vous avez double-cliqué.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

####  **En-tête de colonne double-cliquez**

Le gestionnaire d'événements pour l'événement ColumnDoubleClick fournit un argument du type RowColumnEventArgs qui fournit le numéro d'index de la colonne pour l'en-tête sur lequel vous avez double-cliqué ainsi que d'autres informations.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

####  **En-tête de ligne double-cliquez**

Le gestionnaire d'événements pour l'événement RowDoubleClick fournit un argument du type RowColumnEventArgs qui fournit le numéro d'index de la ligne de l'en-tête sur lequel vous avez double-cliqué ainsi que d'autres informations associées.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

##  **Définition du style ou de l'apparence de Aspose.Cells.GridWeb**

Aspose.Cells.GridWeb a sa propre apparence par défaut mais il est possible de modifier son apparence. Aspose.Cells.GridWeb fournit plusieurs propriétés pour permettre aux développeurs de contrôler entièrement son apparence. Cette rubrique traite de certaines de ces propriétés.

###  **Définition du style ou de l'apparence de Aspose.Cells.GridWeb**

####  **Styles prédéfinis**

Pour économiser les efforts des développeurs, Aspose.Cells.GridWeb propose des styles prédéfinis. Sélectionnez simplement un style dans la liste pour appliquer le style.

|**modes**|**Schéma de couleur**|
| :- | :- |
|Standard|Argent|
|Coloré1|Rose|
|Coloré2|Bleu|
|Professionnel1|Cyan|
|Professionnel2|Encore du cyan|
|Traditionnel1|Sombre|
|Traditionnel2|Gris|
|Coutume|Personnalisé|
Lorsqu'un style particulier est sélectionné, il modifie toute l'apparence du contrôle GridWeb. Les développeurs peuvent sélectionner un style prédéfini à appliquer lors de l'exécution à l'aide du flexible API de Aspose.Cells.GridWeb.

Le contrôle GridWeb fournit la propriété PresetStyle à laquelle les développeurs peuvent attribuer n'importe quel style prédéfini souhaité.

La sortie de l'extrait de code ci-dessous est présentée ci-dessous.

**Contrôle GridWeb avec le style Colorful1 appliqué dessus**

![tâche : image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

####  **Style de la barre d'en-tête**

Si vous jetez un œil au contrôle GridWeb, vous remarquerez deux barres d'en-tête. Un pour les colonnes (c'est-à-dire A, B, C, D, etc.) et un autre pour les lignes (c'est-à-dire 1, 2, 3, 4, etc.). Aspose.Cells.GridWeb permet aux développeurs de contrôler l'apparence de ces barres d'en-tête. Les développeurs peuvent définir le style des barres d'en-tête lors de l'exécution.

{{% alert color="primary" %}}

Le contrôle GridWeb fournit la propriété HeaderBarStyle qui applique un style sur les deux barres d'en-tête du contrôle.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

####  **Style de barre d'onglets**

Il est également possible de définir le style de la barre d'onglets. Veuillez consulter le code suivant

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

####  **Chargement du fichier de style**

Pour appliquer les paramètres de style d'un fichier de style existant au contrôle GridWeb, les développeurs peuvent définir le chemin du fichier de style sur la propriété CustomStyleFileName du contrôle. Mais avant de faire cela, il est nécessaire de définir la propriété PresetStyle du contrôle sur Custom. En effet, ce fichier de style contient des informations de style personnalisées déjà définies par un développeur.

Veuillez consulter l'image suivante qui montre GridWeb avec le style personnalisé qui lui est appliqué.

![tâche : image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

IMPORTANT : Le chargement du fichier de style dans le contrôle GridWeb n'affecte pas les paramètres de formatage des cellules du contrôle.

{{% /alert %}}

####  **Exemple de modèle de style personnalisé**

Voici l’exemple de modèle de style personnalisé. Vous pouvez le modifier selon vos besoins.

{{< highlight "java" >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

##  **Création d'un contrôle sur un formulaire Web**

Cet article vous guidera sur la façon de créer un simple formulaire Web JSP (page serveur Java) comportant un contrôle GridWeb.

**Étape 1 - Créer une structure de répertoires**

 Vous devez créer la structure de répertoires suivante dans le**applications Web**répertoire du serveur Tomcat

![tâche : image_alt_text](working-with-gridweb_7.png)

 Ce sont les répertoires et fichiers que vous devez créer. Veuillez lire les commentaires et les suivre. Vous pouvez obtenir les dernières archives de la version Aspose.Cells.GridWeb for Java à partir de[ce lien](https://downloads.aspose.com/cells/java).

{{< highlight "java" >}}

 SamplePageGridWebJava

SamplePageGridWebJava\grid

//Get acwclient directory from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\acwclient

SamplePageGridWebJava\WEB-INF

SamplePageGridWebJava\WEB-INF\lib

//Get aspose-gridweb-x.x.x.jar file from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\WEB-INF\aspose-gridweb-x.x.x.jar

SamplePageGridWebJava\WEB-INF\web.xml

SamplePageGridWebJava\head.jsp

//Create this excel file using Microsoft Excel or you can use any excel file and rename it SampleExcel.xlsx

SamplePageGridWebJava\SampleExcel.xlsx

SamplePageGridWebJava\SamplePage.jsp

{{< /highlight >}}

**Étape 2 - Ajout de codes dans les fichiers créés**

Cette section montre le code de divers fichiers créés dans la structure de répertoires ci-dessus. Veuillez récupérer ces codes et les ajouter dans vos fichiers en les ouvrant dans le Bloc-notes et en les copiant/collant.

**Web.xml**

{{< highlight "java" >}}

 <?xml version="1.0" encoding="UTF-8"?>

<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://java.sun.com/xml/ns/javaee" xmlns:web="http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" id="WebApp_ID" version="2.5">

  <display-name>testGridWeb</display-name>

  <welcome-file-list>

    <welcome-file>SamplePage.jsp</welcome-file>

  </welcome-file-list>

  <servlet>

    <display-name>GridWebServlet</display-name>

    <servlet-name>GridWebServlet</servlet-name>

    <servlet-class>com.aspose.gridweb.GridWebServlet</servlet-class>

  </servlet>

  <servlet-mapping>

    <servlet-name>GridWebServlet</servlet-name>

    <url-pattern>/GridWebServlet</url-pattern>

  </servlet-mapping>

</web-app>

{{< /highlight >}}

**head.jsp**

{{< highlight "java" >}}

 <%

String path = request.getContextPath();

String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";

%>

<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9"/>

<base href="<%=basePath%>">

<script type="text/javascript" language="javascript"

	src="grid/acw_client/acwmain.js"></script>

<script type="text/javascript" language="javascript"

	src="grid/acw_client/lang_en.js"></script>

<link href="grid/acw_client/menu.css" rel="stylesheet" type="text/css" />

<style>

span.acwxc {

	overflow: hidden;

	border: none;

	display: block;

	white-space: pre;

}

</style>

<style>

span.rotation90 {

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(-90deg);

	-moz-transform: rotate(-90deg);

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3 );

	display: block

}

</style>

<style>

span.rotation-90 {

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1 );

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(90deg);

	-moz-transform: rotate(90deg);

	display: block

}

</style>

<style>

span.wrap {

	white-space: pre-wrap;

	white-space: -moz-pre-wrap;

	white-space: -pre-wrap;

	white-space: -o-pre-wrap;

	word-wrap: break-word;

	-ms-word-break: break-all;

}

</style>

{{< /highlight >}}

**ExemplePage.jsp**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-SamplePage-SamplePage.jsp" >}}

**Étape 3 - Exécution de votre exemple de page Web JSP**

Maintenant, vous avez tout fait. Il est temps d'exécuter la page Web. Veuillez démarrer votre serveur Tomcat, puis collez l'URL suivante dans le navigateur Web.

{{< highlight "java" >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Vous verrez quelque chose comme la capture d'écran suivante. Félicitations, vous avez utilisé avec succès le contrôle GridWeb sur votre page JSP.

![tâche : image_alt_text](working-with-gridweb_8.png)

##  **Grille d'impressionWeb**

Il arrive parfois que les développeurs doivent imprimer le contenu GridWeb inclus à partir d'une page Web sans enregistrer un fichier Excel Microsoft. Le contrôle Aspose.Cells.GridWeb prend en charge cette fonctionnalité.

###  **Grille d'impressionWeb**

Pour imprimer sans enregistrer un fichier séparé, appelez la méthode print() de la classe GridWeb côté client pour imprimer la grille. Vous pouvez également choisir un événement approprié.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

Puisque vous l'appelez du côté client, vous devrez donc d'abord obtenir l'identifiant client Gridweb. Vous pouvez obtenir l'identifiant client en utilisant la méthode gridweb.getClientID().

###  **Exemple de code côté client**

Veuillez consulter le lien suivant qui appelle la méthode gridweb.print() du côté client.

**HTML**

{{< highlight "java" >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

##  **Introduction aux différents modes de grille**

Cet article décrit les différents modes de Aspose.Cells.GridWeb. Ces modes se différencient logiquement en raison de leurs différentes caractéristiques et comportements. Nous avons identifié différents types de mode comme :

- Mode édition
- Mode d'affichage

Tous ces modes ont leurs propres caractéristiques. Les développeurs peuvent travailler avec Aspose.Cells.GridWeb dans n'importe quel mode selon leurs besoins. Nous examinerons chaque mode ci-dessous.

###  **Mode édition**

Par défaut, le contrôle Aspose.Cells.GridWeb est en mode Edition. En mode Édition, vous pouvez éditer ou modifier entièrement le contenu de la grille en utilisant toutes les fonctionnalités offertes par le contrôle Aspose.Cells.GridWeb. Ces fonctionnalités incluent :

- Enregistrement du contenu de la grille dans des fichiers Excel Microsoft.
- Soumission de données à un serveur.
- Formules de calcul.
- Annuler ou abandonner les actions précédentes.
- Gestion des lignes et des colonnes.
- Couper, copier ou coller des données.
- Formatage des cellules, etc.

**Contrôle GridWeb en mode édition**

![tâche : image_alt_text](working-with-gridweb_9.png)

Les développeurs peuvent également passer en mode édition par programme en définissant la propriété EditMode du contrôle GridWeb sur true.

###  **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

###  **Mode d'affichage**

Lorsque le contrôle GridWeb est en mode Affichage, les utilisateurs ne peuvent pas éditer ou modifier le contenu de la grille, ce qui signifie qu'ils peuvent uniquement afficher le contenu de la grille. C'est pourquoi ce mode est appelé mode Affichage. En mode Affichage, quelques boutons (**Soumettre**,**Sauvegarder** et**Annuler**) sont masqués et le menu qui apparaît lors d'un clic droit ne contient que le **Copier** et**Trouver** option.

**Contrôle GridWeb en mode Affichage** 

![tâche : image_alt_text](working-with-gridweb_10.png)

Si les développeurs souhaitent que leurs utilisateurs visualisent uniquement les données, ils peuvent passer en mode Affichage par programmation en définissant la propriété EditMode du contrôle GridWeb sur *false**.

###  **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Même en mode Affichage, les utilisateurs peuvent modifier la hauteur et la largeur des lignes et des colonnes.

{{% /alert %}}
