---
title: Travailler avec GridWeb
type: docs
weight: 20
url: /fr/java/working-with-gridweb/
---

## **Ouverture d'un fichier Microsoft Excel**

Le contrôle Aspose.Cells.GridWeb peut ouvrir et charger des fichiers Microsoft Excel - avec données, mise en forme, graphiques, images, etc. Ce sujet explique comment faire.

Pour ouvrir un fichier Excel à l'aide du contrôle GridWeb :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire web ou à une page.
2. Importez le fichier Excel en spécifiant le chemin du fichier.
1. Exécutez l'application ou ouvrez la page.

Pour charger le contenu d'un fichier Excel dans le contrôle Aspose.Cells.GridWeb, vous devez appeler la méthode importExcelFile pour spécifier le chemin du fichier Excel. Ensuite, le contrôle GridWeb trouvera automatiquement le fichier à partir du chemin spécifié et affichera son contenu. Un extrait de code qui charge le contenu d'un fichier Excel est fourni ci-dessous.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

Le extrait de code ci-dessus peut être utilisé de n'importe quelle manière que vous souhaitez. Par exemple, pour charger automatiquement un fichier Excel lors du chargement d'un formulaire web, ajoutez ce code à l'événement Page_Load du formulaire que vous avez spécifié vous-même.

**Un fichier Excel est chargé dans GridWeb**

![todo:image_alt_text](working-with-gridweb_1.png)

## **Enregistrement d'un fichier Microsoft Excel**

Il est possible de créer de nouveaux fichiers Microsoft Excel ou de manipuler des fichiers existants sur les sites web en mode GUI en utilisant le contrôle Aspose.Cells.GridWeb. Les fichiers peuvent ensuite être enregistrés au format Excel. Aspose.Cells.GridWeb sert efficacement d'éditeur de feuilles de calcul en ligne. Ce sujet décrit comment enregistrer le contenu du tableau dans des fichiers Excel.

### **Enregistrer sous forme de fichier**

Pour enregistrer le contenu du contrôle Aspose.Cells.GridWeb en tant que fichier Excel :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire web ou à une page.
1. Enregistrez votre travail sous forme de fichier Excel à un chemin spécifié.
1. Exécutez l'application ou ouvrez la page.

L'exemple de code ci-dessous illustre comment enregistrer le contenu de la grille dans un fichier Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

Le fragment de code ci-dessus peut être utilisé de plusieurs manières. Une manière courante est d'ajouter un bouton qui enregistre le contenu de la grille dans un fichier Excel lorsqu'il est cliqué. Aspose.Cells.GridWeb propose une approche plus facile pour la tâche. Aspose.Cells.GridWeb dispose d'un événement appelé SaveCommand. Le fragment de code ci-dessus peut être ajouté au gestionnaire d'événements de l'événement SaveCommand qui permet aux utilisateurs d'enregistrer leur travail en cliquant sur le bouton **Enregistrer** intégré à Aspose.Cells.GridWeb.

## **Redimensionner Aspose.Cells.GridWeb et sa barre d'en-tête**

Cet article explique comment redimensionner GridWeb à l'exécution à l'aide de l'API Aspose.Cells.GridWeb. Il explique également comment redimensionner les barres d'en-tête du contrôle Aspose.Cells.GridWeb pour faciliter la lecture de leurs données.

### **Modification de la largeur et de la hauteur de Aspose.Cells.GridWeb**

Modifier la largeur et la hauteur du contrôle Aspose.Cells.GridWeb est une fonctionnalité simple mais importante. Le contrôle Aspose.Cells.GridWeb est représenté par la classe GridWeb dans l'API. Pour redimensionner la largeur et la hauteur du contrôle GridWeb, utilisez simplement ses propriétés de largeur et de hauteur.

{{% alert color="primary" %}}

La largeur et la hauteur du contrôle peuvent être définies en pixels ou en points.

{{% /alert %}}

La sortie du fragment de code suivant est montrée ci-dessous.

**Largeur et hauteur modifiées du contrôle GridWeb**

![todo:image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **Modification de la largeur et de la hauteur de la barre d'en-tête**

Le contrôle Aspose.Cells.GridWeb contient deux barres d'en-tête comme suit :

- Barre d'en-tête supérieure, cette barre d'en-tête représente les colonnes comme A, B, C, D, etc.
- Barre d'en-tête gauche, cette barre d'en-tête représente les lignes comme 1, 2, 3, 4, etc.

Les deux barres d'en-tête sont montrées ci-dessous.

**Barres d'en-tête**

![todo:image_alt_text](working-with-gridweb_3.png)

Modifier la hauteur de la barre d'en-tête supérieure et la largeur de la barre d'en-tête gauche à l'aide des propriétés HeaderBarHeight et HeaderBarWidth du contrôle GridWeb respectivement. La figure ci-dessous montre la sortie de l'exemple de code qui suit.

**Largeur et hauteur de la barre d'en-tête modifiées**

![todo:image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Travailler avec les événements Aspose.Cells.GridWeb**

Tous les développeurs doivent être familiers avec les événements et leur but. Les événements sont utilisés pour envoyer des notifications des changements qui peuvent survenir dans un contrôle ou une classe. Aspose.Cells.GridWeb possède plusieurs événements qui peuvent être utilisés pour effectuer des tâches spécifiques lorsque certains changements se produisent dans le contrôle.

Ce sujet fournit une introduction à tous les événements pris en charge par le contrôle Aspose.Cells.GridWeb ainsi que des détails sur la manière de gérer ces événements.

### **Introduction aux événements de grille**

Le contrôle Aspose.Cells.GridWeb prend en charge plusieurs événements qui offrent davantage de contrôle pour effectuer des opérations lorsque des événements spécifiques sont déclenchés dans le contrôle. Une liste complète des événements pris en charge par le contrôle Aspose.Cells.GridWeb peut être trouvée ci-dessous.

|**Evénements**|**Description**|
| :- | :- |
|CellCommand| Se produit lorsque le lien de commande d'une cellule est cliqué. Lorsque cet événement est déclenché, son paramètre e.Argument fournit le nom de la commande.|
|CellDoubleClick| Se produit lorsque la cellule est double-cliquée.|
|ColumnDeleted| Se produit lorsque l'utilisateur supprime une colonne d'une feuille de calcul à l'aide du menu côté client.|
|ColumnDeleting| Se produit lorsque l'utilisateur essaie de supprimer une colonne d'une feuille de calcul à l'aide du menu côté client.|
|ColumnDoubleClick| Se produit lorsque l'en-tête de colonne est double-cliqué.|
|ColumnInserted| Se produit lorsque l'utilisateur insère une colonne dans une feuille de calcul à l'aide du menu côté client.|
|CustomCommand| Se produit lorsque l'utilisateur clique sur un bouton de commande personnalisé.|
|LoadCustomData| Se produit lorsque la propriété EnableSession du contrôle est définie sur false et que les données de la feuille de calcul doivent être chargées. Vous pouvez gérer cet événement en mode sans session pour charger les données de la feuille de calcul à partir d'un fichier ou d'une base de données.|
|PageIndexChanged| Se produit lorsque l'index de la page de feuille de calcul du contrôle est modifié.|
|RowDeleted| Se produit lorsque l'utilisateur supprime une ligne de la feuille de calcul à l'aide du menu côté client.|
|RowDeleting| Se produit lorsque l'utilisateur essaie de supprimer une ligne d'une feuille de calcul à l'aide du menu côté client.|
|RowDoubleClick| Se produit lorsque l'en-tête de ligne est double-cliqué.|
|RowInserted| Se produit lorsque l'utilisateur insère une ligne dans la feuille de calcul à l'aide du menu côté client.|
|SaveCommand| Se produit lorsque le bouton **Enregistrer** est cliqué.|
|SheetTabClick|Se produit lorsque l'onglet de feuille est cliqué.|
|SubmitCommand|Se produit lorsque le bouton **Soumettre** est cliqué.|
|UndoCommand|Se produit lorsque le bouton **Annuler** est cliqué.|
|AjaxCallFinished|Se déclenche lorsque la mise à jour AJAX du contrôle est terminée. (EnableAJAX doit être défini sur true).|
|CellModifiedOnAjax|Se déclenche lorsque la cellule est modifiée dans l'appel AJAX.|
|AfterColumnFilter|Se déclenche lorsque le filtre est appliqué sur une colonne.|

### **Gestion des événements de grille**

Pour effectuer une opération spécifique lors du déclenchement d'un événement spécifique, nous devons créer un gestionnaire d'événements. Un gestionnaire d'événements effectue la tâche souhaitée lorsqu'un certain événement est déclenché. L'exemple suivant montre comment gérer un événement de grille simple.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **Travailler avec des événements de double clic**

Aspose.Cells.GridWeb contient trois types d'événements de double clic :

- CellDoubleClick, déclenché lorsqu'une cellule est double-cliquée.
- ColumnDoubleClick, déclenché lorsque l'en-tête de colonne est double-cliqué.
- RowDoubleClick, déclenché lorsque l'en-tête de ligne est double-cliqué.

Ce sujet traite de l'activation des événements de double clic dans Aspose.Cells.GridWeb. Il traite également de la création de gestionnaires d'événements pour ces événements.|

### **Activation des événements de double clic**

Tous les types d'événements de double clic peuvent être activés côté client en définissant la propriété EnableDoubleClickEvent du contrôle GridWeb sur true.

{{% alert color="primary" %}}

Par défaut, la propriété EnableDoubleClickEvent est définie sur false. Cela signifie que les événements de double clic ne sont pas activés par défaut. Pour implémenter de tels événements, activez d'abord la fonctionnalité.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

Une fois les événements de double clic activés, il est possible de créer des gestionnaires d'événements pour n'importe quel événement de double clic. Ces gestionnaires d'événements effectuent des tâches spécifiques lorsqu'un événement de double clic donné est déclenché.|

### **Gestion des événements de double clic**

#### **Double Clic Cell**

Le gestionnaire d'événements pour l'événement CellDoubleClick fournit un argument de type CellEventArgs, qui fournit les informations complètes de la cellule sur laquelle un double-clic a été fait.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **Double Clic sur l'en-tête de colonne**

Le gestionnaire d'événements pour l'événement ColumnDoubleClick fournit un argument de type RowColumnEventArgs qui fournit le numéro d'index de la colonne pour l'en-tête qui a été double-cliqué ainsi que d'autres informations.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **Double Clic sur l'en-tête de ligne**

Le gestionnaire d'événements pour l'événement RowDoubleClick fournit un argument de type RowColumnEventArgs qui fournit le numéro d'index de la ligne pour l'en-tête qui a été double-cliqué ainsi que d'autres informations connexes.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Définition du style ou de l'apparence de Aspose.Cells.GridWeb**

Aspose.Cells.GridWeb a son propre aspect par défaut, mais il est possible de changer son apparence. Aspose.Cells.GridWeb propose plusieurs propriétés permettant aux développeurs de contrôler pleinement son apparence. Ce sujet aborde certaines de ces propriétés.

### **Définition du style ou de l'apparence de Aspose.Cells.GridWeb**

#### **Styles prédéfinis**

Pour économiser les efforts des développeurs, Aspose.Cells.GridWeb offre certains styles prédéfinis. Il suffit de sélectionner un style dans la liste pour l'appliquer.

|**Styles**|**Schéma de couleurs**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
Lorsqu'un style particulier est sélectionné, il modifie l'apparence globale du contrôle GridWeb. Les développeurs peuvent sélectionner un style prédéfini à appliquer au moment de l'exécution à l'aide de l'API flexible de Aspose.Cells.GridWeb.

Le contrôle GridWeb fournit la propriété PresetStyle à laquelle les développeurs peuvent affecter n'importe quel style prédéfini souhaité.

Le résultat de l'extrait de code ci-dessous est affiché ci-dessous.

**Contrôle GridWeb avec le style Colorful1 appliqué**

![todo:image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Style de barre d'en-tête**

Si vous examinez le contrôle GridWeb, vous remarquerez deux barres d'en-tête. Une pour les colonnes (c'est-à-dire A, B, C, D, etc.) et une autre pour les lignes (c'est-à-dire 1, 2, 3, 4, etc.). Aspose.Cells.GridWeb permet aux développeurs de contrôler l'apparence de ces barres d'en-tête. Les développeurs peuvent définir le style des barres d'en-tête au moment de l'exécution.

{{% alert color="primary" %}}

Le contrôle GridWeb fournit la propriété HeaderBarStyle qui applique un style sur les deux barres d'en-tête du contrôle.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Style de barre d'onglets**

Il est possible de définir le style de la barre d'onglets également. Veuillez consulter le code suivant

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **Chargement du fichier de style**

Pour appliquer les paramètres de style d'un fichier de style existant au contrôle GridWeb, les développeurs peuvent définir le chemin du fichier de style à la propriété CustomStyleFileName du contrôle. Mais, avant de le faire, il est nécessaire de définir la propriété PresetStyle du contrôle sur Custom. Cela est dû au fait que le fichier de style contient des informations de style personnalisé déjà définies par un développeur.

Veuillez consulter l'image suivante qui montre GridWeb avec le style personnalisé appliqué.

![todo:image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

IMPORTANT : Charger un fichier de style dans un contrôle GridWeb n'affecte pas les paramètres de formatage des cellules du contrôle.

{{% /alert %}}

#### **Modèle d'exemple de style personnalisé**

Voici le modèle d'exemple de style personnalisé. Vous pouvez le modifier selon vos besoins.

{{< highlight java >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Création d'un contrôle sur un formulaire Web**

Cet article vous guidera sur la manière de créer une page web JSP (Java Server Page) simple avec le contrôle GridWeb.

**Étape 1 - Création de la structure de répertoire**

Vous devez créer la structure de répertoire suivante dans le répertoire **webapps** de Tomcat Server

![todo:image_alt_text](working-with-gridweb_7.png)

Il s'agit des répertoires et des fichiers que vous devez créer. Veuillez lire les commentaires et les suivre. Vous pouvez obtenir les derniers archives de publication Aspose.Cells.GridWeb pour Java à partir de [ce lien](https://downloads.aspose.com/cells/java).

{{< highlight java >}}

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

Cette section montre le code pour les différents fichiers créés dans la structure de répertoire ci-dessus. Veuillez obtenir ces codes et les ajouter dans vos fichiers en les ouvrant dans le Bloc-notes et en les copiant/collant.

**Web.xml**

{{< highlight java >}}

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

{{< highlight java >}}

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

**SamplePage.jsp**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-SamplePage-SamplePage.jsp" >}}

**Étape 3 - Exécution de votre page web JSP d'exemple**

Maintenant que vous avez terminé. Il est temps d'exécuter la page web. Veuillez démarrer votre serveur Tomcat et ensuite coller l'URL suivante dans le navigateur web.

{{< highlight java >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Vous verrez quelque chose de similaire à la capture d'écran suivante. Félicitations, vous avez réussi à utiliser le contrôle GridWeb sur votre page JSP.

![todo:image_alt_text](working-with-gridweb_8.png)

## **Impression de GridWeb**

Il arrive que les développeurs aient besoin d'imprimer le contenu de la grille Web inclus depuis une page Web sans enregistrer de fichier Microsoft Excel. Le contrôle Aspose.Cells.GridWeb prend en charge cette fonctionnalité.

### **Impression de GridWeb**

Pour imprimer sans enregistrer de fichier séparé, appelez la méthode d'impression print() de la classe GridWeb côté client pour imprimer la grille. Vous pouvez également choisir un événement approprié.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

Comme vous l'appelez côté client, vous devrez d'abord obtenir l'identifiant client de la grilleWeb. Vous pouvez obtenir l'identifiant client à l'aide de la méthode gridweb.getClientID().

### **Code d'exemple côté client**

Veuillez consulter le lien suivant qui appelle la méthode gridweb.print() côté client.

**HTML**

{{< highlight java >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **Introduction aux différents modes de grille**

Cet article décrit les différents modes de Aspose.Cells.GridWeb. Ces modes sont différenciés logiquement en raison de leurs caractéristiques et comportements différents. Nous avons identifié différents types de mode comme :

- Mode Édition
- Mode Affichage

Tous ces modes ont leurs propres caractéristiques. Les développeurs peuvent travailler avec Aspose.Cells.GridWeb dans n'importe quel mode en fonction de leurs besoins. Nous examinerons chaque mode ci-dessous.

### **Mode Édition**

Par défaut, le contrôle Aspose.Cells.GridWeb est en mode Édition. En mode Édition, vous pouvez entièrement modifier ou modifier le contenu de la grille en utilisant toutes les fonctionnalités offertes par le contrôle Aspose.Cells.GridWeb. Ces fonctionnalités comprennent :

- Enregistrer le contenu de la grille dans des fichiers Microsoft Excel.
- Envoyer des données à un serveur.
- Calculer des formules.
- Annuler ou rejeter des actions précédentes.
- Gérer les lignes et les colonnes.
- Couper, copier ou coller des données.
- Mise en forme des cellules, etc.

**Contrôle GridWeb en mode édition**

![todo:image_alt_text](working-with-gridweb_9.png)

Les développeurs peuvent également passer en mode Édition de manière programmée en définissant la propriété EditMode du contrôle GridWeb sur true.

### **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **Mode visualisation**

Lorsque le contrôle GridWeb est en mode visualisation, les utilisateurs ne peuvent pas modifier ou modifier le contenu de la grille, ce qui signifie que les utilisateurs ne peuvent que consulter le contenu de la grille. C'est pourquoi ce mode est appelé mode visualisation. En mode visualisation, quelques boutons (**Soumettre**, **Enregistrer** et **Annuler**) sont masqués et le menu qui apparaît lors d'un clic droit ne contient que les options **Copier** et **Rechercher**.

**Contrôle GridWeb en mode visualisation** 

![todo:image_alt_text](working-with-gridweb_10.png)

Si les développeurs souhaitent que leurs utilisateurs ne consultent que les données, ils peuvent passer en mode visualisation de manière programmée en définissant la propriété EditMode du contrôle GridWeb sur **false**.

### **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Même en mode visualisation, les utilisateurs peuvent modifier la hauteur et la largeur des lignes et des colonnes.

{{% /alert %}}
